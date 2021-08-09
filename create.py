import os
import unittest
import pandas as pd

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app.main import create_app, db
from app.main.model.peak import Peak

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')

app.app_context().push()

# df = pd.read_csv("/home/batman/Desktop/flask-restplus-boilerplate/14er.csv", encoding='latin1')
df = pd.read_csv("/home/batman/Desktop/flask-REST-portfolio/14er.csv", encoding='latin1')
df_dict = df.to_dict("records")

print(df.head().columns)

for d in df_dict:
    p = Peak(
        mountain_peak=d["Mountain Peak"],
        mountain_range=d["Mountain Range"],
        # elevation_ft=d["Elevation_ft"],
        # fourteener=d["fourteener"],
        # distance_mi=d["Distance_mi"],
        # elevation_gain_ft=d["Elevation Gain_ft"],
        # difficulty=d["Difficulty"],
        # traffic_low=d["Traffic Low"],
        # traffic_high=d["Traffic High"],
        # photo=d["photo"]
    )
    db.session.add(p)
db.session.commit()


# create db in flask shell
# python manage.py db init
# python manage.py db migrate --message 'initial database migration'
# python manage.py db upgrade
# python3 create.py 

# Screenshot
# /home/batman/Desktop/flask_migrate_portfolio_fourteeners.png