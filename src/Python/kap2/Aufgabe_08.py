import random

print('Willkommen im Tippspiel (Glückspiel kann süchtig machen...)')

z = random.randint(0,9)
tippRichtig = False
trys = 0;

while tippRichtig == False and trys < 3:
    trys = trys + 1
    tipp = int(input('geben sie einen Tipp ab!'))

    if (tipp == z):
        tippRichtig = True
    elif (trys < 3):
        if (tipp > z):
            print('Leider falsch, die Zahl ist kleiner!')
        else:
            print('Leider falsch, die Zahl ist größer!')


if (tippRichtig == True):
    print('Herzlichen Glückwunsch, die Zahl war richtig, trotzdem bekommst du nix')
else:
    print('Deine Tipps waren alle Falsch, die Zahl war ', z)