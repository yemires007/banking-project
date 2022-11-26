from user import user_detail
import mysql.connector



myserver = mysql.connector.connect(host='127.0.0.1', user= 'root', passwd='yemires123', database = 'bankapp')
mycursor = myserver.cursor()


class transaction():
    def __init__(self, nu):
        self.nu = nu
    
    def general():
        option = input('Enter 1 to LOGIN \nEnter 2 to REGISTER: ')
        if option == '1':
            user_detail.user_login()
        elif option == '2':
            user_detail.user_register()
            if user_detail.user_register:
                user_detail.user_login()
        else:
            print('Unknown input')

    general()






# details = transaction()
# print(f"{details.option}")


