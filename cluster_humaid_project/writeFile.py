from Dataset import Dataset
from makeClusters import trykmeans 

def writeFile(dataset, trykmeans):
    a = dataset
    c = trykmeans
    str = ""
    h = a.getvolunteersLines()
    v = 1
    for e in c:
        ex = e.getExemplar()
        for i in h:
            if i!= "void" and i[0:(i.index(";"))] == ex[0:(ex.index(":"))]:
                str += "#examplar " + "{}".format(v) + ":\n" + i + "\n"
        str += "#cluster " + "{}".format(v) + ":\n"
        for e in e.getExamples():
            n = e.getName()
            for e in h:
                if e!= "void" and e[0:(e.index(";"))] == n and \
                    e[0:(e.index(";"))] != ex[0:(ex.index(":"))]:
                    str += e + "\n"
        v += 1
    f = open("helpersClustered.txt", "w")
    f.write(str)


# fiz assim: "{}".format(v) pq n funcionou com str(v)