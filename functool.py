from flask import request
from model import session, User
import hashlib


def is_logined():
    user_account = request.cookies.get('account')
    checksum=request.cookies.get('checksum')
    if user_account and checksum:
        user=session.query(User).filter_by(account=account).first()
        if checksum == user.checksum:
            return True
        else:
            return False
    else:
        return False
        
def is_log():
    user_account = request.cookies.get('account')
    print(user_account)
    checksum=request.cookies.get('checksum')
    print(checksum)
    if user_account and checksum:
        if checksum==hashlib.md5(user_account.encode()).hexdigest():
            print('True')
            return True
        else:
            print('False')
            return False
    else:
        return False
    
