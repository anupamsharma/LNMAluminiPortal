"""
This module has utility methods we need for this small application.

"""
import MySQLdb as MDB
import json

class DBUtil(object):
  """
  This class has basic database utility method.
  
  """
  # We need to use the same names in database configuration file.
  HOST = 'host'
  USER = 'user'
  PASSWD = 'passwd'
  DB = 'db'
  
  def __init__(self):
    pass
  
  @staticmethod
  def get_connection(connection_name, config_file_loc):
    assert(isinstance(connection_name, str))
    assert(isinstance(config_file_loc, str))
    config_file = open(config_file)
    data = json.load(config_file)
    assert(connection_name in data)
    
    return MDB.connect(host=data[DBUtil.HOST],
                           user=data[DBUtil.USER],
                           passwd=data[DBUtil.PASSWD],
                           db=data[DBUtil.DB])


  @staticmethod
  def get_result_as_dicts(conn, query_str):
    cursor = con.cursor(MDB.cursors.DictCursor)
    cursor.execute(query_str)
    return cursor.fetchall()
