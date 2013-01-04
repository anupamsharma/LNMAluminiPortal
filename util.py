import MySQLdb
import json

class DBUtil(object):
  """
  This class has basic database utility method 
  """
  
  def get_connection(connection_name, config_file_loc):
    assert(isinstance(connection_name, str))
    assert(isinstance(config_file_loc, str))
    config_file = open(config_file)
    data = json.load(config_file)
    assert(connection_name in data)
  
  db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="john", # your username
                     passwd="megajonhy", # your password
                     db="jonhydb") # name of the data base

# you must create a Cursor object. It will let
#  you execute all the query you need
cur = db.cursor() 

# Use all the SQL you like
cur.execute("SELECT * FROM YOUR_TABLE_NAME")

# print all the first cell of all the rows
for row in cur.fetchall() :
    print row[0]
