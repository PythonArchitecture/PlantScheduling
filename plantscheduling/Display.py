import collections

from terminaltables import AsciiTable

from plantscheduling.PlantServiceImpl import PlantServiceImpl


class Display:

    plantservice = PlantServiceImpl()


    menu = {}
    menu['1'] = "Add Plant."
    menu['2'] = "Delete Plant."
    menu['3'] = "Show Timetable."
    menu['4'] = "Exit."

    def displayMenu(self):
        sortedmenu = collections.OrderedDict(sorted(self.menu.items()))
        for entry in sortedmenu:
            print(entry, self.menu[entry])
        while True:
                selection = input("Please Select:")
                if selection == '1':

                    name = input("Enter name of the plant: ")
                    type = input("Enter type of the plant: ")
                    actiontype = input("Enter type of the watering: ")
                    date = input("Enter date of the watering: ")
                    time = input("Enter time of the watering: ")

                    self.plantservice.newEvent(name, type, actiontype, date, time)

                elif selection == '2':

                    name = input("Enter name of the plant to be deleted: ")

                    self.plantservice.deleteEvent(name)

                elif selection == '3':

                    table = AsciiTable(self.plantservice.displayTable())
                    print(table.table)

                elif selection == '4':
                    break
                else:
                    print("Unknown Option Selected!")

if __name__ == "__main__":
    disp = Display()
    disp.displayMenu()

