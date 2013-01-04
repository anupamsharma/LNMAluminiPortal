"""
This module has utility methods we need for this small application.

"""
import os
import MySQLdb as MDB
import json

class ConfigReader(object):
  """
  This class has basic database utility method.
  
  """
  # We need to use the same names in database configuration file.
  ENV = 'env'
  PROD = 'prod'
  CONNECTION_NAME = 'connection_name'
  PORTAL_HOME_DIR = 'portal_home_dir'
  DEFAULT_CONFIG_FILE = os.path.join(PORTAL_HOME_DIR, 'cfg', 'main_config.json') 

  def __init__(self):
    pass
  
  @staticmethod
  def get_configuration(config_file_loc=None):
    assert(isinstance(connection_name, str))
    if config_file_loc:
      assert(isinstance(config_file_loc, str))
    else:
      config_file_loc = ConfigReader.DEFAULT_CONFIG_FILE
      
    config_file = open(config_file)
    return json.load(config_file)

class DBUtil(object):
  """
  This class has basic database utility method.
  
  """
  # We need to use the same names in database configuration file.
  HOST = 'host'
  USER = 'user'
  PASSWD = 'passwd'
  DB = 'db'
  DEFAULT_CONFIG_FILE = os.path.join(PORTAL_HOME_DIR, 'cfg', 'db_config.json') 

  def __init__(self):
    pass
  
  @staticmethod
  def get_connection(connection_name, config_file_loc):
    assert(isinstance(connection_name, str))
    if config_file_loc:
      assert(isinstance(config_file_loc, str))
    else:
      config_file_loc = DBUtil.DEFAULT_CONFIG_FILE
      
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
