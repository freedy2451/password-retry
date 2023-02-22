p_word = 'a123456'

i = 3 #剩餘機會
while i > 0:
    i = i - 1
    a = input ("請輸入正確的密碼: ")
    if a == p_word: 
        print("登入成功")  
    else:          
        print("密碼錯誤")               
        if i != 0 :
            print("還有{}次機會ˇ".format(i))
        else:
            print("已超過次數，鎖定帳號")
                
