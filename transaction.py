from types import NoneType
from typing import Type
from unittest import result
import mysql.connector
import math



myserver = mysql.connector.connect(host='127.0.0.1', user= 'root', passwd='yemires123', database = 'bankapp')
mycursor = myserver.cursor()


class all_transaction():
    def __init__(self, nu):
        self.nu = nu

    print('Welcome...Select the operation you want to perform')

# TRANSACTION FOR ACCESS
    def operation_access():
        print('1.Check Available Balance\n2.Send Money\n3.Buy Card\n4.Buy Data\n5.Save Money')
        enter = input('Enter command: ')
    
#  CHECK ACCOUNT BALANCE
        if enter == '1':
            password = int(input('Enter password: '))
            myquery = "SELECT * FROM accessbank WHERE password = %s"
            value = (password,)
            mycursor.execute(myquery, value)
            myreg = mycursor.fetchone()
            try:
                if myreg[-1] == password:
                    print('Name:', myreg[1],myreg[2] + ',' ,'Available_balance:', myreg[-4])
            except TypeError:
                print('Incorrect Password')


#  SEND MONEY
        elif enter == '2':
            password = int(input('Enter password: '))
            myquery = "SELECT * FROM accessbank WHERE password = %s"
            value = (password,)
            mycursor.execute(myquery, value)
            myreg = mycursor.fetchone()
            
            try:
                if myreg[-1] == password:
                
                    send_amount = int(input('Enter the amount you want to send: '))
                    con = int(myreg[-4])
                    result = (con - 50)
                    if send_amount > result:
                        print('Insufficient Fund')
                    elif send_amount <= result:
                        print('Destination Bank')
                        destination_bank = input('Enter A to send to ACCESS BANK\nEnter F to send to FIRST BANK\nEnter P to send to POLARIS BANK: ').lower()
                    #     ACCESS BANK
                        if destination_bank == 'a':
                            print('Destination Account Type')
                            destination_accounttype = input('Enter 1 Savings\nEnter 2 Current: ').lower()
                            if destination_accounttype == '1':
                                print('Destination Account Number')
                                destination_account = int(input('Enter account number: '))
                                if destination_account:
                                    myquery = "SELECT * FROM  accessbank WHERE account_no = %s"
                                    value = (destination_account,)
                                    mycursor.execute(myquery, value)
                                    myreg = mycursor.fetchone()
                                    print('Name:', myreg[1],myreg[2] + ',' ,'Account:', myreg[-3], 'Access Bank')
                                    send = input('Enter Y to send the money\nEnter N to cancel: ').lower()
                                    if send == 'y':
                                        query = "SELECT * FROM accessbank WHERE password = %s"
                                        val = (password,)
                                        mycursor.execute(query, val)
                                        myreg = mycursor.fetchone()
                                        new_reg = myreg[-4]
                                        myquery = ("UPDATE accessbank SET available_bal = %s WHERE password  = %s")
                                        new_reg = myreg[-4]
                                        latest_result = (new_reg - send_amount - 50)
                                        value = (latest_result, password)
                                        mycursor.execute(myquery, value)
                                        myserver.commit()
                                        if send:
                                            myquery = "SELECT * FROM  accessbank WHERE account_no = %s"
                                            value = (destination_account,)
                                            mycursor.execute(myquery, value)
                                            myreg = mycursor.fetchone()
                                            myquery = "UPDATE accessbank SET available_bal = %s WHERE account_no  = %s"
                                            new = myreg[-4]
                                            if new is None: 
                                                new = 0
                                                new_result = (new + send_amount - 50)
                                                value = (new_result, destination_account)
                                                mycursor.execute(myquery, value)
                                                myserver.commit()
                                                print(mycursor.rowcount, 'Transaction Completed...')
                                            else: 
                                                new_result = (new + send_amount - 50)
                                                value = (new_result, destination_account)
                                                mycursor.execute(myquery, value)
                                                myserver.commit()
                                                print(mycursor.rowcount, 'Transaction Completed...')     
                                        
                                    elif send == 'n':
                                        print('Transaction Cancelled...')
                                        quit()
                                    else:
                                        print('Unknown Input...Try again')
                                        quit()
                                else:
                                    print('Enter Destination Account Number')
                            elif destination_accounttype == '2':
                                print('Current Account Not Available...')
                            
                            else:
                                print('Unknown Input...Try again')


                        #  FIRST BANK

                        if destination_bank == 'f':
                            print('Destination Account Type')
                            destination_accounttype = input('Enter 1 Savings\nEnter 2 Current: ').lower()
                            if destination_accounttype == '1':
                                print('Destination Account Number')
                                destination_account = int(input('Enter account number: '))
                                if destination_account:
                                    myquery = "SELECT * FROM  firstbank WHERE account_no = %s"
                                    value = (destination_account,)
                                    mycursor.execute(myquery, value)
                                    myreg = mycursor.fetchone()
                                    
                                    print('Name:', myreg[1],myreg[2] + ',' ,'Account:', myreg[-3], 'First Bank')
                                    send = input('Enter Y to send the money\nEnter N to cancel: ').lower()
                                
                                    if send == 'y':
                                        query = "SELECT * FROM accessbank WHERE password = %s"
                                        val = (password,)
                                        mycursor.execute(query, val)
                                        myreg = mycursor.fetchone()
                                        new_reg = myreg[-4]
                                        myquery = ("UPDATE accessbank SET available_bal = %s WHERE password  = %s")
                                        new_reg = myreg[-4]
                                        latest_result = (new_reg - send_amount - 50)
                                        value = (latest_result, password)
                                        mycursor.execute(myquery, value)
                                        myserver.commit()
                                        
                                        if send:
                                            myquery = "SELECT * FROM  firstbank WHERE account_no = %s"
                                            value = (destination_account,)
                                            mycursor.execute(myquery, value)
                                            myreg = mycursor.fetchone()
                                            myquery = "UPDATE firstbank SET available_bal = %s WHERE account_no  = %s"
                                            new = myreg[-4]
                                            if new is None: 
                                                new = 0
                                                new_result = (new + send_amount - 50)
                                                value = (new_result, destination_account)
                                                mycursor.execute(myquery, value)
                                                myserver.commit()
                                                print(mycursor.rowcount, 'Transaction Completed...')
                                            else: 
                                                new_result = (new + send_amount - 50)
                                                value = (new_result, destination_account)
                                                mycursor.execute(myquery, value)
                                                myserver.commit()
                                                print(mycursor.rowcount, 'Transaction Completed...')      
                                        
                                    elif send == 'n':
                                        print('Transaction Cancelled...')
                                        quit()
                                    else:
                                        print('Unknown Input...Try again')
                                        quit()
                                else:
                                    print('Enter Destination Account Number')
                            elif destination_accounttype == '2':
                                print('Current Account Not Available...')
                            
                            else:
                                print('Unknown Input...Try again')


                        #  POLARIS BANK

                        elif destination_bank == 'p':
                            print('Destination Account Type')
                            destination_accounttype = input('Enter 1 Savings\nEnter 2 Current: ').lower()
                            if destination_accounttype == '1':
                                print('Destination Account Number')
                                destination_account = int(input('Enter account number: '))
                                if destination_account:
                                    myquery = "SELECT * FROM  polarisbank WHERE account_no = %s"
                                    value = (destination_account,)
                                    mycursor.execute(myquery, value)
                                    myreg = mycursor.fetchone()
                                    print('Name:', myreg[1],myreg[2] + ',' ,'Account:', myreg[-3], 'Polaris Bank')
                                    send = input('Enter Y to send the money\nEnter N to cancel: ').lower()
                                    if send == 'y':
                                        query = "SELECT * FROM accessbank WHERE password = %s"
                                        val = (password,)
                                        mycursor.execute(query, val)
                                        myreg = mycursor.fetchone()
                                        new_reg = myreg[-4]
                                        myquery = ("UPDATE accessbank SET available_bal = %s WHERE password  = %s")
                                        new_reg = myreg[-4]
                                        latest_result = (new_reg - send_amount - 50)
                                        value = (latest_result, password)
                                        mycursor.execute(myquery, value)
                                        myserver.commit()
                                
                                        if send:
                                            myquery = "SELECT * FROM  polarisbank WHERE account_no = %s"
                                            value = (destination_account,)
                                            mycursor.execute(myquery, value)
                                            myreg = mycursor.fetchone()
                                            myquery = "UPDATE polarisbank SET available_bal = %s WHERE account_no  = %s"
                                            new = myreg[-4]
                                            if new is None: 
                                                new = 0
                                                new_result = (new + send_amount - 50)
                                                value = (new_result, destination_account)
                                                mycursor.execute(myquery, value)
                                                myserver.commit()
                                                print(mycursor.rowcount, 'Transaction Completed...')
                                            else: 
                                                new_result = (new + send_amount - 50)
                                                value = (new_result, destination_account)
                                                mycursor.execute(myquery, value)
                                                myserver.commit()
                                                print(mycursor.rowcount, 'Transaction Completed...') 
                                    elif send == 'n':
                                        print('Transaction Cancelled...')
                                        quit()
                                    else:
                                        print('Unknown Input...Try again')
                                        quit()
                                else:
                                    print('Enter Destination Account Number')
                            elif destination_accounttype == '2':
                                print('Current Account Not Available...')
                            
                            else:
                                print('Unknown Input...Try again')

                    else:
                        print('Enter a valid amount')

                else:
                    print('Enter a correct password')

            except TypeError:
                print('Incorrect Password')


