import unittest

from hidro_app import app


class BasicTestCase(unittest.TestCase):
    def test_url(self):
        tester = app.test_client(self)
        urls = 'curahhujan_tma_klimatologi_kekeringan_kualitasair'.split('_')
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        for p in urls:
            resp = tester.get('/'+p+'/', content_type='html/text')
            self.assertEqual(resp.status_code, 200)


if __name__ == '__main__':
    unittest.main()
