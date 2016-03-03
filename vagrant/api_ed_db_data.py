from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from orm_api_ed import ParameterType, Parameter, RestCall, db_connection_info

# set db connection info
engine = create_engine(db_connection_info)
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
    for x in session.query(RestCall):
        session.delete(x)
    session.commit
    for x in session.query(Parameter):
        session.delete(x)
    session.commit
    for x in session.query(ParameterType):
        session.delete(x)
    session.commit

def createParameterType(name, description):
    ptype = ParameterType(name, description)
    session.add(ptype)
    session.commit()

def createRestCall(method, path, description, exampleRequest, exampleResponse):
    call = RestCall(method, path, description, exampleRequest, exampleResponse)
    session.add(call)
    session.commit()

def addParameter(restCall, type, name, range, description):
    restCall.parameters.add(
    	Parameter(restCall, type, name, range, description))
    session.add(restCall)
    session.commit()

deleteAll()
createParameterType('pathParam', 'A value that appears as part of the URL path.')
createParameterType('queryParam', 'A value that occurs in a key=value expression following a "?" at the end of the URL path.')

call = RestCall(
    'GET', '/shipments', 
	'Return a list of shipment descriptions where an associated trace string matches the "ref" value.',
	'GET /shipments?ref=5555',
	'[{"shipmentId":"J001234567", "status": "Completed"}, {"shipmentId":"K001999997", "status": "In Transit"}]')
call.parameters.append(
	Parameter(call, 'queryParam', 'ref', 'String of length 3-12 characters.', 'A (prefix of a) trace value associated with a shipment.'))
session.add(call)
session.commit()

