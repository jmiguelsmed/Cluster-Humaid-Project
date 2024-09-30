from Volunteer import Volunteer

class Cluster(object):
    """
    Cluster of examples
    """

    def __init__(self, examples):
        """
        Constructor
        Requires:
        examples is a list of objects of a type that has
        a method returning the list of features of an object and
        a method returning the distance among them;
        Ensures:
        object of type Cluster is created
        """
        self._examples = examples
        self._centroid = self.computeCentroid()

    def update(self, examples):
        """
        Update the cluster with a given collection of examples
        Requires:
        examples a list of objects of the type of members in self._examples
        Ensures:
        examples = getExamples();
        returns how much the centroid has changed
        """
        oldCentroid = self._centroid
        self._examples = examples
        if len(examples) > 0:
            self._centroid = self.computeCentroid()
            return oldCentroid.distance(self._centroid)
        else:
            return 0.0

    def computeCentroid(self):
        """
        Compute centroid of the cluster
        Ensures:
        centroid of the cluster
        """
        dim = self._examples[0].dimensionality()
        totVals = [0] * dim
        for e in self._examples:
            for i in range(dim):
                totVals[i] = totVals[i] + int(e.getFeatures()[i]) #e.getFeatures é str, passei para int.
        totValsAveraged = []
        for i in range(dim):
            totValsAveraged.append(totVals[i] / float(len(self._examples)))
        centroid = Volunteer('centroid', totValsAveraged)
        return centroid

    def getExamples(self):
        """
        Examples in the cluster
        Ensures:
        list with examples in the cluster
        """
        return self._examples

    def getCentroid(self):
        """
        Centroid of the cluster
        Ensures:
        centroid of the cluster
        """
        return self._centroid

    def size(self):
        """
        Size of the cluster
        Ensures:
        number of examples in cluster
        """
        return len(self._examples)

    def variability(self):
        """
        Variability
        Ensures:
        variance of the cluster
        """
        totDist = 0.0
        for e in self._examples:
            #print(e.distance(self._centroid))
            totDist += (e.distance(self._centroid)) ** 2
            #print(totDist)
        return totDist

    def members(self):
        """
        Generator method
        """
        for e in self._examples:
            yield e


    def getExemplar(self):
        val = True
        min = self._examples[0].distance(self._centroid)
        for e in self._examples:
            if e.distance(self._centroid) < min:
                d = str(e)
                min = e.distance(self._centroid)
                val = False
        if val:
            return str(self._examples[0])
        else:
            return d

    def __eq__(self, other):
        return self.getExamples() == other.getExamples() and\
            self.getCentroid() == other.getCentroid()

    def __lt__(self, other):
        return len(self.getExamples()) < len(other.getExamples())

    def __str__(self):
        """
        string representation in the form
        "Cluster with centroid [...] contains:
         ex1 ex2 ... exN "
        """
        names = []
        for e in self._examples:
            names.append(e.getName())
        # names.sort()
        result = 'Cluster with centroid ' \
                 + str(self._centroid.getFeatures()) + ' contains:\n'
        for e in names:
            result = result + e + ', '
        return result[:-2]  # remove trailing comma and space
