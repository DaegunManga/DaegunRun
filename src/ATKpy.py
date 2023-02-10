class ATK () :
    def __init__ (self) :
        self.attack_L = []
        self.speed = 5
    
    def create_ATK (self, x, y) :
        self.attack_L.append([x, y])
    
    def move_ATK (self) :
        for L in self.attack_L :
            L[0] += self.speed
            if L[0] > 1020 :
                self.del_ATK(L)
        return self.attack_L
         
    def del_ATK (self, L) :
        self.attack_L.remove(L)
