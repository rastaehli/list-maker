#!/usr/bin/env python
# 
# list-maker-test.py -- test Database implementation of check-list management system.
#

import db
import list_maker
import list_type
import list_item

# init database access objects
myDb = db.DB("list_maker")
lm = list_maker.ListMaker(myDb)

def testDeleteAll():
    lm.deleteAll()
    print "Test: records can be deleted."

def setupEmpty():
    lm.deleteAll()

def testAddCategory():
    setupEmpty()
    lm.addCategory("Shopping")
    categories = lm.getCategories()
    if len(categories) != 1:
        raise ValueError(
            "After adding one categorie, getCategories() length should be 1.")
    print "Test: adding one category works as expected."

def setupOneListType():
    setupEmpty()
    testCategory = lm.addCategory("Shopping")
    description = "Test List type"
    items = []
    items.append(list_item.ListItem("Milk"))
    items.append(list_item.ListItem("Bread"))
    typeId = lm.addListType("Weekly Groceries", testCategory, description, items)

def testAddListType():
    setupEmpty()
    context = "testAddListType"
    testName = "Weekly Groceries"
    testCategory = lm.addCategory("Shopping")
    description = "Test List type"
    items = []
    items.append(list_item.ListItem("Milk"))
    items.append(list_item.ListItem("Bread"))
    typeId = lm.addListType(testName, testCategory, description, items)
    types = lm.listTypes.getAll()
    assertExpected(context+":listTypes.getAll returns 1", 1, len(types))
    type = types[0]
    assertExpected(context+":name", testName, type.name)
    assertExpected(context+":category", testCategory.name, type.category.name)
    assertExpected(context+":description", description, type.description)
    assertExpected(context+":entries count", len(items), len(type.items))
    assertExpected(context+":entries[1]", items[1].name, type.items[1].name)
    print "Test: adding one list type works as expected."

def testGetLatest_none():
    setupEmpty()
    types = lm.getLatest()
    context = "testGetLatest_none"
    assertExpected(context, len(types), 0)

def testGetLatest_one():
    setupOneListType()
    types = lm.getLatest()
    context = "testGetLatest_one"
    assertExpected(context, len(types), 1)

def testGetLatest_max():
    setupOneListType()
    prototype = lm.listTypes.getAll()[0]
    lm.addListType("name01",prototype.category, prototype.description, prototype.items)
    lm.addListType("name02",prototype.category, prototype.description, prototype.items)
    lm.addListType("name03",prototype.category, prototype.description, prototype.items)
    lm.addListType("name04",prototype.category, prototype.description, prototype.items)
    lm.addListType("name05",prototype.category, prototype.description, prototype.items)
    lm.addListType("name06",prototype.category, prototype.description, prototype.items)
    lm.addListType("name07",prototype.category, prototype.description, prototype.items)
    lm.addListType("name08",prototype.category, prototype.description, prototype.items)
    lm.addListType("name09",prototype.category, prototype.description, prototype.items)
    lm.addListType("name10",prototype.category, prototype.description, prototype.items)
    lm.addListType("name11",prototype.category, prototype.description, prototype.items)
    types = lm.getLatest()
    context = "testGetLatest_max"
    assertExpected(context, 10, len(types))

def assertNotNone(context, result):
    if result == None:
        raise ValueError(context+ " result is None.")

def assertExpected(context, expected, actual):
    if expected != actual:
        raise ValueError('In {} expected: {} actual: {}'.format(context, expected, actual))

if __name__ == '__main__':
    testDeleteAll()
    testAddCategory()
    testAddListType()
    testGetLatest_none()
    testGetLatest_one()
    testGetLatest_max()

    print "Success!  All tests pass!"

