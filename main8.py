from claseconjunto import Conjunto


def  opcion1 (c1):
    c2=Conjunto()
    print('CONJUNTO DOS\n')
    c2.agregar()
    c1.mostrar()
    c2.mostrar()
    c3=c1+c2
    c3.mostrar()
def  opcion2 (c1):
    c2=Conjunto()
    print('CONJUNTO DOS\n')
    c2.agregar()
    c1.mostrar()
    c2.mostrar()
    c3=c1-c2
    c3.mostrar()
def opcion3(c1):
    c2=Conjunto()
    print('CONJUNTO DOS\n')
    c2.agregar()
    c1.mostrar()
    c2.mostrar()
    c3=c1==c2
    if(c3==1):
        print('Los conjuntos son iguales')
    else:
        print('Los conjuntos no son iguales')
    
    
switcher = {
    1 : opcion1,
    2 : opcion2,
    3 : opcion3,
}

def switch (argumento,alumno):
    func  =  switcher.get ( argumento , lambda : print ( "Opción incorrecta" ))
    func (c1)
if __name__ == '__main__':
    c1=Conjunto()
    c1.agregar()
    c1.mostrar()
    bandera='falso'
    while bandera=='falso':
     print('')
     print ( "      Menu" )
     print ( " 1 Union de Conjuntos" )
     print ( ' 2 Diferencia de conjuntos')
     print('   3 Comparar conjuntos')
     opcion =  int ( input ( "Ingrese una opción: " ))
     switch(opcion,c1)
     op=(input('Desea Continuar? '))
     if(op=='no'):
         bandera='verdadero'
         print('ADIOS')
   