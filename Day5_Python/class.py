class NewType:
    age = 0
    height = 0
    weight = 0
    
    def walk(self):
        self.w = 1
        print(self.name, 'is walking')

    def sing(self):
        print(self.w)
    

    
man = NewType()
man.name = 'man'
woman = NewType()
#print(woman.name)

#print(man.age)
man.walk()
man.sing()