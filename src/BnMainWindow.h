// qt
#include <QMainWindow>
// std
#include <memory>
namespace Ui{ class BnMainWindow;}
class QProcess;
class QProgressDialog;

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
  void onProcessFinished(int i);
private:
  void cal();
  Ui::BnMainWindow *ui;
  QProgressDialog *progressDialog;
  QHash<std::size_t, QProcess*> processes;
  QStringList inputs;
  QStringList outputs;
  QString result;
};