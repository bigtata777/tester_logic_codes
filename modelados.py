print("modelado de datos")




def radar_atomico(distancia_misil:float, umbral:float, misiles_detectados = False):
    
    if misiles_detectados:
        
        if distancia_misil < umbral:
            
            print("misil esta cerca de la base, evacuar")
            
        else:
            print("misil no esta cerca de la base, estar atentos")
            
    else:
        print("no se detecta misil")