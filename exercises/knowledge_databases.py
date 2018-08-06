from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article( name, topic, rating):
	    article_object = Knowledge(
	        name=name,
	        topic=topic,
	        rating=rating)
	    session.add(article_object)
	    session.commit()


add_article("weather", "rainbow", 10)

add_article("food", "sushi", 2)
add_article("weather", "heat", 10)

	

def query_all_articles():
	articles = session.query(
	    Knowledge).all()
	return articles


print(query_all_articles())


def query_article_by_topic():
	pass

def delete_article_by_topic():
	pass

def delete_all_articles():
	pass

def edit_article_rating():
	pass
