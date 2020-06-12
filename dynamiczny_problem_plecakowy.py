from pathlib import Path
def backpack(ilosc, pojemnosc, waga_koszt):
    matrix = [[0 for col in range(pojemnosc + 1)] for row in range(ilosc)]

    for row in range(len(waga_koszt)):
        for col in range(pojemnosc + 1):
            if waga_koszt[row][0] > col:
                matrix[row][col] = matrix[row - 1][col] 
            else:
                matrix[row][col] = max(matrix[row - 1][col],matrix[row - 1][col - waga_koszt[row][0]] + waga_koszt[row][1])

    #print(matrix)




    j =pojemnosc
    best_ulozenie = [0] * ilosc
    for i in range(len(waga_koszt)-1, -1, -1):  # sprawdzamy od końc(prawy dolny róg macierzy kosztów)
        if i == 0 and matrix[i][j] != 0:
            best_ulozenie[i]=1
        if matrix[i][j] != matrix[i - 1][j]:
            best_ulozenie[i] = 1
            j -= waga_koszt[i][0]
    return matrix[ilosc-1][pojemnosc],best_ulozenie




# ilosc = 6
# pojemnosc = 8
# waga = [2,1,4,1,4,3]
# koszt = [7,4,5,1,4,9]
# w_k = []
# w_k = list(map(lambda x, y:(x,y), waga, koszt))

# pojemnosc = ''
#
# while pojemnosc.isdigit() == False:
#     pojemnosc = input("podaj pojemność plecaka")
#
# pojemnosc = int(pojemnosc)
#
# ilosc = ''
#
# while ilosc.isdigit() == False:
#     ilosc = input("podaj ilosc elementów")
#
# ilosc = int(ilosc)
#
# waga_koszt = []
# i=0
# while i < ilosc:
#     waga = input("podaj wage {} elementu ".format(i + 1))
#     koszt = input("podaj koszt {} elementu ".format(i + 1))
#     if waga.isdigit() and koszt.isdigit():
#         waga_koszt.append(tuple([int(waga),int(koszt)]))
#         i = i + 1
#     else:
#         print("Podane dane sa nieprawidlowe, wprowadz ponownie")


#print(waga_koszt)



mypath = Path("dane.txt")
czy_pusty = mypath.stat().st_size
if(czy_pusty == 0):
    print("Plik jest pusty")

else:
    ilosc = 0
    with open('dane.txt') as f:
        first_line = f.readline()
        ilosc_pojemnosc = first_line.split()
        if ilosc_pojemnosc[1].isdigit() and ilosc_pojemnosc[0].isdigit():
            if int(ilosc_pojemnosc[0])>0 and int(ilosc_pojemnosc[1])>0:
                ilosc = int(ilosc_pojemnosc[0])
                pojemnosc = int(ilosc_pojemnosc[1])
            else:
                print("Tylko wieksze od zera")
        else:
            print("Mozna wprowadzic tylko cyfry")






    waga_koszt = []
    licznik = 0
    with open("dane.txt", 'r') as f:

        for i, x in enumerate(f):
            il = x.split()
            il = len(il)
            if il != 2:
                print("niepoprawnie wprowadzone dane z pliku!")
                break
            if 1 <= i:
                wartosci = x.split()
                if wartosci[1].isdigit() and wartosci[0].isdigit():
                    waga=0
                    koszt=0
                    if int(wartosci[0])>0 and int(wartosci[1])>0:
                        waga = int(wartosci[0])
                        koszt = int(wartosci[1])
                        licznik += 1
                        waga_koszt.append(tuple([waga, koszt]))
                    else:
                        print("Wartości musza być większe od 0")
                else:
                    print("Można wprowadzać tylko cyfry")
                    break


    if ilosc != licznik:
        print("Dane w pliku są niepoprawne")

    else:
        print(backpack(ilosc,pojemnosc,waga_koszt))


