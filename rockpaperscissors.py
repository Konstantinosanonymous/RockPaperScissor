import random
rounds=int(input('Δώσε το Πληθος τον Γύρων: '))
pwin=0
cwin=0
choices=['Πέτρα','Ψαλίδι','Χαρτί']
if rounds==0:
    print('Pls Give A Number Up To 0' )
else:
    for i in range(rounds):
        print('Game',i+1,'o',end=' ')
        player=int(input('Πέτρα(0),Ψαλίδι(1),Χαρτί(2): '))
        pc=random.randint(0, 2)
        print('Ο αντίπαλος είχε: ',choices[pc],end='.')
        if player==pc:
            print('Ισοπαλία')
        elif (player==0 and pc==1)\
            or (player==1 and pc==2)\
            or (player==2 and pc==0):
            pwin+=1
            print('You Won')
        else:
            cwin+=1
            print('You Lost')
    print('Κέρδισες',pwin,'Παιχνίδια...')
    if pwin==cwin:

        print('και ηρθατε ισοπαλια')
    elif pwin>cwin:
        print('Είσαι ο Νικητής')
    else:
        print('αλλά έχασες')
