from grafo import Grafo
import random

edge = 'Aristas'
neighbour = 'Vecinos'

def barabasi(n,d):
  """
  Grafo Barabasi (Método aleatorio)
  n : número de nodos.
  d : número de aristas máximas por nodo.
  """
  g = Grafo('Barabasi-Albert')
  g.addNodo(str(0))

  Aristas = 1
  for i in range(1, n):
    nodosRandom = randomA(i)
    for j in range(i):
      grado = g.givedegreesNodo(str(nodosRandom[j]))
      pr = 1 - grado / d 
      #print(grado, d, pr)
      if random.random() < pr:
        if nodosRandom[j] != i:
            peso = random.randint(1, 50)
            g.addArista('{} -- {}'.format(str(nodosRandom[j]),str(i)), str(nodosRandom[j]), str(i), peso)
            #g.addArista(Aristas, str(i), str(nodosRandom[j]))
            Aristas += 1
  
  return g


def randomA(tamano):
  """
  Forma un arreglo aleatorio para generar el grafo Barabasi
  """
  num = []
  res = []
  t = tamano
  for i in range(tamano):
    num.append(i)
  for i in range(tamano):
    aleatorio = random.randint(0,t-1)
    res.append(num[aleatorio])
    num.pop(aleatorio)
    t = t - 1

  return res

def distanciaEntrePuntos(a,b,c,d):
  """ puntos (a,b) y (c,d) """

  return math.sqrt( (a-c)**2 + (b-d)**2)

print ("Modelo Barabasi  ----------")
nodo = int(input("Ingrese número de nodos: "))
aris = int(input("Ingrese número de arista: "))


barabasi_ = barabasi(nodo,aris)
nodos = barabasi_.nodos.keys()
ventana = pygame.display.set_mode((600,600))
color = (150, 0, 0)
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

  Grafo.proyecta(barabasi_)

  pygame.display.update()
  ventana.fill('black')





