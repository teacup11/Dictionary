from slovar_objekt import slovar
from slovar_objekt import Graph
from risanje import Risanje


def main():
    graph = Graph(slovar)
    bes1 = input('Vnesi prvo besedo: ')
    bes2 = input('Vnesi drugo besedo: ')
    # preverim ali so besede sploh v slovarju
    if graph.sem_v_slovarju(bes1) and graph.sem_v_slovarju(bes2):
        # preverim ali sta besedi povezani
        if graph.sva_povezani(bes1, bes2):
            pot = graph.najkrajsa_pot(bes1, bes2)
            print('Najkrajša pot med besedama {0} ter {1} je: {2}'.format(bes1, bes2, pot))
            print('Pot je dolžine: {0}'.format(graph.dolzina_najkrajsa_pot(bes1, bes2)))
            input('Pritisni enter za grafični izris poti')
            risanje = Risanje()
            risanje.narisi_pot(graph, bes1, bes2, pot)
            risanje.zapri_risalno_okno()
        else:
            print('Med besedama ne obstaja pot.')
    else:
        print('Besedi ali ena izmed njiju nista zapisani v slovarju.')


main()
