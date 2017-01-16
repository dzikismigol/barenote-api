import os

# Define the application directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Define the database - we are working with
# SQLite for this example
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
DATABASE_CONNECT_OPTIONS = {}
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

SECRET_KEY = "ahd823yr9jadip23hjrnasklnf423EDAS!sddqwda"

# JWT configuration
JWT_AUTH_URL_RULE = "/api/login"
JWT_AUTH_ENDPOINT = "login"
JWT_AUTH_HEADER_PREFIX = "Bearer"