import math
class Punto:
    def __init__(self, x, y):
        self.x=x
        self.y=y

class Forma(Punto):
    def __init__(self,x, y, color, nombre):
        super().__init__(x, y)
        self.color=color
        self.nombre=nombre
    def print(self):
        print("Coordenadas x " + str(self.x) + " Coordenadas y " + str(self.y) + " Color -> " + self.color +" Nombre -> "+self.nombre)
    def obtener(self):
        return self.nombre,self.punto.x, self.punto.y
    def cambiarForma(self,x,y):
        self.x=x
        self.y=y

Forma1 = Forma( 2, 6,"Verde","Cuadrado")
Forma1.print()

class Rectangulo(Forma):
    def __init__(self, x, y, color, nombre, lMenor, lMayor):
        super().__init__(x, y, color,nombre)
        self.lMenor=lMenor
        self.lMayor=lMayor
    def print(self):
        super().print()
        print("Lado menor: " + str(self.lMenor)+ " Lado mayor: "+ str(self.lMayor))
    def Area(self):
        area=self.lMenor*self.lMayor
        print("El area es igual a: "+str(area))
    def perimetro(self):
        perimetro=2*self.lMenor+2*self.lMayor
        print("Perimetro: "+str(perimetro))

Rectangulo1=Rectangulo(4, 8, "Azul", "Rectangulo", 4, 9)
Rectangulo1.print()

class Elipse(Forma):
    def __init__(self, x, y, color, nombre, radioMayor, radioMenor):
        super().__init__(x,y,color,nombre)
        self.radioMayor=radioMayor
        self.radioMenor=radioMenor
    def areaElipse(self):
        area=math.pi*(self.radioMayor*self.radioMenor)
        print("Area de Elipse: "+str(area))

Elipse1=Elipse(2,5,"Rojo","Elipse", 6,3)
Elipse1.print()

class Cuadrado(Rectangulo):
    def __init__(self,x,y,color,nombre,lMenor, lMayor):
        super().__init__(x,y, color, nombre, lMenor, lMayor)
    def print(self):
        super().print()

class Circulo(Elipse):
    def __init__(self, x, y, color, nombre, radioMayor, radioMenor):
        super().__init__(x,y, color,nombre,radioMayor, radioMenor)
    def print(self):
        super().print()

Rectangulo2=Rectangulo(4, 8, "Amarillo", "Rectangulo", 3, 6)
Elipse2=Elipse(2,5,"Marrón","Elipse", 8,7)
Cuadrado2=Cuadrado(2,5,"Rosa","Cuadrado",2,8)
Circulo2=Circulo(3,6,"Azul","Circulo",10,5)

tupla=(Rectangulo2,Elipse2,Cuadrado2,Circulo2)
for Forma in tupla:
    print(Forma.print())
