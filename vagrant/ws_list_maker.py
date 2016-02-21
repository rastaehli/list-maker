# ws_list_maker.py
#
# Responsible for handling HTTP requests, implementing pages of the list_maker web site.
# Uses the 'Flask' framework to bind web site page paths to handler methods, bind
# python object to HTML templates to render dynamic content.

from flask import Flask, render_template, request, redirect,jsonify, url_for, flash
app = Flask(__name__)

from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from orm import Base, Category, ListType, ListItem

from flask import session as login_session

APPLICATION_NAME = "List Maker Website"

#Connect to Database and create database session
engine = create_engine('postgresql+psycopg2:///list_maker')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

#Show all categories
@app.route('/')
@app.route('/category/all')
def showCategories():
  categories = session.query(Category).order_by(asc(Category.name))
  return render_template('categories.html', categories = categories)

#Show all ListTypes in category
@app.route('/category/<string:category_name>')
def showListTypes(category_name):
  types = session.query(ListType).filter_by(category = category_name).order_by(asc(ListType.name)).all()
  return render_template('types.html', types = types, cagegory_name = category_name)

#Show new ListType form for Category 
@app.route('/category/<string:category_name>/newListType')
def newListType(category_name):
  types = session.query(ListType).filter_by(category = category_name).order_by(asc(ListType.name)).all()
  return render_template('types.html', types = types, cagegory_name = category_name)

#Show edit ListType form for Category 
@app.route('/listtype/<int:type_id>/edit')
def editListType(type_id):
  type = session.query(ListType).filter_by(id = type_id).one()
  return render_template('items.html', type = type)

#delete ListType from Category 
@app.route('/listtype/<int:type_id>/delete')
def deleteListType(type_id):
  type = session.query(ListType).filter_by(id = list_id).one()
  return render_template('items.html', type = type)

#Show items in ListType 
@app.route('/listtype/<int:id>')
def showListItems(id):
  type = session.query(ListType).filter_by(id = id).one()
  return render_template('items.html', type = type)

#Show new item form for ListType 
@app.route('/listtype/<int:type_id>/newItem')
def newListItem(type_id):
  type = session.query(ListType).filter_by(id = type_id).one()
  return render_template('items.html', type = type)

#Show edit item form for ListType 
@app.route('/listtype/<int:type_id>/<int:item_id>/edit')
def editListItem(type_id, item_id):
  type = session.query(ListType).filter_by(id = type_id).one()
  return render_template('items.html', type = type)

#delete item from ListType 
@app.route('/listtype/<int:type_id>/<int:item_id>/delete')
def deleteListItem(type_id, item_id):
  type = session.query(ListType).filter_by(id = type_id).one()
  return render_template('items.html', type = type)


if __name__ == '__main__':
  # app.secret_key = 'super_secret_key'
  app.debug = True
  app.run(host = '0.0.0.0', port = 5000)
