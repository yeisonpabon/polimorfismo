def multiplicar(a,b):
    return a*b

print(multiplicar(11,22))
print(multiplicar('Hola',11))

##ejercicio 2
class Animal:
    def sonido(self):
        return 'el animal hace un sonido.'
    
class Perro(Animal):
    def sonido(self):
        return 'el perro ladra'

class Gato(Animal):
    def sonido(self):
        return 'el gato maulla'
    
class Pollito(Animal):
    def sonido(self):
        return 'el pollito hace pio pio'
    
animales = [Perro(),Gato(),Pollito()]

for animal in animales:
    print(animal.sonido())


##ejrcicio 3 

class Vector:
    def __init__ (self,x,y):
        self.x = x
        self.y = y

    def __add__(self,other):
        return Vector(self.x * other.x,self.y * other.y)

    def __repr__(self):
        return f'vector ({self.x},{self.y})'

v1=Vector(5,2)
v2=Vector(3,4)

v3= v1 + v2
print(v3) # vetcor(4,6)