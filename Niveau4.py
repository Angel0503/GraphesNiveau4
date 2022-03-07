# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 16:25:11 2022

@author: angel
"""

def extract_min(lst):
    min = lst[0]
    sommet = 0
    for i in range(1,len(lst)):
        print(f"{lst[i]}, {i}")
        if lst[i] < min:
            min = lst[i]
            sommet = i
    return sommet

poids=[
 [float('inf'),2,6,3],
 [2,float('inf'),8,5],
 [5,8,float('inf'),10],
 [5,5,10,float('inf')]
 ]

#print(poids)


"""
-une liste de liste poids décrivant le graphe pondéré : poids
-un sommet s étant le sommet de départ : s
"""
def djikstra(poids, s):
    dist = []
    pred = []
    aTraiter = []
    
    som = s

    """Initialiser les variables"""
    for i in range(len(poids)):
        dist.append([])
        pred.append([])
        if i != som:
            aTraiter.append(i)
        for j in range(len(poids)):
            if i != j and poids[i][j] != float('inf'):
                pred[i].append(j)
            else :
                pred[i].append(float('inf'))
    
    """Traitement"""
    #while(aTraiter != []):
    return dist
        
                
    
#print(djikstra(poids, 0))
    
    