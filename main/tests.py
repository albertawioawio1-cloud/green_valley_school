from django.test import TestCase, Client
from django.urls import reverse
from .models import Announcement, Event, ContactMessage

class GreenValleyTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.announcement = Announcement.objects.create(
            title="Welcome Back", content="Term starts today.", is_active=True
        )

    def test_home_page_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_contact_form_submission(self):
        response = self.client.post(reverse('contact'), {
            'name': 'Test User',
            'email': 'test@example.com',
            'subject': 'Inquiry',
            'message': 'Hello world'
        })
        self.assertEqual(ContactMessage.objects.count(), 1)