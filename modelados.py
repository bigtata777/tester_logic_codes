print("modelado de datos")




def radar_atomico(distancia_misil:float, umbral:float, misiles_detectados = False):
    
    """ Esta funcion es un radar para detectar misiles"""
    
    if misiles_detectados:
        
        if distancia_misil < umbral:
            
            print("misil esta cerca de la base, evacuar")
            
        else:
            print("misil no esta cerca de la base, estar atentos")
            
    else:
        print("no se detecta misil")
        
    return None if misiles_detectados == False else print(f"la distancia del misil es {distancia_misil}")
        
        