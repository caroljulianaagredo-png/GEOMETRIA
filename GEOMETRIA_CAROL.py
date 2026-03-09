import matplotlib.pyplot as plt
from matplotlib.patches import Circle
def hacer_circulo():
  print("vas a hacer un circulo")
fig, ax = plt.subplots()
# Crear el círculo: (centro_x, centro_y), radio
circulo = Circle((0.5, 0.5), 0.2, color='blue', fill=True)
# Añadir el círculo a los ejes
ax.add_patch(circulo)
# Asegurar que el círculo no se deforme (aspecto 1:1)
ax.set_aspect('equal')
# Ajustar límites de los ejes para ver el círculo
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.show()
def hacer_cuadrado():
   print("vas a hacer un cuadrado")
def hacer_rectangulo():
   print("vas a hacer un rectangulo")
def hacer_triangulo():
   print("vas a hacer un triangulo")
def menu():
   print("Menu figuras geometricas")
   print("1. Circulo")
   print("2. Cuadrado")
   print("3. Rectangulo")
   print("4. Triangulo")
   print("Finalizar programa")
while True:
  menu()
  try:
    opcion= int(input("Elige una opcion\n"))
    if opcion== "salir":
     break
    match opcion:
      case 1:
         hacer_circulo()
      case 2:
         hacer_cuadrado()
      case 3:
         hacer_rectangulo()
      case 4:
         hacer_triangulo()
      case 5:
         print("Finalizar programa")
         break
      case _:
        print("opcion no valida")
  except ValueError:
   print("Por favor, ingrese un número válido")
  break # O continuar, según desees