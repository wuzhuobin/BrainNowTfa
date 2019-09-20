#%%
from os import path
import pandas as pd
from matplotlib import pyplot
import openpyxl as xl

input_xlsxs = ['test data output.xlsx']
output = 'result.xlsx'

#%%
def summary(input_xlsxs, output):
  pass
#%%
  # work sheets needed to be generated.
  groupSummary = pd.DataFrame()
  vlfLfHf = pd.DataFrame()
  work_sheets = {
    'l_gain': pd.DataFrame(),
    'l_phase': pd.DataFrame(),
    'l_coherence': pd.DataFrame(),
    'r_gain': pd.DataFrame(),
    'r_phase': pd.DataFrame(),
    'r_coherence': pd.DataFrame(),
  }
  # column_header are generated from input filenames.
  filename_prefix = list(map(lambda fileName: path.splitext(fileName)[0], input_xlsxs))
  for i in range(len(work_sheets)):
    pass
    key = list(work_sheets.keys())[i]
    work_sheets.keys()
    for j in range(len(input_xlsxs)):
      pass
      data_frame = pd.read_excel(input_xlsxs[j])
      if j == 0:
        work_sheets[key]['F'] = data_frame['F']
      if i == 0 & j == 0:
        groupSummary['F'] = data_frame['F']
      work_sheets[key][filename_prefix[j]] = data_frame[key]
    # calculate the mean value
    work_sheets[key]['Average'] = work_sheets[key][filename_prefix].mean(axis=1)
    groupSummary[key] = work_sheets[key]['Average']
    
  with pd.ExcelWriter(output) as writer:
    pass
    groupSummary.to_excel(writer, sheet_name='Group summary', index=False)
    # write an empty work sheet for place holding
    vlfLfHf.to_excel(writer, sheet_name='VLF_LF_HF', index=False)
    for key in work_sheets:
      pass
      work_sheets[key].to_excel(writer, sheet_name=key, index=False)
  # using openpyxl to manipulate data

#%% plot the summary png
  fig = pyplot.figure(figsize=[8.27, 11.69])
  pyplot.subplots_adjust(wspace=0.2, hspace=0.3)
  pyplot.subplot(3, 2, 1)
  pyplot.plot(groupSummary.F, groupSummary.l_gain)
  pyplot.title('l_gain')
  pyplot.subplot(3, 2, 3)
  pyplot.plot(groupSummary.F, groupSummary.l_phase)
  pyplot.title('l_phase')
  pyplot.subplot(3, 2, 5)
  pyplot.plot(groupSummary.F, groupSummary.l_coherence)
  pyplot.title('l_coherence')
  pyplot.subplot(3, 2, 2)
  pyplot.plot(groupSummary.F, groupSummary.r_gain)
  pyplot.title('r_gain')
  pyplot.subplot(3, 2, 4)
  pyplot.plot(groupSummary.F, groupSummary.r_phase)
  pyplot.title('r_phase')
  pyplot.subplot(3, 2, 6)
  pyplot.plot(groupSummary.F, groupSummary.r_coherence)
  pyplot.title('r_coherence')
  fig.savefig(output + '.png')

#%%
