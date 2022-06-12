import random 
import math 
import numpy as np
import pygame


#from grafo import Grafo
from nodo import Nodo 
from arista import Arista 
neighbour = 'Vecino'
edge = 'Arista'
dijkstra = 'Dijkstra'


class Grafo():
  """
  Clase Grafo
  """
  def __init__(self, nombre):
    """
    Inicializa el grafo.
    nombre : Nombre del grafo.
    nodos
    aristas
    """
    self.id = nombre
    self.nodos = {} 
    self.aristas = {}
  
  def savedArchivo(self):
    """
    Guarda datos de grafo en formato .gv
    Warning : Cuidado ya que sobre escribe una vez ejecutado el grafo solicitado.
    """
    file = open('{}.gv'.format(self.id), 'w')
    file.write('digraph #nombre {' + '\n')
    for arista in self.aristas:
      objetoArista = self.aristas[arista]
      nodoInicial = objetoArista.inicio.id
      nodoFinal = objetoArista.final.id
      #file.write('{};'.format(arista) + '\n')a
      file.write('{} -- {};'.format(nodoInicial,nodoFinal) + '\n')
    file.write('}')
    file.close()

  def savedArchivoDijsktra(self, sufijo):
    """
    Guarda datos de grafo en formato .gv 
    Para Dijkstra
    """
    file = open('{}{}.gv'.format(self.id, sufijo), 'w')
    file.write('graph #nombre {' + '\n')
#    nodo = self.nodos
#    print (nodo)
    for arista in self.aristas:
      file.write('{};'.format(arista) + '\n')
