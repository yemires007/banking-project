import mysql.connector
import random
# from gen import generator
import math
from transaction import all_transaction



myserver = mysql.connector.connect(host='127.0.0.1', user= 'root', passwd='yemires123', database = 'bankapp')
mycursor = myserver.cursor()





class user_detail():
    def __init__(self, nu):
        self.nu = nu

# USER LOGIN
    def user_login():
     

        bank = input('Enter A to Login to ACCESS BANK\nEnter F to Login to FIRST BANK\nEnter P to Login to POLARIS BANK: ').lower()

        #  ACCESS BANK
        if bank == 'a':
            username = input('Enter your username: ')
            password = int(input('Enter password: '))

            myquery = "SELECT * FROM accessbank WHERE username = %s AND password = %s"
            value = (username, password)
            mycursor.execute(myquery, value)
            myreg = mycursor.fetchone()
            try:
                if myreg[3] == username and password == myreg[-1]:
                    print('Welcome', myreg[0:8])
                    all_transaction.operation_access()
                    if all_transaction.operation_access:
                        print('Enter "Y" to perform another transaction and "N" to cancel')
                        ask = input('Do you want to perform another transaction: ').lower()
                        if ask == 'y':
                            all_transaction.operation_access()
                        elif ask == 'n':
                            print('Thanks')
                            quit()

            except TypeError:
                print("Don't have an account with us")


        elif bank == 'f':
            username = input('Enter your username: ')
            password = int(input('Enter password: '))

            myquery = "SELECT * FROM firstbank WHERE username = %s AND password = %s"
            value = (username, password)
            mycursor.execute(myquery, value)
            myreg = mycursor.fetchone()
            try:
                if username == myreg[3] and password == myreg[-1]:
                    # print('yes')
                    print('Welcome', myreg[0:8])
                    all_transaction.operation_first()
                    if all_transaction.operation_first:
                        print('Enter "Y" to perform another transaction and "N" to cancel')
                        ask = input('Do you want to perform another transaction: ').lower()
                        if ask == 'y':
                            all_transaction.operation_first()
                        elif ask == 'n':
                            print('Thanks')
                            quit()

            except TypeError:
                print("Don't have an account with us")

        elif bank == 'p':
            username = input('Enter your username: ')
            password = int(input('Enter password: '))

            myquery = "SELECT * FROM polarisbank WHERE username = %s AND password = %s"
            value = (username, password)
            mycursor.execute(myquery, value)
            myreg = mycursor.fetchone()
            try:
                if username == myreg[3] and password == myreg[-1]:
                    print('Welcome', myreg[0:8])
                    all_transaction.operation_polaris()
                    if all_transaction.operation_polaris:
                        print('Enter "Y" to perform another transaction and "N" to cancel')
                        ask = input('Do you want to perform another transaction: ').lower()
                        if ask == 'y':
                            all_transaction.operation_polaris()
                        elif ask == 'n':
                            print('Thanks')
                            quit()

            except TypeError:
                print("Don't have an account with us")



        else:
            print('Unknown Input')




