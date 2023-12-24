nome = str(input('digite o nome do heroi:'))
xp = float(input('digite a quantidade de xp, para saber seu elo: '))
if xp <=1000:
    print('O Herói de nome {} está no nível de Ferro'.format(nome))
elif xp >= 1001 and xp <= 2000:
    print('O Herói de nome {} está no nível de Bronze'.format(nome))
elif xp >=2001 and xp <=5000:
    print('O Herói de nome {} está no nível de Prata'.format(nome))
elif xp >=5001 and xp <=7000:
    print('O Herói de nome {} está no nível de Ouro'.format(nome))
elif xp >=7001 and xp <=8000:
    print('O Herói de nome {} está no nível de Platina'.format(nome))
elif xp >=8001 and xp <=9000:
    print('O Herói de nome {} está no nível de Ascendente'.format(nome))
elif xp >=9001 and xp <=10000:
    print('O Herói de nome {} está no nível de Imortal'.format(nome))
else:
    print('O Herói de nome {} está no nível de Radiante'.format(nome))





