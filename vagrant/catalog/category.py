# Store is responsible for persisting checklist categories:
class Store():

    # create a CategoryStore with a database to persist types.
    def __init__(self, database):
        self.db = database

    def deleteAll(self):
        """Remove all the my records from the database."""
        self.db.execute("DELETE FROM category;", ())

# Category is responsible for modelling a checklist category:
#  - name of the category
class Category():

    # create a Category
    def __init__(self, name):
        self.name = name
