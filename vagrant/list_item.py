#!/usr/bin/env python


# Store is responsible for persisting checklist entries:
class Store():

    # create a Store with a database to persist list entries.
    def __init__(self, database):
        self.db = database

    def deleteAll(self):
        """Remove all the my records from the database."""
        self.db.execute("DELETE FROM list_entry;", ())

    # return all items with this list id
    def getItems(self, listId):
        rows = self.db.fetchAll(
            "SELECT name FROM list_entry WHERE list=%s;", (listId, ))
        items = []
        for row in rows:
            items.append(ListItem(row[0]))
        return items

# ListItem is responsible for modelling a checklist entry:
#  - description only, you don't actually have a checkbox for this description
class ListItem():

    def __init__(self, name):
        self.name = name


