# Se puede crear cualquier programa utilizando solamente sus métodos primitivos y estructuras de control y funciones. Entonces ¿Por qué molestarnos con objetos?

# La respuesta es el control y manejo de la complejidad en proyectos grandes.
# El paradigma de orientación a objetos permite crear "nuevos tipos primitivos" al lenguaje, pero con las características necesarias para representar (modelar) cosas propias del problema que resuelve la aplicación.

# 
# Ejemplo:
#
# Representaremos un perro llamado Firulais con nombre y edad en un diccionario.
# Debemos definir algo así.

dog_1 = {
  "name": "Firulais",
  "age": 4
}

# Para saber el nombre del perro y su edad tendríamos que hacer algo como lo siguiente:

print('Me llamo', dog_1["name"], "y tengo", dog_1["age"], "años")


# Searía más entendible si pusieramos tener el mismo resultado con un codigo más declarativo, algo como:

# print(dog_1.say_name())

# Entenderemos los conceptos necesarios para pasar de un código secuencial a uno en el que podamos crear objetos que respondan a sus propios métodos. 






