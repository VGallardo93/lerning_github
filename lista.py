# -*- coding: utf-8 -*-
import os

miLista = ["SG", "SJ", "EC", "MR"] # [0, 1, 2, 3]
print('\n' + miLista[3] + '\n')
print(miLista[:2])
print(miLista[1:])
miLista.append("VJ") # Agrega un elemento al final
miLista.insert(2, "EO") # Inserta en el indice 2 "EO", desplazando lo demás hacia la derecha.
print(miLista[:])
miLista.extend(["VH", "AH", "AD"]) # Concateno otra lista a mi lista original
print(miLista[:])
print(miLista.index("VH"))
print("SG" in miLista) # Comprobar si existe un elemento en mi lista
miLista.remove("AH") # Elimina un elemento de mi lista
print(miLista[:])
# miLista.remove(5) # Elimina un elemento de mi lista indicando el indice, ESTO MARCA ERROR
miLista.pop() # Elimina el último elemento de mi lista
print(miLista[:])
print('\n')
la = ['ac', 69, 'dc', False, 4]
lb = ['nigga', 23, 'FM', True, 44]
lsum = la + lb
print(lsum[:])
print('\n')
lmul = lb*3
print(lmul[:])
print('_________________________________________________________________________________________________\n')
pass











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