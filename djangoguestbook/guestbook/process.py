from django.http import QueryDict, HttpRequest
from django.contrib.auth.hashers import make_password
from django.utils.timezone import localtime

from article.models import Article

def localize(utc_datetime):
    return localtime(utc_datetime)

def get():
    print("Get 함수")
    article_objects = Article.objects.all()
    articles = article_objects.values()
    result = list()

    for article in articles:
        datetime = localize(article['datetime'])
        datetime_str = f"{datetime.year}년 {datetime.month}월 {datetime.day}일 {datetime.hour:02d}:{datetime.minute:02d}:{datetime.second:02d}"
        tmp = (article['id'], article['nickname'], article['content'], datetime_str)
        result.append(tmp)
    return result

def write(post: QueryDict):
    print("Write 함수")

    secretcode = make_password(post['secretcode'])
    article = Article(nickname=post['nickname'], secretcode=secretcode, content=post['content'])
    article.save()
    print(article)