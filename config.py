from TopSecret import TopSecret
class DevelopmentConfig:
    SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://root:{TopSecret}@localhost/advanced_e_commerce_db'
    CACHE_TYPE = 'SimpleCache'
    DEBUG = True