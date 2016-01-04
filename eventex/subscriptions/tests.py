# teste primero,
# neste arquivo vai tudo o teste das inscripções
from django.core import mail
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm

class SubscribeTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/inscricao/')

    def test_get(self):
        """
        get /inscricao/ para retornar o status 200
        response
        :return:
        """
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        '''
        quando use subscriptions/subscriptions_form.html
        :return:
        '''
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')

    def test_html(self):
        """
        Html contem etiquetas ou tags
        :return:
        """
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 6)
        self.assertContains(self.resp, 'type="text"', 3)
        self.assertContains(self.resp, 'type="email"')
        self.assertContains(self.resp, 'type="submit"')

    def test_csrf(self):
        '''
        Html conter um csrf
        :return:
        '''
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        '''
        contexto do formulario de subcricao
        :return:
        '''
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def teste_form_has_fields(self):
        '''
        Form tem 4 fields
        :return:
        '''
        form = self.resp.context['form']
        self.assertSequenceEqual(['name', 'cpf', 'email', 'phone'], list(form.fields))


class SubscribePostTest(TestCase):
    def setUp(self):
        data = dict(name='Javier Pulido', cpf='12345678901', email='javier.python@gmail.com', phone='11-123456778')
        self.resp = self.client.post('/inscricao/', data)

    def test_post(self):
        '''
        valida o POST e redireciona para /inscricao/
        :return:
        '''
        self.assertEqual(302, self.resp.status_code)

    def teste_send_subscribe_email(self):
        self.assertEqual(1, len(mail.outbox))

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


class SubscribeInvalidPost(TestCase):
    def setUp(self):
        self.resp = self.client.post('/inscricao/', {})
    def test_post(self):
        '''
        post invalido no redirect
        :return:
        '''

        self.assertEqual(200, self.resp.status_code)

    def test_templates(self):
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')

    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_errors(self):
        form = self.resp.context['form']
        self.assertTrue(form.errors)

class SubscribeSuccesMessage(TestCase):
    def test_message(self):
        data = dict(name='Javier Pulido', cpf='12345678901', email='javier.python@gmail.com', phone='11-123456778')

        response = self.client.post('/inscricao/', data, follow=True)
        self.assertContains(response, 'Inscrição realizada com sucesso!')
