import os
import unittest
import tempfile
from myapp import app

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.db,app.config['DATABASE'] = tempfile.mkstemp()
        app.config['TESTing'] = True
        self.app = app.test_client()
        app.init_db()
    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(app.config['DATABASE'])
    def test_empty_db(self):
        rv = self.app.get('/')
        assert 'No entries here so far' in rv.data

if __name__ == '__main__':
    unittest.main()

