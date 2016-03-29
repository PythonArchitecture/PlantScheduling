from plantscheduling.SerializeFile import SerializeFile
from plantscheduling.PlantImpl import PlantImpl

import json


class JsonImpl(SerializeFile):

    @staticmethod
    def writeJson(fileName, accessKey, list):
        """Implementing JSON-serialization using
         standart JSON library"""
        dictionaryTable = JsonImpl.turnToDict(list)
        try:
            with open(fileName, accessKey) as outfile:
                json.dump(dictionaryTable, outfile, sort_keys=True, indent=4)
        except FileNotFoundError or IOError:
            print('Oops, something went wrong with JSON')
