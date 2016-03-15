from plantscheduling.Plant import Plant


class PlantServiceImpl:
    actionlist = []

    def newEvent(self, name, type, actiontype, date, time):
        newAction = Plant(name, type, actiontype, date, time)
        for action in self.actionlist:
            if newAction.name == action.name:
                print("This plant is in the list.")
                return None
        self.actionlist.append(newAction)

    def deleteEvent(self, name):
        for action in self.actionlist:
            if action.name == name:
                self.actionlist.remove(action)
                break
            else:
                print("No match - try again.")

    def displayTable(self):
        table_data = [['Name', 'Type', 'Action', 'Date', 'Time']]
        for action in self.actionlist:
            row = []
            row.append(action.name)
            row.append(action.type)
            row.append(action.actiontype)
            row.append(action.date)
            row.append(action.time)
            table_data.append(row)
        return table_data
