from scipy.stats.stats import pearsonr
import matplotlib.pyplot as plt

x = [-1.6, -1.2, -0.6,  0.8,  0.2,  0.6, 2. , -1.1, -0.9, -0.7, 0.2,  1.5,  1.2, -1.3,  7.,  8.3]
y = [1.2,  1.4, -1.2,  0.2,  1.8, -0.2, 0.5,  1.9, -0.4,  0.2, 1.5, -0.7,  0.9,  1.4, 12.9, 14.1]

corr = pearsonr(x,y)[0]
print(corr)
plt.scatter(x,y)
plt.show()

'''
Ausreisser verzerren die Correlation
Ohne die letzten zwei Werte ist es -0.29 statt 0.88
'''
