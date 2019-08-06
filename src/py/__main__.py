import sys
from core import *
import numpy as np
import pandas as pd
# import matplotlib.pyplot as pyplot

# def main(path):
#   pass
#   rri, time, sbp, dbp, mbp, scbfl, dcbfl, cbfl, scbfr, dcbfr, cbfr = loadExcel(path)
#   y, x = interpolate2Hz(time, rri * 1000)
#   rr = detrend(x, y)
#   y, x = interpolate2Hz(time, 60 / rri)
#   hr = detrend(x, y)
#   y, x = interpolate2Hz(time, sbp)
#   sbp = detrend(x, y)
#   y, x = interpolate2Hz(time, dbp)
#   dbp = detrend(x, y)
#   y, x = interpolate2Hz(time, mbp)
#   map = detrend(x, y)
#   y, x = interpolate2Hz(time, mbp / np.mean(mbp) * 100)
#   map_percent = detrend(x, y)
#   y, x = interpolate2Hz(time, cbfl)
#   vmeanl = detrend(x, y)
#   y, x = interpolate2Hz(time, cbfl / np.mean(cbfl) * 100) 
#   vmeanl_percent = detrend(x, y)
#   y, x = interpolate2Hz(time, cbfr)
#   vmeanr = detrend(x, y)
#   y, x = interpolate2Hz(time, cbfr / np.mean(cbfr) * 100)
#   vmeanr_percent = detrend(x, y)

#   (F_psd_sbp, psd_sbp, F_brs, cross_brs, coh_brs, trans_brs, phase_brs, gain_brs) = tfaCal(x=sbp, y=rr)
#   (F_psd_map, psd_map, F_ldca, cross_ldca, coh_ldca, trans_ldca, phase_ldca, gain_ldca) = tfaCal(x=map, y=vmeanl)
#   (F_psd_map, psd_map, F_ldca_p, cross_ldca_p, coh_ldca_p, trans_ldca_p, phase_ldca_p, gain_ldca_p) = tfaCal(x=map, y=vmeanl_percent)
#   (F_psd_map_p, psd_map_p, F_ldca_p_p, cross_ldca_p_p, coh_ldca_p_p, trans_ldca_p_p, phase_ldca_p_p, gain_ldca_p_p) = tfaCal(x=map_percent, y=vmeanl_percent)
#   (F_psd_map, psd_map, F_rdca, cross_rdca, coh_rdca, trans_rdca, phase_rdca, gain_rdca) = tfaCal(x=map, y=vmeanr)
#   (F_psd_map, psd_map, F_rdca_p, cross_rdca_p, coh_rdca_p, trans_rdca_p, phase_rdca_p, gain_rdca_p) = tfaCal(x=map, y=vmeanr_percent)
#   (F_psd_map_p, psd_map_p, F_rdca_p_p, cross_rdca_p_p, coh_rdca_p_p, trans_rdca_p_p, phase_rdca_p_p, gain_rdca_p_p) = tfaCal(x=map_percent, y=vmeanr_percent)

#   data_frame = pd.DataFrame()
#   data_frame['F'] = F_brs
#   print(len(F_brs))
#   print(len(cross_brs))
#   print(len(trans_brs))

#   data_frame['cross_brs'] = cross_brs
#   data_frame['coh_brs'] = coh_brs
#   data_frame['trans_brs'] = trans_brs
#   data_frame['phase_brs'] = phase_brs
#   data_frame['gain_brs'] = gain_brs

#   data_frame['cross_ldca'] = cross_ldca
#   data_frame['coh_ldca'] = coh_ldca
#   data_frame['trans_ldca'] = trans_ldca
#   data_frame['phase_ldca'] = phase_ldca
#   data_frame['gain_ldca'] = gain_ldca

#   data_frame['cross_ldca_p'] = cross_ldca_p
#   data_frame['coh_ldca_p'] = coh_ldca_p
#   data_frame['trans_ldca_p'] = trans_ldca_p
#   data_frame['phase_ldca_p'] = phase_ldca_p
#   data_frame['gain_ldca_p'] = gain_ldca_p

#   data_frame['cross_ldca_p_p'] = cross_ldca_p_p
#   data_frame['coh_ldca_p_p'] = coh_ldca_p_p
#   data_frame['trans_ldca_p_p'] = trans_ldca_p_p
#   data_frame['phase_ldca_p_p'] = phase_ldca_p_p
#   data_frame['gain_ldca_p_p'] = gain_ldca_p_p

#   data_frame['cross_rdca'] = cross_rdca
#   data_frame['coh_rdca'] = coh_rdca
#   data_frame['trans_rdca'] = trans_rdca
#   data_frame['phase_rdca'] = phase_rdca
#   data_frame['gain_rdca'] = gain_rdca

#   data_frame['cross_rdca_p'] = cross_rdca_p
#   data_frame['coh_rdca_p'] = coh_rdca_p
#   data_frame['trans_rdca_p'] = trans_rdca_p
#   data_frame['phase_rdca_p'] = phase_rdca_p
#   data_frame['gain_rdca_p'] = gain_rdca_p

#   data_frame['cross_rdca_p_p'] = cross_rdca_p_p
#   data_frame['coh_rdca_p_p'] = coh_rdca_p_p
#   data_frame['trans_rdca_p_p'] = trans_rdca_p_p
#   data_frame['phase_rdca_p_p'] = phase_rdca_p_p
#   data_frame['gain_rdca_p_p'] = gain_rdca_p_p

#   print(data_frame)
#   data_frame.to_excel(path.split('.')[0] + '_result.xlsx')

def main(path):
  pass
  print('core')
  core(path)  

if __name__ == '__main__':
  main(sys.argv[1])