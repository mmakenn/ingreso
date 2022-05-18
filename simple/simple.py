from string import Template
from random import randint

ELEMENTS = 10
AGE_RANGE = (0, 100)
MESSAGE = Template("La persona con ID: ${id} es la más ${status}.")

def generateListOfDicts():
    list = []
    for i in range(ELEMENTS):
        age = randint(AGE_RANGE[0], AGE_RANGE[1])
        dic = {"id": i, "edad": age}
        list.append(dic)
    return list

def compareAges(orderedList, age):
    """ Funcion auxiliar """
    for i in range(len(orderedList)):
        ageFromOrderItem = orderedList[i]["edad"]
        if (age < ageFromOrderItem):
            return i
        
    return len(orderedList)

def orderMyListOfDicts(list):
    orderedList = list[:1]
    
    for dic in list[1:]:
        ageToEvaluate = dic["edad"]
        newIndex = compareAges(orderedList, ageToEvaluate)
        orderedList.insert(newIndex, dic)
    
    youngerId = orderedList[0]["id"]
    olderId = orderedList[-1]["id"]

    print(MESSAGE.substitute(id = youngerId, status = "joven"))
    print(MESSAGE.substitute(id = olderId, status = "vieja"))
    
    return orderedList