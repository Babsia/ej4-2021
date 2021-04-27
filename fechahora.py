class FechaHora:
    __dia=0
    __mes=0
    __anio=0
    __hora=0
    __minutos=0
    __seg=0

    def __init__(self,dia=1,mes=1,anio=2020,h=0,m=0,s=0):
        self.__dia=dia
        self.__mes=mes
        self.__anio=anio
        self.__hora=h
        self.__minutos=m
        self.__seg=s
    
    
    def PonerEnHora(self,Hora,min=0,seg=0):
        if type(Hora)==int and type(min)==int and type(seg)==int:
            self.__hora=int(Hora)
            self.__min=int(min)
            self.__seg=int(seg)
        
    
    
    def Mostrar(self):
        print("{}/{}/{}".format(self.__dia,self.__mes,self.__anio))
        print("{}:{}:{}".format(self.__hora,self.__minutos,self.__seg))


    def AdelantarHora(self,hora,min=0,seg=0):
        if type(hora)==int and type(min)==int:
            self.__hora+=int(hora)
            self.__seg+=int(seg)
            self.__minutos+=int(min)
            self.check()

       


    def check(self):

        if self.__seg>=60:
            self.__minutos+=1
            self.__seg=0
        
        if self.__minutos>=60:
            self.__hora+=1
            self.__min=0

        if self.__hora>=24:
            self.__dia+=1
            self.__hora=0



#divisible por 4, y si es divisible por 100, debe ser divisible por 400
        if self.__anio%4==0 and self.__anio%100!=0:
            #Año bisiesto
            
            if self.__mes==2 and self.__dia>29:
                print("ACA")
                print(self.__dia)
                self.__dia=1
                self.__mes+=1
        elif self.__anio%100==0 and self.__anio%400 ==0:
            #Año bisiesto
            
            if self.__mes==2 and self.__dia>29:
                print("ACA NO")
                self.__dia=1
                self.__mes+=1

        else:
            if self.__mes == 2 and self.__dia>28:
                self.__mes+=1
                self.__dia=1
                
            
            if (self.__mes == 4 or self.__mes==6 or self.__mes==9 or self.__mes==11) and (self.__dia>30):
                self.__dia=1
                self.__mes+=1
       
            
            elif (self.__mes==1 or self.__mes==3 or self.__mes==5 or self.__mes==7 or self.__mes==8 or self.__mes==10 or self.__mes==12) and (self.__dia>31):
                self.__dia=1
                self.__mes+=1
                if self.__mes>12:
                    self.__mes=1
                    self.__anio+=1