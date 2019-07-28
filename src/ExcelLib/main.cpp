#include <string>
#include <iostream>

#include "ExcelHelper.h"

int main(int argc, char *argv[])
{
  using namespace std;
  std::string file = "D:/ccode/BrainNowTfa/patient orinigal data.xlsx";
  Eigen::VectorXd rri;
  Eigen::VectorXd time;
  Eigen::VectorXd sbp;
  Eigen::VectorXd dbp;
  Eigen::VectorXd mbp;
  Eigen::VectorXd scbf_i;
  Eigen::VectorXd dcbf_i;
  Eigen::VectorXd cbf_i;
  Eigen::VectorXd scbf_r;
  Eigen::VectorXd dcbf_r;
  Eigen::VectorXd cbf_r;
  ExcelHelper::workSheetToVectors(file, rri, time, sbp, dbp, mbp, scbf_i, dcbf_i, cbf_i, scbf_r, dcbf_r, cbf_r);
  std::cout << "time:" << time << '\n';
  std::cin.get();
  return 0;
}