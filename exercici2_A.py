#En aquest arxiu hi contindrà un diccionari amb 6 keys i un value per cada key. Cal mostrar per consola:
#       La longitud del diccionari.
#       Els valors.
#		Extreure l’últim item.

def diccionari():
    dictLaia = {'febre':'si', 'Edat':23, 'Segon cognom':'Ramos'}
    print(len(dictLaia))
    print(dictLaia.values())
    print(dictLaia.popitem())
    print(dictLaia.values())

#CRIDO LA FUNCIO diccionari
diccionari()