#  BUY CARD
        elif enter == '3':
            password = int(input('Enter password: '))
            myquery = "SELECT * FROM  accessbank WHERE password = %s"
            value = (password,)
            mycursor.execute(myquery, value)
            myreg = mycursor.fetchone()
            try:
                if myreg[-1] == password:

                    
                    
                    print('1.MTN\n2.GLO\n3.AIRTEL')
                    myreg = myreg[-4]
                    buy_card = input('Enter command: ')
                    if buy_card == '1':
                        number = input('Enter number: ')
                        if len(number) != 11:
                            print('Enter a correct number ')
                        else:
                            if not number.isdigit():
                                print('pls enter only digit')
                            elif number[:4] in ['0803', '0703', '0903', '0806', '0706', '0906']:
                                select_amount = int(input('Enter amount: '))
                                if select_amount <= myreg:
                                    myquery = "UPDATE accessbank SET available_bal = %s WHERE password = %s"
                                    result = (myreg - select_amount)
                                    value = (result, password,)
                                    mycursor.execute(myquery, value)
                                    myserver.commit()
                                    print('Successfully send card to this Mtn number', number)
                                else:
                                    print('Insufficient Fund')
                            elif number[:4] not in ['0803', '0703', '0903', '0806', '0706', '0906']:
                                print('Please enter correct mtn number')

                     

                    elif buy_card == '2':
                       
                            number = input('Enter number: ')
                            if len(number) != 11:
                                print('Enter a correct number ')
                            else:
                                if not number.isdigit():
                                    print('pls enter only digit')
                                elif number[:4] in ['0805', '0705', '0905']:
                                    select_amount = int(input('Enter amount: '))
                                    if select_amount <= myreg:
                                        myquery = "UPDATE accessbank SET available_bal = %s WHERE password = %s"
                                        result = (myreg - select_amount)
                                        value = (result, password,)
                                        mycursor.execute(myquery, value)
                                        myserver.commit()
                                        print('Successfully send card to this Glo number', number)
                                    else:
                                        print('Insufficient Fund')
                                elif number[:4] not in ['0805', '0705', '0905']:
                                    print('Please enter correct glo number')
                        

                    elif buy_card == '3':
                        number = input('Enter number: ')
                        if len(number) != 11:
                            print('Enter a correct number ')
                        else:
                            if not number.isdigit():
                                print('pls enter only digit')
                            elif number[:4] in ['0802', '0702', '0701']:
                                select_amount = int(input('Enter amount: '))
                                if select_amount <= myreg:
                                    myquery = "UPDATE accessbank SET available_bal = %s WHERE password = %s"
                                    result = (myreg - select_amount)
                                    value = (result, password,)
                                    mycursor.execute(myquery, value)
                                    myserver.commit()
                                    print('Successfully send card to this Airtel number', number)
                                else:
                                    print('Insufficcient Fund')
                            elif number[:4] not in ['0802', '0702', '0701']:
                                print('Please enter correct airtel number')
                       
                    else:
                        print('Unknown Input')

                else:
                    print('Incorrect Password')
            except TypeError:
                print('Incorrect Password')



        elif enter == '4':
            password = int(input('Enter password: '))
            myquery = "SELECT * FROM  accessbank WHERE password = %s"
            value = (password,)
            mycursor.execute(myquery, value)
            myreg = mycursor.fetchone()
            try:
                if myreg[-1] == password:
                    myreg = myreg[-4]
                    print('1.MTN\n2.GLO\n3.AIRTEL')
                    buy_data = input('Enter command: ')
                    # FOR MTN
                    if buy_data == '1':
                        print('1.1GB for 300\n2.3GB for 1500\n3.10GB for 5000')
                        enter_data = int(input('Enter command: '))
                        if enter_data == 300:
                            number = input('Enter number: ')
                            if len(number) != 11:
                                    print('Enter a correct number ')
                            else:
                                if not number.isdigit():
                                    print('pls enter only digit')
                                elif number[:4] in ['0803', '0703', '0903', '0806', '0706', '0906']:
                                    if enter_data <= myreg:
                                        myquery = "UPDATE accessbank SET available_bal = %s WHERE password = %s"
                                        result = (myreg - enter_data)
                                        value = (result, password,)
                                        mycursor.execute(myquery, value)
                                        myserver.commit()
                                        print('Successfully buy 1GB of data to this Mtn number', number)
                                    elif myreg < enter_data:
                                        print('Insufficient Fund')
                                elif number[:4] not in ['0803', '0703', '0903', '0806', '0706', '0906']:
                                    print('Please enter correct mtn number')


                        elif enter_data == 1500:
                            number = input('Enter number: ')
                            if len(number) != 11:
                                print('Enter a correct number ')
                            else:
                                if not number.isdigit():
                                    print('pls enter only digit')
                                elif number[:4] in ['0803', '0703', '0903', '0806', '0706', '0906']:
                                    if enter_data <= myreg:
                                        myquery = "UPDATE accessbank SET available_bal = %s WHERE password = %s"
                                        result = (myreg - enter_data)
                                        value = (result, password,)
                                        mycursor.execute(myquery, value)
                                        myserver.commit()
                                        print('Successfully buy 3GB of data to this Mtn number', number)
                                    elif myreg < enter_data:
                                        print('Insufficient Fund')
                                elif number[:4] not in ['0803', '0703', '0903', '0806', '0706', '0906']:
                                    print('Please enter correct mtn number')

                        elif enter_data == 5000:
                            number = input('Enter number: ')
                            if len(number) != 11:
                                    print('Enter a correct number ')
                            else:
                                if not number.isdigit():
                                    print('pls enter only digit')
                                elif number[:4] in ['0803', '0703', '0903', '0806', '0706', '0906']:
                                    if enter_data <= myreg:
                                        myquery = "UPDATE accessbank SET available_bal = %s WHERE password = %s"
                                        result = (myreg - enter_data)
                                        value = (result, password,)
                                        mycursor.execute(myquery, value)
                                        myserver.commit()
                                        print('Successfully buy 10GB of data to this Mtn number', number)
                                    elif myreg < enter_data:
                                        print('Insufficient Fund')
                                elif number[:4] not in ['0803', '0703', '0903', '0806', '0706', '0906']:
                                    print('Please enter correct mtn number')
                        else:
                            print('Unknown Input')

                    # FOR GLO
                    elif buy_data == '2':
                        print('1.1GB for 300\n2.3GB for 1500\n3.10GB for 5000')
                        enter_data = int(input('Enter command: '))
                        if enter_data == 300:
                            number = input('Enter number: ')
                            if len(number) != 11:
                                        print('Enter a correct number ')
                            else:
                                if not number.isdigit():
                                    print('pls enter only digit')
                                elif number[:4] in ['0805', '0705', '0905']:
                                    if enter_data <= myreg:
                                        myquery = "UPDATE accessbank SET available_bal = %s WHERE password = %s"
                                        result = (myreg - enter_data)
                                        value = (result, password,)
                                        mycursor.execute(myquery, value)
                                        myserver.commit()
                                        print('Successfully buy 1GB of data to this Glo number', number)
                                    elif myreg < enter_data:
                                        print('Insufficient Fund')

                                elif number[:4] not in ['0805', '0705', '0905']:
                                    print('Please enter correct glo number')

                        elif enter_data == 1500:
                            number = input('Enter number: ')
                            if len(number) != 11:
                                        print('Enter a correct number ')
                            else:
                                if not number.isdigit():
                                    print('pls enter only digit')
                                elif number[:4] in ['0805', '0705', '0905']:
                                    if enter_data <= myreg:
                                        myquery = "UPDATE accessbank SET available_bal = %s WHERE password = %s"
                                        result = (myreg - enter_data)
                                        value = (result, password,)
                                        mycursor.execute(myquery, value)
                                        myserver.commit()
                                        print('Successfully buy 3GB of data to this Glo number', number)
                                    elif myreg < enter_data:
                                        print('Insufficient Fund')
                                elif number[:4] not in ['0805', '0705', '0905']:
                                    print('Please enter correct glo number')

                        elif enter_data == 5000:
                            number = input('Enter number: ')
                            if len(number) != 11:
                                        print('Enter a correct number ')
                            else:
                                if not number.isdigit():
                                    print('pls enter only digit')
                                elif number[:4] in ['0805', '0705', '0905']:
                            # if number:
                                    if enter_data <= myreg:
                                        myquery = "UPDATE accessbank SET available_bal = %s WHERE password = %s"
                                        result = (myreg - enter_data)
                                        value = (result, password,)
                                        mycursor.execute(myquery, value)
                                        myserver.commit()
                                        print('Successfully buy 10GB of data to this Glo number', number)
                                    elif myreg < enter_data:
                                        print('Insufficient Fund')
                                elif number[:4] not in ['0805', '0705', '0905']:
                                    print('Please enter correct glo number')
                        else:
                            print('Unknown Input')

                    #  FOR AIRTEL
                    elif buy_data == '3':
                        print('1.1GB for 300\n2.3GB for 1500\n3.10GB for 5000')
                        enter_data = int(input('Enter command: '))
                        if enter_data == 300:
                            number = input('Enter number: ')
                            if len(number) != 11:
                                    print('Enter a correct number ')
                            else:
                                if not number.isdigit():
                                    print('pls enter only digit')
                                elif number[:4] in ['0802', '0702', '0701']:
                        
                                    if enter_data <= myreg:
                                        myquery = "UPDATE accessbank SET available_bal = %s WHERE password = %s"
                                        result = (myreg - enter_data)
                                        value = (result, password,)
                                        mycursor.execute(myquery, value)
                                        myserver.commit()
                                        print('Successfully buy 1GB of data to this Airtel number', number)
                                    elif myreg < enter_data:
                                        print('Insufficient Fund')
                                elif number[:4] not in ['0802', '0702', '0701']:
                                    print('Please enter correct airtel number')

                        elif enter_data == 1500:
                            number = input('Enter number: ')
                            if len(number) != 11:
                                    print('Enter a correct number ')
                            else:
                                if not number.isdigit():
                                    print('pls enter only digit')
                                elif number[:4] in ['0802', '0702', '0701']:
                                    if enter_data <= myreg:
                                        myquery = "UPDATE accessbank SET available_bal = %s WHERE password = %s"
                                        result = (myreg - enter_data)
                                        value = (result, password,)
                                        mycursor.execute(myquery, value)
                                        myserver.commit()
                                        print('Successfully buy 3GB of data to this Airtel number', number)
                                    elif myreg < enter_data:
                                        print('Insufficient Fund')
                                elif number[:4] not in ['0802', '0702', '0701']:
                                    print('Please enter correct airtel number')

                        elif enter_data == 5000:
                            number = input('Enter number: ')
                            if len(number) != 11:
                                print('Enter a correct number ')
                            else:
                                if not number.isdigit():
                                    print('pls enter only digit')
                                elif number[:4] in ['0802', '0702', '0701']:
                                    if enter_data <= myreg:
                                        myquery = "UPDATE accessbank SET available_bal = %s WHERE password = %s"
                                        result = (myreg - enter_data)
                                        value = (result, password,)
                                        mycursor.execute(myquery, value)
                                        myserver.commit()
                                        print('Successfully buy 10GB of data to this Airtel number', number)
                                    elif myreg < enter_data:
                                        print('Insufficient Fund')
                                elif number[:4] not in ['0802', '0702', '0701']:
                                    print('Please enter correct airtel number')
                        else:
                            print('Unknown Input')

                    else:
                        print('Unknown Input')
            except TypeError:
                print('Incorrect Password')

        elif enter == '5':
            password = int(input('Enter password: '))
            query = " SELECT * FROM accessbank WHERE password=%s"
            value = (password,)
            mycursor.execute(query, value)
            myreg = mycursor.fetchone()
            try:
                if password == myreg[-2]:
                    print('Name:', myreg[1],myreg[2], ',' , 'Available_balance:', myreg[-4], ',' , 'Account:', myreg[-3]) 
                    amount = float(input('Enter amount you want to deposite: '))
                    myquery = "UPDATE accessbank SET available_bal = %s WHERE password=%s"
                    new = myreg[-4]
                    if new is None: 
                        new = 0
                        new_result = (new + amount)
                        value = (new_result, password,)
                        mycursor.execute(myquery, value)
                        myserver.commit()
                        print(mycursor.rowcount, 'Transaction Completed...')
                    else: 
                        new_result = (new + amount)
                        value = (new_result, password)
                        mycursor.execute(myquery, value)
                        myserver.commit()
                        print(mycursor.rowcount, 'Transaction Completed...')   
                
            except TypeError:
                print('Incorrect Password')

        else:
            print('Unknown Input')
            quit()
            


    











    # TRANSACTION FOR FIRST
    def operation_first():
        print('1.Check Available Balance\n2.Send Money\n3.Buy Card\n4.Buy Data\n5.Save Money')
        enter = input('Enter command: ')
    
