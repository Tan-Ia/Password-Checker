import hashlib
import pwnedpasswords
import sys
""" this application check hacked password . console given input check how much strong it is and how much it heacked by heackers"""

def get_password(data):
    """ this function for take console input """
    
    for password in data:
        check_password(password)
      

def check_password(password):
     """this function use for check console given password with pwnedpasswords module """

     hash_pass = hashlib.sha1(password.encode("UTF-8")).hexdigest().upper() # it convert plan string to hash
     check = pwnedpasswords.check(hash_pass)
     if(check >0):
         print(f"Your Passsword was Hacked {check} times .Plz Choose Strong Passsword ")
     else:
         print("Your Password Was Too Strong.Good Luck")
     
     


if __name__ == '__main__':
    get_password(sys.argv[1:])