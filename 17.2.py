import numpy as np
from scipy.stats.stats import pearsonr

def sample(N, p):
    x = np.random.randn(N)
    alpha = 0
    #alpha is set by the computer
    while(True):
        counter = 0
        for i in range(10):
            z = np.random.randn(N)
            y = x + alpha*z
            corr = pearsonr(x,y)[0]
            if corr - p < 0.001:
                counter += 1
        if counter > 4:
            break
        alpha += 0.01
    return x,y, alpha

for item in [(10000, 1), (10000, 0.5), (10000,0.2)]:
    x,y,a = sample(*item)
    print(f"Goal: {item[1]}, Alpha: {round(a, 2)}, Sampletest: {pearsonr(x,y)[0]}")