import re
import datetime
def create_membership():
    now = datetime.datetime.now()
    stnr_date = now.strftime('%Y%m%d')
    
    users = []

    while True : 
        user = {}
        #이름
        while True : 
            username = input('이름 : ')
            if 2<= len(username) <= 4 : 
                pass
            else : 
                print('이름을 올바르게 입력해 주세요')
                continue
            name = list(username)
            name2 = []
            for i in range(0,len(name)) : 
                if 44032 <= ord(name[i]) <= 55203 :
                    name2.append(name[i])
                else : 
                    pass
            if len(name2) == len(name) : 
                break
            else :
                print('이름을 올바르게 입력해 주세요')
                continue

        #비밀번호
        while True : 
            password = input('비밀번호 : ')
            if (8 <= len(password)) and (password[0].isupper()) and ('!' in password or '@' in password or '#' in password or '$' in password) : 
                break
            else : 
                print('비밀번호를 올바르게 입력해 주세요')
                continue

        #이메일
        while True : 
            useremail = input('이메일 : ')
            email = str(useremail)
            if email[-4:] == '.com' : 
                pass
            else : 
                print('이메일을 올바르게 입력해 주세요')
                continue
            if '@' in email : 
                email = email.rstrip('.com').replace('@','a')
                if email.isalnum() == True :
                    break
                elif email.lstrip("@").isalnum() == False : 
                    print('이메일을 올바르게 입력해 주세요')
                    continue
            else : 
                print('이메일을 올바르게 입력해 주세요')
                continue
            
            user["username"] = username
            user["password"] = password
            user["useremail"] = useremail
            user["stnr_date"] = stnr_date  
            
            users.append(user)
            print(users)
            
            ans = input("추가로 입력하시겠습니까? : y/n")
            if ans.lower() == "y" : 
                continue
            else : 
                exit()
        return users


def load_to_txt(user_list):
    f = open('memberdb.txt', 'w', encoding='UTF-8')
    for i in range(len(user_list)):
        result=', '.join(s for s in list(user_list[i].values()))
        f.write(f'{result}\n')
    f.close()
    
def run():
    user_list = create_membership()
    load_to_txt(user_list)
    
run()

        
        