#include <QMainWindow>
namespace Ui{ class BnMainWindow;}
class QProcess;

class BnMainWindow: public QMainWindow
{
  Q_OBJECT;
public:
  explicit BnMainWindow(QWidget *parent = nullptr);
  virtual ~BnMainWindow();
private Q_SLOTS:
  void on_actionOpen_triggered();
  void on_actionExit_triggered();
  void on_pushButtonCal_clicked();
  void onReadyReadStandardOutput(int i);
private:
  void cal();
  Ui::BnMainWindow *ui;
  QList<QProcess*> processes;
  QStringList inputs;
  QStringList outputs;
  QString result;
};