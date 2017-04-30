import hashlib

passwd = '123'
sha1 = hashlib.sha1()
sha1.update(passwd.encode('utf-8'))
print('passwd-sha1ed:', passwd)
print('pw:', sha1.hexdigest())
