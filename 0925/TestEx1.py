#要知道 BasicException > Exception > ValueError
try:
    nums = int(input('請輸入數字：'))
    print(10/nums)
except Exception as ex:                
    print('發生錯誤...')
except ValueError as err:
    #print(err)
    print('數值格式錯誤...')
except ArithmeticError as ae:
    print('數值運算錯誤...')
except ZeroDivisionError as ze:
    print('數值不得為零...')
else:
    print('反正這裡一定會印出來')