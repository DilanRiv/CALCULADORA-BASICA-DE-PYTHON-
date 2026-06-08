                 ## Calculadora Simple en Python ##

while True :

    pregunta = input("Elija la operacion que desea realizar: \n 1. Suma \n 2. Resta \n 3. Multiplicacion \n 4. Division \n 5. POTENCIA \n 6. SALIR \n").strip().lower()

    if pregunta in ["1", "suma"]:  
        num1 = float(input("Ingrese el primer numero: "))
        num2 = float(input("Ingrese el segundo numero: "))
        resultado = num1 + num2
        print ("El resultado de la suma es: ", resultado)

    elif  pregunta == "2" or pregunta.lower() == "resta" :
        num1 = float(input("INGRESE EL PRIMER NUMERO PARA LA RESTA: "))
        num2 = float(input("INGRESE EL SEGUNDO NUMERO PARA LA RESTA: "))
        resultado = num1 - num2
        print ("EL RESULTADO DE LA RESTA ES: ", resultado)

    elif pregunta == "3" or pregunta.lower() == "multiplicacion" :
        num1 = float(input("INGRESE EL PRIMER NUMERO PARA LA MULTIPLICACION: "))
        num2 = float(input("INGRESE EL SEGUNDO NUMERO PARA LA MULTIPLICAION: "))
        resultado = num1 * num2
        print ("EL RESULTADO DE LA MULTIPLICACION ES: ", resultado)
    elif pregunta == "4" or pregunta.lower() == "division" :
        num1 = float(input("INGRESE EL PRIMER NUMERO PARA LA DIVISION:"))
        num2 = float(input("INGRESE EL SEGUNDO NUMERO PARA LA DIVISION: "))
        if num2 == 0 :
            print ("NO SE PUEDE DIVIDIR ENTRE CERO")
        elif resultado == num1 / num2:
            print ("EL RESULTADO DE LA DIVISION ES: ", resultado)

    elif pregunta =="5" or pregunta.lower() =="potencia":
        num1 = int(input("INGRESE EL NUMERO QUE QUIERE POTENCIAR:"))
        num2 = int(input("INGRESE EL NUMERO POTENCIADOR:"))
        resultado = num1 ** num2
        print ("EL RESULTADO DE LA POTENCIA ES: ", resultado)

    elif pregunta == "6" or pregunta.lower() == "salir" :
        print("HASTA LUEGO¡¡")
        break
    else :
        print ("POR EL MOMENTO SOLO SE PUEDEN HACER LAS OPCIONES MOSTRADAS")

  
      

      
      
    
       
