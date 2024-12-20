print("modelado de datos")
import numpy as np 
import pandas as pd     
import re


def radar_atomico(distancia_misil:float, 
                  umbral:float, 
                  angulo:float,
                  localizacion:tuple,
                  misiles_detectados = False):
    
    """ Esta funcion es un radar para detectar misiles"""
    factor_aleatorio = np.abs(np.cos(angulo) + np.exp(-angulo))
    
    umbral = np.sqrt((localizacion[0] - localizacion[1])**2 )
    
    print("factor umbral permitido", umbral)
    
    if misiles_detectados:
        
        distancia_misil = np.sqrt(distancia_misil + factor_aleatorio)
        
        if distancia_misil < 5 + 10*umbral:
            
            print("misil esta cerca de la base, evacuar")
            print("valor umbral permitido", 5 + 10*umbral)
            
        else:
            print("misil no esta cerca de la base, estar atentos")
            
    else:
        print("no se detecta misil")
        

    return print("distancia misil", distancia_misil)
        

if __name__ == "__main__":
    distancia = 10
    umbral  = 12
    angulo = 0.98
    localizacion = (12.3,11.5)
    detectados = True
    print(radar_atomico(distancia,umbral,angulo=angulo, localizacion = localizacion ,misiles_detectados = detectados))

    