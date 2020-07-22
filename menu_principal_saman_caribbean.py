import Modulo1_Gestion_de_cruceros
import Modulo2_Gestion_hab
import Modulo3_venta_de_tour
import Modulo4_Gestion_Restaurante
import Modulo5_estadisticas

# se importa el modulo request para acceder a la api de manera global
#//////////////////////////////////////////////////////////////////////////////////////////////////////////
import requests

r = requests.get("https://saman-caribbean.vercel.app/api/cruise-ships")

d = '---'*100
dic = r.json()
#/////////////////////////////////////////////////////////////////////////////////////////////////////////
#se definen de manera global los diccionarios correspondientes al modulo 4
#////////////////////////////////////////////////////////////////////////////////////////////////////////
alimentos ={"plato 1": {"name":"Pizza","price":11.99,"prest":'paquete'},
            "plato 2": {"name":"Hamburguesa","price":25.99,"prest":'preparacion'},
            "plato 3": {"name":"Cofuta","price":6.99,"prest":'paquete'},
            "plato 4": {"name":"Donas","price":2.99,"prest":'paquete'}

    }
    
    
    
bebidas = {"bebida 1": {"name":"Ron","price":6.99,"prest":'grande'},
           "bebida 2": {"name":"Coca Cola","price":2.99,"prest":'mediano'},
           "bebida 3": {"name":"Cerveza","price":3.99,"prest":'grande'},
           "bebida 4": {"name":"Limonada","price":2.75,"prest": 'grande'},
           "bebida 5": {"name":"sprite","price":2.35,"prest":'mediana'}

    }

    

combos = { "combo 1" : {"name" : "Hamburguesa & Refresco", "price": 15.99},
           "combo 2" : {"name":"Pizza & Refresco", "price": 21.55},
           "combo 3" : {"name": "nuggets & fries", 'price': 12.99},
           "combo 4" : {"name": "helado & brownie", 'price':15.99}

    }

#////////////////////////////////////////////////////////////////////////////////////////////////////////
#funcion main para ejecutar el codigo en si en donde se llaman a los distintios inicializadores de cada modulo segun el usuario quiera.
def main():
        while True:

            print('--'*30)
            print('''
            Bienvenido Al Sistema De Gestion De Saman Caribbean!
            Las Opciones Que Tenemos Disponibles Son Las Siguientes:

            1. Modulo De Gestion De Cruceros.
            2. Modulo De Gestion De Habitaciones.
            3. Modulo De Gestion De Ventas De Tour.
            4. Modulo De Gestion De Restaurante.
            5. Modulo De Estadisticas.
            ------------------------------------------
            6. Salir

            ''')
            print()
            print('--'*30)
            selec = int(input("Ingrese El Numero De La Opcion Que Desea Realizar: "))
            while selec != 1 and selec != 2 and selec != 3 and selec != 4 and selec != 5 and selec != 6 :
                selec = int(input("Error. Por Favor Ingrese Un Caracter numerico valido: "))
            if selec == 1:
                Modulo1_Gestion_de_cruceros.start()
                
                
            elif selec ==2:
                Modulo2_Gestion_hab.main()
                

            elif selec ==3:
                Modulo3_venta_de_tour.main()
                
            elif selec == 4:
                Modulo4_Gestion_Restaurante.menu(alimentos,bebidas)
                
            elif selec == 5:
                Modulo5_estadisticas.main()
            elif selec == 6:
                print("Gracias Por Ingresar En El Sistema De Gestion De Saman Caribbean! Hasta Luego.")
                break
        

    
        
    
    
    
    

main()

