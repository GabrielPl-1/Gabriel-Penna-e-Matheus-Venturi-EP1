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