p_word = 'a123456'

i = 3
while True:
    a = input ("請輸入正確的密碼: ")
    if a != p_word:
        i = i - 1
        print("密碼錯誤，還有{}次機會ˇ".format(i))       
        if i == 0:
            #print("密碼錯誤3次")
            break
    else:
        print("登入成功")        
