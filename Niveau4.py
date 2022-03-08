# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 16:25:11 2022

@author: angel
"""
poids=[
 [float('inf'),2,6,3],
 [2,float('inf'),8,5],
 [5,8,float('inf'),10],
 [5,5,10,float('inf')]
 ]

def extract_min(lst):
    min = lst[0]
    sommet = 0
    for i in range(1,len(lst)):
        if lst[i] < min:
            min = lst[i]
            sommet = i
    return sommet

def succ(lst):
    success=[]
    for i in range(len(lst)):
        if lst[i] != float('inf'):
            success.append(i)
    return success


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
        if i != som:
            aTraiter.append(i)
        if i == s:
            dist.append(None)
            pred.append(None)
        else :
            dist.append('Null')
            pred.append('Null')
    print(dist)  
    
    """Traitement"""
    for i in range(len(poids)):
        successeur = succ(poids[i])
        for val in successeur:
            if val in aTraiter:
                dist[val] = poids[val][extract_min(poids[val])]
        if i == 2:                
            aTraiter.pop(1)
        print(dist)
                
        
        
        
        
        
        
       
        
    
        
                
    
print(djikstra(poids, 0))
    
    