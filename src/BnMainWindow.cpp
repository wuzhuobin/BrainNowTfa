// qt
#include <QFileDialog>
#include <QProgressDialog>
#include <QDebug>
#include <QProcess>
#include <QFileInfo>
// xlnt
#include <xlnt/xlnt.hpp>
//
#include "BnMainWindow.h"
#include "ui_BnMainWindow.h"

// const QString program = "C:/Windows/System32/cmd.exe";
const QString PROGRAM = "tfa.exe";
const QString RESULT = "result.xlsx";
const QStringList SHEET_TITLES = {
  "Group summaray", 
  "VLF_LF_HF", 
  "l_gain", 
  "l_phase", 
  "l_coherence", 
  "r_gain", 
  "r_phase", 
  "r_coherence"
};
const QStringList GROUP_SUMMARY_HEADER = {
  "F",
  "l_gain",
  "l_phase",
  "l_coherence",
  "r_gain",
  "r_phase",
  "r_coherence",
  "",
  "",
  "L side",
  "R side"
};
const QStringList ROW_HEADER = {
   "VLF (0.02-0.07 Hz)",
   "Gain, %/mmHg",
   "Phase, radian",
   "Coherence",
   "LF (0.07-0.20 Hz)",
   "Gain, %/mmHg",
   "Phase, radian",
   "Coherence",
   "HF (0.20-0.35 Hz)",
   "Gain, %/mmHg",
   "Phase, radian",
   "Coherence"
};
BnMainWindow::BnMainWindow(QWidget * parent) :
  QMainWindow(parent)
{
  this->ui = new Ui::BnMainWindow;
  this->ui->setupUi(this);
}

BnMainWindow::~BnMainWindow() 
{
  delete this->ui;
}

void BnMainWindow::on_actionOpen_triggered(){
  this->cal();
}

void BnMainWindow::on_pushButtonCal_clicked() {
  this->cal();
}

void BnMainWindow::on_actionExit_triggered() {
  qApp->exit(0);
}

void BnMainWindow::onReadyReadStandardOutput(int i) {
  QProcess *process = this->processes[i];
  QString data = QString(process->readAll());
  // Check whether the data is valid, it should contain some numbers.
  if(!data.contains(QRegExp("[0-9]"))) {
    return;
  }
  QStringList dataList = data.split("\r\n");
  for(std::size_t i = 0; i < dataList.size(); ++i) {
    dataList[i] = dataList[i].remove(QRegularExpression("[\\[\\](),]"));
  }
  // qDebug() << dataList;
  this->vlf_lf_hf(i, dataList[0]);
  this->l_r_gain_phase_coherence(i, dataList[2], dataList[3], dataList[4], dataList[5], dataList[6], dataList[7]);
  if(i == 0) {
    QStringList frequencies = dataList[1].split(' ');
    for(auto cit = frequencies.cbegin(); cit != frequencies.cend(); ++cit) {
      this->frequency << cit->toDouble();
    }
  }
}

void BnMainWindow::onProcessFinished(int i) {
  delete this->processes.take(i);
  if(this->processes.isEmpty()) {
    this->l_r_gain_phase_coherence_average();
    this->vlf_lf_hf_average();
    this->groupSummary();
    this->wb->save(this->result.toStdString());
  }
}

