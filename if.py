#%%
# LERNING ABOUT GIT
# PYTHON 3.7

# Se elimino el codigo de acceso por edad

print("\tPrograma de evaluación de notas de alumnos.\n")
nota_alumno = float(input("Ingrese la nota del alumno: "))
# nota_alumno = int(input("Ingrese la nota del alumno: "))
print(type(nota_alumno))
print('\n')



def evaluacion(nota):
  valoracion = "El alumno ha aprobado con nota " + str(nota) + '.'
  if nota < 3.94:
    valoracion = "El alumno ha reprobado con nota " + str(nota) + '.'
  return valoracion


# print(evaluacion(int(nota_alumno)))
print(evaluacion(nota_alumno))

#-------------------------------------------------------------------------

print('\n')

print("\n>>> This is The End.")
