#%%
# conda install pandas numpy xlrd
import pandas;
import numpy;
import scipy.signal;
import matplotlib.pyplot;

#%%
# data = pandas.read_excel('D:/ccode/BrainNowTfa/test.xlsx');
data = pandas.read_excel('D:/ccode/BrainNowTfa/patient orinigal data.xlsx')

# data

#%%
# column 1
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


interpolate = numpy.arange(start=0, stop=time[-1], step=0.5)

#%% W3 xyinterp(W2,(col(W1,1)*1000),0.5)
# interpolate = numpy.arange(start=0, stop=time[len(rri) - 1], step=0.5);
rr_at_2hz = numpy.interp(x=interpolate, xp=time, fp=rri * 1000)
matplotlib.pyplot.plot(interpolate, rr_at_2hz)
matplotlib.pyplot.show()

#%% W4 xyinterp(W2,60/col(W1,1),0.5)
# interpolate = numpy.arange(start=0, stop=time[len(rri) - 1], step=0.5);
hr_at_2hz = numpy.interp(x=interpolate, xp=time, fp=60/rri)
matplotlib.pyplot.plot(interpolate, hr_at_2hz)
matplotlib.pyplot.show()

#%% W5   xyinterp(W2,col(W1,3),0.5)
# interpolate = numpy.arange(start=0, stop=time[len(sbp) - 1], step=0.5);
sbp_at_2hz = numpy.interp(x=interpolate, xp=time, fp=sbp)
matplotlib.pyplot.plot(interpolate, sbp_at_2hz)
matplotlib.pyplot.show()

#%% W6  xyinterp(W2,col(W1,4),0.5)
# interpolate = numpy.arange(start=0, stop=time[len(dbp) - 1], step=0.5);
dbp_at_2hz = numpy.interp(x=interpolate, xp=time, fp=dbp)
matplotlib.pyplot.plot(interpolate, dbp_at_2hz)
matplotlib.pyplot.show()

#%% W7  xyinterp(W2,col(W1,5),0.5)
# interpolate = numpy.arange(start=0, stop=time[len(mbp) - 1], step=0.5);
map_at_2hz = numpy.interp(x=interpolate, xp=time, fp=mbp)
matplotlib.pyplot.plot(interpolate, map_at_2hz)
matplotlib.pyplot.show()

#%% W8 xyinterp(W2,(col(W1,5)/mean(col(W1,5))*100),0.5)
# interpolate = numpy.arange(start=0, stop=time[len(mbp) - 1], step=0.5);
map_percent_at_2hz = numpy.interp(x=interpolate, xp=time, fp=mbp / numpy.mean(mbp) * 100)
matplotlib.pyplot.plot(interpolate, map_percent_at_2hz)
matplotlib.pyplot.show()

#%% W9  xyinterp(W2,col(W1,8),0.5)
# print(cbfl)
# interpolate = numpy.arange(start=0, stop=time[len(cbfl) - 1], step=0.5);
vmean_i_at_2hz = numpy.interp(x=interpolate, xp=time, fp=cbfl)
# print(vmean_i_at_2hz);
matplotlib.pyplot.plot(interpolate, vmean_i_at_2hz)
matplotlib.pyplot.show()

#%% W10 xyinterp(W2,(col(W1,8)/mean(col(W1,8))*100),0.5)
# interpolate = numpy.arange(start=0, stop=time[len(cbfl) - 1], step=0.5);
vmean_percent_i_at_2hz = numpy.interp(x=interpolate, xp=time, fp=cbfl / numpy.mean(cbfl) * 100)
matplotlib.pyplot.plot(interpolate, vmean_percent_i_at_2hz)
matplotlib.pyplot.show()

#%% W11   xyinterp(W2,col(W1,11),0.5)
# interpolate = numpy.arange(start=0, stop=time[len(cbfr) - 1], step=0.5);
vmean_r_at_2hz = numpy.interp(x=interpolate, xp=time, fp=cbfr)
matplotlib.pyplot.plot(interpolate, vmean_r_at_2hz)
matplotlib.pyplot.show()

#%% W12 xyinterp(W2,(col(W1,11)/mean(col(W1,11))*100),0.5)
# interpolate = numpy.arange(start=0, stop=time[len(cbfr) - 1], step=0.5);
vmean_percent_r_at_2hz = numpy.interp(x=interpolate, xp=time, fp=cbfr / numpy.mean(cbfr) * 100)
matplotlib.pyplot.plot(interpolate, vmean_percent_r_at_2hz)
matplotlib.pyplot.show()

