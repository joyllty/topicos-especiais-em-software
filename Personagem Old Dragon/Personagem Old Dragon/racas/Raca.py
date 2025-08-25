from abc import ABC, abstractmethod

class Raca(ABC):
    def __init__(self, movimento, infravisao, alinhamento, peso_base):
        self.movimento = movimento
        self.infravisao = infravisao
        self.alinhamento = alinhamento
        self.peso_base = peso_base
    #   self.idades = [] 
        self.habilidades = []
    
    @abstractmethod
    def habilidades():
       pass
    

    
