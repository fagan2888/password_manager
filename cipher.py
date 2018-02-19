from pyDes import triple_des, PAD_PKCS5


def encrypt_password(password_dict):
    des = triple_des(_fill_key(password_dict['key']), padmode=PAD_PKCS5)
    password_dict['password'] = des.encrypt(password_dict['password'])
    return password_dict


def _fill_key(key):
    if len(key) > 16:
        return key[:16]
    elif len(key) < 16:
        missing = 16 - len(key)
        add = 'a' * missing
        return key + add
    else:
        return key


def decrypt_password(password_dict, key):
    des = triple_des(_fill_key(key), padmode=PAD_PKCS5)
    password_dict['password'] = des.decrypt(password_dict['password']).decode('utf8')
    return password_dict
