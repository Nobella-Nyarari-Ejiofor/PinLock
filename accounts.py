class Accounts:
  def __init__(self, first_name,last_name,user_name):
    self.first_name = first_name
    self.last_name = last_name
    self.user_name= user_name

user_accounts = []

def save_account(self):
  """
  This is a function that adds(appends) the account to the user_accounts array
  """
  Accounts.user_accounts.append(self)

def delete_account(self):
  """
  A function that deletes an account that has been selected
  """
  Accounts.user_accounts.remove(self)

@classmethod
def find_by_user_name(cls, user_name):
  """
  A function that checks whether the username provided by user and if it is available returns the account.
  """
  for account in cls.user_name:
    if account.user_name == user_name:
      return account


