import sys
input = [1000]
for line in sys.stdin:
    input.append(line.rstrip().split(' '))
allValid = "true"
errorCodes = []
for i in input:
    if i == "false":
        allValid = "false"
    if i[1] == "false":
        errorCodes.append(i[2])

if allValid == "true":
    print("yes")
else:
    print("No")
    print(','.join(i for i in errorCodes))

