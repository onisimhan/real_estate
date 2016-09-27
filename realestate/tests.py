from django.test import TestCase
from rest_framework.test import APIClient
from model_mommy import mommy


class TestApi(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_post_to_readonly_main_api(self):
        r = self.client.post('/api/main/')
        self.assertEqual(405, r.status_code)
        self.assertIn('not allowed', r._container[0])

    def test_put_to_readonly_main_api(self):
        r = self.client.put('/api/main/')
        self.assertEqual(405, r.status_code)
        self.assertIn('not allowed', r._container[0])

    def test_delete_to_readonly_main_api(self):
        r = self.client.delete('/api/main/')
        self.assertEqual(405, r.status_code)
        self.assertIn('not allowed', r._container[0])

    def test_get_main_api(self):
        mommy.make('realestate.Main', 3)
        r = self.client.get('/api/main/')
        self.assertEqual(3, len(r.data))

    def test_get_main_api_with_filter(self):
        mommy.make('realestate.Main', 2)
        mommy.make('realestate.Main', city='Denver', state='CO')
        mommy.make('realestate.Main', city='Denver', state='CA')
        mommy.make('realestate.Main', city='SomethingElse', state='CA')
        r = self.client.get('/api/main/')
        r_denver = self.client.get('/api/main/?city=Denver')
        r_denver_co = self.client.get('/api/main/?city=Denver&state=CO')
        r_co = self.client.get('/api/main/?state=CO')
        r_ca = self.client.get('/api/main/?state=CA')
        self.assertEqual(5, len(r.data))
        self.assertEqual(2, len(r_denver.data))
        self.assertEqual(1, len(r_denver_co.data))
        self.assertEqual(1, len(r_co.data))
        self.assertEqual(2, len(r_ca.data))
