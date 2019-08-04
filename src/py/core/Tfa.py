#%%
import pandas as pd
import numpy as np
import scipy.signal as sg

#%%
def loadExcel(path):
  pass
  print('loadExcel')
  # column 1
  data = pd.read_excel(path)
  rri = data['R-R'].values
  # column 2
  time = data['Time'].values
  # column 3
  sbp = data['sBP'].values
  # column 4
  dbp = data['dBP'].values
  # column 5
  mbp = data['mBP'].values
  # column 6
  scbfl = data['sCBF_l'].values
  # column 7
  dcbfl = data['dCBF_l'].values
  # column 8
  cbfl = data['CBF_l'].values
  # column 9
  scbfr = data['sCBF_r'].values
  # column 10
  dcbfr = data['dCBF_r'].values
  # column 11
  cbfr = data['CBF_r'].values
  return rri, time, sbp, dbp, mbp, scbfl, dcbfl, cbfl, scbfr, dcbfr, cbfr



#%%

def interpolate2Hz(time, v):
  pass
  print('interpolate2Hz')
  interpolate = np.arange(start=0, stop=time[-1], step=0.5)
  v = np.interp(x=interpolate, xp=time, fp=v)
  return v, interpolate

#%%
def detrend(x, y):
  pass
  print('detrend')
  fitted = np.polyfit(x=x, y=y, deg=3)
  polynomial = np.poly1d(fitted)
  return y - polynomial(x)


#%%
def tfaCal(x, y):
  pass
  print('tfaCal')
  cross_F, cross = sg.csd(x=x, y=y, fs=2, return_onesided=False)
  psd_F_x, psd_x = sg.welch(x=x, fs=2, return_onesided=False)
  trans_F = psd_F_x
  trans = cross / psd_x
  phase = np.angle(cross)
  gain = np.abs(trans)
  return psd_F_x, psd_x, cross, trans, phase, gain

#%%
def psd(x):
  pass
  print('psd')
  return sg.welch(x=x, fs=2, return_onesided=True)

#%%
def saveExcel(v, path):
  pass
  print('saveExcel')
  data = pd.DataFrame()
  data['data'] = v
  data['data2'] = v
  data.to_excel(path)