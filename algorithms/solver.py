import numpy as np
import matplotlib.pyplot as plt
import itertools


# k次基本対称式
def symmetric(arr, k):
    s = 0
    for c in itertools.combinations(arr,k):
        p = np.prod([i for i in c])
        s += p
    return s

# 初期値が乗る円
def init_circle(R, n_split):
    return [np.cos(2*np.pi*n/n_split) + np.cos(2*np.pi*n/n_split)*1j for n in range(n_split)]

class EquationSolver:
    def __init__(self, coef, init_R):
        self.coef = np.array(coef)
        self.coef_ = np.array(coef)
        self.dim = len(self.coef) - 1
        self.init = init_circle(init_R, self.dim)
        self.roots = init_circle(init_R, self.dim)
        self.history = list()
        assert self.coef[0] != 0, "最高次の係数がゼロになっています"
        assert len(self.roots) == self.dim, "初期値を定めてください"
        # 最高次係数が１でないときの処理
        if self.coef[0] != 1:
            self.coef = self.coef / self.coef[0]
    
    # 多項式
    def f(self, x):
        return np.sum([e*x**(self.dim-i)for i,e in enumerate(self.coef)])

    # 求根アルゴリズム
    def search_root(self, i, m):
        prod = 1
        for idx, other_root in enumerate(self.roots):
            if idx != i:
                prod *= self.roots[i] - other_root
        new = self.roots[i] - self.f(self.roots[i]) / prod
        self.roots[i] = new
        
    # 探索
    def solve(self, iterations=10):
        self.iterations = iterations
        for n_iter in range(self.iterations):
            for i in range(self.dim):
                self.search_root(i, n_iter)
            self.history.append(self.roots.copy())
        self.history = np.array(self.history)
    
    
    # 係数検算
    def cal_coef_error(self, root):
         return np.array([abs(symmetric(root, i)*(-1)**(i) - self.coef[i]) for i in range(self.dim+1)])
        
    # 代入検算
    def cal_equation_error(self, root):
        return np.array([abs(self.f(x)) for x in root])
    
    # 結果を出力
    def summary(self):
        # 根の出力
        print("-"*10, "roots", "-"*10)
        for i,x in enumerate(self.roots):
            print(f"x_{i+1} = {x}")
        
        # 係数の出力(検算)
        print("-"*10, "coef", "-"*10)
        for i in range(self.dim+1):
            print(f"x^{self.dim-i} : {self.coef_[0]*symmetric(self.roots,i)*(-1)**(i)}")
    
        # 係数検算の結果を出力
        self.coef_error = self.cal_coef_error(self.roots)
        print("-"*10,"verification(coef)","-"*10)
        if all(self.coef_error < 0.001):
            print(f"good : {self.coef_error.mean()}")
        else:
            print(f"bad : {self.coef_error.mean()}")
        
        # 代入検算の結果を出力
        self.equation_error = self.cal_equation_error(self.roots)
        print("-"*10,"verification(substitution)","-"*10)
        if all(self.equation_error < 0.001):
            print(f"good : {self.equation_error.mean()}")
        else:
            print(f"bad : {self.equation_error.mean()}")
        
    
    def summary_graph(self):
        # 解の収束を可視化
        plt.figure(figsize=(10, 3))
        for i in range(len(self.roots)):
            plt.subplot(1, len(self.roots), i+1)
            plt.plot(range(len(self.history)), abs(self.history[:,i]))
            plt.title(f"x_{i+1}")
        plt.show()
        
        # 解を複素平面上に図示
        for i,x in enumerate(self.roots):
            plt.scatter(x.real, x.imag, label=f"x_{i+1}")
        plt.legend()
        plt.axhline(0, c="gray", alpha=0.5, linestyle="--")
        plt.axvline(0, c="gray", alpha=0.5, linestyle="--")
        plt.show()
