from math import factorial

from django.test import TestCase, override_settings

from Accounts.models import CourseTable


# @override_settings(LOGIN_URL="/login/")
# class LoginTestCase(TestCase):
#
#     def test_login(self):
#         response = self.client.get("/teaherprofile/11/", follow=True)
#         self.assertRedirects(response, "/login/?next=/teaherprofile/11/")


class CourseTestCase(TestCase):
    def setUp(self):
        course = CourseTable.objects.create(name='Python',
                                            description='python')
        CourseTable.objects.create(Title='Python',
                                   Description='Python',
                                   CoursePrice=12)
        def coursetest(self):
            courses = CourseTable.objects.filter(Title='Python')
            Coors = courses[0]
            self.assertEqual(Coors.Title, 'Python')
