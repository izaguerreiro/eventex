from django.test import TestCase
from django.core import mail


class SubscribePostValid(TestCase):
	def setUp(self):
		data = dict(name='Izabela Guerreiro', cpf=12345678901, 
					email='izaguerreiro@gmail.com', phone='12-991266633')
		self.client.post('/inscricao/', data)
		self.email = mail.outbox[0]

	def test_subscription_email_subject(self):
		expect = 'Confirmação de inscrição'
		self.assertEqual(expect, self.email.subject)

	def test_subscription_email_from(self):
		expect = 'izaguerreiro@gmail.com'
		self.assertEqual(expect, self.email.from_email)

	def test_subscription_email_to(self):
		expect = ['izaguerreiro@gmail.com', 'izaguerreiro@gmail.com']
		self.assertEqual(expect, self.email.to)

	def test_subscription_email_body(self):
		contents = [
			'Izabela Guerreiro',
			'12345678901',
			'izaguerreiro@gmail.com',
			'12-991266633',
		]
		for content in contents:
			with self.subTest():
				self.assertIn(content, self.email.body)