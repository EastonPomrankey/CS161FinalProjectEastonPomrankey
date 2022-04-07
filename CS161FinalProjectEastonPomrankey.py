#Easton pomrankey
#CS 161 Final
#14 March 2022


class New_Account():
    '''A class used to create a new account.'''
    def __init__(self, new_account_number = 'none', new_account_name = 'none', new_account_balance = 0): #Attributes in class New_Account.
        '''Used to add attributes to class New_Account.'''
        self.new_account_number = new_account_number #Creates instance new_account_number.
        self.new_account_name = new_account_name #Creates instace New_account_name.
        self.new_account_balance = new_account_balance #Creates instance New_account_balance
     
    def print_new_account(self): 
        '''This will print the new account that has been created.'''
        print('Account Number: {} Account Name: {} Account Balance:\
              ${:.2f}'.format(self.new_account_number, self.new_account_number, self.new_account_balance)) #Print function used to print and format the variables.
        
class AccountInformation():
    '''Class used to help with account manager organization of all acounts, open accounts, 
    close accounts, charge and account, make a payment, maintain an account,
    output a single account or all accounts.'''
    def __init__(self, account_number = 'none', account_name = 'none', account_balance = 0, accounts_on_file = []): #Attributes in class AccountInformation.
        '''Used to add attributes to AccountInformation.'''
        self.account_number = account_number #Creates instance account_number.
        self.accounts_on_file = accounts_on_file #Creates instance accounts_on_file.
        self.account_name = account_name #Creates instance account_name.
        self.account_balance = account_balance #Creates instance account_balance.
        
    def open_account(self, opened_account:New_Account): #Attributes in open_account.
        '''Used to open an account.'''
        self.accounts_on_file.append(opened_account) #Appends(adds) the account that was oppened to accounts_on_file.
        
    def close_account(self, input_account_to_close): #Attributes in close_account.
        '''Used to close an account.'''
        for i in range(len(self.accounts_on_file)): #Indexes through accounts_on_file.
            if self.accounts_on_file[i].new_account_number == input_account_to_close: #Checks to see if the account number matches the account number of the account that is to be closed.
                self.accounts_on_file.remove(self.accounts_on_file[i]) #Removes the account from accounts_on_file
                
    def charge_account(self, account_number_charged, amount_charged_to_account): #Attributes in charge_account.
        '''Used to charge an account.'''
        for i in range(len(self.accounts_on_file)): #Indexes through accounts_on_file.
            if self.accounts_on_file[i].new_account_number == account_number_charged: #Checks to see if the account number that is to be charged is in accounts_on_file.
                self.accounts_on_file[i].new_account_balance = (self.accounts_on_file[i].new_account_balance - amount_charged_to_account) #subtracts the chareg from the accounts balance.
                
    def pay_charge(self, account_number_to_pay , amount_to_pay_on_account): #Attributes in pay_charge
        '''Used to pay charge on an account.'''
        for i in range(len(self.accounts_on_file)): #indexes through accounts_on_file.
            if self.accounts_on_file[i].new_account_number == account_number_to_pay: #Checks to see if the account number to be payed is in accounts_on_file.
                self.accounts_on_file[i].new_account_balance = (self.accounts_on_file[i].new_account_balance + amount_to_pay_on_account) #Pays the charge on the account by adding amount to the account balance.
    
    # def maintain_account(self, account_to_maintain, account_to_maintain_new_name, account_to_maintain_new_balance): #need to be able to get single account so I can change it    
        '''Used to maintain an account'''
        '''I ran into some issues with this block of code and it gives the error, 
        AttributeError: 'New_Account' object has no attribute 'account_to_maintain_new_name and when added to New_Account 
        another attribute error is returned. How can I fix this?'''
        # for account in range(len(self.accounts_on_file)):
        #     if self.accounts_on_file[account].new_account_number == account_to_maintain:
        #         print('Account Number: {} Account Name: {} Account Balance: \
        #               ${}'.format(self.accounts_on_file[account].new_account_number, 
        #               self.accounts_on_file[account].new_account_name.title().replace
        #               (self.accounts_on_file[account].new_account_name.title(), 
        #                 self.accounts_on_file[account].account_to_maintain_new_name.title()), 
        #               self.accounts_on_file[account].new_account_balance.replace
        #               (self.accounts_on_file[account].new_account_balance, 
        #                 self.accounts_on_file[account].account_to_maintain_new_balance)))
                
                
                
    def print_single_account(self, single_account): #Attributes in print_single_account.
        '''Used to print a single account.'''
        for account in range(len(self.accounts_on_file)): #indexes through accounts_on_file.
            if self.accounts_on_file[account].new_account_number == single_account: #Checks to see if the user input account number matches any numbers in accounts_on_file.
                print('Account Number: {} Account Name: {} Account Balance:\
                      ${}'.format(self.accounts_on_file[account].new_account_number, 
                      self.accounts_on_file[account].new_account_name.title(), self.accounts_on_file[account].new_account_balance)) #prints and formats the single account.

    def print_accounts(self): #Attributes in print_accounts.
        '''Used to print all acounts.'''
        print('Number of accounts:', (len(self.accounts_on_file))) #Prints the number of accounts in accounts_on_file.
        for account in self.accounts_on_file: #For all acounts in accounts_on_file
            print('Account Number: {} Account Name: {} Account Balance: ${}'.format(account.new_account_number, account.new_account_name.title(), account.new_account_balance)) #Prints and formats all the accounts on file with all thir information.
        
