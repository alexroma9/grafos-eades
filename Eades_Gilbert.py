from grafo import Grafo
import random

def gilbert(n, pr):
  """
  Grafo Gilbert (Método aleatorio)
  n : número de nodos
  pr : probabilidad asignada que se considerá para generar si / no la arista entre dos nodos.
  """
  g = Grafo('Gilbert')
  for i in range(n):
    g.addNodo(str(i))

  Aristas = 1
  for i in range(n):
    for j in range(n):
      if random.random() < pr:
        if (j != i):
            peso = random.randint(1, 50)
            g.addArista('{} -- {}'.format(str(i),str(j)),str(i),str(j),peso)
            Aristas += 1
  return g
 
print ("Modelo Gilbert  ----------")
nodo = int(input("Ingrese número de nodos: "))
prob = float(input("Ingrese la probabilidad de crear la arista: "))

gilbert_ = gilbert(nodo,prob)
nodos = gilbert_.nodos.keys()
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

  Grafo.proyecta(gilbert_)

  pygame.display.update()
  ventana.fill('black')

