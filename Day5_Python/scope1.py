class BMI: 
    name = 'default_name'  
    def set_name(self, name_arg):
        self.name = name_arg
        name = 'John'
        
    def judge(self, height, weight):
        calculate = weight / (height*height)
        if calculate < 18.5:
            self.result = '過輕'
        elif 18.5 < calculate and calculate < 24:
            self.result = '正常'
        else:
            self.result ='過重'
    def display(self): # 展示結果
        print('Name:', self.name, 'result:',self.result)
        
man = BMI()
man.set_name('Keven')
man.judge(1.82, 50)
man.display()