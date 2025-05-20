import pyxel
from random import*

class App:
    def __init__(self):
        pyxel.init(128, 128,title="Koffre",fps=60)
        pyxel.load("assets.pyxres")

        largeur=[i for i in range(8,112)]
        longueur=[j for j in range(8,112)]
        NbProp=15
        self.proplist=[]
        for i in range(NbProp):

            if longueur!=[] and largeur!=[]:

                x=choice(largeur)
                y=choice(longueur)
                self.proplist.append(Prop(x,y))

                for k in range(x-8,x+8):
                    if k in largeur:
                        largeur.remove(k)
                for k in range(y-8,y+8):
                    if k in longueur:
                        longueur.remove(k)


        self.statut=0
        self.time="jour"
        self.sec=0


        self.player1=Player1(randint(8,120), randint(8,120))

        self.player2=Player2()

        self.stal_list=[]
        for i in range(8) :
            self.stal_list.append((randint(16,112),randint(16,112), choice([32,40]),choice([0,8])))

        pyxel.run(self.update, self.draw)

    def update(self):

        if self.statut==0:
            if pyxel.frame_count%60==0:
                self.sec+=1
                print(self.sec)

                if self.sec==100:
                    self.statut=2
                if self.sec%10==0:
                    if self.time=="jour":
                        self.time="nuit"
                    else:
                        self.time="jour"
                        self.player2.permtir=True

            self.player1.move()

            self.player2.move()
            if self.player2.permtir==True and self.time=="jour":
                if self.player2.tir(self.proplist,self.player1)==True:
                    self.statut=1


    def draw(self):

        if self.statut==0:
            if self.time=="jour":
                pyxel.cls(1)
                pyxel.bltm(0,0, 0, 0,0, 128, 128)

                for i in range(len(self.stal_list)) :
                    pyxel.blt(self.stal_list[i][0], self.stal_list[i][1], 0, self.stal_list[i][2], self.stal_list[i][3], 8,8)

                for prop in self.proplist:
                    prop.show()

                self.player1.show()
            else:
                pyxel.cls(0)
                pyxel.bltm(0,0,1,0,0,128,128)


            self.player2.show()


        elif self.statut==1:
            pyxel.cls(0)
            pyxel.text(32, 64, "THE HUNTER WON ", 7)
        else:
            pyxel.cls(0)
            pyxel.text(32, 64, " THE PROP WON ", 7)

class Player1:
    def __init__(self,x,y,):
        self.x=x
        self.y=y
        self.skin=(choice((0,8)),choice((0,8,16,24)))

    def move(self):
        if pyxel.btn(pyxel.KEY_DOWN) and self.y+8<120:
            self.y+=1
        if pyxel.btn(pyxel.KEY_UP) and self.y>8:
            self.y-=1
        if pyxel.btn(pyxel.KEY_RIGHT) and self.x+8<120:
            self.x+=1
        if pyxel.btn(pyxel.KEY_LEFT) and self.x>8:
            self.x-=1

    def show(self):
        pyxel.blt(self.x, self.y, 0, self.skin[0], self.skin[1], 8, 8, 13)


class Player2:
    def __init__(self):
        self.x=pyxel.mouse_x
        self.y=pyxel.mouse_y
        self.permtir=True

    def show(self):
        pyxel.blt(self.x, self.y, 0, 32, 16, 8, 8, 0)

    def move(self):
        self.x=pyxel.mouse_x
        self.y=pyxel.mouse_y
    def tir(self,proplist,joueur):
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
            self.permtir=False
            for prop in proplist:
                if pyxel.mouse_x>=prop.x-2 and pyxel.mouse_x<prop.x+7 and pyxel.mouse_y>=prop.y-2 and pyxel.mouse_y<prop.y+7:
                    prop.skin=(0,32)
            if pyxel.mouse_x-1>=joueur.x-2 and pyxel.mouse_x-1<joueur.x+7 and pyxel.mouse_y>=joueur.y-2 and pyxel.mouse_y-1<joueur.y+7:
                return True
            return False

class Prop:

    def __init__(self,x,y):
        self.x=x
        self.y=y

        self.skin=(choice((0,8)),choice((0,8,16,24)))

        self.alive=True

    def show(self):
        pyxel.blt(self.x, self.y, 0, self.skin[0], self.skin[1], 8, 8, 13)



App()




