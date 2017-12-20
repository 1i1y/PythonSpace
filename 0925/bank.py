# 類別啟始
class Account:
    #建構子設計
    # 帳戶                              # 物件的方法第一個一定為物件本身(self)
    def __init__(self, name, number, balance): 
        self.__name    = name           # 記得縮排!!!!!
        self.__number  = number         # '__'將權限鎖在這個class內，像Java的private
        self.__balance = balance
    #self.test = '測試測試'             # 想要什麼都可以增加上來
    
    # 金額    
    def deposit(self,amount):
        self.__balance += amount        # 存錢
        
    def withdraw(self,amount):
        self.__balance -= amount        # 提錢
        
    def __str__(self):                  # 將選擇的物件都轉成字串
        #return 'Account類別的__str__'
        return 'name:{0},number:{1},balance:{2}'.format(self.__name,self.__number,self.__balance) 

    @property                           # @ 註記, 盡可能設計成可以當Getter,無法當Setter
    def name(self):
        return self.__name
    @property
    def number(self):
        return self.__number
    @property
    def balance(self):
        return self.__balance
        
    @name.setter                        # @ 註記, 當Setter,讓它有地方寫檢查的地方
    def name(self,name):
        self.__name = name
    @number.setter
    def number(self,number):
        self.__number = number
    @balance.setter
    def balance(self,balance):
        if balance <= 0:                # raise 引發例外，順便說明
            raise ValueError('值不得小於等於零')
        else:
            self.__balance = balance
            
    @staticmethod                       #靜態方法，獨立的區塊(少用)
    def default(name,number):
        return Account(name,number,9999)
# 類別結束

# 模組啟始  
# 模組結束
