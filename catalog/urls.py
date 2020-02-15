from django.urls import path

from .views import NewsListView, add_news_view, news_detail_view

app_name = 'catalog'
urlpatterns = [
    path('', NewsListView.as_view(), name='news-list'),
    path('<int:id>/', news_detail_view, name='news-detail'),
    path('addnews/', add_news_view, name="add-news"),
]
