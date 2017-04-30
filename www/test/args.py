def f(a, b, c=1, *args, d, **kw):
    print(a, b, 'c=', c, 'args:', args, d, 'kw:', kw)

f(1,2, 3, 4, 5, d=6, e='e', f='f')
