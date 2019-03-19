import os





# Database
MONGO_CONNECTIONS = {
    'default': os.environ.get('MONGO_URI') or 'mongodb://localhost:27017/sun',
}