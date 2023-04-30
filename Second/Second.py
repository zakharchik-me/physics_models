y_x, Vy_t, Ay_t, y_t = int(input()), int(input()), int(input()), int(input())

V0x, L = 750000, 0.31
Beta = 238451188037.423664561501

def find_L(U):
    Vy, T, Lx, R = 0, 0, 0, (23-11)/2 * pow(10,-2)
    dV, dR, dT, Ay = 0, 0, pow(10, -12), 0

    while(R>0):
        dR = Vy * dT
        R = R - dR
        dV = Beta * U * (1 / R) * dT
        Vy = Vy + dV
        T = T + dT
        lx = V0x * T
        Ay = dV / dT
    return lx


test_u = 0.138811
test = find_L(test_u)
print(test)