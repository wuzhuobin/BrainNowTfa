#include <iostream>
#include <cstdlib>
#include <QApplication>
#include "BnMainWindow.h"

#pragma comment(linker, "/SUBSYSTEM:console /ENTRY:mainCRTStartup")

int main(int argc, char* argv[]) {
  QApplication app(argc, argv);
  BnMainWindow w;
  w.show();

  return app.exec();
}
