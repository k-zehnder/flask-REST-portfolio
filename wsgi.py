import os
import unittest

#from flask_migrate import Migrate, MigrateCommand
#from flask_script import Manager

from app import blueprint
from app.main import create_app, db
from app.main.model.peaks import Peaks, Ranges, Reviews

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(blueprint)

app.app_context().push()


if __name__ == '__main__':
    app.run()
