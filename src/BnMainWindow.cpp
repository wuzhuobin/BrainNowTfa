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
  QStringList outputs = QString(process->readAll()).split("\r\n");
  xlnt::worksheet ws = this->wb->active_sheet();
  // qDebug() << outputs;
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
      ws[xlnt::cell_reference(i * 2 + 2, row + 3)].value(outputs[index].toDouble());
      ws[xlnt::cell_reference(i * 2 + 3, row + 3)].value(outputs[index + 9].toDouble());
      index++;
    // }
  }
}

void BnMainWindow::onProcessFinished(int i) {
  delete this->processes.take(i);
  if(this->processes.isEmpty()) {
    this->wb->save(this->result.toStdString());
  }
}

void BnMainWindow::cal() {

  this->wb = std::make_shared<xlnt::workbook>();
  xlnt::worksheet &ws = this->wb->active_sheet();
  QStringList rowHeader;
  rowHeader << "VLF (0.02-0.07 Hz)"
    << "Gain, %/mmHg"
    << "Phase, radian"
    << "Coherence"
    << "LF (0.07-0.20 Hz)"
    << "Gain, %/mmHg"
    << "Phase, radian"
    << "Coherence"
    << "HF (0.20-0.35 Hz)"
    << "Gain, %/mmHg"
    << "Phase, radian"
    << "Coherence";
  for(std::size_t i = 0; i < rowHeader.size(); ++i) {
    ws[xlnt::cell_reference(1, i + 3)].value(rowHeader[i].toStdString());
  }
  // wb.save("result.xlsx");

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
    qDebug() << argv1 << argv2;
    process->setArguments(QStringList() << argv1 << argv2);
    connect(process, static_cast<void((QProcess::*)(int, QProcess::ExitStatus))>(&QProcess::finished), [=](int exitCode, QProcess::ExitStatus exitStatus) { 
      qDebug() << exitStatus;
      this->onProcessFinished(i);
    });
    connect(process, &QProcess::readyReadStandardOutput, [=]() { this->onReadyReadStandardOutput(i); });
    connect(process, &QProcess::readyReadStandardError, [=]() { qDebug() << process->readAll(); });
    process->start();
    this->processes[i] = process;
  }
}