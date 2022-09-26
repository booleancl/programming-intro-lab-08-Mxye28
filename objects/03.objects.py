# Hasta ahora todos los elementos primitivos que hemos manejado
# Listas, Diccionarios, Strings, Numbers, etc tienen un cierto tipo
# que vemos con el método especial type()
# 
print(type(1))
print(type(['a','b','c']))
print(type(True)) 
print(type("Hello World"))

class Dog: 
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def say_name(self):    
        print("Mi nombre es", self.name,"y tengo",self.age,"años")
        
firulais = Dog("firulais", 4)
lulu = Dog("lulu", 5)
leon = Dog("leon", 2)
print(type(firulais))

firulais.say_name()
lulu.say_name()
leon.say_name()