#%% W13 Polygraph(polyfit(W3,3,-1),xvals(W3))
rr_3_polynomial = numpy.poly1d(numpy.polyfit(x=interpolate, y=rr_at_2hz, deg=3))
# print(rr_3_polynomial(interpolate))
matplotlib.pyplot.plot(interpolate, rr_3_polynomial(interpolate))
matplotlib.pyplot.show()

#%% W14 Polygraph(polyfit(W4,3,-1),xvals(W4))
hr_3_polynomial = numpy.poly1d(numpy.polyfit(x=interpolate, y=hr_at_2hz, deg=3))
matplotlib.pyplot.plot(interpolate, hr_3_polynomial(interpolate))
matplotlib.pyplot.show()

#%% W15 Polygraph(polyfit(W5,3,-1),xvals(W5))
sbp_3_polynomial = numpy.poly1d(numpy.polyfit(x=interpolate, y=sbp_at_2hz, deg=3))
matplotlib.pyplot.plot(interpolate, sbp_3_polynomial(interpolate))
matplotlib.pyplot.show()

#%% W16 Polygraph(polyfit(W6,3,-1),xvals(W6))
dbp_3_polynomial = numpy.poly1d(numpy.polyfit(x=interpolate, y=dbp_at_2hz, deg=3))
matplotlib.pyplot.plot(interpolate, dbp_3_polynomial(interpolate))
matplotlib.pyplot.show()

#%% W17 Polygraph(polyfit(W7,3,-1),xvals(W7))
map_3_polynomial = numpy.poly1d(numpy.polyfit(x=interpolate, y=map_at_2hz, deg=3))
matplotlib.pyplot.plot(interpolate, map_3_polynomial(interpolate))
matplotlib.pyplot.show()

#%% W18 Polygraph(polyfit(W8,3,-1),xvals(W8))
map_percent_3_polynomial = numpy.poly1d(numpy.polyfit(x=interpolate, y=map_percent_at_2hz, deg=3))
matplotlib.pyplot.plot(interpolate, map_3_polynomial(interpolate))
matplotlib.pyplot.show()

#%% W19 Polygraph(polyfit(W9,3,-1),xvals(W9)) 
vmean_i_3_polynomial = numpy.poly1d(numpy.polyfit(x=interpolate, y=vmean_i_at_2hz, deg=3))
matplotlib.pyplot.plot(interpolate, vmean_i_3_polynomial(interpolate))
matplotlib.pyplot.show()

#%% W20 Polygraph(polyfit(W10,3,-1),xvals(W10))
vmean_percent_i_3_polynomial = numpy.poly1d(numpy.polyfit(x=interpolate, y=vmean_percent_i_at_2hz, deg=3))
matplotlib.pyplot.plot(interpolate, vmean_percent_i_3_polynomial(interpolate))
matplotlib.pyplot.show()

#%% W21 Polygraph(polyfit(W11,3,-1),xvals(W11))
vmean_r_3_polynomial = numpy.poly1d(numpy.polyfit(x=interpolate, y=vmean_r_at_2hz, deg=3))
matplotlib.pyplot.plot(interpolate, vmean_r_3_polynomial(interpolate))
matplotlib.pyplot.show()

#%% W22 Polygraph(polyfit(W12,3,-1),xvals(W12))
vmean_percent_r_3_polynomial = numpy.poly1d(numpy.polyfit(x=interpolate, y=vmean_percent_r_at_2hz, deg=3))
matplotlib.pyplot.plot(interpolate, vmean_percent_r_3_polynomial(interpolate))
matplotlib.pyplot.show()

#%% W23 W3-W13
rr_detrended = rr_at_2hz - rr_3_polynomial(interpolate)
# print(rr_detrended)
matplotlib.pyplot.plot(interpolate, rr_detrended)
matplotlib.pyplot.show()

#%% W24 W4-W14
hr_detrended = hr_at_2hz - hr_3_polynomial(interpolate)
matplotlib.pyplot.plot(interpolate, hr_detrended)
matplotlib.pyplot.show()

#%% W25 W5-W15
sbp_detrended = sbp_at_2hz - sbp_3_polynomial(interpolate)
matplotlib.pyplot.plot(interpolate, sbp_detrended)
matplotlib.pyplot.show()

#%% W26 W6-W16
dbp_detrended = dbp_at_2hz - dbp_3_polynomial(interpolate)
matplotlib.pyplot.plot(interpolate, dbp_detrended)
matplotlib.pyplot.show()

#%% W27 W7-W17
map_detrended = map_at_2hz - map_3_polynomial(interpolate)
matplotlib.pyplot.plot(interpolate, map_detrended)
matplotlib.pyplot.show()

