import os
import unittest
import pandas as pd

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app.main import create_app, db
from app.main.model.peak import Peak, Range

# create app context and push it
app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.app_context().push()

# create database
db.create_all()

# grab data from csv
df = pd.read_csv(
    "/home/batman/Desktop/flask-REST-portfolio/14er.csv", encoding='latin1')
ranges = df["Mountain Range"].unique()

# have to commit to db before looping through
for r in sorted(ranges):
    print(f"range: {r}")
    r = Range(
        mountain_range=r
    )
    db.session.add(r)
db.session.commit()

# loop through ranges and get associated mountain peaks
ranges = Range.query.all()
for r in ranges:
    tmp = df[df["Mountain Range"] == r.mountain_range]
    for index, row in tmp.iterrows():
        print(row['Elevation_ft'], row['Mountain Peak'])
        p = Peak(
            mountain_peak=row["Mountain Peak"],
            # elevation_ft=d["Elevation_ft"],
            # fourteener=d["fourteener"],
            # distance_mi=d["Distance_mi"],
            # elevation_gain_ft=d["Elevation Gain_ft"],
            # difficulty=d["Difficulty"],
            # traffic_low=d["Traffic Low"],
            # traffic_high=d["Traffic High"],
            # photo=d["photo"]

            # foreign key
            range_name=r.mountain_range # r.id
        )
        print(p)
        db.session.add(p)
    db.session.commit()

