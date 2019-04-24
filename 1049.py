# -*- coding: utf-8 -*-

subFilo = input()
Class = input()
subsistence = input()

if subFilo == 'vertebrado':
    if Class == 'ave':
        if subsistence == 'carnivoro':
            print('aguia')
            
        elif subsistence == 'onivoro':
            print('pomba')    
            
    elif Class == 'mamifero':
        if subsistence == 'onivoro':
            print('homem')
            
        elif subsistence == 'herbivoro':
            print('vaca')   
            
elif subFilo == 'invertebrado':
    if Class == 'inseto':
        if subsistence == 'hematofago':
            print('pulga')
            
        elif subsistence == 'herbivoro':
            print('lagarta')  
            
    elif Class == 'anelideo':
        if subsistence == 'hematofago':
            print('sanguessuga')
            
        elif subsistence == 'onivoro':
            print('minhoca')        