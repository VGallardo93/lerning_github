#%%
# -*- coding: utf-8 -*-
# PYTHON 3.7

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

print("\tPrograma de evaluación de notas de alumnos.\n")
nota_alumno = input("Ingrese la nota del alumno: ")
# nota_alumno = int(input("Ingrese la nota del alumno: "))
print(type(nota_alumno))
print('\n')



def evaluacion(nota):
  valoracion = "Aprobado"
  if nota < 5:
    valoracion = "Suspenso"
  return valoracion


print(evaluacion(int(nota_alumno)))

#-------------------------------------------------------------------------

print('\n')
print (msg1 + str(scr) + "\n")
print("\tVerificación de acceso\n")
edad_usuario = int(input("Intruduce tu edad: "))

if edad_usuario < 18:
  print("NO PUEDES PASAR")
elif edad_usuario > 100:
  print("Are you alive?")
else:
  print("Puedes pasar")

print (msg2 + str(scr) + "\n")
scr += 1
























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