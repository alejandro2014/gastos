import json

class JsonConverter:
    def __init__(self):
        self.csvBasePath = './gastos/csv'
        self.jsonbasePath = './gastos/json'

    def csvToJson(self, month):
        fileLines = self.readFileLines(self.csvBasePath + '/' + month + '.csv')
        result = list(map(lambda l: self.getConceptObject(l), fileLines))
        self.writeJsonFile(self.jsonbasePath + '/' + month + '.json', result)

    def getConceptObject(self, conceptCsv):
        conceptSplit = conceptCsv.strip().split("\t")

        return {
            'date': conceptSplit[0],
            'ingCategory': conceptSplit[1],
            'ingSubCategory': conceptSplit[2],
            'message': conceptSplit[3],
            'price': float(conceptSplit[5].translate({ord(','): ''}))
        }

    def readFileLines(self, path):
        file = open(path, 'r')
        fileLines = file.readlines()
        file.close()

        return fileLines

    def writeJsonFile(self, path, jsonInfo):
        outputFile = open(path, 'w')
        outputFile.write(json.dumps(jsonInfo))
        outputFile.close()

jsonConverter = JsonConverter()

jsonConverter.csvToJson('1909')
jsonConverter.csvToJson('1910')
jsonConverter.csvToJson('1911')
jsonConverter.csvToJson('2001')
jsonConverter.csvToJson('2002')
jsonConverter.csvToJson('2003')
jsonConverter.csvToJson('2004')
jsonConverter.csvToJson('2005')
jsonConverter.csvToJson('2006')
jsonConverter.csvToJson('2007')
jsonConverter.csvToJson('2008')
