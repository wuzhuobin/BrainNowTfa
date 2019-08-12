// qt
#include <QFileDialog>
#include <QProgressDialog>
#include <QDebug>
#include <QProcess>
#include <QFileInfo>
//
#include "BnMainWindow.h"
#include "ui_BnMainWindow.h"


// const QString program = "C:/Windows/System32/cmd.exe";

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
  QStringList inputs = QFileDialog::getOpenFileNames(this, tr("Select inputs."), QString(), tr("Excel (*.xlsx *.xls)"));
  // QString outputDir = QFileDialog::getExistingDirectory(this, tr('Select output directory.'));
  // QString program = "D:/Program Files/Git/bin/bash.exe";
  QString program = "tfa.exe";
  for(QString argv1: inputs) {
    QProcess *process = new QProcess(this);
    process->setProgram(program);
    // process->setArguments(QStringList() << "test.sh" << argv1);
    qDebug() << argv1 << argv1.split('.')[0] + "_result.xlsx";
    process->setArguments(QStringList() << argv1 << argv1.split('.')[0] + "_result.xlsx");
    connect(process, static_cast<void((QProcess::*)(int, QProcess::ExitStatus))>(&QProcess::finished), [process](int exitCode, QProcess::ExitStatus exitStatus) { 
      qDebug() << exitStatus;
      delete process;
    });
    connect(process, &QProcess::readyReadStandardOutput, [process]() { qDebug() << process->readLine(); });
    connect(process, &QProcess::readyReadStandardError, [process]() { qDebug() << process->readLine(); });
    process->start();
  }

}

void BnMainWindow::on_actionExit_triggered() {
  qApp->exit(0);
}