#  CHECK ACCOUNT BALANCE
        if enter == '1':
            password = int(input('Enter password: '))
            myquery = "SELECT * FROM firstbank WHERE password = %s"
            value = (password,)
            mycursor.execute(myquery, value)
            myreg = mycursor.fetchone()
            try:
                if myreg[-1] == password:
                    print('Name:', myreg[1],myreg[2] + ',' ,'Available_balance:', myreg[-4])
            except TypeError:
                print('Incorrect Password')


#  SEND MONEY
        elif enter == '2':
            password = int(input('Enter password: '))
            myquery = "SELECT * FROM firstbank WHERE password = %s"
            value = (password,)
            mycursor.execute(myquery, value)
            myreg = mycursor.fetchone()
            
            try:
                if myreg[-1] == password:
                
                    send_amount = int(input('Enter the amount you want to send: '))
                    con = int(myreg[-4])
                    result = (con - 50)
                    if send_amount > result:
                        print('Insufficient Fund')
                    elif send_amount <= result:
                        print('Destination Bank')
                        destination_bank = input('Enter A to send to ACCESS BANK\nEnter F to send to FIRST BANK\nEnter P to send to POLARIS BANK: ').lower()
                    #     ACCESS BANK
                        if destination_bank == 'a':
                            print('Destination Account Type')
                            destination_accounttype = input('Enter 1 Savings\nEnter 2 Current: ').lower()
                            if destination_accounttype == '1':
                                print('Destination Account Number')
                                destination_account = int(input('Enter account number: '))
                                if destination_account:
                                    myquery = "SELECT * FROM  accessbank WHERE account_no = %s"
                                    value = (destination_account,)
                                    mycursor.execute(myquery, value)
                                    myreg = mycursor.fetchone()
                                    print('Name:', myreg[1],myreg[2] + ',' ,'Account:', myreg[-3], 'Access Bank')
                                    send = input('Enter Y to send the money\nEnter N to cancel: ').lower()
                                    if send == 'y':
                                        query = "SELECT * FROM firstbank WHERE password = %s"
                                        val = (password,)
                                        mycursor.execute(query, val)
                                        myreg = mycursor.fetchone()
                                        new_reg = myreg[-4]
                                        myquery = ("UPDATE firstbank SET available_bal = %s WHERE password  = %s")
                                        new_reg = myreg[-4]
                                        latest_result = (new_reg - send_amount - 50)
                                        value = (latest_result, password)
                                        mycursor.execute(myquery, value)
                                        myserver.commit()
                                        if send:
                                            myquery = "SELECT * FROM  accessbank WHERE account_no = %s"
                                            value = (destination_account,)
                                            mycursor.execute(myquery, value)
                                            myreg = mycursor.fetchone()
                                            myquery = "UPDATE accessbank SET available_bal = %s WHERE account_no  = %s"
                                            new = myreg[-4]
                                            if new is None: 
                                                new = 0
                                                new_result = (new + send_amount - 50)
                                                value = (new_result, destination_account)
                                                mycursor.execute(myquery, value)
                                                myserver.commit()
                                                print(mycursor.rowcount, 'Transaction Completed...')
                                            else: 
                                                new_result = (new + send_amount - 50)
                                                value = (new_result, destination_account)
                                                mycursor.execute(myquery, value)
                                                myserver.commit()
                                                print(mycursor.rowcount, 'Transaction Completed...')     
                                        
                                    elif send == 'n':
                                        print('Transaction Cancelled...')
                                        quit()
                                    else:
                                        print('Unknown Input...Try again')
                                        quit()
                                else:
                                    print('Enter Destination Account Number')
                            elif destination_accounttype == '2':
                                print('Current Account Not Available...')
                            
                            else:
                                print('Unknown Input...Try again')


                        #  FIRST BANK

                        if destination_bank == 'f':
                            print('Destination Account Type')
                            destination_accounttype = input('Enter 1 Savings\nEnter 2 Current: ').lower()
                            if destination_accounttype == '1':
                                print('Destination Account Number')
                                destination_account = int(input('Enter account number: '))
                                if destination_account:
                                    myquery = "SELECT * FROM  firstbank WHERE account_no = %s"
                                    value = (destination_account,)
                                    mycursor.execute(myquery, value)
                                    myreg = mycursor.fetchone()
                                    
                                    print('Name:', myreg[1],myreg[2] + ',' ,'Account:', myreg[-3], 'First Bank')
                                    send = input('Enter Y to send the money\nEnter N to cancel: ').lower()
                                
                                    if send == 'y':
                                        query = "SELECT * FROM firstbank WHERE password = %s"
                                        val = (password,)
                                        mycursor.execute(query, val)
                                        myreg = mycursor.fetchone()
                                        new_reg = myreg[-4]
                                        myquery = ("UPDATE firstbank SET available_bal = %s WHERE password  = %s")
                                        new_reg = myreg[-4]
                                        latest_result = (new_reg - send_amount - 50)
                                        value = (latest_result, password)
                                        mycursor.execute(myquery, value)
                                        myserver.commit()
                                        
                                        if send:
                                            myquery = "SELECT * FROM  firstbank WHERE account_no = %s"
                                            value = (destination_account,)
                                            mycursor.execute(myquery, value)
                                            myreg = mycursor.fetchone()
                                            myquery = "UPDATE firstbank SET available_bal = %s WHERE account_no  = %s"
                                            new = myreg[-4]
                                            if new is None: 
                                                new = 0
                                                new_result = (new + send_amount - 50)
                                                value = (new_result, destination_account)
                                                mycursor.execute(myquery, value)
                                                myserver.commit()
                                                print(mycursor.rowcount, 'Transaction Completed...')
                                            else: 
                                                new_result = (new + send_amount - 50)
                                                value = (new_result, destination_account)
                                                mycursor.execute(myquery, value)
                                                myserver.commit()
                                                print(mycursor.rowcount, 'Transaction Completed...')      
                                        
                                    elif send == 'n':
                                        print('Transaction Cancelled...')
                                        quit()
                                    else:
                                        print('Unknown Input...Try again')
                                        quit()
                                else:
                                    print('Enter Destination Account Number')
                            elif destination_accounttype == '2':
                                print('Current Account Not Available...')
                            
                            else:
                                print('Unknown Input...Try again')


                        #  POLARIS BANK

                        elif destination_bank == 'p':
                            print('Destination Account Type')
                            destination_accounttype = input('Enter 1 Savings\nEnter 2 Current: ').lower()
                            if destination_accounttype == '1':
                                print('Destination Account Number')
                                destination_account = int(input('Enter account number: '))
                                if destination_account:
                                    myquery = "SELECT * FROM  polarisbank WHERE account_no = %s"
                                    value = (destination_account,)
                                    mycursor.execute(myquery, value)
                                    myreg = mycursor.fetchone()
                                    print('Name:', myreg[1],myreg[2] + ',' ,'Account:', myreg[-3], 'Polaris Bank')
                                    send = input('Enter Y to send the money\nEnter N to cancel: ').lower()
                                    if send == 'y':
                                        query = "SELECT * FROM firstbank WHERE password = %s"
                                        val = (password,)
                                        mycursor.execute(query, val)
                                        myreg = mycursor.fetchone()
                                        new_reg = myreg[-4]
                                        myquery = ("UPDATE firstbank SET available_bal = %s WHERE password  = %s")
                                        new_reg = myreg[-4]
                                        latest_result = (new_reg - send_amount - 50)
                                        value = (latest_result, password)
                                        mycursor.execute(myquery, value)
                                        myserver.commit()
                                
                                        if send:
                                            myquery = "SELECT * FROM  polarisbank WHERE account_no = %s"
                                            value = (destination_account,)
                                            mycursor.execute(myquery, value)
                                            myreg = mycursor.fetchone()
                                            myquery = "UPDATE polarisbank SET available_bal = %s WHERE account_no  = %s"
                                            new = myreg[-4]
                                            if new is None: 
                                                new = 0
                                                new_result = (new + send_amount - 50)
                                                value = (new_result, destination_account)
                                                mycursor.execute(myquery, value)
                                                myserver.commit()
                                                print(mycursor.rowcount, 'Transaction Completed...')
                                            else: 
                                                new_result = (new + send_amount - 50)
                                                value = (new_result, destination_account)
                                                mycursor.execute(myquery, value)
                                                myserver.commit()
                                                print(mycursor.rowcount, 'Transaction Completed...') 
                                    elif send == 'n':
                                        print('Transaction Cancelled...')
                                        quit()
                                    else:
                                        print('Unknown Input...Try again')
                                        quit()
                                else:
                                    print('Enter Destination Account Number')
                            elif destination_accounttype == '2':
                                print('Current Account Not Available...')
                            
                            else:
                                print('Unknown Input...Try again')

                    else:
                        print('Enter a valid amount')

                else:
                    print('Enter a correct password')

            except TypeError:
                print('Incorrect Password')


