# 1 - Crea una lista que contenga algunos nombres de usuarios incluido 'admin', para cada usuario imprime un mensaje de bienvenida:
# 'Hola {username}, bienvenido'. Unicamente para el usuario admin debe imprimir el mensaje 'Hola admin, quieres visualizar el reporte de uso

user_name = ["María", "Pedro", "Rosa", "Lucas", "Anacleto", "Admin"]
for user in user_name:
    if user != "Admin":
        print (f"Hola {user}, ¡Bienvenido!")
    else:
        print ("Hola admin, ¿quieres visualizar el reporte de uso?")
