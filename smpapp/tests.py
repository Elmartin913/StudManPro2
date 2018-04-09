from django.test import TestCase
from django.urls import reverse, resolve
from smpapp.views import TeacherStartView

# Create your tests here.

class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('teacher_start')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('teacher')
        self.assertEquals(view.func, TeacherStartView.get)