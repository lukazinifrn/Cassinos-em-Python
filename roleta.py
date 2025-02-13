import random

class Gambling():
    def __init__(self):
        self.l1 = "NaN"
        self.l2 = "NaN"
        self.l3 = "NaN"
        
    def letterA(self):
        random_factor = random.randint(0, 100)
        if random_factor <= 60:
            self.l1 = "A"
        if 60 < random_factor <= 80:
            self.l1 = "B"
        if 80 < random_factor <= 100:
            self.l1 = "C"
        return self.l1
    
    def letterB(self):
        random_factor = random.randint(0, 100)
        if random_factor <= 60:
            self.l2 = "B"
        if 60 < random_factor <= 80:
            self.l2 = "A"
        if 80 < random_factor <= 100:
            self.l2 = "C"
        return self.l2
    
    def letterC(self):
        random_factor = random.randint(0, 100)
        if random_factor <= 60:
            self.l3 = "C"
        if 60 < random_factor <= 80:
            self.l3 = "B"
        if 80 < random_factor <= 100:
            self.l3 = "A"
        return self.l3
    
    def return_list_letters(self):    
        return [self.letterA(), self.letterB(), self.letterC()]
