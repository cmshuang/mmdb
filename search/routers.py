class SearchRouter(object):
    """
    A router to control all database operations on models in the
    search application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read search models go to search_db.
        """
        if model._meta.app_label == 'search':
            return 'search'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write search models go to default.
        """
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the search app is involved.
        """
        if obj1._meta.app_label == 'search' or \
           obj2._meta.app_label == 'search':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the search app only appears in the 'search_db'
        database.
        """
        if app_label == 'search':
            return db == 'search'
        return None