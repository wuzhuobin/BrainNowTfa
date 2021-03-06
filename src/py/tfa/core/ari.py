#%%
import numpy as np
import scipy.signal as sg
# from matplotlib import pyplot

#%%
def app0(index, f):
  pass
  N = 15 * f
  t = np.arange(-5 * f, 10 * f - 1) / f

  if index == 0:
    pass
    B = np.array([1])
    A = np.array([1])
  else:
    pass
    ARI = np.array([
      [2, 1.6, 0.2], 
      [2, 1.5, 0.4],
      [2, 1.15, 0.6],
      [2, 0.9, 0.8],
      [1.9, 0.75, 0.9],
      [1.6, 0.65, 0.94],
      [1.2, 0.55, 0.96],
      [0.87, 0.52, 0.97],
      [0.65, 0.5, 0.98]
    ])
    T = ARI[index - 1][0]
    D = ARI[index - 1][1]
    K = ARI[index - 1][2]
    m = f * T
    # print(m)
    n = 2 * D
    # print(n)
    B = np.array([m**2, 1+n*m-2*m**2-K, m**2-n*m])
    A = B + np.array([0, K, 0])
  return B, A

# i = 0
# fs = 10
# print(app0(i, fs))
# i = 1
# fs = 10
# print(app0(i, fs))


#%%
def firpara(u, y, nb, option):
  pass
  u = u.T
  y = y.T
  N = len(u)
  if option == 'u':
    pass
    fai = np.zeros((N, nb), dtype=np.double)
    for i in range(0, N - nb):
      pass
      fai[i] = u[np.arange(i + nb - 1, i - 1, -1)]
    averfai = fai.T @ fai
    ny = y[np.arange(nb, len(y) - 1, dtype=np.double)]
    averfaiy = fai.T @ ny.T
    B = np.linalg.inv(averfai, dtype=np.double) @ averfaiy
  elif option == 'b':
    pass
    fai = np.zeros((N, nb), dtype=np.double)
    u = np.concatenate([np.zeros((nb - 1)), u])
    for i in range(0, N - 1):
      pass
      fai[i] = u[np.arange(i + nb - 1, i - 1, -1, dtype=np.int)]
    averfai = fai.T @ fai
    averfaiy = fai.T @ y.T
    B = np.linalg.inv(averfai) @ averfaiy
  return B, fai

