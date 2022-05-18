import numpy as np
from scipy.stats import chi2

def LikelihoodRatio_test(table):
    """
    入力された2x2クロス表に対して、尤度比検定を行う。
    
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
    log_likelihood_ratio = np.sum(table * np.log(table / H0))
    p_value = 1 - chi2.cdf(x=2*log_likelihood_ratio, df=1)
    return p_value

# 実際に使う
table = np.array([[4,6],
                  [8,30]])
# P値
LikelihoodRatio_test(table)