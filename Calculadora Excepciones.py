# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 22:49:24 2022

@author: macon
"""
        
while True:
    print("\n\t    --Calculadora simple--")
    print("1. Suma \t 2. Resta \t 3. Multiplicación")
    print("4. División  5. Residuo  6.Salir")
    opc= (int(input("Operación a realizar: ")))
    
    if (opc ==1):
        while True:
            try:
                num1=(int(input("Primer número: ")))
                num2=(int(input("Segundo número: ")))
                break
            except ValueError:
                print("Valor no valido. Ingrese numeros enteros.")
        print("\n",num1,"+",num2,"=", num1+num2)
        
    elif (opc ==2):
        while True:
            try:
                num1=(int(input("Primer número: ")))
                num2=(int(input("Segundo número: ")))
                break
            except ValueError:
                print("Valor no valido. Ingrese numeros enteros.")
        print("\n",num1,"-",num2,"=", num1-num2)
        
    elif (opc ==3):
        while True:
            try:
                num1=(int(input("Primer número: ")))
                num2=(int(input("Segundo número: ")))
                break
            except ValueError:
                print("Valor no valido. Ingrese numeros enteros.")
        print("\n",num1,"*",num2,"=", num1*num2)
        
    elif (opc ==4):
        while True:
            try:
                num1=(int(input("Primer número: ")))
                num2=(int(input("Segundo número: ")))
                break
            except ValueError:
                print("Valor no valido. Ingrese numeros enteros.")
        try:
            print("\n",num1,"/",num2,"=", num1/num2)
        except ZeroDivisionError:
            print("\nDivision entre 0. Operacion invalida.")
        finally:
            print("Operacion Finalizada.")
            
    elif (opc ==5):
        while True:
            try:
                num1=(int(input("Primer número: ")))
                num2=(int(input("Segundo número: ")))
                break
            except ValueError:
                print("Valor no valido. Ingrese numeros enteros.")
        try:
            print("\n",num1,"%",num2,"=", num1%num2)
        except ZeroDivisionError:
            print("\nDivision entre 0. Operacion invalida.")
        finally:
            print("Operacion Finalizada.")
            
    elif (opc ==6):
        break
    
print("\nProceso Finalizado. Vuelva pronto.")