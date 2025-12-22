lista = [("name", "Elie"), ("job", "Instructor")]
dic = {}
for key, value in lista:
    dic[key] = value
print (dic)

lista1 = ["CA", "NJ", "RI"]
lista2 = ["California", "New Jersey", "Rhode Island"]
iniciales = {}
for key, value in zip(lista1, lista2):
    iniciales[key] = value
print(iniciales)

vocales = ["a", "e", "i", "o", "u"]
vocaless = {}
for vocal in vocales: 
    vocaless[vocal] = 0
print (vocaless)

alfabeto = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
lettnum = {}
for index, lett in enumerate(alfabeto):
    lettnum[index + 1] = lett
print(lettnum)

s = "awesome sauce"
vowels = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
for letter in s:
    if letter in vowels:
        vowels[letter] += 1
print (vowels)