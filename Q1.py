def Max(arr):
    max = arr[0]
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max

def Min(arr):
    min = arr[0]
    for i in range(len(arr)):
        if arr[i] < min:
            min = arr[i]
    return min

def largestfromL(arr):
    return Max(arr)

def largestfromS(arr):
    return Min(arr)


#Assume that you will input line one by one
#No time cannot finish it 

print("l1?")
l1 = input()
print("l2?")
l2 = input().split(" ")
print("l3?")
l3 = input()
print("l4?")
l4 = input().split(" ")

if l1< l3 :
    print("NO")
    exit()
l2dict = {"S":[],"M":[],"L":[]}
for i in l2:
    if i[-1] == "L":
        l2dict["L"].append(i)
    if i[-1] == "M":
        l2dict["M"].append(i)
    if i[-1] == "S":
        l2dict["S"].append(i)

l4dict = {"S":[],"M":[],"L":[]}
for i in l4:
    if i[-1] == "L":
        l4dict["L"].append(i)
    if i[-1] == "M":
        l4dict["M"].append(i)
    if i[-1] == "S":
        l4dict["S"].append(i)

a = 1

for i in l2dict:
    i = sorted(i, key=len)
for i in l4dict:
    i = sorted(i, key=len)


for i in l4dict:
    for j in i:
        if j in l2dict[j[-1]]:
            #exact size
            l2dict[j[-1]].pop(j)
        elif len(j) < Max(l2dict[j[-1]]):
            # No suitable size
            print("No")
            exit()
        elif len(j) > Max(l2dict[j[-1]]):
            print("Yes")

