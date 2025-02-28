import numpy as np

num_estudiantes = 6500
codigos = np.random.randint(1800000,2250000,num_estudiantes)
nombres = np.array([f"Estudiante_{i}"for i in range(1,num_estudiantes+1)])
promedios = np.round(np.random.uniform(1.8,5.0,num_estudiantes),2)
codigos_carreras = np.random.randint(10,73,num_estudiantes)
codigo_ingresado = int(input("Por favor ingrese un codigo de carrera valido(10-72)"))
filtro_carrera = (codigo_ingresado == codigos_carreras)&(promedios>=4.0)
estudiantes_filtrados = np.where(filtro_carrera)[0]

#print(codigos)  
#print(nombres)
#print(promedios)                   
#print(codigos_carreras)        FUE PARA CORROBORAR QUE EL PROCESO ERA CORRECTO
#print(filtro_carrera)
#print(estudiantes_filtrados)           

print("Estudiantes de la carrera con el codigo:",codigo_ingresado," Con promedio mayor a 4.0\n")
for i in estudiantes_filtrados:
    print("Codigo:",codigos[i],"\nNombre estudiante:",nombres[i])

años_ingreso = (codigos//10000)
filtros_condicionales = (años_ingreso<190)&(promedios>=2.7)&(promedios<=3.2)
estudiantes_condicionales = np.where(filtros_condicionales)[0]

#print(años_ingreso)
#print(filtros_condicionales)
#print(estudiantes_condicionales)

print("\n Estudiantes que ingresaron antes de 1990 y estan en condicional:\n")
for i in estudiantes_condicionales:
    print("Codigo:",codigos[i],"\n Nombre Estudiante:",nombres[i])
    
