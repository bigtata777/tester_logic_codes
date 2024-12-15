print("modelado de datos")
import numpy as np 
import pandas as pd     
import re




def radar_atomico(distancia_misil:float, umbral:float, angulo:float, misiles_detectados = False):
    
    """ Esta funcion es un radar para detectar misiles"""
    factor_aleatorio = np.cos(angulo)
    
    if misiles_detectados:
        
        distancia_misil = np.sqrt(distancia_misil + factor_aleatorio)
        
        if distancia_misil < umbral:
            
            print("misil esta cerca de la base, evacuar")
            
        else:
            print("misil no esta cerca de la base, estar atentos")
            
    else:
        print("no se detecta misil")
        

    return print("distancia misil", distancia_misil)
        

        

if __name__ == "__main__":
    distancia = 10
    umbral  = 12
    angulo = 0.98
    detectados = True
    print(radar_atomico(distancia,umbral,angulo=angulo ,misiles_detectados = detectados))
    
    