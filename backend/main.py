from backend.controllers import app
from backend.models.Entity import Base, engine

if __name__ == '__main__':

    # Uncomment to create and clear database
   # Base.metadata.create_all(engine)

    app_options = {"port": 5000}
    app.run(**app_options)
