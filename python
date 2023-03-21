import getpass
import random

def encrypted(x):

    li = ['1','2','3','4','5','6','7','8','9','0','q','w','e','r','t'
    ,'y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x'
    ,'c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A'
    ,'S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M','`'
    ,'~',';',':','/','?','!','@','#','$','%','^','&','*',')','(','-','_','+','=']

    encrypted_list = []
    for i in x:
        a = random.choice(li)
        y = a
        encrypted_list.append(y)
    encrypted_pwd = ''.join([str(item) for item in encrypted_list])
    return encrypted_pwd


def add():
    name = input('account name: ')
    pwd = getpass.getpass("password:  ")
    confirm_pwd = getpass.getpass("confirm password:  ")
    counter = 0
    while confirm_pwd != pwd:
        counter+=1
        print('** Password must be same **')
        pwd = getpass.getpass('password: ')
        confirm_pwd = getpass.getpass('confirm password: ')
        if counter == 3:
            return 'none','none'
    w = encrypted(pwd)
    with open('passwords.txt', 'a') as f:
        f.write('account name: '+ name + "\n" + 'password: '+ w + "\n"+"\n")
    return name,pwd


def view(d1):
    ask = input('Which Account?  ')
    returner = d1.get(ask)
    return returner

d1 = {}

while True:
    mode = input(
    '''Would you like to add a new password or view existing ones ? 
press a to add , press v to view ,press q to quit   ''').lower()
    if mode == "q":
        break

    if mode == "v":
        print(view(d1))
    elif mode == "a":
        a1,a2 = add()
        d2 = {a1:a2}
        d1.update(d2)  
    else:
        print("Invalid mode.")
        continue
