import random

class Gambling():
    def __init__(self, items: dict = {"item" : "chance"}, list_size: int = 3):
        self.terms = list(items.keys())
        self.chances = list(items.values())
        self.gamb_list = []
        self.list_size = list_size
        
    def result_list(self):
        b = []
        for j in range(self.list_size):
            for i in range(len(self.terms)):
                chance_factor = random.randint(0, 100)
                if chance_factor <= self.chances[i]:
                    b.append(self.terms[i])
            if b:
                self.gamb_list.append(random.choice(b))
            else:
                self.gamb_list.append(random.choice(self.terms))
            b.clear()
        
        return self.gamb_list
    
    
            
                
        
