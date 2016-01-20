list-maker
=============

This project contains my solution for a web application to manage a categorized set of items and their descriptions.

In this case, the items are themselves "list types" that describe the items in a checklist.  The immediate use cases
relevant to this project are:
1) View the site, see a list of categories at left, a list of (up to ten) most recently added "list types" at right.
2) Click a categorie to view a list of all "list types" in that category.
3) Click on a "list type" to view its description and list of checklist items for that type.
4) Log in to the site to see the same views with the addition of an "edit" button for a category and for a "list type".
5) Click "edit" category to add/delete "list types" from that category.
6) Click "edit" "list type" to change the description and checklist items for that type.

The current functionality is demonstrated by running the code in list-maker.py.  Here’s how:

- clone this project to your machine and change to the vagrant directory:
<pre>
    cd /vagrant
</pre>
- launch the virtual machine and enter a virtual terminal:
<pre>    
    vagrant up
    vagrant ssh
</pre>
- in the VM, cd to the catalog folder and initialize the database, then quit psql:
<pre>    
    cd /vagrant/catalog
    psql
    \i list-maker-db.sql
    \q
</pre>
- run the unit tests and verify it reports success:
<pre>    
    python list_maker_test.py
</pre>

