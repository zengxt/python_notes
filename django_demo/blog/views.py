from django.http import HttpResponse

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