#%% W28 W8-W18
map_percent_detrended = map_percent_at_2hz - map_percent_3_polynomial(interpolate)
matplotlib.pyplot.plot(interpolate, map_percent_detrended)
matplotlib.pyplot.show()

#%% W29 W9-W19
vmean_i_detrended = vmean_i_at_2hz - vmean_i_3_polynomial(interpolate)
matplotlib.pyplot.plot(interpolate, vmean_i_detrended)
matplotlib.pyplot.show()

#%% W30 W10-W20
vmean_percent_i_detrended = vmean_percent_i_at_2hz - vmean_percent_i_3_polynomial(interpolate)
matplotlib.pyplot.plot(interpolate, vmean_percent_i_detrended)
matplotlib.pyplot.show()

#%% W31 W11-W21
vmean_r_detrended = vmean_r_at_2hz - vmean_r_3_polynomial(interpolate)
matplotlib.pyplot.plot(interpolate, vmean_r_detrended)
matplotlib.pyplot.show()

#%% W32 W12-W22
vmean_percent_r_detrended = vmean_percent_r_at_2hz - vmean_percent_r_3_polynomial(interpolate)
matplotlib.pyplot.plot(interpolate, vmean_percent_r_detrended)
matplotlib.pyplot.show()

#%% W33 extract(Wpsd(W23,256,128,256), 1,64)
rr_psd = scipy.signal.welch(x=rr_detrended, nperseg=256, noverlap=128, nfft=256, fs=2, window='hann', return_onesided=True)
# rr_psd = scipy.signal.welch(x=rr_detrended, nperseg=256, noverlap=128, nfft=256, fs=2, window='boxcar', return_onesided=True)
# rr_psd = scipy.signal.welch(x=rr_detrended, nperseg=256, noverlap=128, nfft=256, fs=2, window='triang', return_onesided=True)
# rr_psd = scipy.signal.welch(x=rr_detrended, nperseg=256, noverlap=128, nfft=256, fs=2, window='hamming', return_onesided=True)
# rr_psd = scipy.signal.welch(x=rr_detrended, nperseg=256, noverlap=128, nfft=256, fs=2, window='bartlett', return_onesided=True)
# rr_psd = scipy.signal.welch(x=rr_detrended, nperseg=256, noverlap=128, nfft=256, fs=2, window='flattop', return_onesided=True)
# rr_psd = scipy.signal.welch(x=rr_detrended, nperseg=256, noverlap=128, nfft=256, fs=2, window='gaussian', return_onesided=True)
matplotlib.pyplot.plot(rr_psd[0][0: 63], rr_psd[1][0: 63])
matplotlib.pyplot.show()
# print(rr_psd[1].shape)
# print(rr_psd[1][0:63])

#%% W34 extract(Wpsd(W24,256,128,256), 1,64)
hr_psd = scipy.signal.welch(x=hr_detrended, nperseg=256, noverlap=128, nfft=256, fs=2, window='hann', return_onesided=True)
matplotlib.pyplot.plot(hr_psd[0][0: 63], hr_psd[1][0: 63])
matplotlib.pyplot.show()

#%% W35  extract(Wpsd(W25,256,128,256), 1,64)
sbp_psd = scipy.signal.welch(x=sbp_detrended, nperseg=256, noverlap=128, nfft=256, fs=2, window='hann', return_onesided=True)
matplotlib.pyplot.plot(sbp_psd[0][0: 63], sbp_psd[1][0: 63])
matplotlib.pyplot.show()

#%% W36 extract(Wpsd(W26,256,128,256), 1,64)
dbp_psd = scipy.signal.welch(x=dbp_detrended, nperseg=256, noverlap=128, nfft=256, fs=2, window='hann', return_onesided=True)
matplotlib.pyplot.plot(dbp_psd[0][0: 63], dbp_psd[1][0: 63])
matplotlib.pyplot.show()

#%% W37 extract(Wpsd(W27,256,128,256), 1,64)
map_psd = scipy.signal.welch(x=map_detrended, nperseg=256, noverlap=128, nfft=256, fs=2, window='hann', return_onesided=True)
matplotlib.pyplot.plot(map_psd[0][0: 63], map_psd[1][0: 63])
matplotlib.pyplot.show()

#%% W38 extract(Wpsd(W28,256,128,256), 1,64)
map_percent_psd = scipy.signal.welch(x=map_detrended, nperseg=256, noverlap=128, nfft=256, fs=2, window='hann', return_onesided=True)
matplotlib.pyplot.plot(map_percent_psd[0][0: 63], map_percent_psd[1][0: 63])
matplotlib.pyplot.show()

