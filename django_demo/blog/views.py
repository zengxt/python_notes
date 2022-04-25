from django.core.paginator import Paginator
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
    page = request.GET.get("page")
    if page:
        page = int(page)
    else:
        page = 1
    print('page = %d' % page)

    all_article = Article.objects.all()
    top5_article_list = Article.objects.order_by('-publish_date')[0:5]

    paginator = Paginator(all_article, 3)
    page_num = paginator.num_pages
    print('page num = ', page_num)

    page_article_list = paginator.page(page)
    if page_article_list.has_next():
        next_page = page + 1
    else:
        next_page = page
    if page_article_list.has_previous():
        pre_page = page - 1
    else:
        pre_page = page

    return render(request, 'blog/index.html',
                  {'article_list': page_article_list,
                   'top5_article_list': top5_article_list,
                   'page_num': range(1, page_num + 1),
                   'curr_page': page,
                   'next_page': next_page,
                   'pre_page': pre_page})


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
