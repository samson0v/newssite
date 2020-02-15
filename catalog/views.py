from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
import requests

from .models import News, Comment
from .forms import NewsCreationForm
from django.template.loader import get_template


class NewsListView(ListView):
    template_name = 'catalog/catalog.html'
    model = News
    paginate_by = 30


def news_detail_view(request, id):
    obj = get_object_or_404(News, id=id)

    if request.method == 'POST':
        who = request.POST['who']
        text = request.POST['text']
        new = News.objects.get(pk=id)

        html = get_template('users/Email.html')
        email = new.author

        def send_simple_message(html_template, from_email):
            return requests.post(
                "https://api.mailgun.net/v3/sandbox2517dc64a782415286b5162cd77e8559.mailgun.org/messages",
                auth=("api", "9cee744c427a6cd7f2155af894c70e8d-52b6835e-83cc34f0"),
                data={"from": "Mailgun Sandbox <newssite@sandbox2517dc64a782415286b5162cd77e8559.mailgun.org>",
                    "to": "<" + email + ">",
                    "subject": "Hello",
                    "html": html_template
                },
            )

        send_simple_message(html, email)

        comment = Comment.objects.create(new=new, who=who, text=text)
        comment.save()

    return render(request, 'catalog/news.html', {'news': obj})


def add_news_view(request):
    form = NewsCreationForm(request.POST or None)

    if request.method == 'POST':
        user_id = request.POST['user']
        user = User.objects.get(pk=user_id)
        form = NewsCreationForm(request.POST, request.FILES)
        if form.is_valid():
            news = form.save()
            news.author = user.email
            if user.groups.filter(name='administrators').exists() or user.groups.filter(name='editors').exists():
                news.moderated = True
                news.save()
            else:
                news.moderated = False
                news.save()

        else:
            form = NewsCreationForm()

    return render(request, 'catalog/add_news.html', {'form': form})
