import numpy as np
from scipy.stats import chi2

def chi2_test(table):
    """
    入力された2x2クロス表に対して、適合度カイ二乗検定を行う。
    
    引数
    ---------------
    table : array like of ints
        検定の対象とする2x2クロス表

    返り値
    ---------------
    p : float
        P値
    """
    theta_hat = np.sum(table, axis=0)[0] / np.sum(table)
    H0 = np.array([[np.sum(table, axis=1)[0]*theta_hat, np.sum(table, axis=1)[0]*(1-theta_hat)],
                   [np.sum(table, axis=1)[1]*theta_hat, np.sum(table, axis=1)[1]*(1-theta_hat)]])
    chi_square = np.sum((table-H0)**2 / H0)
    p_value = 1 - chi2.cdf(x=chi_square, df=1)
    return p_value

# 実際に使う
t = np.array([[4,6],
              [8,30]])
# P値
print(chi2_test(t))
