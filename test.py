#autentication with py 
user_db = "Rahul"
pass_db = "Rahul123"

user = input("Masukkan username: ")
password = input("Masukkan password: ")

if user == user_db and password == pass_db:
    print("Welcome back, " + user)
else: 
    print("Failed login, please check your username and password")
