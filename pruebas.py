def pos_fun_tiempo(x0,v,t):
    x = x0 + v*t
    if x > 100:
        print("el movil esta a mas de 100 metros")
    elif x == 100:
        print("el movil esta a 100 metros")
    elif x == 0:
        print("el movil no se movio")
    else:
        print("el movil esta a menos de 100 metros")
    return x
movil_1 = pos_fun_tiempo(10,20,5)
movil_2 = pos_fun_tiempo(50,10,5)
def distancia_entre_moviles(x1, x2):
    d = abs(x2 - x1 )
    print("estan separados",d, "metros")
    return d
distancia_entre_moviles(movil_1, movil_2)