# seg_x = [ -3.651437, -2.285495, -5.950580, -2.925318, -0.022436, 0.097322, 1.714918, 0.759397, -0.370812, 0.230426, -0.062103, -0.133841,-1.257611, 0.821082,-6.713676,-5.649186, 2.197243, 0.665995, 0.835562, 0.922694,-3.779185,-1.855731, 4.905784, 2.723674, 3.906812, 3.789671, 3.379661, 1.767550, 0.568296, 0.512269,-0.085780,-3.412937,-6.366575, 3.101856, 3.354800, 1.907026, 3.971007, 2.642626, 1.702065, 1.668018, 1.797033, 1.268710, 1.451449, 1.567453, 1.579481, 0.836254, 0.262332, 1.072359, 0.356604,-1.276993,-2.611706,-1.381688,-1.563065,-2.704743,-1.492614,-0.607329,-1.480669,-1.212626,-0.363515, 0.880223 ]
# seg_x = np.array(seg_x)
# seg_d = [  1.600626, 2.797586, 4.061193, 3.134042, 2.719090, 4.315664, 4.281765, 2.853247, 1.489275, 2.143933, 1.539153, 0.743276, 1.350720, 3.148315, 3.296778, 1.881944, 1.484214, 2.158514, 2.244669, 0.277391,-0.608257, 1.040416, 0.794725,-1.291406,-1.514089,-0.564219,-1.647191,-2.917339,-3.099709,-1.678569,-1.754640,-5.640400,-6.388446,-4.467569,-2.660348,-0.835971, 0.607580,-0.830480,-0.884775,-1.369167,-1.617404,-2.031363,-1.585155,-0.846770,-1.165071,-1.527810,-1.522304,-0.882046,-1.393789,-2.079259,-2.137367,-0.217242, 0.902253,-0.640568, 0.875114, 1.669845, 0.040695,-0.414999, 0.557912, 2.203785 ]
# seg_d = np.array(seg_d)
# L = 12
# option = 'b'
# hopt, fai = firpara(seg_x, seg_d, L, option)
# print('hopt', hopt)
# print('fai', fai)
# seg_x = np.array([-4.5363, -2.6129, 4.1486, 1.9665, 3.1497, 3.0325, 2.6225, 1.0104, -0.18885, -0.24488, -0.84293, -4.1701, -7.1237, 2.3447, 2.5977, 1.1499, 3.2139, 1.8855, 0.94492, 0.91087, 1.0399, 0.51156, 0.6943, 0.8103, 0.82233, 0.079106, -0.49482, 0.31521, -0.40054, -2.0341, -3.3689, -2.1388, -2.3202, -3.4619, -2.2498, -1.3645, -2.2378, -1.9698, -1.1207, 0.12308, 0.2731, 0.54356, 1.6284, 1.3461, -0.68464, -1.2089, 0.71176, -0.83333, -1.1239, 0.0063252, 0.57323, 0.20728, 1.2765, 2.1051, 1.2865, 1.4724, 1.9054, 0.24954, 0.12642, -0.35283])
# seg_d = np.array([0.20537, 1.854, 1.6084, -0.47778, -0.70046, 0.24941, -0.83356, -2.1037, -2.2861, -0.86494, -0.94101, -4.8268, -5.5748, -3.6539, -1.8467, -0.022343, 1.4212, -0.016852, -0.071147, -0.55554, -0.80378, -1.2177, -0.77153, -0.033142, -0.35144, -0.71418, -0.70868, -0.068418, -0.58016, -1.2656, -1.3237, 0.59639, 1.7159, 0.17306, 1.6887, 2.4835, 0.85432, 0.39863, 1.3715, 3.0174, 1.7987, 1.0026, 1.5504, 0.97167, -0.85076, -1.0809, -0.82278, -0.62782, -1.312, -0.66146, -0.37933, -0.8284, 0.7665, 2.113, 1.2933, 1.2192, 2.9441, 2.974, 2.4588, 2.4475])
# L = 12
# option = 'b'
# hopt, fai = firpara(seg_x, seg_d, L, option)
# print('hopt', hopt)
# print('fai', fai)


#%%
def ari(step, fs, L):
  pass
  step = sg.resample_poly(step, 10, fs)
  fs = 10
  P = np.arange(L[0] * fs, L[1] * fs)
  mse = np.zeros(10)
  for i in range(0, 10):
    B, A = app0(i, fs)
    # print(B, A)
    tstp = sg.lfilter(B, A, np.ones(len(step)), 0)
    # print(tstp)
    # mse = np.concatenate((mse, [np.mean(step[P] - tstp[P]) ** 2]))
    mse[i] = np.mean(step[P] - tstp[P]) ** 2
  val = np.sort(mse)
  iv = np.argsort(mse) + 1
  y1 = val[0]
  y2 = val[1]
  y3 = val[2]
  x1 = iv[0] - 1
  x2 = iv[1] - 1
  x3 = iv[2] - 1
  # print('val', val)
  # print('iv', iv)
  # print(x1, x2, x3)
  # print(y1, y2, y3)
  Q = np.array([
    [x1 ** 2, x1, 1],
    [x2 ** 2, x2, 1],
    [x3 ** 2, x3, 1]
  ])
  R = np.array([y1, y2, y3])
  X = np.linalg.inv(Q) @ R
  index = -X[1] / ( 2 * X[0])
  if index < 0 or index > 9:
    index = np.nan
  return index

# stepres = np.array([-0.094131, -0.17251, -0.34492, -0.46352, -0.66771, -0.81334, -0.9795, -1.1332, -1.217, -1.3448, -1.4674, -1.5574])
# fs = 1
# index = ari(stepres, fs, [1, 11])
# print(index)

# stepres = np.array([0.1256,0.13253,0.058541,0.098615,-0.059048,-0.17793,-0.29886,-0.3339,-0.42464,-0.59824,-0.68318,-0.61326])
# fs = 1
# index = ari(stepres, fs, [1, 11])
# print(index)

