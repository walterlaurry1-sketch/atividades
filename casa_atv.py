import datetime
while True: 
     idade = float(input ("digite a idade "))
     if idade >= 18:
         print ("Maior de idade", datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
     elif idade== 0:
         break
     else :
        print ("Menor de idade", datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
   

#class animal:
    #def som(self):
        #print("faz som")

#class cachorro(animal):
    #def som(self):
        #print("au au")        
        