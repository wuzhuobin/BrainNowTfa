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
  xlnt::workbook wb;
  wb.load(this->result.toStdString());
  xlnt::worksheet ws = wb.active_sheet();
  ws[xlnt::cell_reference(1, i + 2)].value(QFileInfo(this->inputs[i]).completeBaseName().toStdString());
  for (std::size_t j = 0; j < outputs.size() - 1; ++j) {
    ws[xlnt::cell_reference(j+2, i + 2)].value(outputs[j].toDouble());
  }
  wb.save(this->result.toStdString());
}

void BnMainWindow::cal() {
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
  xlnt::workbook wb;
  xlnt::worksheet ws = wb.active_sheet();
  ws.title("result");
  QStringList header;
  header << "Name"
    << "Phase-L(VLF)"
    << "Phase-R(VLF)"
    << "Phase-L(LF)"
    << "Phase-R(LF)"
    << "Phase-L(HF)"
    << "Phase-R(HF)"
    << "Phase infract"
    << "Gain infract"
    << "Coherence infract"
    // << "ARI infract"
    << "Phase normal"
    << "Gain normal"
    << "Coherence normal"
    // << "ARI normal"
    ;
  for(size_t i = 0; i < header.size(); ++i) {
    ws[xlnt::cell_reference(i+1, 1)].value(header[i].toStdString());
  }
  wb.save(this->result.toStdString());

  // QString program = "D:/Program Files/Git/bin/bash.exe";
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
      // delete this->processes.takeAt(i);
    });
    connect(process, &QProcess::readyReadStandardOutput, [=]() { this->onReadyReadStandardOutput(i); });
    connect(process, &QProcess::readyReadStandardError, [=]() { qDebug() << process->readAll(); });
    process->start();
    this->processes.push_back(process);
  }
}