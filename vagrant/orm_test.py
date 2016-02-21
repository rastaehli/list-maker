from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from orm import Category, ListType, ListItem

# set db connection info
engine = create_engine('postgresql+psycopg2:///list_maker')
# bind Obj-Relational Mapping in "orm" module to this database
#Base.metadata.bind = engine
# get DB session for this database
Session = sessionmaker(bind=engine)
session = Session()

def getAll(c):
    return session.query(c).all()

def getFirst(c):
    return getAll(c)[0]

def deleteAll():
    for type in session.query(ListType):
        session.delete(type)
    session.commit
    for cat in session.query(Category):
        session.delete(cat)
    session.commit
    print('delete all tested ok')
    # print('ListType count: ', session.query(ListType).count())
    # print('ListItem count: ', session.query(ListItem).count())
    # print('Category count: ', session.query(Category).count())

def createCategory():
    deleteAll()
    cat = Category('Groceries','lists of regular food and staples purchaces')
    session.add(cat)
    session.commit()
    allCategories = getAll(Category)
    assert(len(allCategories) == 1)
    assert(allCategories[0].name == 'Groceries')
    print('create category tested ok')
    # print('categories = ', allCategories)

def updateCategory():
    createCategory()
    oldCat = getFirst(Category)
    oldCat.description = 'updated description'
    session.commit()
    updated = getFirst(Category)
    assert(updated.description == 'updated description')
    print('update category tested ok')

def deleteCategory():
    createCategory()
    cat = getFirst(Category)
    session.delete(cat)
    session.commit()
    assert(len(getAll(Category)) == 0)
    print('delete category tested ok')

def createListType():
    createCategory()
    typ = ListType('Staples', getFirst(Category).name, 'things we need to buy every week')
    session.add(typ)
    session.commit()
    all = getAll(ListType)
    assert(len(all) == 1)
    assert(all[0].name == 'Staples')
    print('create list type tested ok')

def updateListType():
    createListType()
    oldType = getFirst(ListType)
    oldType.description = 'updated description'
    session.commit()
    updated = getFirst(ListType)
    assert(updated.description == 'updated description')
    print('update ListType tested ok')

def deleteListType():
    createListType()
    session.delete(getFirst(ListType))
    session.commit()
    assert(len(getAll(ListType)) == 0)
    print('delete ListType tested ok')

def createListItem():
    createListType()
    typ = getFirst(ListType)
    typ.items = [ 
        ListItem('bread','for sandwiches'),
        ListItem('milk', 'for breakfast cereal'),
        ListItem('eggs', 'for breakfast'),
        ListItem('detergent', 'for laundry') ]
    session.commit()
    assert(len(getAll(ListItem)) == 4)
    assert(getFirst(ListItem).list.name == 'Staples')
    print('createListItem tested ok')

def updateListItem():
    createListItem()
    old = getFirst(ListType)
    for i in old.items:
        if i.name == 'bread':
            i.description = 'updated'
    session.commit()
    updated = getFirst(ListType)
    for i in old.items:
        if i.name == 'bread':
            assert(i.description == 'updated')
        else:
            assert(i.description != 'updated')
    print('updateListItem tested ok')

def deleteListItem():
    createListItem()
    session.delete(getFirst(ListType))
    session.commit()
    assert(len(getAll(ListItem)) == 0)
    print('deleteListItem tested ok')

deleteAll()
createCategory()
updateCategory()
deleteCategory()
createListType()
updateListType()
deleteListType()
createListItem()
updateListItem()
deleteListItem()
