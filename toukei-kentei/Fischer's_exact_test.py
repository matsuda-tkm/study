import numpy as np

# 階乗を計算する関数
def fact(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

# 二項係数を計算する関数
def comb(n,r):
    return fact(n) / fact(r) / fact(n-r)

# 超幾何分布の確率関数の値を計算する関数
def hypergeo(x,table):
    x_1s = table[0][0] + table[0][1]
    x_s1 = table[0][0] + table[1][0]
    x_s2 = table[0][1] + table[1][1]
    x_ss = x_s1 + x_s2
    return comb(x_s1, x) * comb(x_s2, x_1s-x) / comb(x_ss, x_1s)

# フィッシャーの正確検定
def fisher_exact(table, alternative):
    """
    入力された2x2クロス表に対して、フィッシャーの正確検定を行う。
    
    引数
    ---------------
    table : array like of ints
        検定の対象とする2x2クロス表
    alternative : {"greater", "less"}
        右側検定ならgreater, 左側検定ならless
    
    返り値
    ---------------
    p : float
        P値
    """
    x_11 = table[0][0]
    x_1s = table[0][0] + table[0][1]
    x_s1 = table[0][0] + table[1][0]
    x_s2 = table[0][1] + table[1][1]
    x_ss = x_s1 + x_s2
    
    m = max(0, x_1s+x_s1-x_ss)
    M = min(x_1s, x_s1)
    p = 0
    
    # オッズ比 > 1 の検定
    if alternative=="greater":
        for x in range(x_11, M+1):
            p += hypergeo(x, table)
    # オッズ比 < 1 の検定
    elif alternative=="less":
        for x in range(m, x_11+1):
            p += hypergeo(x, table)
    else:
        return None
    return p

# 実際に使う
t = np.array([[6,1],
             [3,4]])
# クロス表
print(t)
# P値
print(fisher_exact(t,"greater"))
