mainList = [1, 2, 2, 3, 4, 4, 5, 5, 6, 7, 7, 8, 9, 10, 10]
provList = []
for i in mainList:
    if i not in provList:
        provList.append(i)

mainList = provList
print(mainList)