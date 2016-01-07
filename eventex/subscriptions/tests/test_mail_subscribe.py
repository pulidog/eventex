from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Javier Pulido', cpf='12345678901', email='javier.python@gmail.com', phone='11-123456778')
        self.resp = self.client.post('/inscricao/', data)

    def test_subscription_email_subject(self):
        email = mail.outbox[0]
        expect = 'confirmacao de inscricao'

        self.assertEqual(expect, email.subject)

    def test_subscription_email_from(self):
        email = mail.outbox[0]
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, email.from_email)

    def test_subscription_mail_to(self):
        email = mail.outbox[0]
        expect = ['contato@eventex.com.br', 'javier.python@gmail.com']
        self.assertEqual(expect, email.to)

    def test_subcription_email_body(self):
        email = mail.outbox[0]

        self.assertIn('Javier Pulido', email.body)
        self.assertIn('12345678901', email.body)
        self.assertIn('javier.python@gmail.com', email.body)
        self.assertIn('11-123456778', email.body)