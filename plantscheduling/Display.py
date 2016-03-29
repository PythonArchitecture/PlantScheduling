import collections
import configparser
import sys
import os.path

from terminaltables import AsciiTable
from plantscheduling.JsonImpl import JsonImpl
from plantscheduling.PickleImpl import PickleImpl
from plantscheduling.PlantImpl import PlantImpl
from plantscheduling.YAMLImpl import YAMLImpl

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


class Display:

    config = configparser.ConfigParser()
    config.read('serialization.cfg')
    serializationType = config['Current Method']['id']

    menu = {}
    menu['1'] = "Add Plant."
    menu['2'] = "Delete Plant."
    menu['3'] = "Show Timetable."
    menu['4'] = "Serialize in preferable way"
    menu['5'] = "Exit."

    def displayMenu(self, inputfunc=input):
        """View implementation,
        that creates a simple menu in console.
        """
        sortedmenu = collections.OrderedDict(sorted(self.menu.items()))
        for entry in sortedmenu:
            print(entry, self.menu[entry])
        while True:
                selection = inputfunc("Please Select:")
                if selection == '1':

                    name = input("Enter name of the plant: ")
                    type = input("Enter type of the plant: ")
                    actiontype = input("Enter type of the watering: ")
                    date = input("Enter date of the watering: ")
                    time = input("Enter time of the watering: ")

                    PlantImpl.newEvent(name, type, actiontype, date, time)

                elif selection == '2':

                    name = input("Enter name of the plant to be deleted: ")

                    PlantImpl.deleteEvent(name)

                elif selection == '3':

                    table = AsciiTable(PlantImpl.displayTable())
                    print(table.table)

                elif selection == '4':

                    if self.serializationType == '1':
                        JsonImpl().writeJson('data.json', 'w', PlantImpl.actionlist)
                        print('Saved to JSON')
                    elif self.serializationType == '2':
                        PickleImpl().writePickle('data.p', 'wb', PlantImpl.actionlist)
                        print('Saved to Pickle')
                    elif self.serializationType == '3':
                        YAMLImpl().writeYAML('data.yaml', 'w', PlantImpl.actionlist)
                        print('Saved to YAML')
                    else:
                        print("Oops, something wrong with configuration file.")

                elif selection == '5':
                    break
                else:
                    print("Unknown Option Selected!")

if __name__ == "__main__":
    disp = Display()
    disp.displayMenu()
