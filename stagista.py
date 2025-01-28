#Costruire una sottoclasse di PErsona, chiamata Stagista, che contiene
#2 variabili di istanza entrambe di tipo intero:
#numero presenza, che registra il numero di ore di presenza
#numero identificativoà
#la sottoclasse deve contenere un costruttore parametrico ed i metodi set ger
#Creare un arrau di tipo stagista memorizzarli in un array e visualizzare lo stagista più giovane


class Persona:
    def __init__(self, numero_presenza, numero_identificativo):
        self._numero_presenza = numero_presenza
        self._numero_identificativo = numero_identificativo

#    def __str__(self):
#        return f"Stagista numero {self._numero_identificativo} ha preso {self._numero_presenza} ore"


class Stagista(Persona):
    def __init__(self, numero_presenza, numero_identificativo):
        super().__init__(numero_presenza, numero_identificativo)


    def set_stagista_numero(self, numero_presenza):
        self._numero_presenza = numero_presenza

    def get_stagista_numero(self):
        return self._numero_presenza

    def set_stagista_identificativo(self, numero_identificativo):
        self._numero_identificativo = numero_identificativo

    def get_stagista_identificativo(self):
        return self._numero_identificativo

