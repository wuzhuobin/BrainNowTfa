#include <iostream>
#include <cstdlib>
#include <QApplication>
#include "BnMainWindow.h"

int main(int argc, char* argv[]) {
  QApplication app(argc, argv);
  BnMainWindow w;
  w.show();

  return app.exec();
}
