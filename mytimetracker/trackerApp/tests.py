from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse


# Create your tests here.


class TrackerTestCase(TestCase):

    def setUp(self):
        super(TrackerTestCase, self).__init__()
        self.client = Client()
        self.another_client = Client()
        self.unlogged_client = Client()
        self.user = User.objects.create_user(
            'dima', password='1234'
        )
        self.user.save()
        self.another_user = User.objects.create_user(
            'dummy', password='dummy'
        )
        self.another_user.save()

    def test_login(self):
        response = self.client.post('/login/', {'username': 'dima',
                                                'password': '1234'}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, '/')

    def test_create_task(self):
        response = self.client.post('/create/',
                                    {"title": "test_task",
                                     "finish_data": "31-04-2020"})
        self.assertEqual(response.status_code, 200)