#%% W39 extract(Wpsd(W29,256,128,256), 1,64)
vmean_i_psd = scipy.signal.welch(x=vmean_i_detrended, nperseg=256, noverlap=128, nfft=256, fs=2, window='hann', return_onesided=True)
matplotlib.pyplot.plot(vmean_i_psd[0][0: 63], vmean_i_psd[1][0: 63])
matplotlib.pyplot.show()

#%% W40 extract(Wpsd(W30,256,128,256), 1,64)
vmean_percent_i_psd = scipy.signal.welch(x=vmean_percent_i_detrended, nperseg=256, noverlap=128, nfft=256, fs=2, window='hann', return_onesided=True)
matplotlib.pyplot.plot(vmean_percent_i_psd[0][0: 63], vmean_percent_i_psd[1][0: 63])
matplotlib.pyplot.show()


#%% W41  extract(Wpsd(W31,256,128,256), 1,64)
vmean_r_psd = scipy.signal.welch(x=vmean_r_detrended, nperseg=256, noverlap=128, nfft=256, fs=2, window='hann', return_onesided=True)
matplotlib.pyplot.plot(vmean_r_psd[0][0: 63], vmean_r_psd[1][0:63])
matplotlib.pyplot.show()

#%% W42 extract(Wpsd(W32,256,128,256), 1,64)
vmean_percent_r_psd = scipy.signal.welch(x=vmean_percent_r_detrended, nperseg=256, noverlap=128, nfft=256, fs=2, window='hann', return_onesided=True)
matplotlib.pyplot.plot(vmean_percent_r_psd[0], vmean_percent_r_psd[1])
matplotlib.pyplot.show()

#%% W43 extract(Wpxy(W25,W23,256,128,256), 1, 64)
brs_cross_spectra = scipy.signal.csd(x=sbp_detrended, y=rr_detrended, fs=2, window='hann', nperseg=256, noverlap=128, nfft=256, return_onesided=False)
# brs_cross_spectra = scipy.signal.csd(x=sbp_detrended, y=rr_detrended, fs=2, window='hann', nperseg=256, noverlap=128, nfft=256, return_onesided=False)
matplotlib.pyplot.plot(brs_cross_spectra[0][0: 63], brs_cross_spectra[1][0: 63])
matplotlib.pyplot.show()


#%% W44  mag(extract(Wtxy(W25,W23,256,128,256),1,64))
brs_gain = brs_cross_spectra[1] / scipy.signal.welch(x=sbp_detrended, fs=2, window='hann', nperseg=256, noverlap=128, nfft=256, return_onesided=False)[1]
matplotlib.pyplot.plot(rr_psd[0][0: 63], numpy.absolute(brs_gain[0: 63]))
matplotlib.pyplot.show()

#%% W45 phase (W43)
brs_phase = [brs_cross_spectra[0], numpy.angle(brs_cross_spectra[1])]
matplotlib.pyplot.plot(brs_phase[0][0: 63], brs_phase[1][0: 63])
matplotlib.pyplot.show()


#%% W46 extract(Wcoh(W25,W23,256,128,256),1,64)
# print(sbp_detrended)
# print(rr_detrended)
brs_coherence = scipy.signal.coherence(x=sbp_detrended, y=rr_detrended, fs=2, window='hann', nperseg=256, noverlap=128, nfft=256)
matplotlib.pyplot.plot(brs_coherence[0][0: 63], brs_coherence[1][0: 63])
matplotlib.pyplot.show()

#%% W47 extract(Wpxy(W27,W29,256,128,256), 1, 64)
l_dca_cross_spectra = scipy.signal.csd(x=map_detrended, y=vmean_i_detrended, fs=2, window='hann', nperseg=256, noverlap=128, nfft=256, return_onesided=False)
matplotlib.pyplot.plot(l_dca_cross_spectra[0][0: 63], l_dca_cross_spectra[1][0: 63])
matplotlib.pyplot.show()

#%% W48 mag(extract(Wtxy(W27,W29,256,128,256),1,64))
l_dca_gain = l_dca_cross_spectra[1] / scipy.signal.welch(x=map_detrended, fs=2, window='hann', nperseg=256, noverlap=128, nfft=256, return_onesided=False)[1]
matplotlib.pyplot.plot(l_dca_cross_spectra[0][0: 63], numpy.absolute(l_dca_gain[0: 63]))
matplotlib.pyplot.show()

