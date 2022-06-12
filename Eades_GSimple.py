from grafo import Grafo 
import random 
from math import sqrt

def distancia(NI, NF):
  x1 = NI.attributos['px']
  y1 = NI.attributos['py']
  x2 = NF.attributos['px']
  y2 = NF.attributos['py']
  dista = sqrt((x2-x1)**2 + (y2-y1)**2)
  return dista


def geosim(n,r):
  """
  Grafo Geografíco Simple (Método aleatorio)
  n : número de nodos.
  r : distancia para generar la arista entre dos nodos.
  """
  g = Grafo('GeoSimple')
  for i in range(n):
    nodo = g.addNodo(str(i))
    nodo.attributos['px'] = random.random()
    nodo.attributos['py'] = random.random() 
  conteoAristas = 1
  for i in range(n):
    for j in range(n):
      if i != j:
        nI = g.giveNodo(str(i))
        nF = g.giveNodo(str(j))
        dista = distancia(nI,nF)
        if dista <= r:
          peso = random.randint(1, 50)
          g.addArista('{} -- {}'.format(str(i), str(j)),str(i),str(j),peso)
          conteoAristas += 1  
  return g

print ("Modelo Geográfico simple  ----------")
n_nodo = int(input("Ingrese número de nodos: "))
dist = float(input("Ingrese la distancia máxima para crear un nodo valor entre 0 y 1: "))

geosim_ = geosim(n_nodo,dist)
nodos = geosim_.nodos.keys()
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

  Grafo.proyecta(geosim_)

  pygame.display.update()
  ventana.fill('black')


