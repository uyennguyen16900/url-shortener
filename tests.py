from unittest import TestCase, main as unittest_main, mock
from app import app
from bson.objectid import ObjectId
from shortener import URL_shortener

url_shortener = URL_shortener()
sample_url_id = ObjectId('5d55cffc4a3d4021f42827a3')
sample_url = {
    'original_url': 'https://github.com/uyennguyen16900',
    'shortened_url': url_shortener.shorten_url('original_url')
}
sample_form_data = {
    'original_url': sample_url['original_url'],
    # 'shortened_url': sample_url['shortened_url']
}

class DrinksTests(TestCase):
    """Flask tests."""

    def setUp(self):
        """Stuff to do before every test."""

        # Get the Flask test client
        self.client = app.test_client()

        # Show Flask errors that happen during tests
        app.config['TESTING'] = True

    def test_index(self):
        """Test the drinks homepage."""
        result = self.client.get('/')
        self.assertEqual(result.status, '200 OK')

    @mock.patch('pymongo.collection.Collection.find_one')
    def test_show_url(self, mock_find):
        """Test showing a shortened url."""
        mock_find.return_value = sample_url

        result = self.client.get(f'/shorten')
        self.assertEqual(result.status, '302 FOUND')

    @mock.patch('pymongo.collection.Collection.insert_one')
    def test_submit_drink(self, mock_insert):
        """Test submitting a url."""
        result = self.client.post('/shorten', data=sample_form_data)

        self.assertEqual(result.status, '200 OK')
