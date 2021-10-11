import turtle


class Risanje(object):

    def __init__(self):
        """ Inicializira objekt Risanje.
         Kreira dva objekta class-a Turtle.
        """
        turtle.setup()
        turtle.screensize(100000, 100000)
        self.__risi_pot = turtle.Turtle()
        self.__risi_prijatelje = turtle.Turtle()
        self.__risi_pot.color('red')
        self.__risi_pot.pensize(2)
        self.__risi_pot.speed('fast')
        self.__risi_prijatelje.speed('fast')

    def narisi_pot(self, graf, start, end, pot):
        """ Z uporabo Turtle grafično prikaže
            najkrajšo pot med dvema besedama."""
        slovar = graf.get_slovar()
        if len(pot) == 1:
            self.__risi_pot.write(start, align='center', font=("Arial", 15, "normal"))
            kot = 360 / len(slovar[start])
            # nariše vse prijatelje
            for bes1 in slovar[start]:
                self.__risi_prijatelje.right(kot)
                self.__risi_prijatelje.forward(100)
                self.__risi_prijatelje.write(bes1, align='right')
                self.__risi_prijatelje.back(100)
            return
        pot = pot[1:]
        self.__risi_pot.write(start, align='center', font=("Arial", 15, "normal"))
        kot = 360 / len(slovar[start])
        # nariše vse prijatelje
        for bes1 in slovar[start]:
            self.__risi_prijatelje.right(kot)
            self.__risi_prijatelje.forward(100)
            self.__risi_prijatelje.write(bes1, align='right')
            self.__risi_prijatelje.back(100)
        # nariše naslednji korak v poti
        self.__risi_pot.penup()
        self.__risi_pot.forward(150)
        self.__risi_pot.pendown()
        self.__risi_pot.forward(300)
        self.__risi_pot.penup()
        self.__risi_pot.forward(150 + 100)
        self.__risi_pot.pendown()
        self.__risi_prijatelje.penup()
        self.__risi_prijatelje.forward(700)
        self.__risi_prijatelje.pendown()

        self.narisi_pot(graf, pot[0], end, pot)

    def zapri_risalno_okno(self):
        """ Z klikom na risalno okno zapremo okno.
        Metoda doddana zato da se okno ne zapre samo
        od sebe po končanem risanju. """
        self.__risi_pot.screen.exitonclick()
