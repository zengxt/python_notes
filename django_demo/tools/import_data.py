#!/usr/bin/python
# -*-encoding=utf8 -*-
import os
import sys

import django

# 必须将项目目录附加到sys.path，否则将会找不到 django_blog 这个模块
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_blog.settings')
django.setup()

from blog.models import Article

data_path = '../data/article'


def main():
    content_list = []
    files = os.listdir(data_path)
    for name in files:
        f = os.path.join(data_path, name)
        with open(f, 'r', encoding='utf-8') as f:
            content = f.read()
            item = (name[:-4], content[:100], content)
            content_list.append(item)
    # Article.objects.all().delete()
    for item in content_list:
        print('saving article: %s' % item[0])
        article = Article()
        article.title = item[0]
        article.brief_content = item[1]
        article.content = item[2]
        article.save()


if __name__ == '__main__':
    main()
