hora = 12
humor = 'sono'
if hora < 12 and humor == 'sono':
    print('Bom dia, hora de acordar!')
elif hora >= 12 and humor == 'sono':
    print('Boa tarde, hora de acordar!')
else:
    print('Você não está com sono.')

if humor == 'sono' or hora <= 8:
    print('café')