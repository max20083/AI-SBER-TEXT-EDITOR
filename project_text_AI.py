import requests
import urllib3
from gigachat import GigaChat



urllib3.disable_warnings()



def get_access_token(auth_key):
    url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"

    payload={
    'scope': 'GIGACHAT_API_PERS'
        }
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'application/json',
    'RqUID': '8568c576-2e4f-409c-b453-a94e7b0a2662',
    'Authorization': f'Basic {auth_key}'
    }
    response = requests.post(url, data=payload, headers=headers, verify=False)
    data = response.json()
    access_token = data.get('access_token')
    return access_token
def resp_ai(us_text,auth_key):
    try:
        with GigaChat(credentials=f"{auth_key}", verify_ssl_certs=False) as giga:  
            response = giga.chat(f"откорректируй этот текст , что бы в нем не было ни синтаксических ни лексических ошибок - {us_text}")  
            with open("text_verify.txt","w") as file:
                file.write(f"{response.choices[0].message.content}")
                file.close()
                return """Файл с названием - text_verify.txt создан , и соедержит нужный вам текст
                                            Спасибо за использование моего проекта !"""
    except:
        return("Произошла ошибка со стороны сервера - Попробуйте еще раз")



def reg(log_input,pass_input):
    with open("bd.txt","r") as file:
        for line in file:
            line_splt=line.split()
            if line_splt[0]==log_input:
                return 0
        file.close()
    with open("bd.txt","a") as file:
        file.write(f"{log_input} {pass_input}\n")
        file.close()
        return 1
    


def auth(login_input,password_input):
    with open("bd.txt","r") as file:
        for line in file:
            line_split=line.split()
            if line_split[0]==login_input and line_split[1]==password_input:
                return 1
        file.close()
        return 0
while True:
    print("""Чтобы пользоваться этой программой нужно войти в аккаунт  зарегестрироваться либо войти в уже существующий аккаунт""")
    print(" ")
    print("""      [1]Зарегистрироваться                                [2]Войти                        [3]Выйти из программы                              """)
    user_input=input()
    if user_input=="1":
        print("Введи логин который ты хочешь")
        log_input=input()
        print("Введи пароль который ты хочешь")
        pass_input=input()
        response_reg=reg(log_input,pass_input)
        if response_reg==1:
            print("Успешная авторизация")
        elif response_reg==0:
            print("Такой пользователь уже существует")
    elif user_input=="2":
        print("Введи свой логин")
        login_input=input()
        print("Введи свой пароль")
        password_input=input()
        response_auth=auth(login_input,password_input)
        if response_auth == 1:
            print("Успешный вход!")
            print("Введи свой апи ключ")
            auth_key=input()
            while True:
                print("Введи текст который нужно сделать без ошибок(если хочешь закончить напиши - !end)")
                us_text=input()
                if us_text == "!end":
                    break
                else:
                    print(resp_ai(us_text,auth_key))
        elif response_auth==0:
            print("Неудалось войти")
    elif user_input=="3":
        print("Спасибо за использование моей программы !")
        break
    else:
        print("Неверный формат ввода")
input()
    
        

        