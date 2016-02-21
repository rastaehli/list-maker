# lm_rest_service.py
# this module is responsible for handling RESTful requests
# intended for the list_maker application.
# For the most part is just delegates to the list_maker, translating
# between the flask.py REST requests and regular python object 
# invocations/exceptions.

import flask

@app.route('/')
    return 'This is the REST interface to list_maker: (add api docs here)'

def mustBeLoggedIn():
	if not session.get('logged_in'):
		abort(401)


@app.route('/categories', methods=['GET'])
def getCategories():
	mustBeLoggedIn()
	catList = service.getCategories()
	return renderJson(catList)

# GET /categories returns list of all "category" items
# GET /latest returns the 10 most recently modified "type" items
# GET /category/{x} returns a list of "types" in category x
# PUT /category/{x} creates category x.
# DELETE /category/{x} deletes category x, updates all references to NULL.  Raises 400 error if does not exist or if not logged in.
# GET /type/{x} returns the definition of a checklist type x
# PUT /type/{x} creates a new checklist type x.
# POST /type/{x} updates type x.
# DELETE /type/{x} deletes type x.  Returns 400 error if it does not exist or if not logged in.
