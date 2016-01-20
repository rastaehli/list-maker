#!/usr/bin/env python
# 
# list-maker-test.py -- test Database implementation of check-list management system.
#

import db
import list_maker

# init database access objects
myDb = db.DB("list_maker_db")
lm = list_maker.ListMaker(myDb)

def testDeleteAll():
    lm.deleteAll()
    print "records can be deleted."



if __name__ == '__main__':
    testDeleteAll()
    testAddCategory()
    testAddListType()
    testGetListTypes()
    testGetLatest()
    print "Success!  All tests pass!"

