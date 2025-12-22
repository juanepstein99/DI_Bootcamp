List = [1, 2, 3, 4]
for num in List:
    print(num)

    List = [1, 2, 3, 4]
for num in List:
    print (num * 20)

Names = ["Elie", "Tim", "Matt"]
Letters = []
for Capletter in Names:
    Letters.append(Capletter[0])
print(Letters)

Numbers = [1, 2, 3, 4, 5, 6]
Even_numbers = []
for num in Numbers:
    if num % 2 == 0:
        Even_numbers.append(num)
print(Even_numbers)

List1 = [1, 2, 3, 4]
List2 = [3, 4, 5, 6]
Commonlist = []
for num in List1:
    if num in List2:
        Commonlist.append(num)
print(Commonlist)

Words = ["Elie", "Tim", "Matt"]
Newwords = []
for word in Words: 
    word = word.lower() 
    word = word[::-1]
    Newwords.append(word)
print  (Newwords)

primero = "frist"
tercero = "third"
Commonlett = []
for lett in primero:
    if lett in tercero:
        Commonlett.append(lett)
print (Commonlett)

Dividido12 = []
for num in range (1, 101):
    if num % 12 == 0:
        Dividido12.append(num)
print (Dividido12)

wow = "amazing"
wvowels = []
for lett in wow:
    if lett not in "aeiou":
        wvowels.append(lett)
print (wvowels)

lista = []
for num in range (3):
    interna = list(range (3))
    lista.append(interna)
print(lista)

listuki = []
for num in range (10):
    intern = list(range(10))
    listuki.append(intern)
print(listuki)