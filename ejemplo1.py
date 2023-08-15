nombreUsuario = "Juanito"
edadUsuario = 19
estaturaUsuario = 1.67
esHinchaDelVerde = True

#comentario 
'''Comentario de
bloque'''

print(f"Su nombre es: {nombreUsuario} y tiene {edadUsuario} años.")
 
comidasFavoritas = ["Frisoles","Pastas","Papitas",
                    "Sopa"]
print(comidasFavoritas);
print(comidasFavoritas[2])


#Entradas por teclado:

lugarTrabajoUsuario = input(nombreUsuario+", Digite su lugar de trabajo: ")
print(f"Señor {nombreUsuario}, usted trabaja en {lugarTrabajoUsuario}")

numeroUno =int(input("Por favor digite el número uno: "))
numeroDos = int(input("Por favor digite el número dos: "))
suma = numeroDos + numeroUno
print(f"Señor {nombreUsuario}, si suma el número {numeroUno} con el número {numeroDos} \n la suma de los dos numeros deberia de ser {suma}")