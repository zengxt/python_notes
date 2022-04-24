import blog.views

from django.urls import path

urlpatterns = [
    path('hello_world', blog.views.hello_word),
    path('article_content', blog.views.article_content),
    path('index', blog.views.get_article_list),
    # path('detail', blog.views.get_article_detail)
    path('detail/<int:article_id>', blog.views.get_article_detail)
]
