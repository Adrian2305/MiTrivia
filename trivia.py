# Lo primero es mostrar en pantalla el texto de bienvenida para quien juegue tu trivia
print ("Bienvenido a mi trivia que te pondra los pelos en punta")
nombre_usuario = input("Digite su nombre: ")
print ("Pondre a prueba tus conocimientos", nombre_usuario)

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

if(respuesta1_usuario=='d'):
  print ("Muy bien!", nombre_usuario)  


print ("\nPregunta 2")
print ("¿Cuando es el dia de la madre?\n")
print ("a) 28 de mayo")
print ("b) 17 de noviembre")
print ("c) 11 de agosto")
print ("d) 1 de junio")

respuesta2_usuario = input("\nTu respuesta: ")

if(respuesta2_usuario=='d'):
  print ("Excelente! Sigue asi")  

print ("\nPregunta 3")
print ("¿Cuando es el dia del niño?\n")
print ("a) 07 de mayo")
print ("b) 25 de noviembre")
print ("c) 21 de agosto")
print ("d) 19 de junio")

respuesta3_usuario = input("\nTu respuesta: ")

if(respuesta3_usuario=='c'):
  print ("Excelente! Tienes la nota maxima", nombre_usuario)  

print("Muchas gracias por participar en la trivia")