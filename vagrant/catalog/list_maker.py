#!/usr/bin/env python
# 
# list-maker.py -- Database implementation of check-list management system.
#

import category
import list_type
import list_item

def createListMaker():
    return ListMaker("noSuchDatabase")

# ListMaker is responsible for creating and managing list types:
#  - creating, reading, updating and deleting list types
#  - categorizing those types; creating/reading/updating/deleting categories
class ListMaker():

    # create a ListMaker with a database to persist the categories and list types
    def __init__(self, database):
        self.database = database
        self.categories = category.Store(database)  # persistent store for categories
        self.listTypes = list_type.Store(database) # persistent store for types
        self.listItems = list_item.Store(database) # persistent store for items

    def deleteType(self, name):
        self.listTypes.delete(name)

    def deleteCategory(self, name):
        self.categories.delete(name)

    def deleteItem(self, name):
        self.listItems.delete(name)

    def deleteAll(self):
        self.categories.deleteAll()
        self.listTypes.deleteAll()
        self.listItems.deleteAll()

