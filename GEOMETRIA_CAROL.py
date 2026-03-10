import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
def area_circulo(radio):
   area = np.pi * radio**2
   return area

def hacer_circulo(radio, x_centro, y_centro, unidad, color):
   area = area_circulo(radio)
   fig, ax = plt.subplots()
   circulo = Circle(
       (x_centro, y_centro),
       radio,
       color=color,
       fill=True,
       label=f"Área = {area:.1f} {unidad}²")
   ax.add_patch(circulo)
   ax.set_aspect('equal')
   ax.set_xlim(x_centro - radio*1.5, x_centro + radio*1.5)
   ax.set_ylim(y_centro - radio*1.5, y_centro + radio*1.5)
   ax.set_xlabel(f'X ({unidad})')
   ax.set_ylabel(f'Y ({unidad})')
   ax.legend()   
   plt.show()
def area_cuadrado(lado):
    return lado**2
def perimetro_cuadrado(lado):
    return 4 * lado

def hacer_cuadrado(lado,x_ini, y_ini, unidad, color):
   area = area_cuadrado(lado)
   perimetro = perimetro_cuadrado(lado)
   x = [x_ini, x_ini+lado, x_ini+lado, x_ini, x_ini]
   y = [y_ini, y_ini, y_ini+lado, y_ini+lado, y_ini]

   fig, ax = plt.subplots()
   ax.plot(
       x, y,
       marker='o',
       color=color,
       label=f"Area={area:.1f} {unidad}²\nPerimetro={perimetro:.1f} {unidad}")
   ax.set_aspect('equal')
   ax.set_xlabel(f"X ({unidad})")
   ax.set_ylabel(f"Y ({unidad})")
   ax.legend()
   plt.grid(True)
   plt.show()
def area_pentagono(lado):
    return (5 * lado**2) / (4 * np.tan(np.pi/5))
def perimetro_pentagono(lado):
    return 5 * lado

def hacer_pentagono(lado, x_centro, y_centro, unidad, color):

   area = area_pentagono(lado)
   perimetro = perimetro_pentagono(lado)

   theta = np.linspace(0, 2*np.pi, 6)

   x = x_centro + lado * np.cos(theta)
   y = y_centro + lado * np.sin(theta)

   fig, ax = plt.subplots()
   ax.plot(
       x, y,
       marker='o',
       linestyle='-',
       color=color,
       label=f"Area={area:.1f} {unidad}²\nPerimetro={perimetro:.1f} {unidad}")
   ax.set_aspect('equal')
   ax.set_xlabel(f"X ({unidad})")
   ax.set_ylabel(f"Y ({unidad})")
   ax.legend()
   plt.grid(True)
   plt.show()
def perimetro_rectangulo(base, altura):
    return 2 * (base + altura)
def diagonal_rectangulo(base, altura):
    return np.sqrt(base**2 + altura**2)

def hacer_rectangulo3d(base, altura, x_ini, y_ini, unidad, color):
   perimetro = perimetro_rectangulo(base, altura)
   diagonal = diagonal_rectangulo(base, altura)

   fig = plt.figure()
   ax = fig.add_subplot(111, projection='3d')

   x = [x_ini, x_ini+base, x_ini+base, x_ini, x_ini]
   y = [y_ini, y_ini, y_ini+altura, y_ini+altura, y_ini]
   z = [0,0,0,0,0]

   ax.plot(x, y, z, color=color,
           label=f"Perimetro={perimetro:.1f} {unidad}\nDiagonal={diagonal:.1f} {unidad}")
   ax.set_xlabel(f"X ({unidad})")
   ax.set_ylabel(f"Y ({unidad})")
   ax.set_zlabel(f"Z ({unidad})")
   ax.legend()
   plt.show()
def area_triangulo(base, altura):
    return (base * altura) / 2
def hipotenusa_triangulo(base, altura):
    return np.sqrt(base**2 + altura**2)

def hacer_triangulo3d(base, altura, x_ini, y_ini, unidad, color):

   area = area_triangulo(base, altura)
   hipotenusa = hipotenusa_triangulo(base, altura)

   fig = plt.figure()
   ax = fig.add_subplot(111, projection='3d')

   v1 = [x_ini, y_ini, 0]
   v2 = [x_ini + base, y_ini, 0]
   v3 = [x_ini, y_ini + altura, altura]

   x = [v1[0], v2[0], v3[0], v1[0]]
   y = [v1[1], v2[1], v3[1], v1[1]]
   z = [v1[2], v2[2], v3[2], v1[2]]

   ax.plot(x, y, z, color=color,
           label=f"Area={area:.1f} {unidad}²\nHipotenusa={hipotenusa:.1f} {unidad}")
   ax.set_xlabel(f"X ({unidad})")
   ax.set_ylabel(f"Y ({unidad})")
   ax.set_zlabel(f"Z ({unidad})")
   ax.legend()
   plt.show()
