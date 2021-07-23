class Addition:      
    def __init__(self, f, s):
        self.first = f
        self.second = s
    
    def calculate(self):
        self.answer = self.first + self.second

    def display(self):
        print("Addition of two numbers = " + str(self.answer))


  
firs_num = int(input("Enter your first number: "))
sec_num = int(input("Enter your second number: "))
obj = Addition(firs_num, sec_num)
  
obj.calculate()
obj.display()