#  BUY CARD
        elif enter == '3':
            password = int(input('Enter password: '))
            myquery = "SELECT * FROM  firstbank WHERE password = %s"
            value = (password,)
            mycursor.execute(myquery, value)
            myreg = mycursor.fetchone()
            try:
                if myreg[-1] == password:

                    
                    
                    print('1.MTN\n2.GLO\n3.AIRTEL')
                    myreg = myreg[-4]
                    buy_card = input('Enter command: ')
                    if buy_card == '1':
                        number = input('Enter number: ')
                        if len(number) != 11:
                            print('Enter a correct number ')
                        else:
                            if not number.isdigit():
                                print('pls enter only digit')
                            elif number[:4] in ['0803', '0703', '0903', '0806', '0706', '0906']:
                                select_amount = int(input('Enter amount: '))
                                if select_amount <= myreg:
                                    myquery = "UPDATE firstbank SET available_bal = %s WHERE password = %s"
                                    result = (myreg - select_amount)
                                    value = (result, password,)
                                    mycursor.execute(myquery, value)
                                    myserver.commit()
                                    print('Successfully send card to this Mtn number', number)
                                else:
                                    print('Insufficient Fund')
                            elif number[:4] not in ['0803', '0703', '0903', '0806', '0706', '0906']:
                                print('Please enter correct mtn number')

                     

                    elif buy_card == '2':
                       
                            number = input('Enter number: ')
                            if len(number) != 11:
                                print('Enter a correct number ')
                            else:
                                if not number.isdigit():
                                    print('pls enter only digit')
                                elif number[:4] in ['0805', '0705', '0905']:
                                    select_amount = int(input('Enter amount: '))
                                    if select_amount <= myreg:
                                        myquery = "UPDATE firstbank SET available_bal = %s WHERE password = %s"
                                        result = (myreg - select_amount)
                                        value = (result, password,)
                                        mycursor.execute(myquery, value)
                                        myserver.commit()
                                        print('Successfully send card to this Glo number', number)
                                    else:
                                        print('Insufficient Fund')
                                elif number[:4] not in ['0805', '0705', '0905']:
                                    print('Please enter correct glo number')
                        

                    elif buy_card == '3':
                        number = input('Enter number: ')
                        if len(number) != 11:
                            print('Enter a correct number ')
                        else:
                            if not number.isdigit():
                                print('pls enter only digit')
                            elif number[:4] in ['0802', '0702', '0701']:
                                select_amount = int(input('Enter amount: '))
                                if select_amount <= myreg:
                                    myquery = "UPDATE firstbank SET available_bal = %s WHERE password = %s"
                                    result = (myreg - select_amount)
                                    value = (result, password,)
                                    mycursor.execute(myquery, value)
                                    myserver.commit()
                                    print('Successfully send card to this Airtel number', number)
                                else:
                                    print('Insufficcient Fund')
                            elif number[:4] not in ['0802', '0702', '0701']:
                                print('Please enter correct airtel number')
                       
                    else:
                        print('Unknown Input')

                else:
                    print('Incorrect Password')
            except TypeError:
                print('Incorrect Password')



        elif enter == '4':
            password = int(input('Enter password: '))
            myquery = "SELECT * FROM  firstbank WHERE password = %s"
            value = (password,)
            mycursor.execute(myquery, value)
            myreg = mycursor.fetchone()
            try:
                if myreg[-1] == password:
                    myreg = myreg[-4]
                    print('1.MTN\n2.GLO\n3.AIRTEL')
                    buy_data = input('Enter command: ')
                    # FOR MTN
                    if buy_data == '1':
                        print('1.1GB for 300\n2.3GB for 1500\n3.10GB for 5000')
                        enter_data = int(input('Enter command: '))
                        if enter_data == 300:
                            number = input('Enter number: ')
                            if len(number) != 11:
                                    print('Enter a correct number ')
                            else:
                                if not number.isdigit():
                                    print('pls enter only digit')
                                elif number[:4] in ['0803', '0703', '0903', '0806', '0706', '0906']:
                                    if enter_data <= myreg:
                                        myquery = "UPDATE firstbank SET available_bal = %s WHERE password = %s"
                                        result = (myreg - enter_data)
                                        value = (result, password,)
                                        mycursor.execute(myquery, value)
                                        myserver.commit()
                                        print('Successfully buy 1GB of data to this Mtn number', number)
                                    elif myreg < enter_data:
                                        print('Insufficient Fund')
                                elif number[:4] not in ['0803', '0703', '0903', '0806', '0706', '0906']:
                                    print('Please enter correct mtn number')


                        elif enter_data == 1500:
                            number = input('Enter number: ')
                            if len(number) != 11:
                                print('Enter a correct number ')
                            else:
                                if not number.isdigit():
                                    print('pls enter only digit')
                                elif number[:4] in ['0803', '0703', '0903', '0806', '0706', '0906']:
                                    if enter_data <= myreg:
                                        myquery = "UPDATE firstbank SET available_bal = %s WHERE password = %s"
                                        result = (myreg - enter_data)
                                        value = (result, password,)
                                        mycursor.execute(myquery, value)
                                        myserver.commit()
                                        print('Successfully buy 3GB of data to this Mtn number', number)
                                    elif myreg < enter_data:
                                        print('Insufficient Fund')
                                elif number[:4] not in ['0803', '0703', '0903', '0806', '0706', '0906']:
                                    print('Please enter correct mtn number')

                        elif enter_data == 5000:
                            number = input('Enter number: ')
                            if len(number) != 11:
                                    print('Enter a correct number ')
                            else:
                                if not number.isdigit():
                                    print('pls enter only digit')
                                elif number[:4] in ['0803', '0703', '0903', '0806', '0706', '0906']:
                                    if enter_data <= myreg:
                                        myquery = "UPDATE firstbank SET available_bal = %s WHERE password = %s"
                                        result = (myreg - enter_data)
                                        value = (result, password,)
                                        mycursor.execute(myquery, value)
                                        myserver.commit()
                                        print('Successfully buy 10GB of data to this Mtn number', number)
                                    elif myreg < enter_data:
                                        print('Insufficient Fund')
                                elif number[:4] not in ['0803', '0703', '0903', '0806', '0706', '0906']:
                                    print('Please enter correct mtn number')
                        else:
                            print('Unknown Input')

                    # FOR GLO
                    elif buy_data == '2':
                        print('1.1GB for 300\n2.3GB for 1500\n3.10GB for 5000')
                        enter_data = int(input('Enter command: '))
                        if enter_data == 300:
                            number = input('Enter number: ')
                            if len(number) != 11:
                                        print('Enter a correct number ')
                            else:
                                if not number.isdigit():
                                    print('pls enter only digit')
                                elif number[:4] in ['0805', '0705', '0905']:
                                    if enter_data <= myreg:
                                        myquery = "UPDATE firstbank SET available_bal = %s WHERE password = %s"
                                        result = (myreg - enter_data)
                                        value = (result, password,)
                                        mycursor.execute(myquery, value)
                                        myserver.commit()
                                        print('Successfully buy 1GB of data to this Glo number', number)
                                    elif myreg < enter_data:
                                        print('Insufficient Fund')

                                elif number[:4] not in ['0805', '0705', '0905']:
                                    print('Please enter correct glo number')

                        elif enter_data == 1500:
                            number = input('Enter number: ')
                            if len(number) != 11:
                                        print('Enter a correct number ')
                            else:
                                if not number.isdigit():
                                    print('pls enter only digit')
                                elif number[:4] in ['0805', '0705', '0905']:
                                    if enter_data <= myreg:
                                        myquery = "UPDATE firstbank SET available_bal = %s WHERE password = %s"
                                        result = (myreg - enter_data)
                                        value = (result, password,)
                                        mycursor.execute(myquery, value)
                                        myserver.commit()
                                        print('Successfully buy 3GB of data to this Glo number', number)
                                    elif myreg < enter_data:
                                        print('Insufficient Fund')
                                elif number[:4] not in ['0805', '0705', '0905']:
                                    print('Please enter correct glo number')

                        elif enter_data == 5000:
                            number = input('Enter number: ')
                            if len(number) != 11:
                                        print('Enter a correct number ')
                            else:
                                if not number.isdigit():
                                    print('pls enter only digit')
                                elif number[:4] in ['0805', '0705', '0905']:
                            # if number:
                                    if enter_data <= myreg:
                                        myquery = "UPDATE firstbank SET available_bal = %s WHERE password = %s"
                                        result = (myreg - enter_data)
                                        value = (result, password,)
                                        mycursor.execute(myquery, value)
                                        myserver.commit()
                                        print('Successfully buy 10GB of data to this Glo number', number)
                                    elif myreg < enter_data:
                                        print('Insufficient Fund')
                                elif number[:4] not in ['0805', '0705', '0905']:
                                    print('Please enter correct glo number')
                        else:
                            print('Unknown Input')

                    #  FOR AIRTEL
                    elif buy_data == '3':
                        print('1.1GB for 300\n2.3GB for 1500\n3.10GB for 5000')
                        enter_data = int(input('Enter command: '))
                        if enter_data == 300:
                            number = input('Enter number: ')
                            if len(number) != 11:
                                    print('Enter a correct number ')
                            else:
                                if not number.isdigit():
                                    print('pls enter only digit')
                                elif number[:4] in ['0802', '0702', '0701']:
                        
                                    if enter_data <= myreg:
                                        myquery = "UPDATE firstbank SET available_bal = %s WHERE password = %s"
                                        result = (myreg - enter_data)
                                        value = (result, password,)
                                        mycursor.execute(myquery, value)
                                        myserver.commit()
                                        print('Successfully buy 1GB of data to this Airtel number', number)
                                    elif myreg < enter_data:
                                        print('Insufficient Fund')
                                elif number[:4] not in ['0802', '0702', '0701']:
                                    print('Please enter correct airtel number')

                        elif enter_data == 1500:
                            number = input('Enter number: ')
                            if len(number) != 11:
                                    print('Enter a correct number ')
                            else:
                                if not number.isdigit():
                                    print('pls enter only digit')
                                elif number[:4] in ['0802', '0702', '0701']:
                                    if enter_data <= myreg:
                                        myquery = "UPDATE firstbank SET available_bal = %s WHERE password = %s"
                                        result = (myreg - enter_data)
                                        value = (result, password,)
                                        mycursor.execute(myquery, value)
                                        myserver.commit()
                                        print('Successfully buy 3GB of data to this Airtel number', number)
                                    elif myreg < enter_data:
                                        print('Insufficient Fund')
                                elif number[:4] not in ['0802', '0702', '0701']:
                                    print('Please enter correct airtel number')

                        elif enter_data == 5000:
                            number = input('Enter number: ')
                            if len(number) != 11:
                                print('Enter a correct number ')
                            else:
                                if not number.isdigit():
                                    print('pls enter only digit')
                                elif number[:4] in ['0802', '0702', '0701']:
                                    if enter_data <= myreg:
                                        myquery = "UPDATE firstbank SET available_bal = %s WHERE password = %s"
                                        result = (myreg - enter_data)
                                        value = (result, password,)
                                        mycursor.execute(myquery, value)
                                        myserver.commit()
                                        print('Successfully buy 10GB of data to this Airtel number', number)
                                    elif myreg < enter_data:
                                        print('Insufficient Fund')
                                elif number[:4] not in ['0802', '0702', '0701']:
                                    print('Please enter correct airtel number')
                        else:
                            print('Unknown Input')

                    else:
                        print('Unknown Input')
            except TypeError:
                print('Incorrect Password')

        elif enter == '5':
            password = int(input('Enter password: '))
            query = " SELECT * FROM firstbank WHERE password=%s"
            value = (password,)
            mycursor.execute(query, value)
            myreg = mycursor.fetchone()
            try:
                if password == myreg[-2]:
                    print('Name:', myreg[1],myreg[2], ',' , 'Available_balance:', myreg[-4], ',' , 'Account:', myreg[-3]) 
                    amount = float(input('Enter amount you want to deposite: '))
                    myquery = "UPDATE firstbank SET available_bal = %s WHERE password=%s"
                    new = myreg[-4]
                    if new is None: 
                        new = 0
                        new_result = (new + amount)
                        value = (new_result, password,)
                        mycursor.execute(myquery, value)
                        myserver.commit()
                        print(mycursor.rowcount, 'Transaction Completed...')
                    else: 
                        new_result = (new + amount)
                        value = (new_result, password)
                        mycursor.execute(myquery, value)
                        myserver.commit()
                        print(mycursor.rowcount, 'Transaction Completed...')   
                
            except TypeError:
                print('Incorrect Password')

        else:
            print('Unknown Input')
            quit()
            



    # TRANSACTION FOR ACCESS
    def operation_polaris():
        print('1.Check Available Balance\n2.Send Money\n3.Buy Card\n4.Buy Data\n5.Save Money')
        enter = input('Enter command: ')
    
