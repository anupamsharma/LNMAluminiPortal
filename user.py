from util import ConfigReader, DBUtil

class User():
    """
    This class represents a user.

    """
    _ALLOWED_ATTRS = []
    # I know this is a bad desing to hard things etc. but this module is just for learning purpose now so its fine.
    _USER_ATTRIBUTES_TO_DB_TABLE_TABLE_NAME = 'userAttributeToDBTable'
    _USER_ATTRIBUTES_TO_DB_TABLE = {}
    _USER_ATTRIBUTES_TO_DB_TABLE_QUERY = "Select AttributeName, TableName FROM %s "
    _CONN = None
    
    def __init__(self, user_id=None):
    """
        If you want to create a new user supply None as user_id.
    Please note this user_id is internal database user_id.
    """
        self._attr_to_value = {}
        self._conn = None
        self._load_attrs_from_db()

    # Ideally we should be asking for a database connection from a pool.
    @staticmethod
    def _get_conn(self):
        if not User._CONN:
            User._CONN = DBUtil.get_connection(ConfigReader().get_configuration(ConfigReader.CONNECTION_NAME))
        return User._CONN
    
    @staticmethod
    def get_valid_attrs():
        if not User._ALLOWED_ATTRS:
            User._ALLOWED_ATTRS = User.get_attrs_to_table_name_map().keys()
        return User._ALLOWED_ATTRS
        
    @staticmethod
    def get_attrs_to_table_name_map():
        if not User._USER_ATTRIBUTES_TO_DB_TABLE:
            query = User._USER_ATTRIBUTES_TO_DB_TABLE_QUERY % (User._USER_ATTRIBUTES_TO_DB_TABLE_TABLE_NAME)
            results = DBUtil.get_result_as_dicts()
            for result in results:
                attr = result[User._ATTRIBUTE_NAME_COLUMN]
                table = result[User._TABLE_NAME_COLUMN]
                User._USER_ATTRIBUTES_TO_DB_TABLE[attr] = table
        return User._USER_ATTRIBUTES_TO_DB_TABLE

    @staticmethod 
    def get_user(unique_attr, unique_attr_value):
        """
        This unique attr can be email id or user id.
        """
        ## Get user id from email id here. Handle the cases when
        # user is not found for given parameters.

        user_id =  something
        ## return instance of user object
        return User(user_id=user_id)

    def write_attrs_to_warehouse(self, create_user=False):
    """
    This function writes the user object attrs to database.
    If create_user flag is true 
    Case 1 . User does not exist in the database this method 
        should create new user in the database and set all the attributes in
    the db from self._attr_to_value.
    Case 2. User exist with same unique attr (like email_id) raise UserExist exception.

    """
        pass

    def set_attribute(self, attri_name, attr_value):
    """
    set attr does not update the values of attributes in the database untill you call
        sync_user_to_db.
    """
        pass

    def get_attribute(self, attr_name):
        ## Handle the cases where attribute not found like raising exception AttrNotFound
        return self._attr_to_value[attr_name]
        pass

    def get_all_attributes():
        if not self._attr_to_value:
            User.get_attrs_to_table_name_map()
        return self._attr_to_value
    pass

    def _load_attrs_from_db(self):
        ## fill up the dict self._attr_to_value from database. 

    def search_user(attr_name_to_value_map, search_options):
        ##Lets not worry about this now.
        pass

    def login(self, password):
        ##Lets not worry about this now.
        pass
