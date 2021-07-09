from flask import Flask

from flask_restful import reqparse, abort, Api, Resource
from . import db_session
from .news import News
import news_resources

app = Flask(__name__)
api = Api(app)


def abort_if_news_not_found(news_id):
    session = db_session.create_session()
    news = session.query(News).get(news_id)
    if not news:
        abort(404, message=f"News {news_id} not found")


api.add_resource(news_resources.NewsListResource, '/api/v2/news')

api.add_resource(news_resources.NewsResource, '/api/v2/news/<int:news_id>')
