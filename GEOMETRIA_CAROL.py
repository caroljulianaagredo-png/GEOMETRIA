while True:
  try:
    opcion= int(input("ingrese una opcion\n1.Circulo\n2.Cuadrado\n3.Rectangulo\n4.Triangulo\n5.Finalizar programa\n"))
    if opcion== "salir":
     break
    match opcion:
      case 1:
         print("vas a hacer un circulo")
      case 2:
         print("vas a hacer un cuadrado")
      case 3:
         print("vas a hacer un rectangulo")
      case 4:
         print("vas a hacer un triangulo")
      case 5:
         print("programa finalizado")
         break
      case _:
        print("opcion no valida")
  except ValueError:
   print("Por favor, ingrese un número válido")
  break # O continuar, según desees