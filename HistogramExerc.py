matrizFixa = [0, 0, 4, 6, 8, 8, 4, 7, 8, 9, 9, 4, 3,2,3,8,2,2,1,0]
matrizEqual = []
hist = []
histAcul = []
pk = []
kLinha = []
n = len(matrizFixa)
l = 10
soma = 0
for x in range(l):
    hist.append(0)
    for y in matrizFixa:
        if x == y:
            hist[x] = hist[x] + 1


for a in range(len(hist)):
    soma += hist[a]
    if a == 0:
        histAcul.append(hist[a])
        pk.append(hist[a] / n)
        kLinha.append(round((l-1)*pk[a]))
    else:
        histAcul.append(soma)
        pk.append(soma / n)
        kLinha.append(round((l-1)*pk[a]))


for b in matrizFixa:
    matrizEqual.append(kLinha[b])


str1 = ' '.join(str(e) for e in matrizFixa)
str2 = ' '.join(str(e) for e in matrizEqual)


print('Inicial =', str1)
print('Final =  ', str2)