# stepres = np.array([0.45302, 0.47381, 0.44384, 0.20205, 0.20281, 0.30301, 0.24642, 0.28656, 0.24128, -0.13617, 0.049927, 0.39886])
# fs = 1
# index = ari(stepres, fs, [1, 11])
# print(index)

# stepres = np.array([0.46802, 0.56301, 0.52389, 0.43362, 0.33027, 0.0098022, -0.19765, -0.23352, -0.1719, 0.0058858, 0.35897, 0.43283])
# fs = 1
# index = ari(stepres, fs, [1, 11])
# print(index)

# stepres = np.array([0.45194, 0.42664, 0.36476, 0.3676, 0.37955, 0.2561, 0.23928, 0.18368, 0.18726, 0.20124, 0.38208, 0.32225])
# fs = 1
# index = ari(stepres, fs, [1, 11])
# print(index)

#%%
def variance5(x, d, fs):
  pass 
  L = fs * 12
  start = 0
  finish = 60 * fs - 1
  i = 0
  hopt_total = np.array([])
  ari_total = np.array([])
  while finish <= len(x):
    pass
    seg_x = x[0: finish]
    seg_d = d[0: finish]
    seg_x = seg_x - np.mean(seg_x)
    seg_d = seg_d - np.mean(seg_d)
    hopt, fai = firpara(seg_x, seg_d, L, 'b')
    hopt = np.array([hopt]).T
    Nt = 32
    # F, Frq = sg.freqz(hopt[0: 10], 1, Nt, fs=fs)
    # print(hopt)
    F, Frq = sg.freqz(hopt[0: 10], 1, Nt)
    # print('F', F, F.shape)
    # print('Frq', Frq, Frq.shape)
    # return
    if hopt_total.size == 0:
      pass
      hopt_total = hopt 
    else:
      pass
      hopt_total = np.block([hopt_total, hopt])
    set_ = sg.convolve(hopt, np.ones([L, 1]))
    stepres = set_[0: L]
    index = ari(stepres, fs, [0, 10])
    ari_total = np.concatenate([ari_total, [index]])

    start += 20
    finish += 20
    i += 1
  return ari_total, F

