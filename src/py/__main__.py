import sys
import numpy as np
from core import *
def main(path):
  pass
  rr, time, sbp, dbp, mbp, scbfl, dcbfl, cbfl, scbfr, dcbfr, cbfr = loadExcel(path)
  y, x = interpolate2Hz(time, rr * 1000)
  rr = detrend(x, y)
  y, x = interpolate2Hz(time, 60 / rr)
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


if __name__ == '__main__':
  main(sys.argv[1])