# -*- coding: utf-8 -*-
"""Oficial_Sistema_de_ordenadas_2D

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PGhT4PFASYMiGCXpRRXocq3kJRGNZFJ8
"""

#parte A

import math #Importar a biblioteca para fazer raiz quadrada

#Escreva qual valor vc quer como origem, podemos utilizar o (0,0) como referência.
x = int(input("Digite a coordenada X da origem transladada: "))
y = int(input("Digite a coordenada Y da origem transladada: "))

#Inicializar as variáveis para contagem de pontos em cada quadrante
q1 = 0
q2 = 0
q3 = 0   
q4 = 0

#Quantos pontos iremos ler?
n = int(input("Digite a quantidade de pontos a serem processados: "))

#Criando as variaves de armazenamento de ponto menor e maior distância, relacionado ou ponto de origem
menor_distancia = None
maior_distancia = None
menor_ponto = None
maior_ponto = None

#Processamento de quantos pontos faremos
for i in range(n):

    #Aqui vamos ler os pontos
    #ponto_x, ponto_y = map(int, input("Digite as coordenadas do ponto separadas por espaço: ").split())
    ponto_x = int(input('Digite o valor do ponto X: '))
    ponto_y = int(input('Digite o valor do ponto Y: '))

    #Cálculo das coordenadas transladadas, se for (0,0) esse passo é insignificante 
    ponto_x_transladado = ponto_x - x
    ponto_y_transladado = ponto_y - y

    #Verificnaod em qual quadrante fica cada ponto
    if ponto_x_transladado > 0 and ponto_y_transladado > 0:
        print("Este ponto está no quadrante 1.")
        q1 = q1 + 1
    elif ponto_x_transladado < 0 and ponto_y_transladado > 0:
        print("Este ponto está no quadrante 2.")
        q2 = q2 + 1
    elif ponto_x_transladado < 0 and ponto_y_transladado < 0:
        print("Este ponto está no quadrante 3.")
        q3 = q3 + 1
    elif ponto_x_transladado > 0 and ponto_y_transladado < 0:
        print("Este ponto está no quadrante 4.")
        q4 = q4 + 1
    elif ponto_x_transladado == 0 and ponto_y_transladado != 0:
        print("Este ponto está sobre o eixo das ordenadas transladado.")
    elif ponto_y_transladado == 0 and ponto_x_transladado != 0:
        print("Este ponto está sobre o eixo das abscissas transladado.")
    else:
        print("Este ponto está na origem transladada.")

    #Cálculo da distância euclidiana
    distancia = math.sqrt(ponto_x_transladado ** 2 + ponto_y_transladado ** 2)

    #Verificando qual o ponto de maior distância relacionado à origem transladada
    if maior_distancia is None or distancia > maior_distancia:
        maior_distancia = distancia
        maior_ponto = (ponto_x, ponto_y)

    #Verificando qual o ponto de menor distância relacionado à origem transladada
    if menor_distancia is None or distancia < menor_distancia:
        menor_distancia = distancia
        menor_ponto = (ponto_x, ponto_y)

#Dados finais
print(f"O ponto que apresenta a menor distância em relação à origem transladada é: {menor_ponto} e a distância é: {menor_distancia}")
print(f"O ponto que apresenta a maior distância em relação à origem transladada é: {maior_ponto} e a distância é: {maior_distancia}")
print(f"Ao todo, existem {q1} pontos no quadrante 1")
print(f"Ao todo, existem {q2} pontos no quadrante 2")
print(f"Ao todo, existem {q3} pontos no quadrante 3")
print(f"Ao todo, existem {q4} pontos no quadrante 4")
#Podemos colocar a contagem de pontos em cima do eixo das abcissas ou ordenadas

#Parte B
print('\nAgora vamos para nosso projeto do robô')

# O robô do robo sempre é: Cima(+y), Direita(+x), Direita(+x)
desl_x = [0, 1, 1]
desl_y = [1, 0, 0]


pos_x = int(input("Posição de origem (x) do robô: "))
pos_y = int(input("Posição de origem (y) do robô: "))
caminhada = int(input("Coloque a duração da Caminhada do robô: "))

tempo = 0
fim = False

while not fim:
    for i in range(3):
        pos_x += desl_x[i]
        pos_y += desl_y[i]
        tempo += 1
        fim = (tempo >= caminhada)
        if fim:
            break

print(f'A posição final do robô é ({pos_x}, {pos_y})')

