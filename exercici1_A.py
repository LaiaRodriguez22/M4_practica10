#En aquest arxiu hi contindrà una funció que, passat per paràmetre
# l’any de naixement, haurà de retornar els anys de l’usuari.

anyNaixement = int(input("Quin any vas neixer? "))

def edatUsuari():
    edat = 2023-anyNaixement
    print(f"Actualment tens {edat} anys o un menys, depenguent del mes." )

#CRIDO LA FUNCIO edatUsuari
edatUsuari()