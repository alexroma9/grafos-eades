from grafo import Grafo
from arista import Arista
import random
weight = 'Peso'

def erdosrenyi(n,m, dirigido=False, auto=False):
  """
  Grafo Erdos-Renyi (método aleatorio)
  n : número de nodos
  m : número de aristas 
  """
  #a = Arista
  g = Grafo('Erdos-Renyi')
  for i in range(n):
      g.addNodo(str(i))
  #edges = {}
  for i in range(m):
    u = random.randint(0, n-1)
    v = random.randint(0, n-1)
    e = (u, v)
    if u != v:
      peso = random.randint(1, 50)
      g.addArista('{} -- {}'.format(str(u), str(v)),str(u),str(v),peso)

  return g


print ("Modelo Erdös y Rényi  ----------")
nodo = int(input("Ingrese número de nodos: "))
arista = int(input("Ingrese número de aristas: "))

erdosrenyi_ = erdosrenyi(nodo,arista)
nodos = erdosrenyi_.nodos.keys()
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

  Grafo.proyecta(erdosrenyi_)

  pygame.display.update()
  ventana.fill('black')