void BnMainWindow::cal() {

  this->wb = std::make_shared<xlnt::workbook>();
  for (std::size_t i = 0; i < SHEET_TITLES.size(); i++) {
    if(i == 0) {
      this->wb->sheet_by_index(i).title(SHEET_TITLES[i].toStdString());
    }
    else{
      this->wb->copy_sheet(this->wb->active_sheet()).title(SHEET_TITLES[i].toStdString());
    }
  }
  // Group summary
  xlnt::worksheet &groupSummary = this->wb->sheet_by_title(SHEET_TITLES[0].toStdString());
  for(std::size_t i = 0; i < GROUP_SUMMARY_HEADER.size(); ++i) {
    groupSummary[xlnt::cell_reference(i + 1, 1)].value(GROUP_SUMMARY_HEADER[i].toStdString());
  }
  for(std::size_t i = 0; i < ROW_HEADER.size(); ++i) {
    groupSummary[xlnt::cell_reference(9, i+2)].value(ROW_HEADER[i].toStdString());
  }
  // VLF_LF_HF
  xlnt::worksheet &vlf_lf_hf = this->wb->sheet_by_title(SHEET_TITLES[1].toStdString());
  for(std::size_t i = 0; i < ROW_HEADER.size(); ++i) {
    vlf_lf_hf[xlnt::cell_reference(1, i+3)].value(ROW_HEADER[i].toStdString());
  }

  this->inputs = QFileDialog::getOpenFileNames(this, tr("Select inputs."), QString(), tr("Excel (*.xlsx *.xls)"));
  if(this->inputs.isEmpty()) {
    return;
  }
  QString outputDir = QFileDialog::getExistingDirectory(this, tr("Select output directory."));
  if(outputDir.isEmpty()) {
    return;
  }
  this->outputs.clear();
  for(QString s: this->inputs) {
    this->outputs << outputDir + '/' + QFileInfo(s).completeBaseName() + "_result.xlsx";
  }
  this->result = outputDir + '/' + RESULT;

  // // QString program = "D:/Program Files/Git/bin/bash.exe";
  this->processes.clear();
  for(size_t i = 0; i < this->inputs.size(); ++i) {
    QProcess *process = new QProcess(this);
    process->setProgram(PROGRAM);
    QString argv1 = this->inputs[i];
    QString argv2 = this->outputs[i];
     // process->setArguments(QStringList() << "test.sh" << argv1);
    // qDebug() << argv1 << argv2;
    process->setArguments(QStringList() << argv1 << argv2);
    connect(process, static_cast<void((QProcess::*)(int, QProcess::ExitStatus))>(&QProcess::finished), [=](int exitCode, QProcess::ExitStatus exitStatus) { 
      qDebug() << exitStatus;
      this->onProcessFinished(i);
    });
    connect(process, &QProcess::readyReadStandardOutput, [=]() { this->onReadyReadStandardOutput(i); });
    connect(process, &QProcess::readyReadStandardError, [=]() { qDebug() << process->readAllStandardError(); });
    process->start();
    this->processes[i] = process;
  }
}

void BnMainWindow::groupSummary() {

}

void BnMainWindow::vlf_lf_hf(int i, QString means) {
  if(means.isEmpty()) {
    return;
  }
  QStringList means_ = means.split(' ');
  xlnt::worksheet &ws = this->wb->sheet_by_title(SHEET_TITLES[1].toStdString());
  // qDebug() << means_;
  // row headers
  QString fileName = QFileInfo(this->inputs[i]).completeBaseName();
  ws[xlnt::cell_reference(2 + i * 2, 1)].value(fileName.toStdString());
  ws.merge_cells(xlnt::range_reference(2 + i * 2, 1, 3 + i * 2, 1));
  ws[xlnt::cell_reference(2 + i * 2, 2)].value("L side");
  ws[xlnt::cell_reference(3 + i * 2, 2)].value("R side");
  std::size_t index = 0;
  for(std::size_t row = 0; row < 12; ++row) {
    // for(std::size_t col = 0; col < 2; ++col) {
      if(row % 4 == 0) {
        continue;
      }
      ws[xlnt::cell_reference(i * 2 + 2, row + 3)].value(means_[index].toDouble());
      ws[xlnt::cell_reference(i * 2 + 3, row + 3)].value(means_[index + 9].toDouble());
      index++;
    // }
  }
}

