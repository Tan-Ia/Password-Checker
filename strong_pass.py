import pwnedpasswords
import hashlib
import sys
import requests

""" this application check hacked password . console given input check how much strong it is and how much it heacked by heackers"""

def get_password(args):
    """ password get by console"""
    for password in args:
        heashed=hash_password(password)
        print(heashed)
        # checked=check_password(heashed)

def response_data(password):
    response=requests.get('https://api.pwnedpasswords.com/range/' + password)
  
    if(response.status_code == 200):
         return response 
    else:
        raise RuntimeError("plz check Again")
       

def hash_password(password):
    hash_pass = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    head , foot = hash_pass[:5] , hash_pass[5:]
  
    response = response_data(head)
    hashed_pass = [line.split(':') for line in response.text.splitlines()]
    for suffix,hass_count in hashed_pass:
        # print(len(suffix))
        if(suffix == foot ):
            return int(hass_count)
        else:
            return 0
    
    
  


# def check_password(hash_pass):
#     match_pass = pwnedpasswords.range(hash_pass['head'])

    
  
    # for i,counts in match_pass.items():
        # print(f"{i} - {hash_pass['foot']}")
        # if( counts>0):
        #     if(hash_pass['full'] == i ):
        #         print(f"{count}")
        #     else:
        #         print("0")

       
      
    # print(match_pass[hash_pass['full']])
    # return match_pass.join(',')


# def pass

if __name__ == "__main__":
    get_password(sys.argv[1:])