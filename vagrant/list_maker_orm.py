#!/usr/bin/env python
# 
# list-maker.py -- Database implementation of check-list management system.
#

from lm_orm import ListType, Category
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# ListMaker is responsible for creating and managing list types:
#  - creating, reading, updating and deleting list types
#  - categorizing those types; creating/reading/updating/deleting categories
class ListMaker():

    # create a ListMaker with a database to persist the categories and list types
    def __init__(self):
        self.engine = create_engine('postgresql+psycopg2:///list_maker')
 
    def deleteType(self, type):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        self.listTypes.delete(type)

    def deleteCategory(self, category):
        self.categories.delete(category.name)

    def deleteAll(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        session.query(ListType).filter().delete()
        session.query(Category).filter().delete()
        session.commit

    def addCategory(self, name):
        return self.categories.add(name)

    def getCategories(self):
        return self.categories.getAll()

    def addListType(self, name, category, description, listEntries):
        return self.listTypes.add(name, category, description, listEntries)

    def getLatest(self):
        return self.listTypes.getLatest()


