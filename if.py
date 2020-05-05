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

print("\n>>> This is The End.")
