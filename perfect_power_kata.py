prime = []
m = int(input())
n = int(input())
for i in range(m, n+1):
    if(i%2==1):
        prime.append(i)
print(prime)
gap = int(input())
for j in prime:
    res = j + gap
    if res in prime:
        print([j,res])
        break
    else:
        print('None')     
