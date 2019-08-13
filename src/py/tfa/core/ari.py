#%%
import numpy as np

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
    T = ARI[index][1]
    D = ARI[index][2]
    K = ARI[index][3]
    m = f * T
    n = 2 * D
    B = np.array([m**2, 1+n*m-2*m**2-K, m**2-n**m])
    A = B + np.array([0, K, 0])
  return B, A
#%%
  def ari(step, fs, L):
    pass

#%%

#%%
