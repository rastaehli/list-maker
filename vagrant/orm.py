from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()


class Category(Base):

    def __init__(self, name, description):
        self.name = name
        self.description = description

    __tablename__ = 'category'

    name = Column(String(32), primary_key=True)
    description = Column(String(256))

    def __repr__(self):
        return "<Category(name='%s', description='%s')>" % (
            self.name, self.description)

class ListType(Base):

    def __init__(self, name, category, description):
        self.name = name
        self.category = category
        self.description = description

    __tablename__ = 'list_type'

    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    description = Column(String(256))
    category = Column(String,  ForeignKey('category.name'))

    items = relationship("ListItem",
        back_populates='list',
        cascade="all, delete, delete-orphan")

    def __repr__(self):
        return "<ListType(name='%s', category='%s', description='%s')>" % (
            self.name, self.category, self.description)

class ListItem(Base):

    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    __tablename__ = 'list_item'

    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    description = Column(String(256))

    list_id = Column(Integer, ForeignKey('list_type.id'))
    list = relationship(ListType, 
        back_populates='items')

    def __repr__(self):
        return "<ListItem(name='%s', description='%s')>" % (
            self.name, self.description)

if __name__ == '__main__':
    engine = create_engine('postgresql+psycopg2:///list_maker')
    Base.metadata.create_all(engine)