void BnMainWindow::vlf_lf_hf_average() {
  xlnt::worksheet &ws = this->wb->sheet_by_title(SHEET_TITLES[1].toStdString());
  xlnt::worksheet &groupSummary = this->wb->sheet_by_title(SHEET_TITLES[0].toStdString());
  ws[xlnt::cell_reference(2 + this->inputs.size() * 2, 1)].value("Average");
  ws[xlnt::cell_reference(2 + this->inputs.size() * 2, 2)].value("L side");
  ws[xlnt::cell_reference(3 + this->inputs.size() * 2, 2)].value("R side");
  std::size_t index = 0;
  for(std::size_t row = 0; row < 12; ++row) {
    double averageL = 0;
    double averageR = 0;
    if (row % 4 == 0) {
      continue;
    }
    for(std::size_t i = 0; i < this->inputs.size(); ++i) {
      averageL += ws[xlnt::cell_reference(i * 2 + 2, row + 3)].value<double>();
      averageR += ws[xlnt::cell_reference(i * 2 + 3, row + 3)].value<double>();
    }
    averageL /= this->inputs.size();
    averageR /= this->inputs.size();
    // for(std::size_t col = 0; col < 2; ++col) {
      ws[xlnt::cell_reference(this->inputs.size() * 2 + 2, row + 3)].value(averageL);
      ws[xlnt::cell_reference(this->inputs.size() * 2 + 3, row + 3)].value(averageR);
      groupSummary[xlnt::cell_reference(8 + 2, row + 2)].value(averageL);
      groupSummary[xlnt::cell_reference(8 + 3, row + 2)].value(averageR);
      index++;
    // }
  }

}

void BnMainWindow::l_r_gain_phase_coherence(int i, QString l_gain, QString l_phase, QString l_coherence, QString r_gain, QString r_phase, QString r_coherence) {
  this->l_r_gain_phase_coherence(i, QStringList{l_gain, l_phase, l_coherence, r_gain, r_phase, r_coherence});
}

void BnMainWindow::l_r_gain_phase_coherence(int i, QStringList values) {

  QString fileName = QFileInfo(this->inputs[i]).completeBaseName();
  for(std::size_t j = 2; j < SHEET_TITLES.size(); ++j) {
    xlnt::worksheet &ws = this->wb->sheet_by_title(SHEET_TITLES[j].toStdString());
    ws[xlnt::cell_reference(2 + i, 1)].value(fileName.toStdString());
    QStringList valueList = values[j - 2].split(' ');
    for(std::size_t k = 0; k < valueList.size(); ++k) {
      ws[xlnt::cell_reference(2 + i, 2 + k)].value(valueList[k].toDouble());
    }
  }
}

void BnMainWindow::l_r_gain_phase_coherence_average() {
  xlnt::worksheet &groupSummary = this->wb->sheet_by_title(SHEET_TITLES[0].toStdString());
  for(std::size_t i = 2; i < SHEET_TITLES.size(); ++i) {
    xlnt::worksheet &ws = this->wb->sheet_by_title(SHEET_TITLES[i].toStdString());
    for(std::size_t j = 0; j < this->frequency.size(); ++j) {
      QList<double> values;
      for (std::size_t k = 0; k < this->inputs.size(); ++k) {
        values << ws[xlnt::cell_reference(2 + k, j + 2)].value<double>();
      }
      // qDebug() << values;
      double average = std::accumulate(values.cbegin(), values.cend(), 0.0) / this->inputs.size();
      ws[xlnt::cell_reference(2 + this->inputs.size(), j + 2)].value(average);
      ws[xlnt::cell_reference(1, j + 2)].value(this->frequency[j]);
      if(i == 2) {
        groupSummary[xlnt::cell_reference(1, j + 2)].value(this->frequency[j]);
      }
      groupSummary[xlnt::cell_reference(i, j + 2)].value(average);
    }
    ws[xlnt::cell_reference(2 + this->inputs.size(), 1)].value("Average");
    ws[xlnt::cell_reference(1, 1)].value("F");
  }
}