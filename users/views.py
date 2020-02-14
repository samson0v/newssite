from django.shortcuts import render
from .forms import SignUpForm
from django.contrib.auth.models import User

from django.template.loader import get_template
from django.contrib.auth.models import Group

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from .tokens import account_activation_token
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode

import requests
from django.urls import reverse
from django.contrib.auth import authenticate, login


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = False
            user.refresh_from_db()
            user.additionalinfo.birth_date = form.cleaned_data.get('birth_date')
            group = Group.objects.all()[0]
            user.groups.add(group)
            user.save()

            current_site = get_current_site(request)
            email = form.cleaned_data.get('email')

            htmly = get_template('users/Email.html')
            d = {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            }
            html_content = htmly.render(d)

            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = account_activation_token.make_token(user),
            link = 'http://' + current_site.domain + reverse('activate', kwargs={'uidb64': uid, 'token': token})
            print(link)

            def send_simple_message(user, html_template, from_email):
                return requests.post(
                    "https://api.mailgun.net/v3/sandbox2517dc64a782415286b5162cd77e8559.mailgun.org/messages",
                    auth=("api", "9cee744c427a6cd7f2155af894c70e8d-52b6835e-83cc34f0"),
                    data={"from": "Mailgun Sandbox <newssite@sandbox2517dc64a782415286b5162cd77e8559.mailgun.org>",
                        "to": "Vitalii Bidochka <" + email + ">",
                        "subject": "Hello Vitalii Bidochka",
                        "html": html_content
                    },
                )

            send_simple_message(user, html_content, email)

    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.additionalinfo.email_confirmed = True
        user.save()
        return render(request, 'users/reg_finish.html')
    else:
        return render(request, 'users/account_activation_invalid.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        username = User.objects.get(email=email.lower()).username
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'users/reg_finish.html')
        else:
            return render(request, 'users/account_activation_invalid.html')

    return render(request, 'users/login.html')
