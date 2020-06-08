from pyexcel_odsr import get_data
from scipy.stats.stats import pearsonr

def get_stocks(string):
    out = get_data(string)[string][1:]
    return [item[1] for item in out]

facebook, DB, Apple = get_stocks("FB.csv"), get_stocks("DB.csv"), get_stocks("AAPL.csv")

corr_AF = pearsonr(Apple, facebook)[0]
corr_DF = pearsonr(DB, facebook)[0]
corr_DA = pearsonr(Apple, DB)[0]

print("Apple, Facebook: ", corr_AF)
print("DB, Facebook: ", corr_DF)
print("Apple, DB: ", corr_DA)