account_list = AccountInformation() #creates a list with Accountinformation.
def print_menu(): #Prints the menu
   menuOp = ' '
   while menuOp != '8' :
       ''' Outputs a menu for the account manager to select what task they would like to perform.
       When the user inputs a nuber coresponding to the task they wish to perform they will be promted
       to input an account number and other information such as amounts, balances, and names.'''
       menuOp = ''
       print('MENU')
       print('1 - Open account') 
       print('2 - Close account') 
       print('3 - Charge account') 
       print('4 - Pay charge')
       print('5 - Maintain account information')
       print('6 - Output individual account')
       print('7 - Output accounts') 
       print('8 - Quit\n')
       while menuOp != '1' and menuOp != '2' and menuOp != '3' and menuOp != '4' and menuOp != '5'\
           and menuOp != '6' and menuOp != '7' and menuOp != '8':
           #Asks user to select an option only if one of these numbers is selected.
          menuOp = input('Choose an option:\n') #Prompts the user to select an option from the menu.
          
          
       if menuOp == '1': #Opens account.
           print('You choose open account') #Informs teh user that they choose to open an account.
           print('Enter an account number:') #Prompts the user to enter an account number.
           user_input_account_number = input() #Assigns the account number with user_input_account_number.
           print('Enter your full name:') #Asks the user to enter their full name.
           user_input_full_name = input() #Assigns the users name to user_input_full_name.
           print('Enter account balance:') #Asks the user to enter in an account balance.
           user_input_account_balance = int(input()) #Assigns the users account balance with user_input_account_balance.
           opened_account = New_Account(user_input_account_number, user_input_full_name, user_input_account_balance) 
           #Assigns opened_account with the new account that was just created by the user.
           account_list.open_account(opened_account)#Adds the account to the list account_list.
        
       elif menuOp == '2': #Closes an account.
           print('You choose to remove a account') #Informs the user that they choose to remove an account.
           print('Enter account number:') #Prompts the user to enter an account number.
           input_account_to_close = input() #Assigns the account number with input_accoount_to_close.
           account_list.close_account(input_account_to_close)#Allows the varible to be used in close_account.
        
       elif  menuOp == '3': #Charges an amount to a users account balance.
            print('You choose to charge an account') #Informs the user that they choose to charge an account.
            print('Enter the account number:') #Prompts the user to enter an account number.
            account_number_charged = input() #Assigns the input to account_number_charged.
            print('Enter amount to charge:') #Ask the user to enter the amount that is to be charged to the account.
            amount_charged_to_account = int(input()) #Assigns the integer with amount_charged_to_account.
            account_list.charge_account(account_number_charged , amount_charged_to_account) #Allows the varibles to be used in charge_account.
            
       elif  menuOp == '4': #Used to pay a charge on the users account.
            print('You choose to pay an account charge') #Informs the user that they choose to pay a charge.
            print('Enter the account number:') #Aks for the users account number.
            account_number_to_pay = input() #Sets the input to account_number_to_pay.
            print('Enter amount to pay:') #Propmts the user to choose an amount they want to pay.
            amount_to_pay_on_account = int(input()) #Sets the integer to amount_to_pay_on_account.
            account_list.pay_charge(account_number_to_pay , amount_to_pay_on_account) #Allows the variables to be used in pay_charge.
            
            #The below is meant to be able to allow the account manager to maintain the account by being able to change the name and account balance.
            #I think the below code is correct and that the problem is within maintain_account in the class AccountInformation.
       # elif menuOp == '5': #Used to maintain an account by changing the name or balance in the account.
       #      print('Enter account number for the account you want to maintain') #Asks account manager for account number.
       #      account_to_maintain = input() #sets the input to account_to_maintain.
       #      print('Enter new name for account') #Asks the account manager to enter a new name for the account.
       #      account_to_maintain_new_name = input() #Sets the input name to account_to_maintain.
       #      print('Enter new balance for account') #Asks the account manager to change the balance of the account.
       #      account_to_maintain_new_balance = int(input()) #Sets the new integer to account_to_maintain_new_balance.
       #      account_list.maintain_account(account_to_maintain, account_to_maintain_new_name, account_to_maintain_new_balance) #allows the variables to be in main account.
           
       elif menuOp == '6':#print account information for individual
           print('Enter account number for the account you want to see') #Giving the account manager directions.
           single_account = input() #sets their input to single_account.
           account_list.print_single_account(single_account) #Allows single account to be in print_single_account.
       
       elif menuOp == '7':#print account infor for all acounts
           print(account_list.print_accounts()) #Prints everything in print_accounts.
           
if __name__ == "__main__": #Calls main.
    print_menu()         #Prints the menu to display to the account manager.