def perimetro_estrella(lado):
    return 10 * lado
def area_estrella(radio):
    return (5 * radio**2 * np.sin(2*np.pi/5)) / 2
def hacer_estrella3d(radio, x_centro, y_centro, unidad, color):

   area = area_estrella(radio)
   perimetro = perimetro_estrella(radio)

   fig = plt.figure()
   ax = fig.add_subplot(111, projection='3d')
   r_in = radio / 2
   r_out = radio
   n_puntas = 5
   angulos = np.linspace(0, 2*np.pi, 2*n_puntas + 1)

   x = []
   y = []

   for i, angulo in enumerate(angulos):
       r = r_out if i % 2 == 0 else r_in
       x.append(x_centro + r*np.cos(angulo))
       y.append(y_centro + r*np.sin(angulo))
   x = np.array(x)
   y = np.array(y)
   z = np.sqrt((x-x_centro)**2 + (y-y_centro)**2)
   z = radio - z
   ax.plot_trisurf(x, y, z, color=color,
       label=f"Area≈{area:.1f} {unidad}²\nPerimetro≈{perimetro:.1f} {unidad}")
   ax.set_xlabel(f"X ({unidad})")
   ax.set_ylabel(f"Y ({unidad})")
   ax.set_zlabel(f"Z ({unidad})")
   ax.legend()
   plt.show()
def menu():
   print("Menu figuras geometricas")
   print("1. Circulo")
   print("2. Cuadrado")
   print("3. Pentagono")
   print("4. Rectangulo")
   print("5. Triangulo")
   print("6. Estrella")
   print("7. Finalizar programa")
while True:
  menu()
  try:
    opcion= int(input("Elige una opcion\n"))
    if opcion== "salir":
     break
    match opcion:
      case 1:
         unidad = input("Ingrese la unidad (cm, m, etc): ")
         radio=float(input(f"Radio ({unidad}): "))
         x_c=float(input(f"Centro X ({unidad})"))
         y_c=float(input(f"Centro Y ({unidad})"))
         color=(input("Ingrese el color del circulo"))
         hacer_circulo(radio, x_c, y_c, unidad, color)
      case 2:
         unidad = input("Ingrese la unidad de medida (cm, m, etc): ")
         lado=float(input(f"Base ({unidad}): "))
         x_ini= float(input(f"X inical ({unidad}): "))
         y_ini=float(input(f"Y inicial ({unidad}): "))
         color=(input("Ingrese el color del cuadrado"))
         hacer_cuadrado(lado, x_ini, y_ini, unidad, color)
      case 3:
          unidad = input("Ingrese la unidad de medida (cm, m, etc): ")
          lado = float(input(f"Radio del pentagono ({unidad}): "))
          x_centro = float(input(f"Centro X ({unidad}): "))
          y_centro = float(input(f"Centro Y ({unidad}): "))
          color=(input("Ingrese el color del pentagono"))
          hacer_pentagono(lado, x_centro, y_centro, unidad, color)
      case 4:
         unidad = input("Ingrese la unidad de medida (cm, m, etc): ")
         base=float(input(f"Base ({unidad}): "))
         altura=float(input(f"Altura ({unidad}): "))
         x_ini=float(input(f"X inicial ({unidad}): "))
         y_ini=float(input(f"Y inicial ({unidad}): "))
         color=input("Ingrese el color del rectangulo")
         hacer_rectangulo3d(base, altura, x_ini, y_ini, unidad, color)
      case 5:
         unidad = input("Ingrese la unidad de medida (cm, m, etc): ")
         base=float(input(f"Base ({unidad}): "))
         altura=float(input(f"Altura ({unidad}): "))
         x_ini=float(input(f"X inicial ({unidad}): "))
         y_ini=float(input(f"Y inicial ({unidad}): "))
         color=input("Ingresa un color del triangulo")
         hacer_triangulo3d(base, altura, x_ini, y_ini, unidad, color)
      case 6:
         unidad = input("Ingrese la unidad de medida (cm, m, etc): ")
         radio = float(input(f"Radio ({unidad}): "))
         x_centro = float(input(f"Centro X ({unidad}): "))
         y_centro = float(input(f"Centro Y ({unidad}): "))
         color = input("Color de la estrella: ")
         hacer_estrella3d(radio, x_centro, y_centro, unidad, color)
      case 7:
         print("Finalizar programa")
         break
      case _:
        print("opcion no valida")
  except ValueError:
   print("Por favor, ingrese un número válido")
  break # O continuar, según desees