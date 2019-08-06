// qt
#include <QFileDialog>
#include <QProgressDialog>
#include <QDebug>
#include <QProcess>
//
#include "BnMainWindow.h"
#include "ui_BnMainWindow.h"

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

void BnMainWindow::on_actionOpen_triggered() {
  QStringList inputs = QFileDialog::getOpenFileNames(this, tr("Select inputs"), QString(), tr("Excel (*.xlsx)"));

  
}

void BnMainWindow::on_actionExit_triggered() {
  qApp->exit(0);
}