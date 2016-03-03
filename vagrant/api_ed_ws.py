# api_ed_ws.py
#
# Responsible for handling HTTP requests, implementing pages of the api_ed web site.
# Uses the 'Flask' framework to bind web site page paths to handler methods, bind
# python object to HTML templates to render dynamic content.

from flask import Flask, render_template, request, redirect,jsonify, url_for, flash
app = Flask(__name__)

from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from orm_api_ed import Base, ParameterType, Parameter, RestCall, db_connection_info

from flask import session as login_session

APPLICATION_NAME = "API Editor Website"

#Connect to Database and create database session
engine = create_engine(db_connection_info)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

#Show all REST calls
@app.route('/')
@app.route('/api/all')
def showRestCalls():
  restCalls = session.query(RestCall).order_by(asc(RestCall.path))
  return render_template('restCalls.html', restCalls = restCalls)

#Show all detail of RestCall
@app.route('/api/<int:call_id>')
def showRestCallDetail(call_id):
  restCall = session.query(RestCall).filter_by(id = call_id).one()
  return render_template('restCallDetail.html', restCall = restCall)

if __name__ == '__main__':
  # app.secret_key = 'super_secret_key'
  app.debug = True
  app.run(host = '0.0.0.0', port = 5000)
