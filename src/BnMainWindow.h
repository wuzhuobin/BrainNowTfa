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
  void groupSummary();
  void vlf_lf_hf(int i, QString means);
  void l_r_gain_phase_coherence(int i, QString l_gain, QString l_phase, QString l_coherence, QString r_gain, QString r_phase, QString r_coherence);
  void l_r_gain_phase_coherence(int i, QStringList values);
  void l_r_gain_phase_coherence_average();
  Ui::BnMainWindow *ui;
  std::shared_ptr<xlnt::workbook> wb;
  QHash<std::size_t, QProcess*> processes;
  QStringList inputs;
  QStringList outputs;
  QString result;
};