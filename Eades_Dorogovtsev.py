import random 
import math 
import numpy as np
import pygame

from grafo import Grafo
import random

def dorogovtsev_mendes(n, directed=False):
    """
    Grafo Dorogovtsev (Método aleatorio)
    n : número de nodos.
    """
    g = Grafo('Dorogovtse')
    g.addArista('0 -- 1', str(0), str(1))
    g.addArista('0 -- 2', str(0), str(2))
    g.addArista('1 -- 2', str(1), str(2))
    for nAdic in range(3, n-2):
        num_edges = len(g.aristas)
        random_edges = random.randint(1,num_edges-1)
        list_edge = list(g.aristas.keys())
        edges_select = list_edge[random_edges]
        nI = g.aristas[edges_select].inicio.id
        nF = g.aristas[edges_select].final.id
        peso = random.randint(1, 50)
        peso2 = random.randint(1, 50)

        g.addArista('{} -- {}'.format(str(nAdic), str(nI)), str(nAdic), str(nI),peso)
        g.addArista(str('{} -- {}'.format(str(nAdic), str(nF))), str(nAdic), str(nF),peso2)

    return g


print ("Modelo Dorogovtsev  ----------")
nodo = int(input("Ingrese número de nodos: "))

dorogovtsev_mendes_ = dorogovtsev_mendes(nodo)
nodos = dorogovtsev_mendes_.nodos.keys()
ventana = pygame.display.set_mode((500,500))
color = (200, 0, 0)
for nodo in nodos:
  objetoNodo = Grafo.giveNodo(nodo)
  if objetoNodo.x == 0 and objetoNodo.y == 0:
    objetoNodo.x = random.random() * 500
    objetoNodo.y = random.random() * 500

c1 = 55
c2 = 0.35
active=True
radio = 3

while active:


  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      active = False

  Grafo.proyecta(dorogovtsev_mendes_)

  pygame.display.update()
  ventana.fill('black')

