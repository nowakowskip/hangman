#hangman

def logo():
    a = "888"                                                           
    b = "888"                                                           
    c = "888"                                                           
    d = "88888b.  8888b. 88888b.  .d88b. 88888b.d88b.  8888b. 88888b."  
    e = '888 "88b    "88b888 "88bd88P"88b888 "888 "88b    "88b888 "88b' 
    f = "888  888.d888888888  888888  888888  888  888.d888888888  888" 
    g = "888  888888  888888  888Y88b 888888  888  888888  888888  888" 
    h = '888  888"Y888888888  888 "Y88888888  888  888"Y888888888  888' 
    i = "                             888"                              
    j = "                        Y8b d88P"                              
    k = '                         "Y88P"'                              
    lista = (a,b,c,d,e,f,g,h,i,j,k)
    
    for i in lista:
        print (i)

slowo = "hangman".upper()
import os
result = []
for i in range(len(slowo)):
    result.append("_")
    
ile = 1

def rysowanie(litera):
    #funkcja zapisuje pojedyńczą literę
    pustalista = []
    for i in slowo:
        if i == litera:
            pustalista.append(i)
        else:
            pustalista.append("_")
    return (pustalista)

def rysowanie2(lista):
    #funkcja zapisuje całość
    for i in lista:
        if i.isalpha():
            indexy =[index for index, value in enumerate(lista) if value == i]
            for j in indexy:
                result[j] = i
    return result

def ile_zostalo(lista):
    #funkcja liczy ile zostało do odganięcia
    ile = 0
    for i in lista:
        if i == "_":
            ile += 1
    return ile

def calosc(lista):
    #funkcja ładnie wypisuje listę
    for i in lista:
        print (i, " ", end="")

def zgadnij_slowo(zgd):
    if zgd == slowo:
        return True
    else:
        return False

os.system('clear') #czyszczenie konsoli
logo()
print ("Spróbuj odgadnąć literę lub całe słowo, wielkość liter nie ma znaczenia")
print ("Let's play a game!")
print ("")
while ile != 0:
    strzal = input("Litera lub słowo: ").upper() #zgadywanie litery
    if len(strzal) > 1:
        if zgadnij_slowo(strzal) == True:
            break
    wynik = rysowanie2(rysowanie(strzal))
    os.system('clear') #czyszczenie konsoli
    logo()
    calosc(wynik) #ładne wypisywanie
    print ("")
    ile = ile_zostalo(wynik)
print ("Wygrałeś!")

