import matplotlib.pyplot as plt
from matplotlib.patches import Circle
def hacer_circulo():
   print("vas a hacer un circulo")
   fig, ax = plt.subplots()
   # Crear el círculo: (centro_x, centro_y), radio
   circulo = Circle((0.5, 0.5), 0.2, color='red', fill=True)
   # Añadir el círculo a los ejes
   ax.add_patch(circulo)
   # Asegurar que el círculo no se deforme (aspecto 1:1)
   ax.set_aspect('equal')
   # Ajustar límites de los ejes para ver el círculo
   plt.xlim(0, 1)
   plt.ylim(0, 1)
   plt.show()
import matplotlib.pyplot as plt
def hacer_cuadrado():
   print("vas a hacer un cuadrado")
   x = [1, 3, 3, 1, 1]
   y = [1, 1, 3, 3, 1]
   # Crear la figura
   plt.figure()
   plt.plot(x, y, marker='o') # 'o' añade puntos en los vértices
   # Asegurar que los ejes tengan la misma escala
   plt.axis('equal')
   # Añadir etiquetas y mostrar
   plt.title("Cuadrado en Matplotlib")
   plt.grid(True)
   plt.show()
import matplotlib.pyplot as plt
import matplotlib.patches as patches
def hacer_rectangulo():
   print("vas a hacer un rectangulo")
   fig, ax = plt.subplots()
   # 2. Crear el rectángulo (esquina_x, esquina_y, ancho, alto)
   # Coordenadas: (0.2, 0.3), Ancho: 0.5, Alto: 0.4
   rect = patches.Rectangle((0.2, 0.3), 0.5, 0.4, 
                         linewidth=2, 
                         edgecolor='r', 
                         facecolor='skyblue',
                         alpha=0.6)
   # 3. Añadir el rectángulo a los ejes
   ax.add_patch(rect)
   # 4. Configurar límites para que se vea el rectángulo
   ax.set_xlim(0, 1)
   ax.set_ylim(0, 1)
   ax.set_aspect('equal') # Para que los ejes estén a la misma escala
   plt.show()
import matplotlib.pyplot as plt
def hacer_triangulo():
   print("vas a hacer un triangulo")
   x = [0, 1, 0.5, 0]
   y = [0, 0, 1, 0]
   plt.figure()
   plt.plot(x, y, marker='o') # 'marker' es opcional, muestra los puntos
   plt.title("Triángulo en Matplotlib")
   plt.grid(True)
   plt.show()
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