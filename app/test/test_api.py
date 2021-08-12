import unittest
from flask_testing import TestCase

from app.main import db
from wsgi import app
from app.main.model.peaks import Peaks, Ranges, Reviews

class FlaskTestCase(TestCase):
    """ API Tests """

    def create_app(self):
        app.config.from_object("test")
        return app

    def setUp(self):
        db.create_all()

        # add range to db
        ranges = Ranges(mountain_range="Elk Mountains")
        db.session.add(ranges)
        db.session.commit()
        
        # add peak to db given a range
        one_range = ranges.query.first()
        peak = Peaks(
            mountain_peak="Castle Peak",
            elevation_ft=14279,
            fourteener="Y",
            distance_mi=2365,
            elevation_gain_ft=4600,
            difficulty="Hard Class 2",
            traffic_low=1000,
            traffic_high=3000,
            photo="https://www.14ers.com/photos/castlegroup/peakphotos/large/200807_Cast04.jpg",
            range_name=one_range.mountain_range # foreign key
        )
        db.session.add(peak)
        db.session.commit()   

        # add review to db given peak
        mountain_peak = "Castle Peak"
        wanted_peak_obj = Peaks.query.filter_by(mountain_peak=mountain_peak).first()
        r = Reviews(
            reviewer_name="reviewer2",
            review_text="hard climb2!",
            review_peak=wanted_peak_obj.mountain_peak
        )
        db.session.add(r)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    # test databases
    def test_db(self):
        ranges_test = Ranges.query.first()
        peaks_test = Peaks.query.filter_by(mountain_peak="Castle Peak").first()
        reviews_test = Reviews.query.first()
        assert ranges_test.mountain_range == "Elk Mountains"
        assert peaks_test.mountain_peak == "Castle Peak"
        assert peaks_test.photo == "https://www.14ers.com/photos/castlegroup/peakphotos/large/200807_Cast04.jpg"
        assert reviews_test.reviewer_name == "reviewer2"

    # test index
    def test_index(self):
        tester = self.app.test_client(self)
        response = tester.get('/', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.content_type == 'application/json')

    # test peaks
    def test_peaks(self):
        tester = self.app.test_client(self)
        response = tester.get('/peaks/', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.content_type == 'application/json')

    # test reviews
    def test_index(self):
        tester = self.app.test_client(self)
        response = tester.get('/reviews/', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.content_type == 'application/json')
    
    # test reviews by peak
    def test_index(self):
        tester = self.app.test_client(self)
        response = tester.get('/reviews/Castle Peak', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.content_type == 'application/json')

    # test photo
    def test_photo(self):
        tester = self.app.test_client(self)
        response = tester.get('/peaks/Castle Peak', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.content_type == 'application/json')

if __name__ == '__main__':
    unittest.main(verbosity=2)