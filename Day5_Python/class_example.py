class Human:

    blood_color = 'red'
    eye_shape = 'circle'

    def cry(self):
        print(self.blood_color, 'crying')
    def set_name(self, your_name):
        print('set name', your_name)
        self.my_name = your_name

p1 = Human()
p2 = Human()

p1.cry()  #   Human.cry(p1)
p1.cry()  #   Human.cry(p2)

p1.set_name('charlie')

'''
set_name(self, your_name)
set_name(p1, your_name):
    p1.my_name = your_name
'''

print(p1.my_name)