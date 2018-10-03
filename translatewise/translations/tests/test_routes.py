from translatewise.tests.base import BaseTestCase
from translatewise import db
from translatewise.translations.models import Translation


class FlaskTestCase(BaseTestCase):

    def test_index_get(self):
        response = self.client.get('/')
        assert response.status_code == 200

    def test_index_post(self):
        response = self.client.post(
            '/',
            data=dict(text="hello"),
            follow_redirects=True,
            headers={"Content-Type": "application/x-www-form-urlencoded"}
            )

        translation = db.session.query(Translation).get(1)

        assert translation.text == "hello"
        assert response.status_code == 200
