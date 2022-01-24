from gettext import find
from accounts  import Accounts
from passwords import Password

def create_account(first_name,last_name,user_name,password):
  accounts = Accounts(first_name,last_name,user_name,password)
  return accounts

def save_account(accounts):
  accounts.save_account()

def delete_account(accounts):
  accounts.delete_account()

def find_accounts(user_name):
  return Accounts.find_by_username(user_name)

def isexist_accounts(user_name):
  return Accounts.account_exist(user_name)

def display_accounts():
  return Accounts.display_account()

def create_page(page,password):
  passwords = Password(page,password)
  return passwords

def save_page(passwords):
  passwords.save_page()

def find_page(pager):
    return Password.find_by_page(pager)


def isexist_page(pager):
    return Password.page_exists(pager)


def delete_page(passwords):
    passwords.delete_page()


def display_pages():
    return Password.display_page()


  



def main():
  print("WELCOME TO PINLock.")
  print("Use the following numbers to select your choice of action.")
  print("1)LOGIN\n 2)SIGN UP\n 3)ACCOUNTS DISPLAY\n 4) ABOUT PinLock\n 5)LOG OUT")


# Option for the about us display
  option = int(input())
  if option == 4:
    print("\nABOUT PINLock")
    print("We are the leading security password lockers. We ensure that your passwords are stored safely and securely from hackers. We also help you have a systmatic way of accessing your passwords incase you don't remember them.")

  if option == 1:
    print("Enter your username")
    username = input()
    print("Enter your password")
    password =input()
    account =find_accounts(username)
    if account.user_name == username and account.password == password :
       print("You have loged in")
   
       while True:
         print(f'Welcome {username} , you have successfuly logged in .Use the following numbers to select your next course of action.')
         print('1)Save new password\n  2)Delete Password\n 3)Display saved password\n 4)Log Out')
        
         log_choice = int(input())
         if log_choice == 1 :
            print('New page')
            print('*'*100)

            print('Page name')
            page = input()

            print('password')
            password = input()

            # created and saved page
            save_page(create_page(page, password))





if __name__ == "__main__":
  main()

