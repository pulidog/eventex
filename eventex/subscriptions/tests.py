# teste primero,
# neste arquivo vai tudo o teste das inscripções


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




