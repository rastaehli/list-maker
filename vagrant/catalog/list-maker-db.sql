-- Table definitions for the list-maker project.

--psql commands to create the database and connect to it:
DROP DATABASE IF EXISTS list_maker;
CREATE DATABASE list_maker;
\c list_maker;

DROP TABLE IF EXISTS CATEGORY;
DROP TABLE IF EXISTS LIST_TYPE;
DROP TABLE IF EXISTS LIST_ENTRY;

CREATE TABLE CATEGORY(
	id SERIAL UNIQUE PRIMARY KEY, -- GUID for this row
	name VARCHAR(32));  -- display name for this category

CREATE TABLE LIST_TYPE(
	id SERIAL UNIQUE PRIMARY KEY,  -- GUID for this row
	name VARCHAR(32), -- display name for this type
	category INTEGER REFERENCES CATEGORY,  -- identifies category row to which this type belongs.
	description VARCHAR(1024));  -- free text description of list purpose.

CREATE TABLE LIST_ENTRY(
	list INTEGER REFERENCES LIST_TYPE,  -- GUID for LIST_TYPE to which this entry belongs.
	name VARCHAR(64));  -- display name for this list entry
