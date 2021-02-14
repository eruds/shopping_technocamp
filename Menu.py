from os import system
from time import sleep
from Login import login, signup

def redirect(res) : 
    if(res == "Keluar") : 
        print("Keluar dari program...")
        sleep(1)
        system("cls")
        exit()
    elif(res == "Login") : 
        username = input("Username : ")
        password = input("Password : ")
        user = login(username, password)
        sleep(1)
        system("cls")
        MainMenu(True, user)
    elif(res == "Signup") : 
        signup()
        sleep(1)
        system("cls")
        MainMenu(False)

def MainMenu(loggedIn, user = {}) :
    menuList = [
        "Home",
        "Login", 
        "Signup",
        "Keluar"
    ] if not loggedIn else [
        "Home", 
        "Cart",
        "Shop",
        "Keluar"
    ]
    currentUser = {} if not loggedIn else user 
    print("Main Menu: ")
    for i in range(len(menuList)) : 
        item = menuList[i]
        print(f"{i+1}. {item}")
    res = int(input("Apa yang ingin anda lakukan? : "))
    while res not in range(1,len(menuList) + 1) : 
        print("Input tidak valid")
        res = int(input("Apa yang ingin anda lakukan? : "))
    system("cls")
    redirect(menuList[res - 1])