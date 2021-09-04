def P_G(G, i, n):
    t = (1 + i) ** n
    return (G / i) * (((t - 1) / (i * t)) - (n / t))

def A_G(G, i, n):
    t = (1 + i) ** n
    return G * ((1/i) - (n / (t - 1)))

