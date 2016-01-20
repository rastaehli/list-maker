# Store is responsible for persisting checklist types:
class Store():

    # create a ListTypeStore with a database to persist types.
    def __init__(self, database):
        self.db = database

    def deleteAll(self):
        """Remove all the my records from the database."""
        self.db.execute("DELETE FROM list_type;", ())

# ListType is responsible for modelling a checklist type:
#  - description only, not one you can actually check items off
#  - creating, reading, updating list items in this type
#  - categorizing this type
class ListType():

    # create a ListType
    def __init__(self, name, category, items):
        self.name = name
        self.category = category
        self.items = items



