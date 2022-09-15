# Lo primero es mostrar en pantalla el texto de bienvenida para quien juegue tu trivia
print ("Bienvenido a mi trivia que te pondra los pelos en punta")
nombre_usuario = input("Digite su nombre: ")
puntaje = 0
print ("Pondre a prueba tus conocimientos y obtendras un puntaje al finalizar la trivia ", nombre_usuario)

# Es importante dar instrucciones sobre cómo jugar:
print ("Responder las siguientes preguntas escribiendo la letra de la alternativa correcta y presionando 'Enter' para enviar tu respuesta correcta:\n")

# OJO, el \n al final de la línea 6 es para dar un "salto de línea"

# Pregunta 1
print ("Pregunta 1")
print ("1) ¿Cuando es el dia del padre?\n")
print ("a) 25 de mayo")
print ("b) 19 de noviembre")
print ("c) 14 de agosto")
print ("d) 18 de junio")

# Almacenamos la respuesta del usuario en la variable "respuesta_1"
respuesta1_usuario = input("\nTu respuesta: ")

while respuesta1_usuario not in ('a','b','c','d'):
  respuesta1_usuario = input("Para avanzar a la siguiente pregunta debes responder con las letras de las alternativas.")

if respuesta_1 == 'a':
  print("Respuesta incorrecta", nombre_usuario)
elif respuesta_1 == 'b':
  print("Respuesta incorrecta", nombre_usuario)
elif respuesta_1 == 'c':
  print("Respuesta incorrecta", nombre_usuario)
else:
  puntaje = 10
  print ("Muy bien!\n", nombre_usuario, "Tienesss")
  print ("Tienes: ", puntaje , "puntos acumulados")

print ("\nPregunta 2")
print ("¿Cuando es el dia de la madre?\n")
print ("a) 28 de mayo")
print ("b) 17 de noviembre")
print ("c) 11 de agosto")
print ("d) 1 de junio")

respuesta2_usuario = input("\nTu respuesta: ")

while respuesta2_usuario not in ('a','b','c','d'):
  respuesta2_usuario = input("Para avanzar a la siguiente pregunta debes responder con las letras de las alternativas.")

if respuesta_2 == 'a':
  print("Respuesta incorrecta", nombre_usuario)
elif respuesta_2 == 'b':
  print("Respuesta incorrecta", nombre_usuario)
elif respuesta_2 == 'c':
  print("Respuesta incorrecta", nombre_usuario)
else:
  print ("Muy bien!", nombre_usuario)
  puntaje = puntaje + 10
  print("Tienes: ",puntaje,"acomulados")

print ("\nPregunta 3")
print ("¿Cuando es el dia del niño?\n")
print ("a) 07 de mayo")
print ("b) 25 de noviembre")
print ("c) 21 de agosto")
print ("d) 19 de junio")

respuesta3_usuario = input("\nTu respuesta: ")

while respuesta3_usuario not in ('a','b','c','d'):
  respuesta3_usuario = input("Para avanzar a la siguiente pregunta debes responder con las letras de las alternativas.")

if respuesta_3 == 'a':
  print("Respuesta incorrecta", nombre_usuario)
elif respuesta_3 == 'b':
  print("Respuesta incorrecta", nombre_usuario)
elif respuesta_3 == 'd':
  print("Respuesta incorrecta", nombre_usuario)
else:
  print ("Muy bien!", nombre_usuario)
  puntaje = puntaje + 10
  print("Tienes ",puntaje, "acumulados. Es la nota maxima. Felicidades!")

print("Muchas gracias por participar en la trivia")