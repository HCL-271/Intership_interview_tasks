import sys
l1 = input()
l1 = l1.split()
#ints = [eval(x) for x in l1]
#print(ints)
#list(map(int, l1))

N = l1[0]
M = l1[1]
#print(l1)
N = int(N)
arr = [0]*N
for i in range(0, int(M)):
  schet = input()
  schet = schet.split()
  l = input()
  l = l.split()
  diff = int(schet[0]) - int(schet[1])
  #print(diff)
  if (diff > 0):
    for j in range(5):
      index = int(l[j])
      #print(l[j])
      arr[index]+= diff
  else:
    for j in range(5, 10):
      index = int(l[j])
      #print(int(l[j])) 
      arr[index]-= diff

min = arr[0]
count = 0
for i in range(N):
  if (arr[i]>min):
    count+=1


print(count)    
