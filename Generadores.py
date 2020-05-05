#%%
# -*- coding: utf-8 -*-
# PYTHON 3.7

# GENERADORES

import os
# from subprocess import call
from subprocess import run # python 3,5+

# os.system("cls") # Envia un comando a la terminal para limpiar la pantalla
# os.system no se recomienda (antigua y obsoleta), se recomienda call()
# call("cls", shell = True) # Envia un comando a la terminal para limpiar la pantalla
"""
Advertencia Usar shell=Truepuede ser un peligro para la seguridad.
Consulte la advertencia en Argumentos de uso frecuente para obtener
más detalles.
https://docs.python.org/2/library/subprocess.html
"""
run("cls", shell = True)
# https://recursospython.com/guias-y-manuales/subprocess-creacion-y-comunicacion-con-procesos/
msg1 = "\nStart script "
msg2 = "\nEnd\
 script "
scr = 1 # It indicates script number

# Copy and paste the sentences bellow

# print (msg1 + str(scr) + "\n")

# print (msg2 + str(scr) + "\n")
# scr += 1

'''
> mayor que
< menor que
== igual que
>= mayor o igual que
<= menor o igual que
!= destinto que
'''

"""
# GENERADORES

- Estructuras que extraen valores de una función y se almacenan en objetos iterables (que se pueden recorrer).
- Estos valores se almacenan de uno en uno.
- Cada vez que un generador almacena un valor, esta permanece en un estado pausado hasta que se solicita el siguente. Esta caracteristica se le conoce como "suspencion de estado.


- Son mas eficientes que las funciones tradicionales
- Muy utiles con listas de valores infinitos
- Bajo determinados escenarios, será muy util que un generador devuelva los valores de uno en uno.
"""

#%%
# Metodo tradicional
def funPares(limite):
  num = 1
  miLista = []
  while num < limite:
    miLista.append(num * 2)
    num += 1
  return miLista


def generaPares(limite):
  num = 1
  while num < limite:
    yield num * 2
    num += 1


devfunormal = funPares(10)
print(devfunormal)
print(type(devfunormal))
print('\n')

devuelvePares = generaPares(10)

for i in devuelvePares:
  print(i)

# for i in devuelvePares:
#   print(devuelvePares)

print(type(devfunormal))
print('\n')

#%%

def generaPares2(limite):
  num = 1
  while num < limite:
    yield num * 2
    num += 1

devuelvePares2 = generaPares2(10)

print(next(devuelvePares2))
print("Aqui podria ir mas código...")
print(next(devuelvePares2))
print("Aqui podria ir mas código...")
print(next(devuelvePares2))
print("Aqui podria ir mas código...")
print('\n')

#%%
""" YIELD FROM """

def dev_city(*ciudades): #  El * le indica a la funcion que recivirá un numero indeterminado
                         #  de elementos, será una TUPLA
  for elemento in ciudades: # Bucle for padre
    yield from elemento # reemplaza a las 2 lineas de codigos siguientes
    # for subElemento in elemento:
      # yield subElemento

city_devuelta = dev_city("Madrir", "Barcelona", "Bilbao", "Valencia")
print(next(city_devuelta))
print(next(city_devuelta))


#%%
""" YIELD FROM """

def dev_city2(*ciudades): #  El * le indica a la funcion que recivirá un numero indeterminado
                          #  de elementos, será una TUPLA
  yield from ciudades

city_devuelta = dev_city2("Madrir", "Barcelona", "Bilbao", "Valencia")
# print(next(city_devuelta))
# print(next(city_devuelta))
# print(next(city_devuelta))
# print(next(city_devuelta))
# print(next(city_devuelta)) # Error, exede el número de elementos

try:
  while True:
    print(next(city_devuelta))

except StopIteration:
  print('>>> StopIteration.')

finally:
  print('\nEnd script.\n')



#%%
other_cities = ["Strasbourg", "Freiburg", "Stuttgart", 
                "Vienna / Wien", "Hannover", "Berlin", 
                "Zurich"]

city_iterator = iter(other_cities)
while city_iterator:
    try:
        city = next(city_iterator)
        print(city)
    except StopIteration:
        break










#%%
path_s = os.path.abspath(__file__)
phrase_f = " ... >>> Finished succesfully."
guion = len(path_s)

print('\n' + '-' * ((len(path_s)) + len(phrase_f))) # Solo para estética. Hace coincidir los guiones con el punto final ">>> Finished succesfully."
print("\n" + path_s + "\033[1;3;33m" + phrase_f + '\033[0;m' + "\n")
# print (type(path_s))
# print ('\n')
print("\t\033[1;0mEND.\033[0;m\n")
print('-' * ((len(path_s)) + len(phrase_f)) + '\n')
print('\n')


# %%

'''

       Negro       0;30     Gris oscuro    1;30
       Azul        0;34     Azul claro     1;34
       Verde       0;32     Verde claro    1;32
       Cyan        0;36     Cyan claro     1;36
       Rojo        0;31     Rojo claro     1;31
       Purpura     0;35     Purpura claro  1;35
       Marron      0;33     Amarillo       1;33
       Gris claro  0;37     blanco         1;37

https://en.wikipedia.org/wiki/ANSI_escape_code
'''