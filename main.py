# EXo 1.1.a
def noms():
    tab = []
    with open('Bom.txt') as f:
        lignes = f.readlines()
        for line in lignes:
            r = line.split(':')
            tab.append(r[0]) # Ajoute R au tablo
    return tab    
print(noms())
#EXo 1.1.b
def valeurs():
    tab = []
    with open('Bom.txt') as f:
        lignes = f.readlines()
        for line in lignes:
            r = line.split(':')
            tab.append(r[1])
    # REmove \n
    for i in range(len(tab)):
        tab[i] = tab[i].replace('\n', '')
    return tab

print(valeurs())

# EXo 1.1.c
def tablo():
    tablo = []
    for i in range(len(noms())):
        tablo.append(noms()[i] + ' : ' + valeurs()[i])
        tablo[i] = tablo[i].split(' : ')
    return tablo

#Afficher le nombre de resistances, valeur min et max et les noms respectifs
def maxelements(seq):
    ''' Return list of position(s) of largest element '''
    max_indices = []
    if seq:
        max_val = seq[0]
        for i,val in ((i,val) for i,val in enumerate(seq) if val >= max_val):
            if val == max_val:
                max_indices.append(i)
            else:
                max_val = val
                max_indices = [i]

    return max_indices
def minelements(seq):
    ''' Return list of position(s) of largest element '''
    min_indices = []
    if seq:
        min_val = seq[0]
        for i,val in ((i,val) for i,val in enumerate(seq) if val <= min_val):
            if val == min_val:
                min_indices.append(i)
            else:
                min_val = val
                min_indices = [i]

    return min_indices

print("Nombre de resistances : ", len(tablo()))
print("La resistance", tablo()[maxelements(valeurs())[0]][0], "a la resistence maximale, soit", tablo()[maxelements(valeurs())[0]][1], "homms")
print("La resistance", tablo()[minelements(valeurs())[0]][0], "a la resistence minimale, soit", tablo()[minelements(valeurs())[0]][1], "homms")

# EXo 1.2

def valeur_39(tab):
    tabo = []
    for i in range(len(tab)):
        if tab[i][1] == '39':
            tabo.append(tab[i][0])
        else:
            continue
    return "La resistance 39 kOhms est presente", len(tabo), "fois et ce sont les resistances : ", tabo
print(valeur_39(tablo()))
# Exo 1.3

def valeur_n(tab,n):
    tabo = []
    for i in range(len(tab)):
        if tab[i][1] == str(n):
            tabo.append(tab[i][0])
        else:
            continue
    return "La resistance",str(n), " Kohms est presente", len(tabo), "fois et ce sont les resistances : ", tabo

print(valeur_n(tablo(), 77))
# Exo 1.4
def tab_trie(tab):
    tabo, result = [], []
    for i in range(len(tab)):
        tabo.append(tab[i][1])
    for i in tabo:
        if i not in result:
            result.append(i)
        else:
            continue
    return "Liste des valeurs differentes : ", result, "Nombre de valeurs differentes : ", len(result)
print(tab_trie(tablo()))

# Exo 1.5

#Classifier les valeurs par tranches
def tranches(tab):
    tranche = []
    for i in range(len(tab)):
        if int(tab[i][1]) < 10:
            tranche.append([tab[i][0], tab[i][1], '0-10'])
        elif int(tab[i][1]) < 20:
            tranche.append([tab[i][0], tab[i][1], '10-20'])
        elif int(tab[i][1]) < 30:
            tranche.append([tab[i][0], tab[i][1], '20-30'])
        elif int(tab[i][1]) < 40:
            tranche.append([tab[i][0], tab[i][1], '30-40'])
        elif int(tab[i][1]) < 50:
            tranche.append([tab[i][0], tab[i][1], '40-50'])
        elif int(tab[i][1]) < 60:
            tranche.append([tab[i][0], tab[i][1], '50-60'])
        elif int(tab[i][1]) < 70:
            tranche.append([tab[i][0], tab[i][1], '60-70'])
        elif int(tab[i][1]) < 80:
            tranche.append([tab[i][0], tab[i][1], '70-80'])
        elif int(tab[i][1]) < 90:
            tranche.append([tab[i][0], tab[i][1], '80-90'])
        elif int(tab[i][1]) < 100:
            tranche.append([tab[i][0], tab[i][1], '90-100'])
        else:
            pass
    return tranche
print(tranches(tablo()))
# Exo 1.6
import matplotlib.pyplot as plt

def dico_valeurs(tab):
    dico_x = {}
    dico_y = {}
    for i in  range(len(tab)):
        if tab[i][2] not in dico_x:
            dico_x[tab[i][2]] = 1
        else:
            dico_x[tab[i][2]] += 1
    for i in range(len(tab)):
        if tab[i][1] not in dico_y:
            dico_y[tab[i][1]] = 1
        else:
            dico_y[tab[i][1]] += 1
    return dico_x, dico_y

def graphique():
    plt.plot(dico_valeurs(tranches(tablo()))[0].keys(), dico_valeurs(tranches(tablo()))[0].values(), color='g')
    plt.savefig('ploto.png')
graphique()



"""# Exo 2
from tkinter import *
window=Tk()
# add widgets here

window.geometry("1000x500")
window.mainloop()"""