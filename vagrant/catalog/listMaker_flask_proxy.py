def createListMaker():
	return ListMaker("noSuchDatabase")

# ListMaker is responsible for creating and managing list types:
#  - creating, reading, updating and deleting list types
#  - categorizing those types; creating/reading/updating/deleting categories
class ListMaker():

	# create a ListMaker with a database to persist the categories and list types
    def __init__(self, database):
        self.database = database

    def deleteType(self, name):
    	print("deleting type", name)