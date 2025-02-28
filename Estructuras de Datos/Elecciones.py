import numpy as np

numeros = 5000
n_personas = 30
votos = np.random.randint(1,n_personas+1,numeros)
votos_personas = np.bincount(votos)[1:]
personas = np.arange(1,n_personas+1)
indice = np.argsort(votos_personas)[::-1]
personas_ordenadas = personas[indice]
votos_ordenados = votos_personas[indice]

#print(votos)
#print(votos_personas)
#print(personas)
#print(indice)
#print(personas_ordenadas)
#print(votos_ordenados)

for i in range(n_personas):
    print("El candidato",personas_ordenadas[i],"obtuvo",votos_ordenados[i],"votos")
