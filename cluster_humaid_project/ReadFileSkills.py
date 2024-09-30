inFile = open("skills.txt", 'r')
inData = inFile.read()
inData = inData.splitlines()
c = []
fullList = []
ind = []
for i in inData[1:]:
    a = i.split("; ")
    c.append(a)
i = 0
while i in range(0,len(c)):
    d = {}
    while i < len(c) and c[i][0][0] != "#":
        d[c[i][1]] = c[i][0]
        i += 1
    if d != {}:
        fullList.append(d)
    i += 1

print(fullList)   
        





#é preciso ter a classe example
inFile2 = open("helpersArrived2.txt", 'r')
inData2 = inFile2.read()
inData2 = inData2.splitlines()
h = inData2.index("#Helpers:")
e = inData2.index("#Exemplars:")
print(inData2)
print(inData2[h + 1 : e] + inData2[e + 1 :])
inData2 = inData2[h + 1 : e] + inData2[e + 1 :]
print(" \n")
objectList = []
voluntariosList = []
for i in range(0, len(inData2)-1):
    line = inData2[i].split("; ")
    name = line[0]
    line = line[1:]
    # print(line)
    # d1 = fullList[4]
    # print(d1[line[4]])
    vector = []
    # print(len(fullList))
    for i in range(len(fullList)):
        if line[i] in fullList[i]:
            vector.append(fullList[i][line[i]])
        else:
            # print("dicionário: ",fullList[i])
            # print("info: ", line[i])
            vector.append(fullList[i]["others"])
        # print("vetor: ", vector)
    voluntariosList.append(name)
    voluntariosList.append(vector)
    objectList.append(Example(name,vector))
# print(objectList)
# print(voluntariosList)
# print(len(voluntariosList)/2)








class ReadSkills():

    def __init__(self, file):
        self._file = file
        self._skillList = self.createList()

    def createList(self):
        inFile = open(self._file, 'r')
        inData = inFile.read()
        inData = inData.splitlines()
        c = []
        fullList = []
        ind = []
        for i in inData[1:]:
            a = i.split("; ")
            c.append(a)
        i = 0
        while i in range(0,len(c)):
            d = {}
            while i < len(c) and c[i][0][0] != "#":
                d[c[i][1]] = c[i][0]
                i += 1
            if d != {}:
                fullList.append(d)
            i += 1
        return fullList

    def getSkill(self):
        return self._skillList

    def __str__(self):
        return str(self.getSkill())





class ReadVolunteer():
    def __init__(self, file):
        self._file = file
        self._volList = self.createList()
    
    def createList(self):
        inFile2 = open(self._file, 'r')
        inData2 = inFile2.read()
        inData2 = inData2.splitlines()
        h = inData2.index("#Helpers:")
        e = inData2.index("#Exemplars:")
        inData2 = inData2[h + 1 : e] + inData2[e + 1 :]        
        return inData2

    def getVolList(self):
        return self._volList

    def __str__(self):
        return str(self.getVolList())
        

class VolunteerList():

    def __init__(self, dictList, volunteerList):
        """ """
        self._dictList = dictList
        self._volunteerList = volunteerList
        self._objectList = self.CreateList()

    def CreateList(self):
        fullList = self._dictList
        inData2 = self._volunteerList
        objectList = []
        voluntariosList = []
        for i in range(0, len(inData2)-1):
            line = inData2[i].split("; ")
            name = line[0]
            line = line[1:]
            vector = []
            for i in range(len(fullList)):
                if line[i] in fullList[i]:
                    vector.append(fullList[i][line[i]])
                else:
                    vector.append(fullList[i]["others"])
            voluntariosList.append(name)
            voluntariosList.append(vector)
            # print(name)
            # print(vector)
            objectList.append(Example(name,vector))
            # print(str(Example(name,vector)))
        return objectList
    
    def getObjectList(self):
        return self._objectList

    def __str__(self):
        l = []
        for e in self.getObjectList():
            l.append(str(e))
        return str(l)
                
a = ReadVolunteer("helpersArrived2.txt")
b = ReadSkills("skills.txt")
c = VolunteerList(b.createList(),a.createList())
print(c)
