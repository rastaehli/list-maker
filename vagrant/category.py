# Store is responsible for persisting checklist categories:
class Store():

    # create a CategoryStore with a database to persist types.
    def __init__(self, database):
        self.db = database

    def deleteAll(self):
        """Remove all the my records from the database."""
        self.db.execute("DELETE FROM category;", ())

    def getAll(self):
        rows = self.db.fetchAll(
            "SELECT id, name FROM category;", ())
        categories = []
        for row in rows:
            categories.append(Category(row[0], row[1]))
        return categories

    def getCategory(self, catId):
        rows = self.db.fetchAll(
            "SELECT id, name FROM category WHERE id=%s;", (catId, ))
        if len(rows) != 1:
            raise ValueError("Expected one category with id=%s, found: %s", catId, len(rows))
        return Category(rows[0][0], rows[0][1])

    def add(self, name):
        newCat = Category(None, name)  # set id from db insert
    	newCat.id = self.db.insert("category", "%s",
                        (newCat.name, ))
        return newCat

# Category is responsible for modelling a checklist category:
#  - name of the category
class Category():

    # create a Category
    def __init__(self, catId, name):
        self.id = catId
        self.name = name
