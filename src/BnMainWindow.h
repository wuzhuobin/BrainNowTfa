#include <QMainWindow>
namespace Ui{ class BnMainWindow;}

class BnMainWindow: public QMainWindow
{
  Q_OBJECT;
public:
  explicit BnMainWindow(QWidget *parent = nullptr);
  virtual ~BnMainWindow();
private Q_SLOTS:
  void on_actionOpen_triggered();
  void on_actionExit_triggered();
private:
  Ui::BnMainWindow *ui;
};