#include <xlnt/xlnt.hpp>
#include "ExcelHelper.h"

void ExcelHelper::workSheetToVectors(
  const std::string & path,
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
  Eigen::VectorXd &cbf_r
  ) {
    xlnt::workbook workbook;
    workbook.load(path);
    xlnt::worksheet worksheet = workbook.active_sheet();
    xlnt::range rows = worksheet.rows(false);
    rri.resize(rows.length() - 1);
    time.resize(rows.length() - 1);
    sbp.resize(rows.length() - 1);
    dbp.resize(rows.length() - 1);
    mbp.resize(rows.length() - 1);
    scbf_i.resize(rows.length() - 1);
    dcbf_i.resize(rows.length() - 1);
    cbf_i.resize(rows.length() - 1);
    scbf_r.resize(rows.length() - 1);
    dcbf_r.resize(rows.length() - 1);
    cbf_r.resize(rows.length() - 1);
    for (int i = 1; i < rows.length(); ++i)
    {
        rri[i - 1] = rows[i][1].value<double>();
        time[i - 1] = rows[i][2].value<double>();
        sbp[i - 1] = rows[i][3].value<double>();
        dbp[i - 1] = rows[i][4].value<double>();
        mbp[i - 1] = rows[i][5].value<double>();
        scbf_i[i - 1] = rows[i][6].value<double>();
        dcbf_i[i - 1] = rows[i][7].value<double>();
        cbf_i[i - 1] = rows[i][8].value<double>();
        scbf_r[i - 1] = rows[i][9].value<double>();
        dcbf_r[i - 1] = rows[i][10].value<double>();
        cbf_r[i - i] = rows[i][11].value<double>();
    }
}