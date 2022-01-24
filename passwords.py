class Password:
  def __init__(self,password,page):
    self.password = password
    self.page = page 

user_password= []

def save_page(self):
  """
  Saves the password to the user_passwords array
  """
  Password.user_password.append(self)

def remove_page(self):
  """
 Deletes a password  
  """
  Password.user_password.remove(self)

@classmethod
def display_page(cls):
  """
  Function to display passwords
  """
  return cls.user_password
@classmethod
def find_by_page(cls, pager):
        for pagy in cls.user_passwords:
            if pagy.page == pager:
                return pagy

@classmethod
def page_exists(cls, pager):
        for pagy in cls.user_passwords:
            if pagy.page == pager:
                return pagy
        return False