# bp = [4.1055, 5.4715, 1.8064, 4.8316, 7.7345, 7.8543, 9.4719, 8.5164, 7.3862, 7.9874, 7.6949, 7.6231, 6.4994, 8.578, 1.0433, 2.1078, 9.9542, 8.423, 8.5925, 8.6797, 3.9778, 5.9012, 12.663, 10.481, 11.664, 11.547, 11.137, 9.5245, 8.3253, 8.2692, 7.6712, 4.344, 1.3904, 10.859, 11.112, 9.664, 11.728, 10.4, 9.459, 9.425, 9.554, 9.0257, 9.2084, 9.3244, 9.3364, 8.5932, 8.0193, 8.8293, 8.1136, 6.48, 5.1453, 6.3753, 6.1939, 5.0522, 6.2643, 7.1496, 6.2763, 6.5443, 7.3934, 8.6372, 8.7872, 9.0577, 10.143, 9.8602, 7.8295, 7.3052, 9.2259, 7.6808, 7.3902, 8.5204, 9.0873, 8.7214, 9.7907, 10.619, 9.8006, 9.9865, 10.42, 8.7637, 8.6405, 8.1613, 9.0236, 8.1573, 7.1145, 6.8927, 7.6976, 7.637, 7.3, 6.9729, 8.2124, 8.6565, 7.7823, 8.4619, 8.5288, 9.7433, 8.9806, 8.9882, 9.5055, 14.085, 10.31, 8.8024, 10.933, 9.6597, 7.4242, 3.4061, 5.737, 6.8522, 3.5848, 4.18, 5.821, 4.3249, 3.7844, 3.154, 0.95011, -0.65584, -1.4524, -1.4755, -2.7394, -6.7893, -8.3624, -9.7929, -10.953, -11.019, -11.19, -11.453, -8.5728, -7.4781, -6.2746, -4.9361, -1.9121, -2.0387, -4.4165, -7.1673, -4.5839, 0.12823, 0.15936, 3.0325, 3.3392, 1.6327, -0.79807, 0.037498, 2.1688, 3.5067, 5.5519, 6.15, 6.755, 8.035, 13.772, 8.4876, 5.1894, 5.4881, 4.5702, 5.7638, 4.3873, 3.2006, 2.2325, 2.0224, 0.53363, 0.054794, 0.46262, 1.419, 1.8239, 2.2976, 7.1541, 6.4131, 5.5029, 5.729, 5.377, 5.8854, 5.2816, 5.3831, 5.3658, 7.6959, 11.304, 10.706, 14.606, 10.973, 4.6738, 5.2899, 4.2331, 3.8497, 4.2006, 6.5477, 6.3672, 5.239, 6.597, 5.2025, 5.0485, 6.1904, 5.8958, 5.5626, 5.5837, 8.1941, 7.1689, 7.1539, 5.8039, 4.4138, 4.8977, 4.3487, 5.0498, 4.8974, 5.0617, 4.2016, 3.6528, 4.1655, 4.2439, 4.4726, 4.5939, 4.4906, 6.0636, 7.1168, 8.9884, 9.2581, 8.155, 8.7787, 9.0145, 6.4794, 7.1451, 9.8189, 8.1973, 8.7988, 8.84, 8.1946, 7.2192, 7.3576, 8.2087, 7.0136, 4.4197, 3.3091, 3.4561, 5.4118, 6.1466, 5.3797, 6.2036, 5.6991, 10.741, 9.0479, 6.2274, 6.4441, 5.3594, 1.2861, 7.2767, 16.918, 5.5296, 7.8124, 5.9573, 0.81292, -0.59873, 1.2951, -0.65394, -1.4651, -0.54044, 1.4513, 0.62372, 1.0023, -2.025, -0.48125, 0.52021, -1.9714, -2.2623, -1.2807, 0.11802, -0.015027, -0.63813, 2.2043, 2.4141, -0.22598, 0.33418, 0.62799, 1.2121, 0.36413, 1.4757, 2.2757, 1.5768, 1.3505, 0.65445, 0.59072, 2.9838, 3.8245, 5.344, 5.4014, 4.903, 3.8338, 3.4454, 3.2283, 2.5285, 2.1917, 1.1064, -0.088273, 0.1234, -0.27907, -0.11945, -1.7167, -1.5833, 0.13324, -0.45281, 0.14059, 0.13029, 0.65806, 1.5498, 0.65672, 1.5492, 3.6549, 2.3181, 1.4521, 2.8151, 3.2372, 3.8967, 2.4364, 3.784, 3.3158, 2.5302, 3.6372, 3.8656, 4.2779, 3.5219, 3.8732, 4.5463, 5.0643, 5.4556, 4.2422, 4.6541, 5.6818, 5.0038, 4.1136, 3.852, 3.3755, 1.8209, 1.6854, 0.66654, 0.45022, -0.16148, -0.41137, 1.0959, 0.96228]
# bp = np.array(bp)
# rfv = [0.3295, 1.5265, 2.7901, 1.8629, 1.448, 3.0445, 3.0106, 1.5821, 0.21815, 0.87281, 0.26803, -0.52784, 0.079599, 1.8772, 2.0257, 0.61082, 0.21309, 0.88739, 0.97355, -0.99373, -1.8794, -0.23071, -0.4764, -2.5625, -2.7852, -1.8353, -2.9183, -4.1885, -4.3708, -2.9497, -3.0258, -6.9115, -7.6596, -5.7387, -3.9315, -2.1071, -0.66354, -2.1016, -2.1559, -2.6403, -2.8885, -3.3025, -2.8563, -2.1179, -2.4362, -2.7989, -2.7934, -2.1532, -2.6649, -3.3504, -3.4085, -1.4884, -0.36887, -1.9117, -0.39601, 0.39872, -1.2304, -1.6861, -0.71321, 0.93266, -0.28601, -1.0822, -0.53439, -1.1131, -2.9355, -3.1656, -2.9075, -2.7126, -3.3967, -2.7462, -2.4641, -2.9132, -1.3183, 0.028208, -0.79143, -0.86555, 0.8593, 0.8893, 0.37407, 0.36272, 1.5744, 0.45904, -0.66152, -0.73346, -0.23401, 0.19231, -0.085373, -0.54573, 1.0733, 1.1312, -0.28384, -0.53816, 0.65625, 1.8783, 1.499, 1.5421, 2.3283, 1.2308, 0.26981, 0.76629, 1.7193, 1.2373, -3.3022, -6.5631, -5.0977, -1.9976, 0.59204, 3.1028, 3.85, 1.7022, 0.66185, -0.40197, -3.2154, -5.2596, -4.9254, -4.4081, -5.0833, -5.2171, -4.3717, -4.5088, -5.4482, -4.3685, -5.3011, -6.3139, -5.6745, -3.9274, -3.4835, -4.2634, -3.4433, -2.9614, -2.6021, -2.9993, -2.218, -2.2244, -2.4586, -2.1394, -1.1484, -2.5247, -3.3339, -2.488, -0.28603, 0.92413, 0.44676, 0.1423, 1.7914, 2.3347, 1.0248, 0.93547, 1.9329, -0.10548, -0.53033, -0.14849, 0.14838, -0.96771, -1.45, -0.58113, -0.47479, -0.89688, 0.030455, 0.98679, -0.07378, 0.47481, 2.352, 3.27, 2.181, 1.5313, 1.8989, 3.3059, 1.7713, 1.5107, 2.0163, 3.0316, 3.7521, 1.7998, 2.2637, 3.0694, 4.8311, 4.0002, 2.6527, 2.2605, 2.2397, 2.1175, 0.73863, 0.40937, 0.7558, -1.5165, -2.0943, -1.3629, 0.66514, 0.76429, -0.23913, -0.054274, 1.2659, 0.15621, -1.7153, -2.4437, -1.0657, -0.96052, -1.8013, -1.4197, -1.1348, -2.7522, -4.0487, -2.6212, -0.57654, -0.52815, -1.4612, -1.6487, -1.3353, -0.1262, -1.1172, -2.0099, -0.4527, -0.97193, -1.7998, -0.69161, -0.91973, -0.85457, -1.2312, -0.96821, -0.9202, -1.0684, -0.72598, -0.15087, 1.3355, -0.91859, -4.0489, -2.9424, -1.2267, 2.3722, 4.9225, 4.7108, 3.9582, 2.1845, -1.1497, -3.0937, -2.6029, -2.5721, -3.2412, -2.1407, -1.9684, -3.7646, -5.1878, -3.2168, -3.2636, -4.4388, -3.6875, -2.3155, -2.0496, -2.6044, -0.92325, 1.6029, 1.5431, 1.4215, 2.2655, 3.3091, 2.085, -0.88712, -1.2506, -0.53621, 0.92379, 0.5769, -0.4177, -0.26654, -0.2951, -0.86807, -1.5871, -0.82923, 0.4093, -0.55642, -1.1572, -1.2307, 0.13393, 0.64674, 0.3815, 0.77543, 1.3786, 0.6241, -0.91863, 0.52382, 0.29959, -1.8154, -1.5116, 0.016128, 1.0302, 0.46282, -0.55656, -1.3879, -0.71007, 0.37018, -1.4258, -1.76, -1.88, -0.33655, -0.2106, -1.3567, -1.616, -1.302, -0.065924, -0.72736, -0.27105, -0.080769, -1.2328, -0.60831, 1.4503, 0.35573, -0.3968, 0.16585, 1.6876, 0.67626, 0.47018, 1.0905, 3.7775, 4.4558, 2.0057, 2.5489, 2.4277, 4.3822, 4.2034, 2.9546, 2.3362, 1.826, -0.43106, -0.82609, -1.6265, -2.9811, -3.6585, -1.9098, -0.96753, -1.3685, -0.61696, 0.20724, 2.2779, 1.1829]
# rfv = np.array(rfv)
# fs = 1  
# ari_total, F = variance5(bp, rfv, fs)
# print(np.nanmean(ari_total))
# print(F)

#%%
