from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
import time

array = [-1]*9
print(array[1])
symbol = 'x'

def change():
    global symbol
    if symbol == 'x':
        symbol = 'o'
    elif symbol == 'o':
        symbol = 'x'

def check_duplicate(num):
    global symbol
    if array[num-1] == -1:
        array[num-1] = symbol
        return False
    else:
        print(array[num-1])
        return True

def check_win():
    #horizontal
    for x in range (0,9,3):
        win = True
        for y in range (3):
            if array[x+y] != symbol:
                win = False
        if win == True:
            return True
    #vertical
    for y in range (3):
        win = True
        for x in range (3):
            if array[3*x+y] != symbol:
                win = False
        if win == True:
            return True

    #diagonal
    if array[0] == array[4] == array[8] == symbol:
        return True
    elif array[2] == array[4] == array[6] == symbol:
        return True
    
    return False

def show_popup():
    pop = Popup(title='Winner', content=Label(text=''), auto_dismiss=False)
    winner = ""
    if symbol == 'x':
        winner = "player 1 with symbol: x wins"
    else:
        winner = "player 2 with symbol: o wins"
    pop.content.text = winner
    pop.open()


class MyTTT(GridLayout):
    global array, symbol

    pass

    turns = 0

    turn1 = ObjectProperty(None)
    turn2 = ObjectProperty(None)

    def update_button_text(self, num):
        self.children[9-num].text = str(symbol)

    def turn(self):
        if self.turns%2==1:
            self.turn1.text = "Wait"
            self.turn2.text = "Go"
        else:
            self.turn1.text = "Go"
            self.turn2.text = "Wait"
   
    def onClick(self, num):
        global array, symbol
        print("hello {}".format(num))
        duplicate = check_duplicate(num)
        print (duplicate)
        if not duplicate:
            self.turns +=1
            self.update_button_text(num)
            self.turn()
            win = check_win()
            # self.b1.text = symbol
            print (win)
            if win:
                array = [-1]*9
                time.sleep(1)
                show_popup()
            change()

class TicTacToe(App):
    def build(self):
        return MyTTT()
    

ttt = TicTacToe()
ttt.run()