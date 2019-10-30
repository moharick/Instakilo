from django.test import TestCase
from .models import *
# Create your tests here.

class Profiletest(TestCase):
    numusers=10
    def setUp(self):
        self.tempprofiles = []
        for i in range(self.numusers):
            tmp=Profile()
            tmp.save()
            self.tempprofiles.append(tmp)

    def test_follow(self):
        follower=Profile()
        follower.save()
        for i in self.tempprofiles:
            follower.follow(i)
        self.assertEquals(follower.following.count(),self.numusers)
        for u in self.tempprofiles:
            self.assertEquals(u.followers.count(),1)