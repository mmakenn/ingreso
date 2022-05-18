import simple

TEST_LIST = simple.generateListOfDicts()
ORDERED_LIST = simple.orderMyListOfDicts(TEST_LIST)

ages = []
for item in TEST_LIST:
    ages.append(item["edad"])

max = max(ages)
min = min(ages)
maxFromMyTestedMethod = ORDERED_LIST[-1]["edad"]
minFromMyTestedMethod = ORDERED_LIST[0]["edad"]

testMax = (max == maxFromMyTestedMethod)
print("Testeando edad maxima del diccionario original coincide con edad maxima de la lista ordenada: " + str(testMax))
testMin = (min == minFromMyTestedMethod)
print("Testeando edad minima del diccionario original coincide con edad maxima de la lista ordenada: " + str(testMin))

orderedAges = ages.copy()
orderedAges.sort()

testOrder = True
i = 0
while (testOrder and i < len(ages)):
    if not (orderedAges[i] == ORDERED_LIST[i]["edad"]):
        testOrder = False
    i = i + 1

print("Testeando que el diccionario sea correctamente ordenado: " + str(testOrder))

print("Test finalizado.")
if (testMax and testMin and testOrder):
    print("Resultado: OK")
else:
    print("Resultado: ERROR")