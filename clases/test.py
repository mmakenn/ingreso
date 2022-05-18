import clases
from math import pi

test_circle = clases.Circulo(2)


testError1 = False
try:
    TEST_IMPOSSIBLE_CIRCLE = clases.Circulo(0)
except ValueError:
    testError1 = True
    print("Testeando imposibilidad de crear Circulo radio 0, arroja ValueError: True")

testError2 = False
try:
    TEST_IMPOSSIBLE_CIRCLE2 = clases.Circulo(-1)
except ValueError:
    testError2 = True
    print("Testeando imposibilidad de crear Circulo radio negativo, arroja ValueError: True")

testGetRadius = (test_circle.radius == 2)
print("Testeando getter del radio: " + str(testGetRadius))

test_circle.radius = 3
testSetRadius = (test_circle.radius == 3)
print("Testeando setter del radio: " + str(testSetRadius))

testError3 = False
try:
    test_circle.radius = 0
except ValueError:
    testError3 = True
    print("Testeando imposibilidad de cambiar radio del Circulo a 0, arroja ValueError: True")

testError4 = False
try:
    test_circle.radius = -1
except ValueError:
    testError4 = True
    print("Testeando imposibilidad de cambiar radio del Circulo a valor negativo, arroja ValueError: True")

testPerimeter = (test_circle.perimeter() == 2*pi*3)
print("Testeando metodo para calcular el perimetro: " + str(testPerimeter))

testArea = (test_circle.area() == pi*(3**2))
print("Testeando metodo para calcular el area: " + str(testArea))

MULTIPLY_CIRCLE = test_circle * 5
testMultiply = (MULTIPLY_CIRCLE.radius == 15)
print("Testeando multiplicacion de circulo crea uno nuevo y es correcto: " + str(testMultiply))
testMultiplyOriginalNotChange = (test_circle.radius == 3)
print("Testeando multiplicacion de circulo crea uno nuevo y el original no sufre cambios: " + str(testMultiplyOriginalNotChange))

testError5 = False
try:
    TEST_IMPOSSIBLE_MULTIPLY_CIRCLE = test_circle * -1
except ValueError:
    testError5 = True
    print("Testeando imposibilidad de multiplicar Circulo por valor negativo, arroja ValueError: True")

testError6 = False
try:
    TEST_IMPOSSIBLE_MULTIPLY_CIRCLE = test_circle * 0
except ValueError:
    testError6 = True
    print("Testeando imposibilidad de multiplicar Circulo por valor 0, arroja ValueError: True")

print("Pruebas finalizadas.")
if (testGetRadius and testSetRadius and 
    testPerimeter and testArea and 
    testError1 and testError2 and testError3 and testError4 and
    testMultiply and testMultiplyOriginalNotChange and testError5 and testError6):
    print("Resultado: OK")
else:
    print("Resultado: ERROR")