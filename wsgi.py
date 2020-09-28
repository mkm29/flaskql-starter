import os
from app.server import create_app

# Get environment from variable
env = os.getenv('ENV', 'LOCAL')
application = create_app(env=env)

if __name__ == "__main__":
    application.run(debug=True)
