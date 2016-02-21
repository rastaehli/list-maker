import category
import list_item

# Store is responsible for persisting checklist types:
class Store():

    # create a ListTypeStore with a database to persist types.
    def __init__(self, database):
        self.db = database
        self.categories = category.Store(self.db)
        self.listItems = list_item.Store(self.db)

    def deleteAll(self):
        """Remove all the type records from the database."""
        self.listItems.deleteAll()
        self.db.execute("DELETE FROM list_type;", ())

    def delete(self, type):
        """Remove all the records for type includeing list entries."""
        self.db.execute("DELETE FROM LIST_ENTRY e WHERE e.list=%s; DELETE FROM list_type t WHERE t.id=%s;", 
            (type.id, type.id))

    def add(self, name, category, description, listItems):
        newType = ListType( None, name, category, description, listItems)
        newType.id = self.db.insert("list_type", "%s, %s, %s",
            (newType.name, newType.category.id, newType.description))
        for item in newType.items:
            self.db.execute("INSERT INTO list_entry values (%s, %s);",
                (newType.id, item.name))
        return newType

    def getAll(self):
        rows = self.db.fetchAll(
            "SELECT id, name, category, description FROM list_type;", ())
        types = []
        for row in rows:
            listId = row[0]
            catId = row[2]
            category = self.categories.getCategory(catId)
            items = self.listItems.getItems(listId)
            aType = ListType(listId, row[1], category, row[3], items)
            types.append(aType)
        return types

    def getLatest(self):
        rows = self.db.fetchAll(
            "SELECT id, name, category, description FROM list_type ORDER BY id LIMIT 10;", ())
        types = []
        for row in rows:
            listId = row[0]
            catId = row[2]
            category = self.categories.getCategory(catId)
            items = self.listItems.getItems(listId)
            aType = ListType(listId, row[1], category, row[3], items)
            types.append(aType)
        return types

# ListType is responsible for modelling a checklist type:
#  - description only, not one you can actually check items off
#  - creating, reading, updating list items in this type
#  - categorizing this type
class ListType():

    # create a ListType
    def __init__(self, rowId, name, category, description, items):
        self.id = rowId
        self.name = name
        self.category = category
        self.description = description
        self.items = items



