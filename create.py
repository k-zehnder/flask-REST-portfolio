import os
import unittest
import pandas as pd

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

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
    print(f"range: {r}")
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
        print(row['Elevation_ft'], row['Mountain Peak'])
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

# wanted_peak = Peak.query.filter_by(mountain_peak=data["mountain_peak"]).first()
# mountain_peak = "Castle Peak"
# wanted_peak_obj = Peaks.query.filter_by(mountain_peak=mountain_peak).first()

# r = Reviews(
#     reviewer_name="reviewer1",
#     review_text="hard climb!",
#     review_peak=wanted_peak_obj.mountain_peak
# )
# db.session.add(r)
# db.session.commit()

#from app.main import db
#from app.main.model.peaks import Peaks, Reviews, Ranges
