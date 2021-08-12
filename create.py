import os
import unittest
import pandas as pd

from app.main import create_app, db
from app.main.model.peaks import Peaks, Ranges, Reviews

# create app context and push it
app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.app_context().push()

# create database
db.create_all()

# grab data from csv
df = pd.read_csv("14er.csv", encoding='latin1')
ranges = df["Mountain Range"].unique()

# have to commit to db before looping through
for r in sorted(ranges):
    r = Ranges(
        mountain_range=r
    )
    db.session.add(r)
db.session.commit()

# loop through ranges and get associated mountain peaks
ranges = Ranges.query.all()
for r in ranges:
    tmp = df[df["Mountain Range"] == r.mountain_range]
    for index, row in tmp.iterrows():
        p = Peaks(
            mountain_peak=row["Mountain Peak"],
            elevation_ft=row["Elevation_ft"],
            fourteener=row["fourteener"],
            distance_mi=row["Distance_mi"],
            elevation_gain_ft=row["Elevation Gain_ft"],
            difficulty=row["Difficulty"],
            traffic_low=row["Traffic Low"],
            traffic_high=row["Traffic High"],
            photo=row["photo"],
            range_name=r.mountain_range # foreign key
        )
        print(p)
        db.session.add(p)
    db.session.commit()


