#%%
# conda install pandas numpy xlrd
import pandas;
import numpy;
import scipy.signal;
import matplotlib.pyplot;

#%%
data = pandas.read_excel('D:/ccode/BrainNowTfa/test.xlsx');
# data

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

#%% W3
# interpolate = numpy.arange(start=0, stop=time[len(rri) - 1], step=0.5);
rr_at_2hz = numpy.interp(x=interpolate, xp=time, fp=rri * 1000);
matplotlib.pyplot.plot(interpolate, rr_at_2hz);
matplotlib.pyplot.show();

#%% W4
# interpolate = numpy.arange(start=0, stop=time[len(rri) - 1], step=0.5);
hr_at_2hz = numpy.interp(x=interpolate, xp=time, fp=60/rri);
matplotlib.pyplot.plot(interpolate, hr_at_2hz);
matplotlib.pyplot.show();

#%% W5
# interpolate = numpy.arange(start=0, stop=time[len(sbp) - 1], step=0.5);
sbp_at_2hz = numpy.interp(x=interpolate, xp=time, fp=sbp);
matplotlib.pyplot.plot(interpolate, sbp_at_2hz);
matplotlib.pyplot.show();

#%% W6
# interpolate = numpy.arange(start=0, stop=time[len(dbp) - 1], step=0.5);
dbp_at_2hz = numpy.interp(x=interpolate, xp=time, fp=dbp);
matplotlib.pyplot.plot(interpolate, dbp_at_2hz);
matplotlib.pyplot.show();

#%% W7
# interpolate = numpy.arange(start=0, stop=time[len(mbp) - 1], step=0.5);
map_at_2hz = numpy.interp(x=interpolate, xp=time, fp=mbp);
matplotlib.pyplot.plot(interpolate, map_at_2hz);
matplotlib.pyplot.show();

#%% W8
# interpolate = numpy.arange(start=0, stop=time[len(mbp) - 1], step=0.5);
map_percent_at_2hz = numpy.interp(x=interpolate, xp=time, fp=mbp * numpy.mean(mbp) * 100);
matplotlib.pyplot.plot(interpolate, map_percent_at_2hz);
matplotlib.pyplot.show();

#%% W9
# print(cbfl)
# interpolate = numpy.arange(start=0, stop=time[len(cbfl) - 1], step=0.5);
vmean_i_at_2hz = numpy.interp(x=interpolate, xp=time, fp=cbfl);
print(vmean_i_at_2hz);
matplotlib.pyplot.plot(interpolate, vmean_i_at_2hz);
matplotlib.pyplot.show();

#%% W10
# interpolate = numpy.arange(start=0, stop=time[len(cbfl) - 1], step=0.5);
vmean_percent_i_at_2hz = numpy.interp(x=interpolate, xp=time, fp=cbfl * numpy.mean(cbfl) * 100);

#%% W11
# interpolate = numpy.arange(start=0, stop=time[len(cbfr) - 1], step=0.5);
vmean_r_at_2hz = numpy.interp(x=interpolate, xp=time, fp=cbfr);

#%% W12
# interpolate = numpy.arange(start=0, stop=time[len(cbfr) - 1], step=0.5);
vmean_percent_r_at_2hz = numpy.interp(x=interpolate, xp=time, fp=cbfr / numpy.mean(cbfr) * 100);
print(vmean_percent_r_at_2hz)
matplotlib.pyplot.plot(interpolate, vmean_percent_r_at_2hz);
matplotlib.pyplot.show();

#%% W13
rr_3_polynomial = numpy.poly1d(numpy.polyfit(x=interpolate, y=rr_at_2hz, deg=3));
print(rr_3_polynomial(interpolate))
matplotlib.pyplot.plot(interpolate, rr_3_polynomial(interpolate));
matplotlib.pyplot.show();

#%% W14
hr_3_polynomial = numpy.poly1d(numpy.polyfit(x=interpolate, y=hr_at_2hz, deg=3));

#%% W15
sbp_3_polynomial = numpy.poly1d(numpy.polyfit(x=interpolate, y=sbp_at_2hz, deg=3));

#%% W16
dbp_3_polynomial = numpy.poly1d(numpy.polyfit(x=interpolate, y=dbp_at_2hz, deg=3));

#%% W17
map_3_polynomial = numpy.poly1d(numpy.polyfit(x=interpolate, y=map_at_2hz, deg=3));

#%% W18
map_percent_3_polynomial = numpy.poly1d(numpy.polyfit(x=interpolate, y=map_percent_at_2hz, deg=3));

#%% W19
vmean_i_3_polynomial = numpy.poly1d(numpy.polyfit(x=interpolate, y=vmean_i_at_2hz, deg=3));

#%% W20
vmean_percent_i_3_polynomial = numpy.poly1d(numpy.polyfit(x=interpolate, y=vmean_percent_i_at_2hz, deg=3));

#%% W21
vmean_r_3_polynomial = numpy.poly1d(numpy.polyfit(x=interpolate, y=vmean_r_at_2hz, deg=3));

#%% W22
vmean_percent_r_3_polynomial = numpy.poly1d(numpy.polyfit(x=interpolate, y=vmean_percent_r_at_2hz, deg=3));

#%% W23
rr_detrended = rr_at_2hz - rr_3_polynomial(interpolate);
print(rr_detrended)
matplotlib.pyplot.plot(interpolate, rr_detrended);
matplotlib.pyplot.show();

#%% W24
hr_detrended = hr_at_2hz - hr_3_polynomial(interpolate);

#%% W25
sbp_detrended = sbp_at_2hz - sbp_3_polynomial(interpolate);

#%% W26
dbp_detrended = dbp_at_2hz - dbp_3_polynomial(interpolate);

#%% W27
map_detrended = map_at_2hz - map_3_polynomial(interpolate);

#%% W28
map_percent_at_2hz = map_percent_at_2hz - map_percent_3_polynomial(interpolate);

#%% W29
vmean_i_detrended = vmean_i_at_2hz - vmean_i_3_polynomial(interpolate);

#%% W30
vmean_percent_i_detrended = vmean_percent_i_at_2hz - vmean_percent_i_3_polynomial(interpolate);

#%% W31
vmean_r_detrended = vmean_r_at_2hz - vmean_r_3_polynomial(interpolate);

#%% W32
vmean_percent_r_detrended = vmean_percent_r_at_2hz - vmean_percent_r_3_polynomial(interpolate);

#%% W33
rr_psd = scipy.signal.welch(x=rr_detrended, nperseg=256);
matplotlib.pyplot.plot(rr_psd[0], rr_psd[1]);
matplotlib.pyplot.show();
print(rr_psd[1])

#%%
