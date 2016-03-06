from django.test import TestCase
from datetime import datetime
from django.shortcuts import resolve_url as r
from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
	def setUp(self):
		self.obj = Subscription(
				name='Izabela Guerreiro',
				cpf='12345678901',
				email='izaguerreiro@gmail.com',
				phone='12-99126-6633'
			)
		self.obj.save()
	
	def test_create(self):	
		self.assertTrue(Subscription.objects.exists())

	def test_created_at(self):
		""" Subscription must have an auto created_at attr """
		self.assertIsInstance(self.obj.created_at, datetime)

	def test_str(self):
		self.assertEqual('Izabela Guerreiro', str(self.obj))

	def test_paid_default_to_False(self):
		""" By default paid must be False """
		self.assertEqual(False, self.obj.paid)

	def test_get_absolute_url(self):
		url = r('subscriptions:detail', self.obj.pk)
		self.assertEqual(url, self.obj.get_absolute_url())