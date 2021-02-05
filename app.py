print('salom mening ismim ZEUS, istalgan savolingizni bering')
def reload():
    
    a = input('')
    salom = ['salom', 'Salom', 'assalom']
    ism = ['ismingiz nima', 'isming nima', 'sani isming nima', 'seni isming nima', 'isming', 'ismin', 'kimsan?', 'sen kimsan?']


    if(a in salom and a in salom[0]):
        print('Salom alekum')
    elif(a in salom and a in salom[2]):
        print('Valekum assalom')
    elif(a in salom and a in salom[1]):
        print('Assalomu alekum')
    elif(a in salom):
        print('Assalomu alekum')
    elif(a in ism):
        print('Mening ismim ZEUS, sizning ismingiz nima?')
        name = input('')
        print('tanishganimdan hursandman',name)
    else:
        print('men sizni tushunmadim')


while True:
    reload()
