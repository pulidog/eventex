from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Javier Pulido', cpf='12345678901', email='javier.python@gmail.com', phone='11-123456778')
        self.resp = self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'confirmacao de inscricao'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'javier.python@gmail.com'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_mail_to(self):
        expect = ['javier.python@gmail.com', 'javier.python@gmail.com']
        self.assertEqual(expect, self.email.to)

    def test_subcription_email_body(self):
        contents = ['Javier Pulido', '12345678901', 'javier.python@gmail.com', '11-123456778']

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)

        # self.assertIn('Javier Pulido', self.email.body)
        # self.assertIn('12345678901', self.email.body)
        # self.assertIn('javier.python@gmail.com', self.email.body)
        # self.assertIn('11-123456778', self.email.body)