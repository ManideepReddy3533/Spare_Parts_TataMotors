class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:manideep@localhost/flaskdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'xyz_123467890'

print("suceess running")