# Import
from newscatcher import Newscatcher

# URL
news_source = Newscatcher('nytimes.com')
last_news_list = news_source.news

# Article attributes
article = last_news_list[0]
article.keys()
#dict_keys(['title', 'title_detail', 'links', 'link', 'id', 'guidislink', 'summary', 'summary_detail', 'published', 'published_parsed', 'tags', 'media_content', 'media_credit', 'credit'])