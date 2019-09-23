import requests

#url = 'http://localhost:5000/api' #For LocalHost
url = 'https://tunggalmat.pythonanywhere.com/api'

tot_cus = input('Jumlah Customer (1-10) :')
input_user = []
for i in range(int(tot_cus)) : 
    print ('USER',i+1)
    EDUCATION = input('EDUCATION (1-4) : ')
    SEX = input('SEX (1-2): ')
    MARRIAGE = input('MARRIAGE (1-3): ')
    PAY_1 = input('PAY_1 (0-4): ')
    PAY_2 = input('PAY_2 (0-4): ')
    PAY_3 = input('PAY_3 (0-4): ')
    print ('-----------------------------\n')
    user = {"EDUCATION":int(EDUCATION),"SEX":int(SEX),"MARRIAGE":int(MARRIAGE),"PAY_1":int(PAY_1),"PAY_2":int(PAY_2),"PAY_3":int(PAY_3)}
    input_user.append(user)

r = requests.post(url,json=(input_user))

print(r.json())