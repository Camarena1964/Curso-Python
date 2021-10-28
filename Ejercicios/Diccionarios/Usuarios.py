users = {
    "Sandra":"123456",
    "Paco":"Pacotorro",
    "Fati":"Percheron",
    "Perri":"GuauGuau",
    "María":"Rosario",
    "Jesús":"Salvación"
}
user = input("Por favor ingrese su nombre de usuario: ")
password = input("Por favor ingrese su contraseña: ")
for key, value in users.items():
    if user == key and password == value:
        print(f"Hola {user}, bienvenid@! :) ")
        break
    if user == key and password != value:
        print("Tu contraseña es incorrecta, por favor intenta de nuevo")
        break
    if user != key and password == value:
        print("El nombre de usuario ingresado no existe, por favor intente con otro")