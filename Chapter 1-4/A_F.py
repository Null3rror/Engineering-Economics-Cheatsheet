def A_F(F, i, n):
    t = (1 + i) ** n
    return F * (i / (t - 1))

def F_A(A, i, n):
    t = (1 + i) ** n
    return A * ((t - 1) / i)

def F_Aj(A, i, j, n):
    if i == j:
        return n * A * ((1 + j) ** (n - 1))
    t = (1 + i) ** n
    t2 = (1 + j) ** n
    return A * ((t - t2) / (i - j))
