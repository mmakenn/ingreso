from string import Template
from random import randint

MESSAGE = Template("La persona con ID: ${id} es la más ${status}.")

def generateListOfDicts():
    list = []
    for i in range(10):
        age = randint(0, 100)
        dic = {"id": i, "edad": age}
        list.append(dic)
    return list

def compareAges(orderedList, age):
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

list = generateListOfDicts()
orderMyListOfDicts(list)