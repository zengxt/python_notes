from django.http import HttpResponse
from django.shortcuts import render

from .models import Article


# Create your views here.


def hello_word(request):
    return HttpResponse("Hello World!!")


def article_content(request):
    article = Article.objects.all()[0]
    article_id = article.article_id
    title = article.title
    brief_content = article.brief_content
    content = article.content
    publish_date = article.publish_date
    result_str = "article_id: %s\n title: %s\n brief_content: %s\n content: %s\n publish_date: %s\n" \
                 % (article_id, title, brief_content, content, publish_date)
    return HttpResponse(result_str)


def get_article_list(request):
    all_article = Article.objects.all()
    return render(request, 'blog/index.html', {'article_list': all_article, 'top_new_article_list': all_article})


def get_article_detail(request, article_id):
    all_article = Article.objects.all()

    previous_article = None
    curr_article = None
    next_article = None
    for index, article in enumerate(all_article):
        if index == 0:
            pre_article_index = index
            next_article_index = index + 1
        elif index == len(all_article) - 1:
            pre_article_index = index - 1
            next_article_index = index
        else:
            pre_article_index = index - 1
            next_article_index = index + 1

        if article.article_id == article_id:
            previous_article = all_article[pre_article_index]
            curr_article = article
            next_article = all_article[next_article_index]
            break

    section_list = curr_article.content.split('\n')
    return render(request, 'blog/detail.html',
                  {'curr_article': curr_article,
                   "section_list": section_list,
                   "previous_article": previous_article,
                   "next_article": next_article})
