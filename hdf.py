def hdf():
    while 1:
        s = input('请输入规格：')
        a,b,c,d = s.split('-')
        if float(a) < 6:
            e = (1.82 * float(b) + 0.16) * (1.82 * float(c) + 0.16) + (1.82 * float(c)+0.16) / 2
            print(round(e,2))
        if a == '6':
            e = (1.82 * float(b) + 0.16) * (1.82 * float(c) + 0.16)*2 + (1.82 * float(c)+0.16) / 2 + (1.82 * float(c)+0.16) + int(d)*4.69
            print(round(e,2))
hdf()
