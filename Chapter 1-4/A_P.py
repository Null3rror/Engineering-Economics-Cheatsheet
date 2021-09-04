from P_F import *

def A_P(P, i, n, inf=False):
    if inf:
        return P * i
    t = (1 + i) ** n
    return P * ((i * t) / (t - 1))

def P_A(A, i, n, inf=False):
    if inf:
        return A / i
    t = (1 + i) ** n
    return A * ((t - 1) / (i * t))


def P_Aj(A1, i, j, n):
    if i == j:
        return (n * A1) / (1 + i)
    else:
        return A1 * ((1 - (F_P(1, j, n) * P_F(1, i, n))) / (i - j))
