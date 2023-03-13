lista = [2,5,2,10,4,67,23,45,54,100,10066,15,24]

while True:
    i = 0
    s = 0
    while i < len(lista) - 1:
        if lista[i] > lista[i+1]:
            lista[i], lista[i+1] = lista[i+1], lista[i]
            s = s + 1
        i = i + 1
    if(s == 0):
        break

print(lista)