#!/usr/bin/env python


# Store is responsible for persisting checklist items:
class Store():

    # create a ListItem with a database to persist it.
    def __init__(self, database):
        self.db = database

    def deleteAll(self):
        """Remove all the my records from the database."""
        self.db.execute("DELETE FROM list_item;", ())


# ListItem is responsible for modelling a checklist item:
#  - description only, you don't actually have a checkbox for this description
class ListItem():

    def __init__(self, name, description):
        self.name = name
        self.description = description


