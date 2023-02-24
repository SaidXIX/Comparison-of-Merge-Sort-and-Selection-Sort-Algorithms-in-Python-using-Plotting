import random
import time
import matplotlib.pyplot as plt

def gen_liste(taille):
    liste = []
    i = 0
    random.seed(50)
    for i in range(0, taille):
        liste.append(random.randint(0, 900))
    return liste


def tri_selection(tab):
    for i in range(len(tab)):
        # Trouver le min
        min = i
        for j in range(i + 1, len(tab)):
            if tab[min] > tab[j]:
                min = j

        tmp = tab[i]
        tab[i] = tab[min]
        tab[min] = tmp
    return tab


def triFusion(tab):
    if len(tab) > 1:
        mid = len(tab) // 2

        G = tab[:mid]  # sous-tableau gauche
        D = tab[mid:]  # sous-tableau droit

        triFusion(G)
        triFusion(D)

        # Fusion
        i = j = k = 0

        while i < len(G) and j < len(D):
            if G[i] < D[j]:
                tab[k] = G[i]
                i += 1
            else:
                tab[k] = D[j]
                j += 1
            k += 1

        while i < len(G):
            tab[k] = G[i]
            i += 1
            k += 1

        while j < len(D):
            tab[k] = D[j]
            j += 1
            k += 1


def main():
    x=[]
    y=[]
    t=[]
    for j in range(100, 2050, 50):
        t.append(j)
        L = gen_liste(j)
        times=0
        timef=0
        for i in range(0, 11):
            # début de calcul du temps d'exe du tri par séléction
            start = time.perf_counter()
            s = tri_selection(L)
            end = time.perf_counter()
            print(s)
            print("La taille du tableau est : ", len(L))
            print(i, "temps d'execution du tri par selection est")
            time0 = (end - start) * 1000
            times = times+time0
            print(time0)
            # debut de calcul du tri par fusion
            start1 = time.perf_counter()
            f = triFusion(L)
            end1 = time.perf_counter()
            print(f)
            print("La taille du tableau est : ", len(L))
            time1 = (end1 - start1) * 1000
            timef = timef+time1
            print(i, "temps d'execution du tri par fusion est")
            print(time1)
        x.append(times/10)
        y.append(timef/10)
    print("Temps moyen tri par selection: ", x)
    print("Temps moyen tri par fusion: ", y)
    print("Tableau des tailles : ", t)
    plt.plot(t, x)
    plt.plot(t, y)
    plt.show()


main()

