#  CHECK ACCOUNT BALANCE
        if enter == '1':
            password = int(input('Enter password: '))
            myquery = "SELECT * FROM polarisbank WHERE password = %s"
            value = (password,)
            mycursor.execute(myquery, value)
            myreg = mycursor.fetchone()
            try:
                if myreg[-1] == password:
                    print('Name:', myreg[1],myreg[2] + ',' ,'Available_balance:', myreg[-4])
            except TypeError:
                print('Incorrect Password')


#  SEND MONEY
        elif enter == '2':
            password = int(input('Enter password: '))
            myquery = "SELECT * FROM polarisbank WHERE password = %s"
            value = (password,)
            mycursor.execute(myquery, value)
            myreg = mycursor.fetchone()
            
            try:
                if myreg[-1] == password:
                
                    send_amount = int(input('Enter the amount you want to send: '))
                    con = int(myreg[-4])
                    result = (con - 50)
                    if send_amount > result:
                        print('Insufficient Fund')
                    elif send_amount <= result:
                        print('Destination Bank')
                        destination_bank = input('Enter A to send to ACCESS BANK\nEnter F to send to FIRST BANK\nEnter P to send to POLARIS BANK: ').lower()
                    #     ACCESS BANK
                        if destination_bank == 'a':
                            print('Destination Account Type')
                            destination_accounttype = input('Enter 1 Savings\nEnter 2 Current: ').lower()
                            if destination_accounttype == '1':
                                print('Destination Account Number')
                                destination_account = int(input('Enter account number: '))
                                if destination_account:
                                    myquery = "SELECT * FROM  accessbank WHERE account_no = %s"
                                    value = (destination_account,)
                                    mycursor.execute(myquery, value)
                                    myreg = mycursor.fetchone()
                                    print('Name:', myreg[1],myreg[2] + ',' ,'Account:', myreg[-3], 'Access Bank')
                                    send = input('Enter Y to send the money\nEnter N to cancel: ').lower()
                                    if send == 'y':
                                        query = "SELECT * FROM polarisbank WHERE password = %s"
                                        val = (password,)
                                        mycursor.execute(query, val)
                                        myreg = mycursor.fetchone()
                                        new_reg = myreg[-4]
                                        myquery = ("UPDATE polarisbank SET available_bal = %s WHERE password  = %s")
                                        new_reg = myreg[-4]
                                        latest_result = (new_reg - send_amount - 50)
                                        value = (latest_result, password)
                                        mycursor.execute(myquery, value)
                                        myserver.commit()
                                        if send:
                                            myquery = "SELECT * FROM  accessbank WHERE account_no = %s"
                                            value = (destination_account,)
                                            mycursor.execute(myquery, value)
                                            myreg = mycursor.fetchone()
                                            myquery = "UPDATE accessbank SET available_bal = %s WHERE account_no  = %s"
                                            new = myreg[-4]
                                            if new is None: 
                                                new = 0
                                                new_result = (new + send_amount - 50)
                                                value = (new_result, destination_account)
                                                mycursor.execute(myquery, value)
                                                myserver.commit()
                                                print(mycursor.rowcount, 'Transaction Completed...')
                                            else: 
                                                new_result = (new + send_amount - 50)
                                                value = (new_result, destination_account)
                                                mycursor.execute(myquery, value)
                                                myserver.commit()
                                                print(mycursor.rowcount, 'Transaction Completed...')     
                                        
                                    elif send == 'n':
                                        print('Transaction Cancelled...')
                                        quit()
                                    else:
                                        print('Unknown Input...Try again')
                                        quit()
                                else:
                                    print('Enter Destination Account Number')
                            elif destination_accounttype == '2':
                                print('Current Account Not Available...')
                            
                            else:
                                print('Unknown Input...Try again')


                        #  FIRST BANK

                        if destination_bank == 'f':
                            print('Destination Account Type')
                            destination_accounttype = input('Enter 1 Savings\nEnter 2 Current: ').lower()
                            if destination_accounttype == '1':
                                print('Destination Account Number')
                                destination_account = int(input('Enter account number: '))
                                if destination_account:
                                    myquery = "SELECT * FROM  firstbank WHERE account_no = %s"
                                    value = (destination_account,)
                                    mycursor.execute(myquery, value)
                                    myreg = mycursor.fetchone()
                                    
                                    print('Name:', myreg[1],myreg[2] + ',' ,'Account:', myreg[-3], 'First Bank')
                                    send = input('Enter Y to send the money\nEnter N to cancel: ').lower()
                                
                                    if send == 'y':
                                        query = "SELECT * FROM polarisbank WHERE password = %s"
                                        val = (password,)
                                        mycursor.execute(query, val)
                                        myreg = mycursor.fetchone()
                                        new_reg = myreg[-4]
                                        myquery = ("UPDATE polarisbank SET available_bal = %s WHERE password  = %s")
                                        new_reg = myreg[-4]
                                        latest_result = (new_reg - send_amount - 50)
                                        value = (latest_result, password)
                                        mycursor.execute(myquery, value)
                                        myserver.commit()
                                        
                                        if send:
                                            myquery = "SELECT * FROM  firstbank WHERE account_no = %s"
                                            value = (destination_account,)
                                            mycursor.execute(myquery, value)
                                            myreg = mycursor.fetchone()
                                            myquery = "UPDATE firstbank SET available_bal = %s WHERE account_no  = %s"
                                            new = myreg[-4]
                                            if new is None: 
                                                new = 0
                                                new_result = (new + send_amount - 50)
                                                value = (new_result, destination_account)
                                                mycursor.execute(myquery, value)
                                                myserver.commit()
                                                print(mycursor.rowcount, 'Transaction Completed...')
                                            else: 
                                                new_result = (new + send_amount - 50)
                                                value = (new_result, destination_account)
                                                mycursor.execute(myquery, value)
                                                myserver.commit()
                                                print(mycursor.rowcount, 'Transaction Completed...')      
                                        
                                    elif send == 'n':
                                        print('Transaction Cancelled...')
                                        quit()
                                    else:
                                        print('Unknown Input...Try again')
                                        quit()
                                else:
                                    print('Enter Destination Account Number')
                            elif destination_accounttype == '2':
                                print('Current Account Not Available...')
                            
                            else:
                                print('Unknown Input...Try again')


                        #  POLARIS BANK

                        elif destination_bank == 'p':
                            print('Destination Account Type')
                            destination_accounttype = input('Enter 1 Savings\nEnter 2 Current: ').lower()
                            if destination_accounttype == '1':
                                print('Destination Account Number')
                                destination_account = int(input('Enter account number: '))
                                if destination_account:
                                    myquery = "SELECT * FROM  polarisbank WHERE account_no = %s"
                                    value = (destination_account,)
                                    mycursor.execute(myquery, value)
                                    myreg = mycursor.fetchone()
                                    print('Name:', myreg[1],myreg[2] + ',' ,'Account:', myreg[-3], 'Polaris Bank')
                                    send = input('Enter Y to send the money\nEnter N to cancel: ').lower()
                                    if send == 'y':
                                        query = "SELECT * FROM polarisbank WHERE password = %s"
                                        val = (password,)
                                        mycursor.execute(query, val)
                                        myreg = mycursor.fetchone()
                                        new_reg = myreg[-4]
                                        myquery = ("UPDATE polarisbank SET available_bal = %s WHERE password  = %s")
                                        new_reg = myreg[-4]
                                        latest_result = (new_reg - send_amount - 50)
                                        value = (latest_result, password)
                                        mycursor.execute(myquery, value)
                                        myserver.commit()
                                
                                        if send:
                                            myquery = "SELECT * FROM  polarisbank WHERE account_no = %s"
                                            value = (destination_account,)
                                            mycursor.execute(myquery, value)
                                            myreg = mycursor.fetchone()
                                            myquery = "UPDATE polarisbank SET available_bal = %s WHERE account_no  = %s"
                                            new = myreg[-4]
                                            if new is None: 
                                                new = 0
                                                new_result = (new + send_amount - 50)
                                                value = (new_result, destination_account)
                                                mycursor.execute(myquery, value)
                                                myserver.commit()
                                                print(mycursor.rowcount, 'Transaction Completed...')
                                            else: 
                                                new_result = (new + send_amount - 50)
                                                value = (new_result, destination_account)
                                                mycursor.execute(myquery, value)
                                                myserver.commit()
                                                print(mycursor.rowcount, 'Transaction Completed...') 
                                    elif send == 'n':
                                        print('Transaction Cancelled...')
                                        quit()
                                    else:
                                        print('Unknown Input...Try again')
                                        quit()
                                else:
                                    print('Enter Destination Account Number')
                            elif destination_accounttype == '2':
                                print('Current Account Not Available...')
                            
                            else:
                                print('Unknown Input...Try again')

                    else:
                        print('Enter a valid amount')

                else:
                    print('Enter a correct password')

            except TypeError:
                print('Incorrect Password')


