import requests

r = requests.get("https://saman-caribbean.vercel.app/api/cruise-ships")

d = '---'*100
dic = r.json()

restship1 = dic[0]["sells"]
restship2 = dic[1]["sells"]
restship3 = dic[2]["sells"]
restship4 = dic[3]["sells"]


def m4_statistic():
    print(f"En el barco {dic[0]['name']} los 5 productos mas vendidos del restaurante son los siguiente:\n\n1.{restship1[0]['name']}. //   Con un total de {restship1[0]['amount']} unidades vendidas.\n2.{restship1[1]['name']}. //   Con un total de {restship1[1]['amount']} unidades vendidas.\n3.{restship1[2]['name']}. //   Con un total de {restship1[2]['amount']} unidades vendidas.\n4.{restship1[3]['name']}. //   Con un total de {restship1[3]['amount']} unidades vendidas.\n5.{restship1[4]['name']}. //   Con un total de {restship1[4]['amount']} unidades vendidas.")
    print("\n")
    print("--"*30)
    print(f"En el barco {dic[1]['name']} los 5 productos mas vendidos del restaurante son los siguiente:\n\n1.{restship2[0]['name']}. //   Con un total de {restship2[0]['amount']} unidades vendidas.\n2.{restship2[1]['name']}. //   Con un total de {restship2[1]['amount']} unidades vendidas.\n3.{restship2[2]['name']}. //   Con un total de {restship2[2]['amount']} unidades vendidas.\n4.{restship2[3]['name']}. //   Con un total de {restship2[3]['amount']} unidades vendidas.\n5.{restship2[4]['name']}. //   Con un total de {restship2[4]['amount']} unidades vendidas.")
    print("\n")
    print("--"*30)
    print(f"En el barco {dic[2]['name']} los 5 productos mas vendidos del restaurante son los siguiente:\n\n1.{restship3[0]['name']}. //   Con un total de {restship3[0]['amount']} unidades vendidas.\n2.{restship3[1]['name']}. //   Con un total de {restship3[1]['amount']} unidades vendidas.\n3.{restship3[2]['name']}. //   Con un total de {restship3[2]['amount']} unidades vendidas.\n4.{restship3[3]['name']}. //   Con un total de {restship3[3]['amount']} unidades vendidas.\n5.{restship3[4]['name']}. //   Con un total de {restship3[4]['amount']} unidades vendidas.")
    print("\n")
    print("--"*30)
    print(f"En el barco {dic[3]['name']} los 5 productos mas vendidos del restaurante son los siguiente:\n\n1.{restship4[0]['name']}. //   Con un total de {restship4[0]['amount']} unidades vendidas.\n2.{restship4[1]['name']}. //   Con un total de {restship4[1]['amount']} unidades vendidas.\n3.{restship4[2]['name']}. //   Con un total de {restship4[2]['amount']} unidades vendidas.\n4.{restship4[3]['name']}. //   Con un total de {restship4[3]['amount']} unidades vendidas.\n5.{restship4[4]['name']}. //   Con un total de {restship4[4]['amount']} unidades vendidas.")

def main():
    print('Sistema de estadisticas De Saman Caribbean\n\n Actualmente SOLO Disponemos de las Estadisticas de el restaurante por barco.')
    selec = int(input("\n1.Visualizar\n2.No, Gracias\n\n>>"))
    while selec != 1 and selec != 2:
        selec = int(input("Error. Ingrese Un caracter numerico valido."))
    if selec == 2:
        print("Muy Bien! Hasta Luego!")
    elif selec == 1:
        m4_statistic()

