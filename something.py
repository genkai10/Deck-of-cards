import time
import turtle
import random
wn=turtle.Screen()
wn.bgcolor("black")
wn.setup(800,600)
wn.title("Deck of cards")

pen=turtle.Turtle()
#pen.speed(0)
pen.hideturtle()

#time.sleep(3)

class Card():
    def __init__(self,name,suit):
        self.name=name
        self.suit=suit
        self.symbols ={"D":"♦", "C":"♣", "H":"♥", "S":"♠"}

    def print_card(self):

        if self.suit=="S":
            symbol="♠"
        #clubs(♣), diamonds(♦), hearts(♥) and spades(♠),
        print(f"{self.name}{self.symbols[self.suit]}")

    def render(self,x,y,pen):
        #Draw the border
        pen.penup()
        pen.goto(x,y)
        pen.color("white")
        pen.goto(x-50,y+75)
        #pen.begin_fill()
        pen.pendown()
        pen.goto(x+50,y+75)
        pen.goto(x+50,y-75)
        pen.goto(x-50,y-75)
        pen.goto(x-50,y+75)
        #pen.end_fill()
        pen.penup()
        if self.name !="":
            #Draw the suit in the middle
            pen.goto(x-20,y-35)
            #pen.color("white")
            #pen.begin_fill()
            pen.write(self.symbols[self.suit],False,font=("Courier New",56,"normal"))
            #pen.end_fill()

            #Draw top left
            pen.goto(x-40,y+45)
            pen.write(self.name,False,font=("Courier New",18,"normal"))
            pen.goto(x-40,y+25)
            pen.write(self.symbols[self.suit],False,font=("Courier New",18,"normal"))

            #Draw bottom right

            pen.goto(x+30,y-55)
            pen.write(self.name, False, font=("Courier New", 18, "normal"))
            pen.goto(x+30,y-75)
            pen.write(self.symbols[self.suit], False, font=("Courier New", 18, "normal"))

'''card=Card("A","S")
card.render(0,0,pen)'''

class Deck():
    def __init__(self):
        self.cards=[]

        names=("A","K","Q","J","T","9","8","7","6","5","4","3","2")
        suits=("D","C","H","S")

        for name in names:
            for suit in suits:
                card=Card(name,suit)
                self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def get_card(self):
        card=self.cards.pop()
        return card

    def reset_deck(self):
        self.cards = []

        names = ("A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2")
        suits = ("D", "C", "H", "S")

        for name in names:
            for suit in suits:
                card = Card(name, suit)
                self.cards.append(card)

        self.shuffle()


#create deck
deck=Deck()
#shuffle deck
deck.shuffle()
#reset deck
deck.reset_deck()
#card=deck.get_card()
#card.render(0,0,pen)

#render 5 cards in a row (back)
start_x=-250
for x in range(1):
    card=Card("","")
    card.render(start_x +x*125,0,pen)

time.sleep(5)

#render 5 cards in a row
start_x=-250
for x in range(1):
    card=deck.get_card()
    card.render(start_x +x*125,0,pen)


#for card in deck.cards:
    #pen.clear()
    #card.render(0,0,pen)
    #card.print_card()


wn.mainloop()
