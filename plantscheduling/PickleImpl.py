from plantscheduling.PlantImpl import PlantImpl
from plantscheduling.SerializeFile import SerializeFile

import pickle


class PickleImpl(SerializeFile):

    @staticmethod
    def writePickle(fileName, accessKey, list):
        """Implementing Pickle serialization using
         standart Pickle library"""
        dictionaryTable = PickleImpl.turnToDict(list)
        try:
            pickle.dump(dictionaryTable, open(fileName, accessKey))
        except pickle.PicklingError:
            print('Oops, something went wrong with Pickle')
