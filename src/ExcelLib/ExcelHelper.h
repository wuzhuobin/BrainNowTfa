#include <string>
#include <Eigen/Eigen>

namespace ExcelHelper
{
void workSheetToVectors(
    const std::string &path,
    Eigen::VectorXd &rri,
    Eigen::VectorXd &time,
    Eigen::VectorXd &sbp,
    Eigen::VectorXd &dbp,
    Eigen::VectorXd &mbp,
    Eigen::VectorXd &scbf_i,
    Eigen::VectorXd &dcbf_i,
    Eigen::VectorXd &cbf_i,
    Eigen::VectorXd &scbf_r,
    Eigen::VectorXd &dcbf_r,
    Eigen::VectorXd &cbf_r);
}; // namespace ExcelHelper