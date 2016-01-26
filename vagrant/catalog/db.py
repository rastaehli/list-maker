import psycopg2
import pdb

# Convenience wrapper for database access via psycopg2.
# Responsible for opening/closing connections, managing 
# transactions.
class DB():

    def __init__(self, dbname):
        self.dbname = dbname

    def connect(self):
        """Connect to the PostgreSQL database.  Returns a database connection."""
        try:
            return psycopg2.connect("dbname=%s" % self.dbname)
        except:
            print "unable to connect to %s" % self.dbname

    def execute(self, sql, params):
        # print sql, params
        conn = self.connect()
        result = conn.cursor().execute(sql, params)
        conn.commit()
        conn.close()
        
    # insert values list (DEFAULT will be appended for id column) into table
    def insert(self, table, valuesList, params):
        # print sql, params
        conn = self.connect()
        cursor = conn.cursor()
        sql = "INSERT INTO "+table+" values (DEFAULT, "+valuesList+") RETURNING id;"
        cursor.execute(sql, params)
        rowid = cursor.fetchone()[0]
        conn.commit()
        conn.close()
        return rowid

    def fetchAll(self, sql, params):
        # print sql, params
        conn = self.connect()
        cur = conn.cursor()
        cur.execute(sql, params)
        resultRows = cur.fetchall()
        conn.commit()
        conn.close()
        return resultRows
