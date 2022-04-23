import blog.views

from django.urls import path

urlpatterns = [
    path('hello_world', blog.views.hello_word),
    path('article_content', blog.views.article_content)
]
