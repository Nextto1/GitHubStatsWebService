# Import the Blueprint class from Flask to create a blueprint instance
from flask import Blueprint

# Create a Blueprint instance named 'main'. The first argument is the blueprint's name,
# and the second argument is the import name, which is typically set to __name__.
main = Blueprint('main', __name__)

# Import the routes module from the current package. This import statement should be placed
# after the blueprint creation to avoid circular imports.
from . import routes