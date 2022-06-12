from nodo import Nodo
#weight = 'Peso'

class Arista:
  def __init__(self, n_arista, nodo_fuente: Nodo, nodo_destino: Nodo,peso):
    """
    Clase Arista
    n_arista : Nombre
    nodo_fuente : 
    nodo_destino :
    """
    self.id = n_arista
    self.inicio = nodo_fuente
    self.final = nodo_destino
    self.attributos = {
            'Peso': peso,
    }

