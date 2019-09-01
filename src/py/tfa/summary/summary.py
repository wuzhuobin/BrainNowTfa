#%%
import pandas as pd
from matplotlib import pyplot

input_xlsx = 'result.xlsx'
output = 'result.xlsx.png'

#%%
def summary(input_xlsx, output):
  pass
#%%
  data_frame = pd.read_excel(input_xlsx)
  fig = pyplot.figure(figsize=[8.27, 11.69])
  pyplot.subplots_adjust(wspace=0.2, hspace=0.3)
  pyplot.subplot(3, 2, 1)
  pyplot.plot(data_frame.F, data_frame.l_gain)
  pyplot.title('l_gain')
  pyplot.subplot(3, 2, 3)
  pyplot.plot(data_frame.F, data_frame.l_phase)
  pyplot.title('l_phase')
  pyplot.subplot(3, 2, 5)
  pyplot.plot(data_frame.F, data_frame.l_coherence)
  pyplot.title('l_coherence')
  pyplot.subplot(3, 2, 2)
  pyplot.plot(data_frame.F, data_frame.r_gain)
  pyplot.title('r_gain')
  pyplot.subplot(3, 2, 4)
  pyplot.plot(data_frame.F, data_frame.r_phase)
  pyplot.title('r_phase')
  pyplot.subplot(3, 2, 6)
  pyplot.plot(data_frame.F, data_frame.r_coherence)
  pyplot.title('r_coherence')
  fig.savefig(output)

#%%
