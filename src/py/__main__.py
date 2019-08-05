import sys
import numpy as np
import pandas as pd
# import matplotlib.pyplot as pyplot
from core import *

def main(path):
  pass
  rri, time, sbp, dbp, mbp, scbfl, dcbfl, cbfl, scbfr, dcbfr, cbfr = loadExcel(path)
  y, x = interpolate2Hz(time, rri * 1000)
  rr = detrend(x, y)
  y, x = interpolate2Hz(time, 60 / rri)
  hr = detrend(x, y)
  y, x = interpolate2Hz(time, sbp)
  sbp = detrend(x, y)
  y, x = interpolate2Hz(time, dbp)
  dbp = detrend(x, y)
  y, x = interpolate2Hz(time, mbp)
  map = detrend(x, y)
  y, x = interpolate2Hz(time, mbp / np.mean(mbp) * 100)
  map_percent = detrend(x, y)
  y, x = interpolate2Hz(time, cbfl)
  vmeanl = detrend(x, y)
  y, x = interpolate2Hz(time, cbfl / np.mean(cbfl) * 100) 
  vmeanl_percent = detrend(x, y)
  y, x = interpolate2Hz(time, cbfr)
  vmeanr = detrend(x, y)
  y, x = interpolate2Hz(time, cbfr / np.mean(cbfr) * 100)
  vmeanr_percent = detrend(x, y)

  (F_brs, psd_sbp, cross_brs, trans_brs, phase_brs, gain_brs) = tfaCal(x=sbp, y=rr)
  (F_ldca, psd_map, cross_ldca, trans_ldca, phase_ldca, gain_ldca) = tfaCal(x=map, y=vmeanl)
  (F_ldca_p, psd_map, cross_ldca_p, trans_ldca_p, phase_ldca_p, gain_ldca_p) = tfaCal(x=map, y=vmeanl_percent)
  (F_ldca_p_p, psd_map_p, cross_ldca_p_p, trans_ldca_p_p, phase_ldca_p_p, gain_ldca_p_p) = tfaCal(x=map_percent, y=vmeanl_percent)
  (F_rdca, psd_map, cross_rdca, trans_rdca, phase_rdca, gain_rdca) = tfaCal(x=map, y=vmeanr)
  (F_rdca_p, psd_map, cross_rdca_p, trans_rdca_p, phase_rdca_p, gain_rdca_p) = tfaCal(x=map, y=vmeanr_percent)
  (F_rdca_p_p, psd_map_p, cross_rdca_p_p, trans_rdca_p_p, phase_rdca_p_p, gain_rdca_p_p) = tfaCal(x=map_percent, y=vmeanr_percent)

  data_frame = pd.DataFrame()
  data_frame['F'] = F_brs
  data_frame['cross_brs'] = cross_brs
  data_frame['phase_brs'] = phase_brs
  data_frame['gain_brs'] = gain_brs
  data_frame['']

  # pyplot.figure()
  # pyplot.plot(F_brs[0: 63], phase_brs[0: 63])
  # pyplot.show()
  # pyplot.figure()
  # pyplot.plot(F_brs[0: 63], cross_brs[0: 63])
  # pyplot.show()
  # pyplot.figure()
  # pyplot.plot(F_brs[0: 63], gain_brs[0: 63])
  # pyplot.show()


if __name__ == '__main__':
  main(sys.argv[1])