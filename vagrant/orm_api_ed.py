from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()


class RestCall(Base):

    def __init__(self, method, path, description, exampleRequest, exampleResponse):
        self.method = method
        self.path = path
        self.description = description
        self.exampleRequest = exampleRequest
        self.exampleResponse = exampleResponse

    __tablename__ = 'rest_call'

    id = Column(Integer, primary_key=True)
    method = Column(String(8))
    path = Column(String(64))
    description = Column(String(512))
    exampleRequest = Column(String(512))
    exampleResponse = Column(String(512))

    parameters = relationship("Parameter",
    	back_populates='restCall',
    	cascade="all, delete, delete-orphan")

    def __repr__(self):
        return "<RestCall(method='%s', path='%s')>" % (
            self.method, self.path)

class Parameter(Base):

    def __init__(self, aRestCall, type, name, range, description):
    	self.restCall = aRestCall
        self.type = type
        self.name = name
        self.range = range
        self.description = description

    __tablename__ = 'parameter'

    id = Column(Integer, primary_key=True)
    restCallId = Column(Integer, ForeignKey('rest_call.id'))
    restCall = relationship(RestCall, back_populates='parameters')
    type = Column(String(32), ForeignKey('parameter_type.name'))
    name = Column(String(32))
    range = Column(String(64))
    description = Column(String(256))

    def __repr__(self):
        return "<Parameter(type='%s', name='%s', range='%s')>" % (
            self.type, self.name, self.range)

class ParameterType(Base):

    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    __tablename__ = 'parameter_type'

    name = Column(String(64), primary_key=True)
    description = Column(String(256))

    def __repr__(self):
        return "<ParameterType(name='%s', description='%s')>" % (
            self.name, self.description)

db_connection_info = 'postgresql+psycopg2:///api_ed_db'

if __name__ == '__main__':
    engine = create_engine(db_connection_info)
    Base.metadata.create_all(engine)
