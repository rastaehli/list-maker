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
        self.listTypes = list_type.Store(database, ) # persistent store for types
 
    def deleteType(self, type):
        self.listTypes.delete(type)

    def deleteCategory(self, category):
        self.categories.delete(category.name)

    def deleteAll(self):
        self.listTypes.deleteAll()
        self.categories.deleteAll()

    def addCategory(self, name):
        return self.categories.add(name)

    def getCategories(self):
        return self.categories.getAll()

    def addListType(self, name, category, description, listEntries):
        return self.listTypes.add(name, category, description, listEntries)

    def getLatest(self):
        return self.listTypes.getLatest()


