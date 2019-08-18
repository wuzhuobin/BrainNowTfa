// qt
#include <QMainWindow>
// std
#include <memory>
namespace Ui{ class BnMainWindow;}
namespace xlnt{class workbook;}
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
  void onProcessFinished(int i);
private:
  void cal();
  Ui::BnMainWindow *ui;
  std::shared_ptr<xlnt::workbook> wb;
  QHash<std::size_t, QProcess*> processes;
  QStringList inputs;
  QStringList outputs;
  QString result;
};