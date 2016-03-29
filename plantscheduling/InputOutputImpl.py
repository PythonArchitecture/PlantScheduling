from plantscheduling.JsonImpl import JsonImpl
from plantscheduling.PickleImpl import PickleImpl
from plantscheduling.Plant import Plant
from plantscheduling.YAMLImpl import YAMLImpl
from io import StringIO

import pickle
import unittest
import ast


class InOutImpl(unittest.TestCase):

    jsonTest = JsonImpl()
    pickleTest = PickleImpl()
    yamlTest = YAMLImpl()

    listTest = []
    plant = Plant('a', 'a', 'a', 'a', 'a')
    listTest.append(plant)
    temp = pickleTest.turnToDict(listTest)

    def testJson(self):
        """Testing implementation of JSON serialization
        by comparing with correctly formed JSON-file"""
        self.jsonTest.writeJson('testfiles/testJson.json', 'w', self.listTest)
        with open('testfiles/testJson.json', 'r') as out:
            textToTest = StringIO(out.read()).getvalue()
        with open('testfiles/correctJson.json', 'r') as out:
            textCorrect = StringIO(out.read()).getvalue()
        self.assertEqual(textToTest, textCorrect)

    def testPickle(self):
        """Testing implementation of Pickle serialization
        by comparing with correctly formed Pickle-file"""
        self.pickleTest.writePickle('testfiles/testPickle.p', 'wb', self.listTest)
        with open('testfiles/testPickle.p', 'rb') as out:
            encodedTest = pickle.load(out)
        with open('testfiles/encodedPickle.txt', 'r') as out:
            textCorrect = ast.literal_eval(StringIO(out.read()).getvalue())
        self.assertEqual(encodedTest, textCorrect)

    def testYaml(self):
        """Testing implementation of YAML serialization
        by comparing with correctly formed YAML-file"""
        self.yamlTest.writeYAML('testfiles/testYaml.yaml', 'w', self.listTest)
        with open('testfiles/testYaml.yaml', 'r') as out:
            textToTest = StringIO(out.read()).getvalue()
            print(textToTest)
        with open('testfiles/correctYaml.yaml', 'r') as out:
            textCorrect = StringIO(out.read()).getvalue()
            print(textCorrect)
        self.assertEqual(textToTest, textCorrect)
