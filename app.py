from Customer import Customer
import pymysql
from Operator import Operator

mysql_config = {
        'host': '35.246.24.203',
        'port': 3306,
        'user': 'root',
        'passwd': '3022008a',
        'database': 'progSDTeamProject',
    }
# connect to mysql
db = pymysql.connect(**mysql_config)

class app:
    def __init__(self):
        print("app running")
    # mysql configs

    # Customer Operator Manager 登陆
    def login(self,par: list):
        # email password
        currentEmail = par[0]
        currentPassword = par[1]
        option = par[2]
        cursor = db.cursor()

        if option == '1':
            oneSQL = "SELECT * FROM Customers WHERE email = %s"
            cursor.execute(oneSQL, currentEmail)
            db.commit()

        elif option == '2':
            oneSQL = "SELECT * FROM Operators WHERE email = %s"
            cursor.execute(oneSQL, currentEmail)
            db.commit()

        elif option == '3':
            oneSQL = "SELECT * FROM Manager WHERE email = %s"
            cursor.execute(oneSQL, currentEmail)
            db.commit()

        oneData = cursor.fetchone()

        try:
            rightPassword = oneData[2]
        except TypeError as e:
            return False #登陆失败 请检查邮箱名与密码

        if currentPassword == rightPassword:
            return True
        else:
            return False


    def register(self,par: list):
        # par : name:str,password:str,email:str
        customer = Customer()
        flag = customer.add(par)
        if flag is True:
            return True
        else:
            return False


    #之后改为从框中输入
    def enterCode(self):
        code = input("Enter code: ")
        return code

    def registerOM(self,par: list):
        # 先生成code
        operator = Operator()
        # par : name:str,password:str,email:str
        operator.generateCode(par)
        userCode = self.enterCode()  #之后修改
        flag = operator.add(userCode)
        if flag is True:
            return True
        else:
            return False


if __name__ == '__main__':
    app = app()
    par1 = ["Yuqing Ren", "9988", "renyuqing@gmail.com"]

    par2 = ["zhangruixian@gmail.com", "3022008a", '1']
    par3 = ["renyuqing@gmail.com", "9988", '1']
    par4 = ["zhangruixian@gmail.com", "3022008", '2']
    print(app.login(par2))  # 测试登陆成功
    print(app.login(par3))  # 测试登陆失败
    print(app.login(par4))  # 测试登陆成功

    print(app.register(par1))
    print(app.login(par3))

    print(app.registerOM(par1))











