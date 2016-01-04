
from django.contrib import messages
from django.core import mail
from django.shortcuts import render
from django.template.loader import render_to_string
from eventex.subscriptions.forms import SubscriptionForm
from django.http import HttpResponseRedirect, HttpResponse

def subscribe(request):
    # pega o POST do formulario de inscricao
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        # se é valido esse form , ele prenche os dados
        if form.is_valid():
            # caso de susseso
            body = render_to_string('subscriptions/subscription_email.txt', form.cleaned_data)
            mail.send_mail('confirmacao de inscricao',
                           body,
                           'contato@eventex.com.br',
                           ['contato@eventex.com.br', form.cleaned_data['email']]
                           )
            messages.success(request, 'Inscrição realizada com sucesso!')
            return HttpResponseRedirect('/inscricao/')
        else:
            # se não é valido ele joga um cod 200
            return render(request, 'subscriptions/subscription_form.html',
                          {'form': form})
    else:
        context = {'form': SubscriptionForm()}
        return render(request, 'subscriptions/subscription_form.html', context)


