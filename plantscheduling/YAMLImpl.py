from plantscheduling.PlantImpl import PlantImpl

import yaml

from plantscheduling.SerializeFile import SerializeFile


class YAMLImpl(SerializeFile):

    @staticmethod
    def writeYAML(fileName, accessKey, list):
        """Implementing YAML-serialization using
         yaml library"""
        dictionaryTable = YAMLImpl.turnToDict(list)
        try:
            with open(fileName, accessKey) as outfile:
                dumpYaml = yaml.dump(dictionaryTable, default_flow_style=False)
                outfile.write(dumpYaml)
        except yaml.YAMLError:
            print('Oops, something went wrong with YAML')
