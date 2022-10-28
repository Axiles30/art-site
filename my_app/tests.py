from django.test import TestCase
from django.urls import resolve
from my_app.views import start_page
from my_app.models import Article
import unittest
from django.http import HttpRequest
from datetime import datetime

class HomePageTest(TestCase) :
	def test_root_url_resolve_to_home_page_view(self) :
		found = resolve('/')
		self.assertEqual(found.func, start_page)

	def test_home_page_return_correct_html(self) :
		request = HttpRequest()
		response = start_page(request)
		html = response.content.decode('utf8')
		self.assertTrue(html.startswith('<html>'))
		self.assertTrue(html.endswith('</html>'))
	# self.browser.get('http://127.0.0.1:0000')



class ArticleModelTest(TestCase):

	def test_article_model_save_and_retrieve(self):
		article1 = Article(
			title='article 1',
			full_text='full_text 1',
			summary='summary 1',
			category='category 1',
			pubdate=datetime.now(),
		)
		article1.save()

		article2 = Article(
			title='article 2',
			full_text='full_text 2',
			summary='summary 2',
			category='category 2',
			pubdate=datetime.now(),
		)
		article2.save()

		all_articles = Article.objects.all()


		self.assertEqual(len(all_articles), 2)

		self.assertEqual(
			all_articles[0].title,
			article1.title
		)
		self.assertEqual(
			all_articles[1].title,
			article2.title
		)


if __name__ == 'main' :
	unittest.main()
