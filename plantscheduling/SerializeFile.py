class SerializeFile:

    @staticmethod
    def turnToDict(actionlist):
        """Creating a dictionary out of
        generified list to use regular
        methods for serialization"""
        dictionaryList = []
        dictionaryTable = {'plants': dictionaryList}
        for plant in actionlist:
            tempDictionary = {'name': plant.name,
                              'type': plant.type,
                              'actiontype': plant.actiontype,
                              'date': plant.date,
                              'time': plant.time}
            sorted(tempDictionary.keys())
            dictionaryList.append(tempDictionary)
        return dictionaryTable
