print("modelado de datos")
import numpy as np 
import pandas as pd     
import re


def radar_atomico(distancia_misil:float, 
                  umbral:float, 
                  angulo:float,
                  localizacion:tuple,
                  misiles_detectados = False):
    
    """ Esta funcion es un radar para detectar misiles
    dado un cierto umbral de distancia a mi base de guerra"""
    
    factor_aleatorio = np.abs(np.cos(angulo) + 0.98*np.exp(-angulo))
    
    umbral = np.sqrt((localizacion[0] - localizacion[1])**2 )
    
    
    print("factor umbral permitido", umbral)
    
    if misiles_detectados:
        
        distancia_misil = np.sqrt(distancia_misil + factor_aleatorio)
        
        distancia_riesgo = (distancia_misil - ( 5 + 10*umbral))
        
        probabilidad_de_riesgo = (1/(1+np.exp(-umbral)))
        
        distancia_riesgo = probabilidad_de_riesgo*distancia_riesgo
        
        if distancia_misil < 5 + 10*umbral:
            
            print("misil esta cerca de la base, evacuar")
            print("valor umbral permitido", 5 + 10*umbral)
            print("distancia de riesgo", distancia_riesgo)
            
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
    print(radar_atomico(distancia,umbral,angulo=angulo, 
                        localizacion = localizacion ,
                        misiles_detectados = detectados))

    