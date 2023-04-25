# create class
class User:
    def __init__(self,name,email,age):
        self.name=name
        self.email=email
        self.age=age
  # create method      
    def greeting(self):
      return f'My name is {self.name} and I am {self.age}'   
        
    def has_birthday(self):
       self.age+=1

 #extend class
class Customer (User):
      def __init__(self,name,email,age):
        self.name=name
        self.email=email
        self.age=age
        self.balance=0

      def set_balance(self,balance):
          self.balance=balance
      def greeting(self):
        return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'  

# init user object
brad=User('Brad Traversy','gh#gmail.com',37)

# initialize customer
janet=Customer('Janet Jackson', "janet@gmail.com",25)
janet.set_balance(500)
brad.has_birthday() 
print(brad.greeting())
print(janet.greeting())