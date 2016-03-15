from plantscheduling.Plant import Plant


class PlantServiceImpl:
    actionlist = []

    def newEvent(self, name, type, actiontype, date, time):
        """Creating a new instance of Plant defining all the
        information needed to be performed in th schedule.

        >>> pl = PlantServiceImpl()
        >>> pl.newEvent("Lilly", "a", "s", "q", "q")
        >>> len(pl.actionlist) == 1
        True
        >>> pl.newEvent("Lilly", "1", "2", "3", "4")
        This plant is already in the list
        >>> len(pl.actionlist) == 1
        True
        """
        newAction = Plant(name, type, actiontype, date, time)
        for action in self.actionlist:
            if newAction.name == action.name:
                print("This plant is already in the list")
                return None
        self.actionlist.append(newAction)

    def deleteEvent(self, name):
        """Deleting an alredy existing instance of Plant
        using field _name as a key.

        >>> pl = PlantServiceImpl()
        >>> pl.newEvent("Lilly", "a", "s", "q", "q")
        >>> pl.deleteEvent("L")
        No match.
        >>> pl.deleteEvent("Lilly")
        >>> len(pl.actionlist) == 0
        True
        """
        for action in self.actionlist:
            if action.name == name:
                self.actionlist.remove(action)
                break
            else:
                print("No match.")
                break

    def displayTable(self):
        """Display the schedule as set of ASCII symbols in console.

        >>> pl = PlantServiceImpl()
        >>> table = pl.displayTable()
        >>> len(table) == 1
        True
        >>> pl.newEvent("Lilly", "a", "s", "q", "q")
        >>> table = pl.displayTable()
        >>> len(table) == 2
        True
        >>> pl.deleteEvent("Lilly")
        >>> table = pl.displayTable()
        >>> len(table) == 1
        True
        """

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
