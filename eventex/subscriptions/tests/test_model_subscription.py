from datetime import datetime

from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(name='Javier Pulido',
                           cpf='12345678901',
                           email='javier.python@gmail.com',
                           phone='11-123456778'
                           )
        self.obj.save()

    def test_create(self):

        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):

        self.assertIsInstance(self.obj.created_at, datetime)
