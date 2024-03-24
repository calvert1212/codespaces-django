class item:
 
    # default constructor
    def __init__(self, name):
        self.name = [name]
        self.attr = []
    
    def add_atrr(self, att):
        self.attr.append(att)
    
    # a method for printing data members
    def print_iname(self):
        print(self.name)
 