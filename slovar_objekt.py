import json
from collections import deque


# slovar
with open('slovar_besed_ter_sosedov.txt', 'r') as f:
    data = f.read()  # oblike str in ne iowrapper
    slovar = json.loads(data)


class Graph(object):

    def __init__(self, graph_slovar=None):
        """ Inicializira objekt graf.
            Če ni slovarja naredi prazen slovar.
        """
        if graph_slovar is None:
            graph_slovar = {}
        self.__graph_slovar = graph_slovar

    def vozlisca(self):
        """ Vrne seznam vozlišč grafa. """
        return list(self.__graph_slovar.keys())

    def get_slovar(self):
        return self.__graph_slovar

    def __generiraj_stranice(self):
        """ Metoda ki generira stranice grafa.
            Stranice so predstavljene kot množice z enim ali dvema vozliščema.
            Vrne seznam množic.
        """
        stranice = []
        for vozlisce in self.__graph_slovar:
            for sosed in self.__graph_slovar[vozlisce]:
                if {sosed, vozlisce} not in stranice:  # izberem tipa množica ker nima vrstnega reda
                    stranice.append({vozlisce, sosed})
        return stranice

    def stranice(self):
        """ Vrne seznam stranic grafa. """
        return self.__generiraj_stranice()

    def __str__(self):
        """ Izpiše graf kot niz oblike
            vozlišča: ...
            stranice: ..."""
        niz = "vozlišča: "
        for i in self.__graph_slovar:
            niz += str(i) + " "
        niz += "\nstranice: "
        for stranica in self.__generiraj_stranice():
            niz += str(stranica) + " "
        return niz

    def osamljena_vozlisca(self):
        """ Vrne seznam vseh vozlišč ki so stopnje 0. """
        graph = self.__graph_slovar
        osamljena = []
        for voz in graph:
            if not graph[voz]:  # nima prijateljev
                osamljena.append(voz)
        return osamljena

    def sem_v_slovarju(self, bes):
        """ Vrne True če je beseda v slovarju,
        v nasprotnem primeru vrne False."""
        return bes in self.vozlisca()

    def najkrajsa_pot(self, bes1, bes2):
        """ Z uporabo algoritma 'Breadth-first-search'
        vrne najkrajšo pot med dvema besedama."""
        srecane = {bes1: [bes1]}
        x = deque()
        x.append(bes1)
        while len(x):  # len(x) > 0 is True
            trenutno = x.popleft()  # isto kot x.pop(0) samo hitreje
            for naslednji in self.__graph_slovar[trenutno]:  # po prijateljih
                if naslednji not in srecane:
                    srecam_zdaj = srecane[trenutno] + [naslednji]
                    srecane[naslednji] = srecam_zdaj
                    x.append(naslednji)
        return srecane.get(bes2)

    def sva_povezani(self, bes1, bes2):
        """ Vrne True če med besedama obstaja pot,
        v nasprotnem primeru vrne False"""
        if self.najkrajsa_pot(bes1, bes2) is None:
            return False
        return True

    def dolzina_najkrajsa_pot(self, bes1, bes2):
        """ Vrne število korakov ki so potrebnih da preidemo iz ene
        besede v drugo. """
        return len(self.najkrajsa_pot(bes1, bes2)) - 1



#print('Naš graf vsebuje: {0} osamljenih besed'.format(len(graph.osamljena_vozlisca())))

