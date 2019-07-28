#include <QMainWindow>
namespace Ui{ class BnMainWindow;}

class BnMainWindow: public QMainWindow
{
  Q_OBJECT;
public:
  explicit BnMainWindow(QWidget *parent = nullptr);
  virtual ~BnMainWindow();
private:
  Ui::BnMainWindow *ui;
};