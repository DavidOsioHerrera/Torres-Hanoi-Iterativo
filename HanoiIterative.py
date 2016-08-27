# autor: David Osio Herrera


def reco(x):
    # Funcion encaragda de recorrer los discos en los arreglos#
    r = len(x)
    for j in range(0, r - 1):
        # Elimina el primera dato del arreglo y mueve todos los demas una posicion adelante
        x[j] = x[j + 1]
        # (Deja el utlimo dato repetido)

    if r >= 1:
        # Elimina el ultimo dato del arreglo mientras exista
        x.pop()


def swapDisco(y, z):
    # Funcion encargada de hacer el movimiento legal necesario entre dos postes

    if len(y) == 0:
        # Si el poste Y esta vacio mueve el disco superior de Z a Y
        print("Mueve el disco", z[0], "de manera legal")
        temp = z[0]
        y.insert(0, temp)
        reco(z)

    elif (len(z) == 0) or (y[0] < z[0]):
        # Si el poste Z esta vacio o el disco superior en Y es menor que el de Z mueve el disco superior de Y a Z
        print("Mueve el disco", y[0], "de manera legal")
        temp = y[0]
        z.insert(0, temp)
        reco(y)

    else:  # Para cualquier otro escenario mueve el disco superor de Z a Y
        print("Mueve el disco", z[0], "de manera legal")
        temp = z[0]
        y.insert(0, temp)
        reco(z)


def hanoiSol(a, b, c):
    # Funccion encargada de solucionar el problema para cualquier caso
    print("Torre inicial A =", a)
    print("Torre final C =", c)
    print()

    if n % 2 != 0:
        # Soluciona los casos de discos impares
        for j in range(1, movs):
            if j % 3 == 1:
                swapDisco(a, c)
            if j % 3 == 2:
                swapDisco(a, b)
            if j % 3 == 0:
                swapDisco(b, c)

            print("A=", a)
            print("B=", b)
            print("C=", c)
            print()

    if n % 2 == 0:
        # Soluciona los casos de discos impares
        for j in range(1, movs):

            if j % 3 == 1:
                swapDisco(a, b)

            if j % 3 == 2:
                swapDisco(a, c)

            if j % 3 == 0:
                swapDisco(c, b)

            print("A=", a)
            print("B=", b)
            print("C=", c)
            print()

    print('Hecho!')
    print()
    print("Torre inicial A =", a)
    print("Torre final C =", c)

n = int(input('Numero de discos: '))  # Numero de discos
A = []  # Torre A
B = []  # Torre B
C = []  # Torre C
movs = pow(2, n)  # Moviemtos necesarios para resolver el problema (2^n)

for i in range(1, n + 1):
    # Crea el numero de discos necesarios en la torre A
    A.append(i)

hanoiSol(A, B, C)
