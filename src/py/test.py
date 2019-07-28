#%%
# conda install pandas numpy xlrd
import pandas;
import numpy;

#%%
data = pandas.read_excel('D:/ccode/BrainNowTfa/test.xlsx');
data

#%%
# column 1
rri = data['R-R'].values;
# column 2
time = data['Time'].values;
# column 3
sbp = data['sBP'].values;
# column 4
dbp = data['dBP'].values;
# column 5
mbp = data['mBP'].values;
# column 6
scbfl = data['sCBF_l'].values;
# column 7
dcbfl = data['dCBF_l'].values;
# column 8
cbfl = data['CBF_l'].values;
# column 9
scbfr = data['sCBF_r'].values;
# column 10
dcbfr = data['dCBF_r'].values;
# column 11
cbfr = data['CBF_r'].values;


interpolate = numpy.arange(start=0, stop=time[-1], step=0.5);

#%%
rri_at_2hz = numpy.interp(x=interpolate, xp=time, fp=rri * 1000);
print(rri_at_2hz);

#%%
hr_at_2hz = numpy.interp(x=interpolate, xp=time, fp=60/rri);
print(hr_at_2hz);



#%%
sbp_at_2hz = numpy.interp(x=interpolate, xp=time, fp=sbp);
dbp_at_2hz = numpy.interp(x=interpolate, xp=time, fp=dbp);
mbp_at_2hz = numpy.interp(x=interpolate, xp=time, fp=mbp);


#%%
