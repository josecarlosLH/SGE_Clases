class Empleado:
    def __init__(self, nombre, apellido, dni, direccion, antiguedad, tlf, salario):
        self.nombre=nombre
        self.apellido=apellido
        self.dni=dni
        self.direccion=direccion
        self.antiguedad=antiguedad
        self.tlf=tlf
        self.salario=salario
    def imprimir(self):
        print("Nombre: ", self.nombre , " Apellido: " , self.apellido , " DNI: " , self.dni ,
              " Dirección: " , self.direccion , " Antigüedad: " , self.antiguedad ,
              "Telefono: " , self.tlf , "Salario: " , self.salario)

    def cambiarSupervisor(self, supervisor):
        self.supervisor=supervisor
        print("El nuevo supervisor es: ", supervisor)

    def incrementarSalario(self, incremento):
        self.salario= (self.salario * incremento)/100 + self.salario
        print("El salario incrementado es: ", self.salario)

empleado1=Empleado("Juan", "Garcia","454454s","Calle falsa 123",2,65478541,25000)
empleado2=Empleado("Maria","Marquez","234454s","Calle 3",1,6878541,15000)

empleado1.imprimir()
empleado1.incrementarSalario(2)

print("--------------------FIN EMPLEADO-----------------")

class Secretario(Empleado):
    def __init__(self,nombre, apellido, dni, direccion, antiguedad, tlf, salario, fax, despacho, puesto):
        Empleado.__init__(self,nombre, apellido, dni, direccion, antiguedad, tlf, salario)
        self.fax=fax
        self.despacho=despacho
        self.puesto=puesto

    def incrementarSalario(self):
        super(Secretario, self).incrementarSalario(5)

    def imprimir(self):
        super(Secretario, self).imprimir()
        print("Puesto: " + str(self.puesto))

secretario1=Secretario("Pepe","Martin","5458787w","Calle 1",3,65475413,30000, "9657854123","D01","Secretario de direccion")
secretario2=Secretario("Sandra","Moreno","6523527t","Calle 67",2,67895432,30000, "9665756746","D01","Secretario de direccion")

secretario1.imprimir()
print(
    "El fax del secretario ", secretario1.nombre, " es: ", secretario1.fax,
    "El despacho de secretario ", secretario1.nombre, " es el: ", secretario1.despacho,
    "Su puesto en la empresa es ", secretario1.puesto)
secretario1.incrementarSalario()
print("--------------------FIN SECRETARIO-----------------")

class Coche:
    def __init__(self,matricula, marca, modelo):
        self.matricula=matricula
        self.marca=marca
        self.modelo=modelo

coche1 = Coche("25412EEE","Seat","Ibiza")
coche2 = Coche("32154EEE","Huindai","Montero")

listaClientes = ["Jose","Fernando","Isa"]

class Vendedor(Empleado):
    def __init__(self, nombre, apellido, dni, direccion, antiguedad, tlf, salario, coche1, area, comision, listaClientes ):
        Empleado.__init__(self, nombre, apellido, dni, direccion, antiguedad, tlf, salario)
        self.coche = coche1
        self.area=area
        self.comision=comision
        self.listaClientes=listaClientes

    def alta(self, nombre):
        self.listaClientes.append(nombre)

    def baja(self, nombre):
        self.listaClientes.remove(nombre)

    def cambiarCoche(self, coche):
        self.coche=coche
        print("El nuevo coche es: ", coche.marca)

    def incrementarSalario(self):
        super(Vendedor, self).incrementarSalario(10)

listaVendedores=["Tomás","Luis","Antonio"]

vendedor1=Vendedor("Sergio","Lopez","6523527t","Calle Villa",1,674523652,20000, coche1, "Ventas", 5, listaClientes)
vendedor1.imprimir()

print(
    "Marcar coche: ", vendedor1.coche.marca,
    "Area de trabajo: ", vendedor1.area,
    "Comisión: ", vendedor1.comision,
    "Lista de clientes: ", vendedor1.listaClientes)
vendedor1.incrementarSalario()

print("--------------------FIN VENDEDOR-----------------")

class Jefe(Empleado):
    def __init__(self, nombre, apellido, dni, direccion, antiguedad, tlf, salario, secretario1, coche2, despacho, listaVendedores ):
        Empleado.__init__(self, nombre, apellido, dni, direccion, antiguedad, tlf, salario)
        self.secretario=secretario1
        self.coche=coche2
        self.despacho=despacho
        self.listaVendedores=listaVendedores

    def incrementarSalario(self):
        super(Jefe, self).incrementarSalario(20)

    def cambiarSecretario(self, secretario):
        self.secretario=secretario
        print("El nuevo secretario es: ", secretario.nombre)

    def cambiarCoche(self, coche):
        self.coche=coche
        print("El nuevo coche es: ", coche.marca)

    def altaVendedor(self, nombre):
        self.listaVendedores.append(nombre)

    def bajaVendedor(self, nombre):
        self.listaVendedores.remove(nombre)

jefe1=Jefe("Jose Juan","Martinez","54125478E","Calle Sevilla",5,674541214,40000,secretario1,coche2,"Direccion",listaVendedores)
jefe1.imprimir()

print(
    "Secretario: ", jefe1.secretario.nombre," --- ",
    "Marca coche: ", jefe1.coche.marca," --- ",
    "Despacho: ", jefe1.despacho," --- ",
    "Lista de vendedores: ", jefe1.listaVendedores)
jefe1.incrementarSalario()
print("------------------------FIN JEFE-----------------")