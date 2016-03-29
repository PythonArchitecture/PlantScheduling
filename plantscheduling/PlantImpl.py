from plantscheduling.Plant import Plant


class PlantImpl:
    actionlist = []

    @staticmethod
    def newEvent(name, type, actiontype, date, time):
        """Creating a new instance of Plant defining all the
        information needed to be performed in th schedule.

        >>> pl = PlantImpl()
        >>> pl.newEvent("Lilly", "a", "s", "q", "q")
        >>> len(pl.actionlist) == 1
        True
        >>> pl.newEvent("Lilly", "1", "2", "3", "4")
        This plant is already in the list
        >>> len(pl.actionlist) == 1
        True
        """
        newAction = Plant(name, type, actiontype, date, time)
        for action in PlantImpl.actionlist:
            if newAction.name == action.name:
                print("This plant is already in the list")
                return None
        PlantImpl.actionlist.append(newAction)

    @staticmethod
    def deleteEvent(name):
        """Deleting an alredy existing instance of Plant
        using field _name as a key.

        >>> pl = PlantImpl()
        >>> pl.newEvent("Lilly", "a", "s", "q", "q")
        >>> pl.deleteEvent("L")
        No match.
        >>> pl.deleteEvent("Lilly")
        >>> len(pl.actionlist) == 0
        True
        """
        for action in PlantImpl.actionlist:
            if action.name == name:
                PlantImpl.actionlist.remove(action)
                break
            else:
                print("No match.")
                break

    @staticmethod
    def displayTable():
        """Display the schedule as set of ASCII symbols in console.

        >>> pl = PlantImpl()
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
        for action in PlantImpl.actionlist:
            row = []
            row.append(action.name)
            row.append(action.type)
            row.append(action.actiontype)
            row.append(action.date)
            row.append(action.time)
            table_data.append(row)
        return table_data
