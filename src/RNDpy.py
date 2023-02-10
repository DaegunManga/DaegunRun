import random
import OBJpy

class round :
    def __init__ (self, L) :
        self.round_L = L
        self.round_n = 0
        self.obj = OBJpy.object()
    
    def startgame (self, t) :
        if (t+1) % 600 == 0 :

            self.round_n += 1
            self.round(t)
            return self.obj.move_OBJ(), self.round_n, True
        else :
            self.round(t)
            return self.obj.move_OBJ(), self.round_n, False


    def round (self, t) :

        if t % (120 - 10*self.round_n) == 0 :
            try :
                L1 = self.round_L[self.round_n][random.randint(0, len(self.round_L[self.round_n])-1)]
                if L1[3] == 'up' :
                    self.obj.append_OBJ(0, L1[0], L1[1], L1[2])
                else :
                    self.obj.append_OBJ(600 - L1[2], L1[0], L1[1], L1[2])
            except IndexError :
                pass
