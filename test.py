import json
from collections import deque
import turtle


with open('slovar_besed_ter_sosedov.txt', 'r') as beri:
    data = beri.read()
    slovar = json.loads(data)


def najkrajsa_pot(graph, bes1, bes2):
    """ Z uporabo algoritma 'Breadth-first-search'
    vrne najkrajšo pot med dvema besedama."""
    srecane = {bes1: [bes1]}
    x = deque()
    x.append(bes1)
    while len(x):  # len(x) > 0 is True
        trenutno = x.popleft()  # isto kot x.pop(0) samo hitreje
        for naslednji in graph[trenutno]:  # po prijateljih
            if naslednji not in srecane:
                srecam_zdaj = srecane[trenutno] + [naslednji]
                srecane[naslednji] = srecam_zdaj
                x.append(naslednji)
    return srecane.get(bes2)


print(najkrajsa_pot(slovar, 'okno', 'drevo'))
#print(slovar['okno'])
print(najkrajsa_pot(slovar, 'oklo', 'drevo'))
#print(slovar['oklo'])

turtle.setup()
turtle.screensize(2000, 2000)
risi_pot = turtle.Turtle()
risi_prijatelje = turtle.Turtle()
risi_pot.color('red')
risi_pot.speed('fast')
risi_prijatelje.speed('fast')


def narisi_pot(slovar, start, end, pot):
    """ rekurzivna pot med besedama"""
    if len(pot) <= 1:
        risi_pot.write(start, align='center')
        print('nisem pot sem točka.')
        return 'nisem pot sem točka.'
    kot = 360 / len(slovar[start])
    # zacetna smer : leva
    risi_prijatelje.right(180-kot)
    risi_pot.left(180)
    # uredim besede
    for bes1 in slovar[start]:
        if bes1 in pot:
            risi_pot.forward(70)
            risi_pot.write(bes1, align='right')
            risi_pot.back(70)
            risi_pot.right(kot)
        risi_prijatelje.forward(70)
        risi_prijatelje.write(bes1, align='right')
        risi_prijatelje.back(70)
        risi_prijatelje.right(kot)
    risi_prijatelje.penup()
    risi_prijatelje.right(180 + kot)
    risi_prijatelje.forward(300)
    risi_prijatelje.pendown()
    pot = pot[1:]
    narisi_pot(slovar, pot[0], end, pot)


p = najkrajsa_pot(slovar, 'okno', 'drevo')
narisi_pot(slovar, 'okno', 'drevo', p)
#narisi_pot(slovar, 'okno', 'drevo',['okno', 'oklo', 'klo', 'klok', 'klek', 'krek', 'drek', 'drev', 'drevo'])
risi_pot.screen.exitonclick()
