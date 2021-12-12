# By updating django-admin we can get a nice interface to login and search which users 
# have been created, create or make changes to users


from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
# reverse will allow us to generate urls for our django-admin page
# Client is the test client that will make test requests to the application in our unittests


class AdminSiteTests(TestCase):
    
    # Run before every test in our TestCase class
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@snbcore.com',
            password='test123'
        )
        # Helper function that allows to log in a user with django authentication
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='test@snbcore.com',
            password='password123',
            name = 'Test user full name'
        )

        # So we have a client, admin who is logged in, and a 
        # spare user we can use to test things like listing users

    # test that users are listed in django-admin. We need to 
    # do this because we need to customize django-admin to 
    # work with our custom user model
    def test_users_listed(self):
        """Test that users are listed on user page"""

        # create url for list user page
        # By using the reverse function instead of typing
        # manually we don't have to change the url everywhere if we do change it
        # keywords like core_user_changelist is defined in the django-admin docs
        url = reverse('admin:core_user_changelist')
        
        # response: The test client will be used to perform 
        # an HTTP GET on the url found here
        res = self.client.get(url)

        # a django custom assertion: checks whether
        #  - Response contains specified item 
        #        (looks into the output obj)
        #  - whether HTTP response was 200
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)


    def test_user_change_page(self):
        """Test that the user edit page works"""
        # /admin/core/user/:id
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)


    def test_create_user_page(self):
        """Test that the create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)




