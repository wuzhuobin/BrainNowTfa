// qt
#include <QFileDialog>
#include <QProgressDialog>
#include <QDebug>
#include <QProcess>
#include <QFileInfo>
#include <QProgressDialog>
#include <QThread>
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
  this->progressDialog = nullptr;
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

void BnMainWindow::onProcessFinished(int i) {
  delete this->processes.take(i);
  this->progressDialog->setValue(this->inputs.size() - this->processes.size());
  if(this->processes.isEmpty()) {
    QProcess process(this);
    process.setProgram(PROGRAM);
    process.setArguments(QStringList() << "-s" << this->outputs << this->result );
    process.start();
    process.waitForFinished();
  }
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

  // // QString program = "D:/Program Files/Git/bin/bash.exe";
  this->processes.clear();
  for(size_t i = 0; i < this->inputs.size(); ++i) {
    QProcess *process = new QProcess(this);
    process->setProgram(PROGRAM);
    QString argv1 = this->inputs[i];
    QString argv2 = this->outputs[i];
     // process->setArguments(QStringList() << "test.sh" << argv1);
    // qDebug() << argv1 << argv2;
    process->setArguments(QStringList() << "-c" << argv1 << argv2);
    connect(process, static_cast<void((QProcess::*)(int, QProcess::ExitStatus))>(&QProcess::finished), [=](int exitCode, QProcess::ExitStatus exitStatus) { 
      qDebug() << exitStatus;
      this->onProcessFinished(i);
    });
    connect(process, &QProcess::readyReadStandardOutput, [=]() { qDebug() << process->readAllStandardOutput(); });
    connect(process, &QProcess::readyReadStandardError, [=]() { qDebug() << process->readAllStandardError(); });
    process->start();
    this->processes[i] = process;
  }
  if(this->progressDialog != nullptr) {
    delete this->progressDialog;
  }
  this->progressDialog = new QProgressDialog(this, Qt::Dialog | Qt::CustomizeWindowHint);
  this->progressDialog->setRange(0, this->inputs.size());
  this->progressDialog->setAutoClose(true);
  this->progressDialog->setAutoReset(true);
  this->progressDialog->setCancelButton(nullptr);
  // this->progressDialog->show();
  this->progressDialog->exec();
}
