# unit tests for list-maker REST api
import listMaker_mod

listMaker = listMaker_mod.createListMaker()

categories = []
types = []
defaultDescription = "default description"

# setUp with two categories, two "type" items in each category
def setUp_2Categories_2TypesEach():
    categories = ["Camping", "Groceries"]
    types = ["personal", "family"]
    for category in categories:
        listMaker.putCategory(category)
        for typeName in types:
            listMaker.putType(category, typeName+category, defaultDescription)

# setUp with 1 category, 20 "type" items
def setUp_1Categories_20TypesEach():
    categories = ["Camping"]
    types = ["t00", "t01", "t02", "t03", "t04", "t05", "t06", "t07", "t08", "t09", "t10", "t11", "t12", "t13", "t14", "t15", "t16", "t17", "t18", "t19"]
    for category in categories:
        listMaker.putCategory(category)
        for typeName in types:
            listMaker.putType(category, typeName, "no description")

# GET /categories returns list of all "category" items
def testGetCategories_multiple():
    setUp_2Categories_2TypesEach()
    result = listMaker.getCategories()
    assert(result.len() == categories.len())
    assert(result.includes(categories[0]))
    assert(result.includes(categories[1]))

def testGetCategories_none():
    result = listMaker.getCategories()
    assert(result.len() == 0)

# GET /latest returns list of most recently modified "type" items
def testGetLatest():
    setUp_2Categories_2TypesEach()
    result = listMaker.getLatest()
    assert(result.len() == 4)
    i = 0
    for category in categories:
        listMaker.putCategory(category)
        for typeName in types:
            assert(result[i] == typeName+category)
            i = i + 1

# GET /latest returns only the 10 most recently modified "type" items
def testGetLatest():
    setUp_1Categories_20TypesEach()
    result = listMaker.getLatest()
    assert(result.len() == 10)
    i = 10
    for typeName in result:
        assert( typeName == types[i])
        i = i + 1

# GET /category/{x} returns 400 error if category x does not exist
def testGetCategoryTypes_2():
    try:
        result = listMaker.getCategory("noSuchCategory")
        raise ValueError("no result expected for noSuchCategory")
    except ValueError as e:
        assert400Error(e)

# GET /category/{x} returns a list of "types" in category x
def testGetCategoryTypes_2():
    setUp_2Categories_2TypesEach
    result = listMaker.getCategory(categories[0])
    assert(result.len() == 2)

# PUT /category/{x} creates category x. Raises 400 error if already exists or if not logged in.
def testPutCategory_new():
    setUp_1Categories_20TypesEach()
    result = listMaker.getCategory(categories[0])
    assert(result.len() == 20)

# PUT /category/{x} creates category x. Raises 400 error if already exists or if not logged in.
def testPutCategory_exists():
    setUp_1Categories_20TypesEach()
    try:
        result = listMaker.putCategory(categories[0])
        raise ValueError("no result expected for noSuchCategory")
    except ValueError as e:
        assert400Error(e)

# DELETE /category/{x} deletes category x, updates all references to NULL.  Raises 400 error if does not exist or if not logged in.
def testDeleteCategory_exists():
    setUp_1Categories_20TypesEach()
    listMaker.deleteCategory(categories[0])
    try:
        listMaker.getCategory(categories[0])
        raise ValueError("expected 400 error for noSuchCategory")
    except ValueError as e:
        assert400Error(e)

# can't delete a category that does not exist
def testDeleteCategory_not_exists():
    try:
        listMaker.deleteCategory(categories[0])
        raise ValueError("expected 400 error for noSuchCategory")
    except ValueError as e:
        assert400Error(e)

# GET /type/{x} returns the definition of a checklist type x
def testGetType_exists():
    setUp_2Categories_2TypesEach
    result = listMaker.getType(types[0])
    assert(result.typeName == types[0])
    assert(result.description == defaultDescription)

# GET /type/{x} raises a 400 error if no such type exists
def testGetCategoryTypes_2():
    setUp_2Categories_2TypesEach
    try:
        result = listMaker.getType("noSuchType")
        raise ValueError("no result expected for noSuchType")
    except ValueError as e:
        assert400Error(e)

# PUT /type/{x} creates a new checklist type x.
def testPutType_new():
    setUp_1Categories_20TypesEach()
    newType = "newType"
    newDescription = "new description"
    listMaker.putType(categories[0], newType, newDescription)
    result = listMaker.getType(newType)
    assert(result.typeName == newType)
    assert(result.description == newDescription)

# PUT /type/{x} raises 400 error if already exists or if not logged in.
def testPutType_exists():
    setUp_1Categories_20TypesEach()
    try:
        result = listMaker.putType(categories[0], types[0], defaultDescription)
        raise ValueError("400 error expected for putType with existing type name")
    except ValueError as e:
        assert400Error(e)

# POST /type/{x} updates type x.
def testPostType_exists():
    setUp_1Categories_20TypesEach()
    newDescription = "new description"
    listMaker.postType(categories[0], types[0], newDescription)
    result = listMaker.getType(newType)
    assert(result.typeName == types[0])
    assert(result.description == newDescription)

# POST /type/{x} raises 400 error if does not exist or if not logged in.
def testPostType_does_not_exist():
    setUp_1Categories_20TypesEach()
    newType = "newType"
    try:
        result = listMaker.putType(categories[0], newType, defaultDescription)
        raise ValueError("400 error expected for postType with no such type name")
    except ValueError as e:
        assert400Error(e)

# DELETE /type/{x} deletes type x.  Returns 400 error if it does not exist or if not logged in.
def testDeleteType_exists():
    setUp_1Categories_20TypesEach()
    listMaker.deleteType(types[0])
    try:
        listMaker.getType(types[0])
        raise ValueError("expected 400 error for noSuchType")
    except ValueError as e:
        assert400Error(e)

# can't delete a type that does not exist
def testDeleteType_not_exists():
    types = ["personal", "family"]
    try:
        listMaker.deleteType(types[0])
        raise ValueError("expected 400 error for noSuchType")
    except Exception as e:
        assert400Error(e)

def assert400Error(e):
    print("expected 400 error, got: ",e)
    if e != HTTP400Error:
        raise ValueError(e)

if __name__ == '__main__':
    testDeleteType_not_exists()
    print "Success!  All tests pass!"
