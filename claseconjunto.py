class Conjunto:
    __Lis=[]
    def __init__(self):
        self.__Lis=[]
    def agregar(self):
        n=int(input('Numero agregar finalice con 00 '))
        while(n!=00):
             self.__Lis.append(n)
             n=int(input('Numero agregar finalice con 00 '))
    def getElem(self,ind):
        return self.__Lis[ind]
    def aE(self,nm):
        self.__Lis.append(nm)
    def getRango(self):
        return (len(self.__Lis))
        
    def __add__(self,otro):
        union=Conjunto()
        for i in range(self.getRango()):
             union.aE(self.getElem(i))
        for i in range(otro.getRango()):
            b=0
            j=0
            while(j<self.getRango())and(b==0):
                if(otro.getElem(i)==self.getElem(j)):
                     b=1
                else:
                   j=j+1
            if(b==0):
                union.aE(otro.getElem(i))
        return union
    def __sub__(self,otro):
        union=Conjunto()
        for i in range(otro.getRango()):
            b=0
            j=0
            while(j<self.getRango())and(b==0):
                if(otro.getElem(i)!=self.getElem(j)):
                     j=j+1
                else:
                   b=1
            if(b==1):
                union.aE(otro.getElem(i))
        return union
    def mostrar(self):
        print(self.__Lis)                
    def __eq__(self,otro):
        if(self.getRango()==otro.getRango()):
            ban=0
            for i in range(otro.getRango()):
                b=0
                j=0
                while(j<self.getRango())and(b==0):
                    if(otro.getElem(i)!=self.getElem(j)):
                        j=j+1
                    else:
                        b=1
                        ban=ban+1
            if(ban==self.getRango()):
                return 1            
        else:
            return ('No se puede comparar la cantidad de elementos no es igual')