#  BUY CARD
        elif enter == '3':
            password = int(input('Enter password: '))
            myquery = "SELECT * FROM  polarisbank WHERE password = %s"
            value = (password,)
            mycursor.execute(myquery, value)
            myreg = mycursor.fetchone()
            try:
                if myreg[-1] == password:

                    
                    
                    print('1.MTN\n2.GLO\n3.AIRTEL')
                    myreg = myreg[-4]
                    buy_card = input('Enter command: ')
                    if buy_card == '1':
                        number = input('Enter number: ')
                        if len(number) != 11:
                            print('Enter a correct number ')
                        else:
                            if not number.isdigit():
                                print('pls enter only digit')
                            elif number[:4] in ['0803', '0703', '0903', '0806', '0706', '0906']:
                                select_amount = int(input('Enter amount: '))
                                if select_amount <= myreg:
                                    myquery = "UPDATE polarisbank SET available_bal = %s WHERE password = %s"
                                    result = (myreg - select_amount)
                                    value = (result, password,)
                                    mycursor.execute(myquery, value)
                                    myserver.commit()
                                    print('Successfully send card to this Mtn number', number)
                                else:
                                    print('Insufficient Fund')
                            elif number[:4] not in ['0803', '0703', '0903', '0806', '0706', '0906']:
                                print('Please enter correct mtn number')

                     

                    elif buy_card == '2':
                       
                            number = input('Enter number: ')
                            if len(number) != 11:
                                print('Enter a correct number ')
                            else:
                                if not number.isdigit():
                                    print('pls enter only digit')
                                elif number[:4] in ['0805', '0705', '0905']:
                                    select_amount = int(input('Enter amount: '))
                                    if select_amount <= myreg:
                                        myquery = "UPDATE polarisbank SET available_bal = %s WHERE password = %s"
                                        result = (myreg - select_amount)
                                        value = (result, password,)
                                        mycursor.execute(myquery, value)
                                        myserver.commit()
                                        print('Successfully send card to this Glo number', number)
                                    else:
                                        print('Insufficient Fund')
                                elif number[:4] not in ['0805', '0705', '0905']:
                                    print('Please enter correct glo number')
                        

                    elif buy_card == '3':
                        number = input('Enter number: ')
                        if len(number) != 11:
                            print('Enter a correct number ')
                        else:
                            if not number.isdigit():
                                print('pls enter only digit')
                            elif number[:4] in ['0802', '0702', '0701']:
                                select_amount = int(input('Enter amount: '))
                                if select_amount <= myreg:
                                    myquery = "UPDATE polarisbank SET available_bal = %s WHERE password = %s"
                                    result = (myreg - select_amount)
                                    value = (result, password,)
                                    mycursor.execute(myquery, value)
                                    myserver.commit()
                                    print('Successfully send card to this Airtel number', number)
                                else:
                                    print('Insufficcient Fund')
                            elif number[:4] not in ['0802', '0702', '0701']:
                                print('Please enter correct airtel number')
                       
                    else:
                        print('Unknown Input')

                else:
                    print('Incorrect Password')
            except TypeError:
                print('Incorrect Password')



        elif enter == '4':
            password = int(input('Enter password: '))
            myquery = "SELECT * FROM  polarisbank WHERE password = %s"
            value = (password,)
            mycursor.execute(myquery, value)
            myreg = mycursor.fetchone()
            try:
                if myreg[-1] == password:
                    myreg = myreg[-4]
                    print('1.MTN\n2.GLO\n3.AIRTEL')
                    buy_data = input('Enter command: ')
                    # FOR MTN
                    if buy_data == '1':
                        print('1.1GB for 300\n2.3GB for 1500\n3.10GB for 5000')
                        enter_data = int(input('Enter command: '))
                        if enter_data == 300:
                            number = input('Enter number: ')
                            if len(number) != 11:
                                    print('Enter a correct number ')
                            else:
                                if not number.isdigit():
                                    print('pls enter only digit')
                                elif number[:4] in ['0803', '0703', '0903', '0806', '0706', '0906']:
                                    if enter_data <= myreg:
                                        myquery = "UPDATE polarisbank SET available_bal = %s WHERE password = %s"
                                        result = (myreg - enter_data)
                                        value = (result, password,)
                                        mycursor.execute(myquery, value)
                                        myserver.commit()
                                        print('Successfully buy 1GB of data to this Mtn number', number)
                                    elif myreg < enter_data:
                                        print('Insufficient Fund')
                                elif number[:4] not in ['0803', '0703', '0903', '0806', '0706', '0906']:
                                    print('Please enter correct mtn number')


                        elif enter_data == 1500:
                            number = input('Enter number: ')
                            if len(number) != 11:
                                print('Enter a correct number ')
                            else:
                                if not number.isdigit():
                                    print('pls enter only digit')
                                elif number[:4] in ['0803', '0703', '0903', '0806', '0706', '0906']:
                                    if enter_data <= myreg:
                                        myquery = "UPDATE polarisbank SET available_bal = %s WHERE password = %s"
                                        result = (myreg - enter_data)
                                        value = (result, password,)
                                        mycursor.execute(myquery, value)
                                        myserver.commit()
                                        print('Successfully buy 3GB of data to this Mtn number', number)
                                    elif myreg < enter_data:
                                        print('Insufficient Fund')
                                elif number[:4] not in ['0803', '0703', '0903', '0806', '0706', '0906']:
                                    print('Please enter correct mtn number')

                        elif enter_data == 5000:
                            number = input('Enter number: ')
                            if len(number) != 11:
                                    print('Enter a correct number ')
                            else:
                                if not number.isdigit():
                                    print('pls enter only digit')
                                elif number[:4] in ['0803', '0703', '0903', '0806', '0706', '0906']:
                                    if enter_data <= myreg:
                                        myquery = "UPDATE polarisbank SET available_bal = %s WHERE password = %s"
                                        result = (myreg - enter_data)
                                        value = (result, password,)
                                        mycursor.execute(myquery, value)
                                        myserver.commit()
                                        print('Successfully buy 10GB of data to this Mtn number', number)
                                    elif myreg < enter_data:
                                        print('Insufficient Fund')
                                elif number[:4] not in ['0803', '0703', '0903', '0806', '0706', '0906']:
                                    print('Please enter correct mtn number')
                        else:
                            print('Unknown Input')

                    # FOR GLO
                    elif buy_data == '2':
                        print('1.1GB for 300\n2.3GB for 1500\n3.10GB for 5000')
                        enter_data = int(input('Enter command: '))
                        if enter_data == 300:
                            number = input('Enter number: ')
                            if len(number) != 11:
                                        print('Enter a correct number ')
                            else:
                                if not number.isdigit():
                                    print('pls enter only digit')
                                elif number[:4] in ['0805', '0705', '0905']:
                                    if enter_data <= myreg:
                                        myquery = "UPDATE polarisbank SET available_bal = %s WHERE password = %s"
                                        result = (myreg - enter_data)
                                        value = (result, password,)
                                        mycursor.execute(myquery, value)
                                        myserver.commit()
                                        print('Successfully buy 1GB of data to this Glo number', number)
                                    elif myreg < enter_data:
                                        print('Insufficient Fund')

                                elif number[:4] not in ['0805', '0705', '0905']:
                                    print('Please enter correct glo number')

                        elif enter_data == 1500:
                            number = input('Enter number: ')
                            if len(number) != 11:
                                        print('Enter a correct number ')
                            else:
                                if not number.isdigit():
                                    print('pls enter only digit')
                                elif number[:4] in ['0805', '0705', '0905']:
                                    if enter_data <= myreg:
                                        myquery = "UPDATE polarisbank SET available_bal = %s WHERE password = %s"
                                        result = (myreg - enter_data)
                                        value = (result, password,)
                                        mycursor.execute(myquery, value)
                                        myserver.commit()
                                        print('Successfully buy 3GB of data to this Glo number', number)
                                    elif myreg < enter_data:
                                        print('Insufficient Fund')
                                elif number[:4] not in ['0805', '0705', '0905']:
                                    print('Please enter correct glo number')

                        elif enter_data == 5000:
                            number = input('Enter number: ')
                            if len(number) != 11:
                                        print('Enter a correct number ')
                            else:
                                if not number.isdigit():
                                    print('pls enter only digit')
                                elif number[:4] in ['0805', '0705', '0905']:
                            # if number:
                                    if enter_data <= myreg:
                                        myquery = "UPDATE polarisbank SET available_bal = %s WHERE password = %s"
                                        result = (myreg - enter_data)
                                        value = (result, password,)
                                        mycursor.execute(myquery, value)
                                        myserver.commit()
                                        print('Successfully buy 10GB of data to this Glo number', number)
                                    elif myreg < enter_data:
                                        print('Insufficient Fund')
                                elif number[:4] not in ['0805', '0705', '0905']:
                                    print('Please enter correct glo number')
                        else:
                            print('Unknown Input')

                    #  FOR AIRTEL
                    elif buy_data == '3':
                        print('1.1GB for 300\n2.3GB for 1500\n3.10GB for 5000')
                        enter_data = int(input('Enter command: '))
                        if enter_data == 300:
                            number = input('Enter number: ')
                            if len(number) != 11:
                                    print('Enter a correct number ')
                            else:
                                if not number.isdigit():
                                    print('pls enter only digit')
                                elif number[:4] in ['0802', '0702', '0701']:
                        
                                    if enter_data <= myreg:
                                        myquery = "UPDATE polarisbank SET available_bal = %s WHERE password = %s"
                                        result = (myreg - enter_data)
                                        value = (result, password,)
                                        mycursor.execute(myquery, value)
                                        myserver.commit()
                                        print('Successfully buy 1GB of data to this Airtel number', number)
                                    elif myreg < enter_data:
                                        print('Insufficient Fund')
                                elif number[:4] not in ['0802', '0702', '0701']:
                                    print('Please enter correct airtel number')

                        elif enter_data == 1500:
                            number = input('Enter number: ')
                            if len(number) != 11:
                                    print('Enter a correct number ')
                            else:
                                if not number.isdigit():
                                    print('pls enter only digit')
                                elif number[:4] in ['0802', '0702', '0701']:
                                    if enter_data <= myreg:
                                        myquery = "UPDATE polarisbank SET available_bal = %s WHERE password = %s"
                                        result = (myreg - enter_data)
                                        value = (result, password,)
                                        mycursor.execute(myquery, value)
                                        myserver.commit()
                                        print('Successfully buy 3GB of data to this Airtel number', number)
                                    elif myreg < enter_data:
                                        print('Insufficient Fund')
                                elif number[:4] not in ['0802', '0702', '0701']:
                                    print('Please enter correct airtel number')

                        elif enter_data == 5000:
                            number = input('Enter number: ')
                            if len(number) != 11:
                                print('Enter a correct number ')
                            else:
                                if not number.isdigit():
                                    print('pls enter only digit')
                                elif number[:4] in ['0802', '0702', '0701']:
                                    if enter_data <= myreg:
                                        myquery = "UPDATE polarisbank SET available_bal = %s WHERE password = %s"
                                        result = (myreg - enter_data)
                                        value = (result, password,)
                                        mycursor.execute(myquery, value)
                                        myserver.commit()
                                        print('Successfully buy 10GB of data to this Airtel number', number)
                                    elif myreg < enter_data:
                                        print('Insufficient Fund')
                                elif number[:4] not in ['0802', '0702', '0701']:
                                    print('Please enter correct airtel number')
                        else:
                            print('Unknown Input')

                    else:
                        print('Unknown Input')
            except TypeError:
                print('Incorrect Password')

        elif enter == '5':
            password = int(input('Enter password: '))
            query = " SELECT * FROM polarisbank WHERE password=%s"
            value = (password,)
            mycursor.execute(query, value)
            myreg = mycursor.fetchone()
            try:
                if password == myreg[-2]:
                    print('Name:', myreg[1],myreg[2], ',' , 'Available_balance:', myreg[-4], ',' , 'Account:', myreg[-3]) 
                    amount = float(input('Enter amount you want to deposite: '))
                    myquery = "UPDATE polarisbank SET available_bal = %s WHERE password=%s"
                    new = myreg[-4]
                    if new is None: 
                        new = 0
                        new_result = (new + amount)
                        value = (new_result, password,)
                        mycursor.execute(myquery, value)
                        myserver.commit()
                        print(mycursor.rowcount, 'Transaction Completed...')
                    else: 
                        new_result = (new + amount)
                        value = (new_result, password)
                        mycursor.execute(myquery, value)
                        myserver.commit()
                        print(mycursor.rowcount, 'Transaction Completed...')   
                
            except TypeError:
                print('Incorrect Password')

        else:
            print('Unknown Input')
            quit()
            


    