#      file.write('{} [label="{}"]'.format(arista,self.nodos[nodo].attributos['Dijkstra']) + '\n')
#      nodo = nodo + 1

    for nodo in self.nodos:
      file.write('{} [label="{}"]'.format(nodo,self.nodos[nodo].attributos['Dijkstra']) + '\n')
    file.write('}')
    file.close()

  def addNodo(self, nombreNodo):
    """
    Crea nodo , si esta creado no hace nada de lo contrario crea.
    """
    if nombreNodo in self.nodos:
        pass
    else:
      _nodo = Nodo(nombreNodo)
      self.nodos[nombreNodo] = _nodo
    return self.nodos[nombreNodo]
  
  def addArista(self, nombreArista, nombreNodoOrigin, nombreNodoDestino, peso=0):
    """
    Crea arista, si esta creada no hace nada, de lo contrario crea.
    """
    #if nombreArista in self.aristas:
    #    pass
    #else:
    arista_ = self.aristas.get(nombreArista)

    if arista_ is None:
        nodoOrigen = self.addNodo(nombreNodoOrigin)
        nodoDestino = self.addNodo(nombreNodoDestino)
        #_arista = Arista(nombreArista,self.nodos[nombreNodoOrigin],self.nodos[nombreNodoDestino],peso)
        _arista = Arista(nombreArista,nodoOrigen,nodoDestino,peso)
        self.aristas[nombreArista] = _arista
        nodoOrigen.attributos[neighbour].append(nodoDestino)
        nodoDestino.attributos[neighbour].append(nodoOrigen)
        nodoOrigen.attributos[edge].append(_arista)
        nodoDestino.attributos[edge].append(_arista)

  def giveNodo(self, nombre):
    return self.nodos[nombre]
  
  def givedegreesNodo(self, nombreNodo):
    """
    Entrega el grado del nodo considerado.
    """
    if not nombreNodo in self.nodos:
      print('Nodo no existe')

    else:
      _nodo = self.nodos[nombreNodo]
      grado = len(_nodo.attributos[neighbour])
      return grado
  
  def bfs(grafoGenerado, s):
      """
      BFS
      : parametro s : nodo fuente o root
      : g grafo generado por BFS
      """
      gbfs = Grafo('BFS')
      visitado = [s]
      cola = [s]
      diccionarioNodos = grafoGenerado.nodos
      while cola:
          m = cola.pop(0)
          for nodoAdjacente in diccionarioNodos[m].attributos['Vecino']:
              if nodoAdjacente.id not in visitado:
                  visitado.append(nodoAdjacente.id)
                  cola.append(nodoAdjacente.id)
                  gbfs.addArista('{} -- {}'.format(str(m), str(nodoAdjacente.id)),str(m),str(nodoAdjacente.id))     
      return gbfs

  def dfsr(grafoGenerado, nodoFuente, visitados, grafoDFSR):
      diccionarioNodos = grafoGenerado.nodos
      visitados.append(nodoFuente)
      for nodoAdjacente in diccionarioNodos[nodoFuente].attributos['Vecino']:
          if nodoAdjacente.id not in visitados:
              grafoDFSR.addArista('{} -- {}'.format(str(nodoFuente), str(nodoAdjacente.id)),str(nodoFuente),str(nodoAdjacente.id))     
              visitados,grafoDFSR = Grafo.dfsr(grafoGenerado, nodoAdjacente.id, visitados, grafoDFSR)
              #grafoDFSR = DFSR(grafoGenerado, nodoAdjacente.id, visitados, grafoDFSR)
      return visitados,grafoDFSR


  def dfsi(grafoGenerado, nodoFuente):
      """
      Funcion para generar un arbol DFS dado un grafo : grafoGenerado
      y un nodo inicio : nodoFuente
      Utilizamos el array visitados por que nodos hemos pasado
      DFS utiliza una pila para recorrer el grafo Last in First Out
      """

      gdfsi = Grafo('DFSi')
      diccionarioNodos = grafoGenerado.nodos 
      visitados = [nodoFuente]
      pila = [nodoFuente]
      while pila:
          m = pila.pop()
          if m not in visitados:
              visitados.append(m)
          for nodoAdjacente in diccionarioNodos[m].attributos['Vecino']:
              if nodoAdjacente.id not in visitados:
                  if nodoAdjacente.id not in pila:
                      pila.append(nodoAdjacente.id)

          if pila:
              ultimoNodo = pila[-1]
              gdfsi.addArista('{} -- {}'.format(str(m), str(ultimoNodo)),str(m),str(ultimoNodo))

      return gdfsi


  def dijkstra(grafoFuente, s, t):
      """
      dijkstra encuentra camino más corto entre nodos en un grafo.
      :param grafoFuente: el grafo original
      :param s: node fuente
      :param t: node objetivo
      :return g un grafo del nodo fuente al nodo objetivo
      """
      l = []
      dist = {}
      prev = {}
      descubierto = {}
      diccNodos = grafoFuente.nodos
      diccAristas = grafoFuente.aristas
      for v in diccNodos:
          dist[v] = float('inf')
          prev[v] = None
          descubierto[v] = False
      dist[s] = 0
      l.append((s, dist[s]))
      while len(l) != 0:
          u = min(l, key=lambda x: x[1])
          l.remove(u)
          u = u[0]
          descubierto[u] = True
          if u == t:
              break
          for v in diccNodos[u].attributos['Vecino']:
              if not descubierto[v.id]:
                  try:
                      alt = dist[u] + diccAristas['{} -- {}'.format(u,v.id)].attributos["Peso"]
                  except:
                      alt = dist[u] + diccAristas['{} -- {}'.format(v.id,u)].attributos["Peso"]
                  if alt < dist[v.id]:
                      dist[v.id] = alt
                      prev[v.id] = u
                      l.append((v.id, dist[v.id]))

      u = t
      g = Grafo('Dijkstra')
      while u is not None:
          nodoU = g.addNodo(u)
          nodoU.attributos['Dijkstra'] = dist[u]
          if prev[u] is not None:
              nodoPrevioU = g.addNodo(prev[u])
              nodoPrevioU.attributos['Dijkstra'] = dist[prev[u]]
              g.addArista('{} -- {}'.format(prev[u],u),prev[u],u)
              u = prev[u]
          else:
              break
      return g

  def proyecta(g):
      nodos = g.nodos.keys()
      nodos = list(nodos)
      aristas = g.aristas.keys()
      aristas = list(aristas)
      for nodoID in nodos:
          objetoNodo = g.dameNodo(nodoID)
          x = objetoNodo.x
          y = objetoNodo.y
          coordenadas = np.array([x,y])
          vecinos = objetoNodo.atributos['Vecinos']
          s = np.zeros(2)
          for vecinoID in vecinos:
              objetoVecino = g.dameNodo(vecinoID.id)
              x1 = objetoVecino.x 
              y1 = objetoVecino.y
              d = distanciaEntrePuntos(x,y,x1,y1)
              ga = c2*math.log(d/c1)
              vVecino = np.array([x1,y1])
              #nombreArista = '{} -- {}'.format(nodoID, vecinoID)

              vF = vVecino - coordenadas
              normalizar = np.linalg.norm(vF)
              vF = vF/normalizar 
              vF = ga * vF 
              s += vF
          coordenadas += s 
          nx = coordenadas[0]
          ny = coordenadas[1]
          objetoNodo.gx = nx 
          objetoNodo.gy = ny 
    
      for nodoID in nodos:
          objetoNodo = g.dameNodo(nodoID)
          objetoNodo.x = objetoNodo.gx
          objetoNodo.y = objetoNodo.gy
  
      for arista in aristas:
          objetoArista = g.aristas[arista]
          nodo0 = objetoArista.n0
          nodo1 = objetoArista.n1 
          x1 = nodo0.x 
          y1 = nodo0.y
          x2 = nodo1.x 
          y2 = nodo1.y

          d = distanciaEntrePuntos(x1,y1,x2,y2)

    
          pygame.draw.circle(ventana,color,(int(x1),int(y1)),radio)
          pygame.draw.circle(ventana,color,(int(x2),int(y2)),radio)
          pygame.draw.line(ventana, 'white', (int(x1), int(y1)), (int(x2), int(y2)), 1)

