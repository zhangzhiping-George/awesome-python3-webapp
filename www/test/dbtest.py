import orm, asyncio
from models import User, Blog, Comment

loop = asyncio.get_event_loop()

@asyncio.coroutine
def test():
    yield from orm.create_pool(loop=loop, user='www-data', host='localhost', password='www-data', database='awesome',unix_socket="/var/run/mysqld/mysqld.sock")
    u = User(id =1, name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
    yield from u.save()

for x in test():
    #print('x in test(): %s' %x)
    pass