#%% W49 mag(extract(Wtxy(W27,W30,256,128,256),1,64))
l_dca_gain_percent = scipy.signal.csd(x=map_detrended, y=vmean_percent_i_detrended, fs=2, window='hann', nperseg=256, noverlap=128, nfft=256, return_onesided=False)[1] / scipy.signal.welch(map_detrended, fs=2, window='hann', nperseg=256, noverlap=128, nfft=256, return_onesided=False)[1]
matplotlib.pyplot.plot(map_psd[0][0: 63], numpy.absolute(l_dca_gain_percent[0: 63]))
matplotlib.pyplot.show()

#%% W50  mag(extract(Wtxy(W28,W30,256,128,256),1,64))
l_dca_gain_percent_percent = scipy.signal.csd(x=map_percent_detrended, y=vmean_percent_i_detrended, fs=2, window='hann', nperseg=256, noverlap=128, nfft=256, return_onesided=False)[1]/scipy.signal.welch(map_detrended, fs=2, window='hann', nperseg=256, noverlap=128, nfft=256, return_onesided=False)[1]
matplotlib.pyplot.plot(map_psd[0][0: 63], numpy.absolute(l_dca_gain_percent_percent[0: 63]))
matplotlib.pyplot.show()

#%% W51 phase (W47)
l_dca_phase = [l_dca_cross_spectra[0], numpy.angle(l_dca_cross_spectra[1])]
matplotlib.pyplot.plot(l_dca_phase[0][0: 63], l_dca_phase[1][0: 63])
matplotlib.pyplot.show()


#%% W52 extract(Wcoh(W27,W29,256,128,256),1,64)
l_dca_coherence = scipy.signal.coherence(x=map_detrended, y=vmean_i_detrended, fs=2.0, window='hann', nperseg=256, noverlap=128, nfft=256)
matplotlib.pyplot.plot(l_dca_coherence[0][0: 63], l_dca_coherence[1][0: 63])
matplotlib.pyplot.show()

#%% W53 extract(Wpxy(W27,W31,256,128,256), 1, 64)
r_dca_cross_spectra = scipy.signal.csd(x=map_detrended, y=vmean_r_detrended, fs=2, window='hann', nperseg=256, noverlap=128, nfft=256, return_onesided=False)
matplotlib.pyplot.plot(r_dca_cross_spectra[0][0: 63], r_dca_cross_spectra[1][0: 63])
matplotlib.pyplot.show()

#%% W54  mag(extract(Wtxy(W27,W31,256,128,256),1,64))
r_dca_gain = r_dca_cross_spectra[1] / scipy.signal.welch(x=map_detrended, fs=2, window='hann', nperseg=256, noverlap=128, nfft=256, return_onesided=False)[1]
matplotlib.pyplot.plot(map_psd[0][0: 63], numpy.absolute(r_dca_gain[0: 63]))
matplotlib.pyplot.show()


#%% W55 mag(extract(Wtxy(W27,W32,256,128,256),1,64))
r_dca_gain_percent = scipy.signal.csd(x=map_detrended, y=vmean_percent_r_detrended, fs=2, window='hann', nperseg=256, noverlap=128, nfft=256, return_onesided=False)[1] / scipy.signal.welch(x=map_detrended, fs=2, window='hann', nperseg=256, noverlap=128, nfft=256, return_onesided=False)[1]
matplotlib.pyplot.plot(map_psd[0][0: 63], numpy.absolute(r_dca_gain_percent[0: 63]))
matplotlib.pyplot.show()

#%% W56  mag(extract(Wtxy(W28,W32,256,128,256),1,64))
r_dca_gain_percent_percent = scipy.signal.csd(x=map_percent_detrended, y=vmean_percent_i_detrended, fs=2, window='hann', nperseg=256, noverlap=128, nfft=256, return_onesided=True)[1]/map_psd[1]
matplotlib.pyplot.plot(map_psd[0][0: 63], numpy.absolute(r_dca_gain_percent_percent[0: 63]))
matplotlib.pyplot.show()


#%% W57 phase (W53)
r_dca_phase = [r_dca_cross_spectra[0], numpy.angle(r_dca_cross_spectra[1])]
matplotlib.pyplot.plot(r_dca_phase[0][0: 63], r_dca_phase[1][0: 63])
matplotlib.pyplot.show()

#%% W58 extract(Wcoh(W27,W31,256,128,256),1,64)
r_dca_coherence = scipy.signal.coherence(x=map_detrended, y=vmean_r_detrended, fs=2.0, window='hann', nperseg=256, noverlap=128, nfft=256)
matplotlib.pyplot.plot(r_dca_coherence[0][0: 63], r_dca_coherence[1][0: 63])
matplotlib.pyplot.show()

#%%
#%%

#%%
'W23.xlsx'.split('.')[0] + 'asdfasd.xlsx'

#%%