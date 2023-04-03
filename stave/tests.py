from django.test import TestCase
from stave.models import Stave
from base.models import User
# Create your tests here.
class StaveTest(TestCase):
    def setUp(self):
        user = User.objects.create(username='Matanmi', email='me@me.com', first_name='Yeah', last_name='Oh')
        Stave.objects.create(user=user, content='Yeah i am a motherfucking starboy')
    
    def test_username(self):
        stave = Stave.objects.get(user__username='Matanmi')
        self.assertEqual(stave.user.username, 'Matanmi')
    
    def test_content(self):
        stave = Stave.objects.get(user__username='Matanmi')
        self.assertLessEqual(len(stave.content), 280)