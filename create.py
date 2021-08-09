import os
import unittest
import pandas as pd

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app.main import create_app, db
from app.main.model.peak import Peak, Range

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')

app.app_context().push()

# df = pd.read_csv("/home/batman/Desktop/flask-restplus-boilerplate/14er.csv", encoding='latin1')
df = pd.read_csv(
    "/home/batman/Desktop/flask-REST-portfolio/14er.csv", encoding='latin1')
ranges = df["Mountain Range"].unique()

db.create_all()

# for r in sorted(ranges):
#     r = Range(
#         mountain_range=r
#     )
#     db.session.add(r)
#     db.session.commit()
#     print(f"range: {r}")
    # tmp = df[df["Mountain Range"] == r]
    # for index, row in tmp.iterrows():
    #     print(row["Elevation_ft"], row["Mountain Peak"])
    #     p = Peak(
    #         mountain_peak=row["Mountain Peak"],
    #         range_mountain_range=r.id
    #     )
    #     db.session.add(p)
    #     db.session.commit()

ranges = df["Mountain Range"].unique()

for r in sorted(ranges):
    print(f"range: {r}")
    r = Range(
        mountain_range=r
    )
    db.session.add(r)
db.session.commit()


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
            range_id=r.id
        )
        print(p)
        db.session.add(p)
    db.session.commit()

#############################################################
# for d in df_dict:
#     p = Peak(
#         mountain_peak=d["Mountain Peak"],
#         mountain_range=d["Mountain Range"],
#         # elevation_ft=d["Elevation_ft"],
#         # fourteener=d["fourteener"],
#         # distance_mi=d["Distance_mi"],
#         # elevation_gain_ft=d["Elevation Gain_ft"],
#         # difficulty=d["Difficulty"],
#         # traffic_low=d["Traffic Low"],
#         # traffic_high=d["Traffic High"],
#         # photo=d["photo"]
#     )
#     db.session.add(p)
# db.session.commit()


# create db in flask shell
# python manage.py db init
# python manage.py db migrate --message 'initial database migration'
# python manage.py db upgrade
# python3 create.py

# Screenshot
# /home/batman/Desktop/flask_migrate_portfolio_fourteeners.png