#  USER REGISTER
    def user_register():
        
        bank = input('Enter A to register with ACCESS BANK\nEnter F to register with FIRST BANK\nEnter P to register with POLARIS BANK: ').lower()

        # WHEN BANK IS ACCESS
        if bank == 'a':
            
            print('Welcome to Access Bank')

            firstname = input('Enter Firstname: ')
            lastname = input ('Enter Lastname: ')
            username = input('Enter Username: ')
            phone = input('Enter Phone: ')
            password = input('Enter Password: ')
            if len(password) != 4:
                print('Password must not pass 4 digit')
                quit()
            else:
                if not password.isdigit():
                    print('please enter only digit')
                    quit()
                else:
                    confirm_password = input('Re-enter Password: ')
                    digits = [i for i in range(0, 10)]
                    random_str = ""
                    for i in range(10):
                        index = math.floor(random.random() * 10)
                        random_str += str(digits[index])
                    acc = random_str
                    if password == confirm_password:
                        if len(phone) != 11:
                            print('Enter a correct number')
                            quit()

                        else:
                            if not phone.isdigit():
                                print('please enter only digit')
                                quit()
                            elif phone[:4] in ['0803', '0703', '0903', '0806', '0706', '0906']:
                                mtn = 'MTN'
                                myquery = "INSERT INTO accessbank (firstname, lastname, username, phone, phone_service, account_no, password, confirmpassword) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
                                value = (firstname, lastname, username, phone, mtn, acc, password, confirm_password)
                                mycursor.execute(myquery, value)
                                myserver.commit()
                                print('Successfully register with MTN', phone, 'and Account_no', acc, 'Access Bank')

                            elif phone[:4] in ['0805', '0705', '0905']:
                                glo = 'GLO'
                                myquery = "INSERT INTO accessbank (firstname, lastname, username, phone, phone_service, account_no, password, confirmpassword) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
                                value = (firstname, lastname, username, phone, glo, acc, password, confirm_password)
                                mycursor.execute(myquery, value)
                                myserver.commit()
                                print('Successfully register with GLO', phone, 'and Account_no', acc, 'Access Bank')

                            elif phone[:4] in ['0802', '0702', '0701']:
                                airtel = 'AIRTEL'
                                myquery = "INSERT INTO accessbank (firstname, lastname, username, phone, phone_service, account_no, password, confirmpassword) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
                                value = (firstname, lastname, username, phone, airtel, acc, password, confirm_password)
                                mycursor.execute(myquery, value)
                                myserver.commit()
                                print('Successfully register with AIRTEL', phone, 'and Account_no', acc, 'Access Bank')
                    else:
                        print('Password and Confirm password does not match')
                        quit()



        # WHEN BANK IS FIRSTBANK
        elif bank == 'f':
            print('Welcom to First Bank')

            firstname = input('Enter Firstname: ')
            lastname = input ('Enter Lastname: ')
            username = input('Enter Username: ')
            phone = input('Enter Phone: ')
            # password = int(input('Enter Password: '))
            password = input('Enter Password: ')
            if len(password) != 4:
                print('Password must not pass 4 digit')
                quit()
            else:
                if not password.isdigit():
                    print('please enter only digit')
                    quit()
                else:
                    confirm_password = input('Re-enter Password: ')
                    
                    digits = [i for i in range(0, 10)]
                    random_str = ""
                    for i in range(10):
                        index = math.floor(random.random() * 10)
                        random_str += str(digits[index])
                    acc = random_str
                    if password == confirm_password:
                        if len(phone) != 11:
                            print('Enter a correct number')
                            quit()

                        else:
                            if not phone.isdigit():
                                print('please enter only digit')
                            elif phone[:4] in ['0803', '0703', '0903', '0806', '0706', '0906']:
                                mtn = 'MTN'
                                myquery = "INSERT INTO firstbank (firstname, lastname, username, phone, phone_service, account_no, password, confirmpassword) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
                                value = (firstname, lastname, username, phone, mtn, acc, password, confirm_password)
                                mycursor.execute(myquery, value)
                                myserver.commit()
                                print('Successfully register with MTN', phone, 'and Account_no', acc, 'First Bank') 

                            elif phone[:4] in ['0805', '0705', '0905']:
                                glo = 'GLO'
                                myquery = "INSERT INTO firstbank (firstname, lastname, username, phone, phone_service, account_no, password, confirmpassword) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
                                value = (firstname, lastname, username, phone, glo, acc, password, confirm_password)
                                mycursor.execute(myquery, value)
                                myserver.commit()
                                print('Successfully register with GLO', phone, 'and Account_no', acc, 'First Bank')

                            elif phone[:4] in ['0802', '0702', '0701']:
                                airtel = 'AIRTEL'
                                myquery = "INSERT INTO firstbank (firstname, lastname, username, phone, phone_service, account_no, password, confirmpassword) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
                                value = (firstname, lastname, username, phone, airtel, acc, password, confirm_password)
                                mycursor.execute(myquery, value)
                                myserver.commit()
                                print('Successfully register with AIRTEL', phone, 'and Account_no', acc, 'First Bank')
                    else:
                        print('Incorrect password')
                        quit()


        # WHEN BANK IS POLARISBANK
        elif bank == 'p':
            print('Welcome to Polaris Bank')

            firstname = input('Enter Firstname: ')
            lastname = input ('Enter Lastname: ')
            username = input('Enter Username: ')
            phone = input('Enter Phone: ')
            password = int(input('Enter Password: '))
            confirm_password = int(input('Re-enter Password: '))
            digits = [i for i in range(0, 10)]
            random_str = ""
            for i in range(10):
                index = math.floor(random.random() * 10)
                random_str += str(digits[index])
            acc = random_str
            if password == confirm_password:
                if len(phone) != 11:
                    print('Enter a correct number')
                    quit()

                else:
                    if not phone.isdigit():
                        print('please enter only digit')
                    elif phone[:4] in ['0803', '0703', '0903', '0806', '0706', '0906']:
                        mtn = 'MTN'
                        myquery = "INSERT INTO polarisbank (firstname, lastname, username, phone, phone_service, account_no, password, confirmpassword) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
                        value = (firstname, lastname, username, phone, mtn, acc, password, confirm_password)
                        mycursor.execute(myquery, value)
                        myserver.commit()
                        print('Successfully register with MTN', phone, 'and Account_no', acc, 'Polaris Bank')

                    elif phone[:4] in ['0805', '0705', '0905']:
                        glo = 'GLO'
                        myquery = "INSERT INTO polarisbank (firstname, lastname, username, phone, phone_service, account_no, password, confirmpassword) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
                        value = (firstname, lastname, username, phone, glo, acc, password, confirm_password)
                        mycursor.execute(myquery, value)
                        myserver.commit()
                        print('Successfully register with GLO', phone, 'and Account_no', acc, 'Polaris Bank')

                    elif phone[:4] in ['0802', '0702', '0701']:
                        airtel = 'AIRTEL'
                        myquery = "INSERT INTO polarisbank (firstname, lastname, username, phone, phone_service, account_no, password, confirmpassword) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
                        value = (firstname, lastname, username, phone, airtel, acc, password, confirm_password)
                        mycursor.execute(myquery, value)
                        myserver.commit()
                        print('Successfully register with AIRTEL', phone, 'and Account_no', acc, 'Polaris Bank')
            else:
                print('Incorrect password')

        else:
            print('Unknown Input')




















