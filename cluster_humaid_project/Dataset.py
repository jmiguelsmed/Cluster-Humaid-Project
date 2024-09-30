# 2021-2022 Programação II
# Grupo 114
# 58607 José Medeiros
# 58559 Madalena Machado

from Volunteer import Volunteer

class Dataset:
    """
    Reads both files, stores the information.
    """
    def __init__(self, skillsFile, helpersFile):
        """
        Creates a vector

        Requires: skillsFile, skills, is a text file with similar structure to the one
        indicated in the quiz, where each

        Ensures: Stores information from the files on the respective attributes.
        """
        self._skillsFile = skillsFile
        self._helpersFile = helpersFile
        self._centroids = []
        self._helpers = []
        self._features = []
        self._volunteersLines = []
        self.readFiles()

    def getFeatures(self):
        return self._features

    def getSkillsFile(self):
        return self._skillsFile

    def getHelpersFile(self):
        return self._helpersFile

    def getCentroids(self):
        return self._centroids

    def getvolunteersLines(self):
        return self._volunteersLines

    def getHelpers(self):
        return self._helpers

    def setSkillsFile(self,newS):
        self._skillsFile = newS

    def setHelpersFile(self,newH):
        self._helpersFile = newH

    def setCentroids(self, newC):
        self._centroids = newC

    def setHelpers(self, newH):
        self._helpers = newH

    def setFeatures(self, newF):
        self._features = newF

    def setVolunteersLines(self, newV):
        self._volunteersLines = newV

    def createList(self, skills, volunteer):
        objectList = []
        for i in range(len(volunteer)):
            line = volunteer[i].split("; ")
            name = ''
            vector = []
            for x in range(len(line)):
                if self._features[x] == "#Name":
                    name = line[x]
                elif line[x] in skills[self._features[x]]:
                    value = skills[self._features[x]][line[x]]
                    vector.append(value)
                else:
                    value = skills[self._features[x]]["others"]
                    vector.append(value)
            if vector != []:
                objectList.append(Volunteer(name, vector))

        return objectList

    def readFiles(self):
        inFile = open(self._skillsFile, 'r')
        inData = inFile.read()
        inData = inData.splitlines()
        mainDict = {}

        for i in inData[1:]:
            featLines = i.split("; ")

            if featLines[0][0] == "#":
                feat = featLines[1]
                mainDict[feat] = {}
            else:
                mainDict[feat][featLines[1]] = featLines[0]

        inFile2 = open(self._helpersFile, 'r')
        inData2 = inFile2.read()
        inData2 = inData2.splitlines()
        hIndex = inData2.index("#Helpers:")
        eIndex = inData2.index("#Exemplars:")
        nIndex = inData2.index("#Name and features:")
        allHelpers = inData2[hIndex + 1: eIndex] + inData2[eIndex + 1:]
        feature = " ".join(inData2[nIndex + 1:hIndex]).split("; ")

        self._features = feature
        self._helpers = self.createList(mainDict, allHelpers)
        self._centroids = self.createList(mainDict, inData2[eIndex + 1:])
        self._volunteersLines = allHelpers

    def __str__(self):
        helpersList = []
        for helper in self.getHelpers():
            helpersList.append(str(helper))

        return "Helpers:{}".format(helpersList)

    def __eq__(self, other):
        return self.getHelpersFile() == other.getHellpersFile() and \
               self.getSkillsFile() == other.getSkillsFile()

    def __lt__(self, other):
        return len(self.getvolunteersLines()) < len(other.getvolunteersLines())
