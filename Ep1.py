import random
dado1 =random.randint(1,6)
dado2 = random.randint(1,6)
soma = dado1 + dado2 
a = input('Você quer apostar ? ')
fichas = 100
while fichas>0:
    if a == 'sim':
        b = input('que tipo de apostar voce quer fazer?')
        if b=='line bet':
            c=int(input('Quantas fichas voce quer apostar ?'))
            fichas= (fichas - c)
            if soma==7 or soma==11:
                print ('voce ganhou ' + str(c) + ' fichas')
                fichas = fichas+(2*c)
            elif soma==2 or soma==3 or soma==12:
                print ('voce perdeu '+ str(c) +' fichas')
                fichas = fichas - c
            else:
                print('você está entrando na fase points')
                dado3= random.randint(1,6)
                dado4=random.randint(1,6)
                soma2=dado3+dado4
                if soma2==soma:
                    print('você ganhou'+ str(2*c)+ 'fichas')
                    fichas = fichas +(2*c)
                elif soma2==7:
                    print ('você perdeu'+ str(c)+ 'ficha')
                    fichas=fichas-c
                else: 
                    print('você vai permanecer na fase points')
                    x=input('Que tipo de aposta você quer fazer ? ')
                    if x=='fields':
                        h=int(input('Quanto você quer apostar ? '))
                        fichas = fichas - h
                        if soma2==2:
                            print('Você ganhou' + str(3*h) +'fichas')
                            fichas= fichas+(3*h)
                        elif soma==12:
                            print ('você ganhou' + str(4*h)+ 'fichas')
                        elif soma==5 or soma==6 or soma==7 or soma==8:
                            print ('você perdeu' + str(h)+ 'fichas')
                        else:
                            print ('você ganhou '+ str(2*h)+ 'fichas')
                            fichas= fichas+(2*h)
                    elif x=='any crops':
                        j=int(input('quanto você quer apostar ? '))
                        fichas = fichas - j
                        if soma2==2 or soma2==3 or soma2==7:
                            print('você ganhou '+ str(7*j)+ 'fichas')
                            fichas= fichas + (7*j)
                        else:
                            print('você perdeu '+ str(j)+ 'fichas')
                    elif x=='twelve':
                        r=int(input('Quanto você quer apostar ?  '))
                        if soma2==12:
                            print ('Você ganhou' + str(12*r)+ 'fichas')
                        else:
                            print ('Você perdeu' + str(r)+ 'fichas')
        elif b=='fields':
            e= int(input('Quanto você quer apostar ? '))
            fichas=fichas-e
            if soma == 2:
                print("você ganhou" + str(5*e) + "fichas")
                fichas=fichas+(4*e)
            elif soma == 12:
                print ('você ganhou' + str(3*e)+ ' fichas')
                fichas=fichas+(3*e)
            elif soma == 5 or soma==6 or soma==7 or soma==8:
                print ("você perdeu "+ str(e) + " fichas")
            else:
                print ('você ganhou ' + str(2*e) + 'fichas')
                fichas = fichas+(2*e)
        elif b=='any crops':
            f=int(input('Quanto você quer apostar ?'))
            fichas = fichas - f 
            if soma==2 or soma==3 or soma==7:
                print ('você ganhou' + str(7*f)+ ' fichas')
                fichas = fichas + (7*f)
            else:
                print ('você perdeu ' + str(f) + ' moedas')