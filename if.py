#%%
# LERNING ABOUT GIT
# PYTHON 3.7

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
print("\tVerificación de acceso\n")
edad_usuario = int(input("Intruduce tu edad: "))

if edad_usuario < 18:
  print("NO PUEDES PASAR")
elif edad_usuario > 100:
  print("Are you alive?")
else:
  print("Puedes pasar")

print("\n>>> This is The End.")
