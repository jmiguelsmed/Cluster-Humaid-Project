#2021-2022 Programação II
#Grupo 114
#58607 José Medeiros
#58559 Madalena Machado

from minkowskiDist import minkowskiDist

class Volunteer(object):
    """
    Example for clustering
    """

    def __init__(self, name, features):
        """
        Constructor
        Requires:
        name is string;
        features is list of numbers representing the feature vector;
        label is string with the label of the example
        Ensures:
        object of type Example created
        """
        self._name = name
        self._features = features


    def dimensionality(self):
        """
        Dimensionality of the feature vector
        Ensures:
        dimensionality of the feature vector
        """
        return len(self._features)


    def setName(self, name):
        """
        Name setting
        Ensures:
        self._name = name
        """
        self._name = name

        
    def setFeatures(self, features):
        """
        Features setting
        Ensures:
        self._features = features
        """
        self._features = features
        

    def setLabel(self, label):
        """
        Label setting
        Ensures:
        self._label = label
        """
        self._label = label

    
    def getFeatures(self):
        """
        Features
        Ensures:
        feature vector
        """
        return self._features[:] #passei para int, mas nao daqui o problema


    def getLabel(self):
        """
        Object label
        Ensures:
        object label
        """
        return self._label


    def getName(self):
        """
        Object Name
        Ensures:
        object name
        """
        return self._name


    def distance(self, other):
        """
        Euclidean distance wrt a given example
        Requires:
        other is an example
        Ensures:
        the Euclidean distance between feature vectors
        of self and other
        """
        return minkowskiDist(self._features, other.getFeatures(), 2)


    def __str__(self):
        """
        String representation
        Ensures:
        string representation in the form "name:features:label"
        """
        return self._name + ':' + str(self._features)

    def __lt__(self, other):
        soma1 = 0
        soma2 = 0
        for e in self.getFeatures():
            soma1 += int(e)
        for e in other.getFeatures():
            soma2 += int(e)
        return soma1 < soma2

    def __eq__(self, other):
        return self.getFeatures() == other.getFeatures()
