from grafo import Grafo
import random


def malla(m, n, dirigido=False):
  """
  Grafo Malla (Método aleatorio)
  m : número de filas
  n : número de columnas
  """
  g = Grafo('Malla')
  Aristas = 1
  Nodos = 1
  for fila in range(m):
    for columna in range(n):  
      if columna < (n-1):
        peso = random.randint(1, 50)
        g.addArista('{} -- {}'.format(fila * n + columna, fila * n + columna + 1), str(fila * n + columna), str(fila * n + columna + 1),peso)
        #g.addArista('{} -- {}'.format(str(fila), str(columna)),str(fila),str(columna),peso)
#        g.addArista(Aristas, str(Nodos), str(Nodos + 1))    
        Aristas += 1
      if fila < (m-1):
        peso2 = random.randint(1, 50)
        #g.addArista('{} -- {}'.format(str(fila), str(columna)),str(fila),str(columna),peso)
        g.addArista('{} -- {}'.format(fila * n + columna, (fila+1)* n + columna), str(fila * n + columna), str((fila+1)* n + columna),peso2)
#        g.addArista(Aristas, str(Nodos), str(Nodos + 2))
        Aristas += 1      
      Nodos += 1
  return g

print ("Modelo Malla  ----------")
columnas = int(input("Ingrese número de columnas: "))
filas = int(input("Ingrese número de filas: "))

malla_ = malla(columnas,filas)
nodos = malla_.nodos.keys()
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

  Grafo.proyecta(malla_)

  pygame.display.update()
  ventana.fill('black')

