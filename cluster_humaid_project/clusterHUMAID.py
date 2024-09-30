from Dataset import Dataset
from makeClusters import trykmeans 
from writeFile import writeFile

def clusterHUMAID(k, skillsFile, hellpersArrivedFile):
    a = Dataset(skillsFile,hellpersArrivedFile)
    c = trykmeans(a.getHelpers(),a.getCentroids(),k,True)
    writeFile(a,c)


clusterHUMAID(2, "skills4.txt","helpersArrived4.txt")