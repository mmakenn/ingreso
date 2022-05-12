from string import Template
from random import randint

""" Tamaño de la matriz --> MxN (filas x columnas) """
M = 5
N = 5

""" Numeros consecutivos a considerar """
V = 4

""" Limites superior e inferior del dominio de enteros comprendidos en la matrix """
MAXVALUE = 0
MINVALUE = 10

FOUND_MESSAGE = Template("Numeros consecutivos desde ${inicio} hasta ${fin}")

matrix = []
for row in range(M):
    rowValues = []
    for column in range(N):
        x = randint(MAXVALUE, MINVALUE)
        rowValues.append(x)
    matrix.append(rowValues)

def searchConsecutive(list):
    previousElement = list[0]
    if (len(list) > 1):
        for element in list[1:]:
            nextCalculated = previousElement + 1
            if (nextCalculated != element):
                return False
            previousElement = element
    return True

foundConsecutive = []
for row in range(M):
    for initialColumn in range(N-V+1):
        finalColumn = initialColumn + V
        rowConsecutive = searchConsecutive(matrix[row][initialColumn:finalColumn])
        if (rowConsecutive):
            inicialPosition = "Fil" + str(row) + " Col" + str(initialColumn)
            finalPosition = "Fil" + str(row) + " Col" + str(finalColumn)
            foundConsecutive.append( (inicialPosition, finalPosition) )

for column in range(N):
    for initialRow in range(M-V+1):
        finalRow = initialRow + V
        columnValues = []
        for row in range(initialRow, finalRow):
            columnValues.append(matrix[row][column])
        columnConsecutive = searchConsecutive(columnValues)
        if (columnConsecutive):
            inicialPosition = "Fil" +str(initialRow) + " Col" + str(column)
            finalPosition = "Fil" + str(finalRow) + " Col" + str(column)
            foundConsecutive.append( (inicialPosition, finalPosition) )

if (len(foundConsecutive) > 0):
    for found in foundConsecutive:
        print(FOUND_MESSAGE.substitute(inicio = found[0], fin = found[1]))
else:
    print("No se encontraron valores consecutivos.")
