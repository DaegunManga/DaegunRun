import pygame
class object :
    def __init__ (self) :
        self.O_list = []
        self.O_start_X = 1020
        self.speed = -12


    def append_OBJ (self, O_strat_y, jpg, Xsize, Ysize) :
        self.O_list.append([self.O_start_X, O_strat_y, jpg, Xsize, Ysize])


    def delete_OBJ (self, L) :
        self.O_list.remove(L)


    def move_OBJ (self) :
        for L in self.O_list :

            L[0] += self.speed
            
            if L[0] <= -L[3] :
                self.delete_OBJ(L)

        return self.O_list