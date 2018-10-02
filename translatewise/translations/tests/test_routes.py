from translatewise.tests.base import BaseTestCase


class FlaskTestCase(BaseTestCase):

    def test_index_get(self):
        response = self.client.get('/')
        assert response.status_code == 200

    def test_index_post(self):
        response = self.client.post('/')
        assert response.status_code == 200
