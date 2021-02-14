import database as db 
import uuid

def login(username = "", password = "") : 
    database = db.getData()
    for i in database : 
        user = database[i]
        uid = user["username"]
        pwd = user["password"]
        if(username == uid and password == pwd) : 
            print("Berhasil Login sebagai user ", username)
            return user
    print("User tidak ditemukan")
    return None

def signup() : 
    username = input("Masukkan username : ")
    password = input("Masukkan password : ")
    email = input("Masukkan Email : ")
    user = {
        "id" : str(uuid.uuid4()),
        "username" : username, 
        "password" : password,
        "email" : email, 
        "cart" : [{}], 
        "delivered" : [{}], 
        "onProcess" : [{}]
    }
    key = user["username"] + "_" + user["id"]
    database = db.getData()
    database[key] = user
    db.setDatabase(database)
    print("Sign Up Berhasil.")
