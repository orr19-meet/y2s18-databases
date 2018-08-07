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
	

def query_all_articles():
	articles = session.query(
	    Knowledge).all()
	return articles


#print(query_all_articles())


def query_article_by_topic(topic):
	articles = session.query(
	    Knowledge).filer_by(topic=topic).all()
	return articles
	

def delete_article_by_topic(topic):
	session.query(
	    Knowledge).filter_by(topic=topic).delete()
	session.commit()
add_article("weather", "rainbow", 10)

add_article("food", "sushi", 2)
add_article("weather", "heat", 5)

delete_article_by_topic("rainbow")
	
def delete_all_articles():
	articles = session.query(
	    Knowledge).delete()
	session.commit()

def edit_article_rating(updated_rating,name ):
	article=session.query(
	    Knowledge).filter_by(name=name).first()
	article.rating=updated_rating
	session.commit()

def delete_article_by_rating(threshold):
	articles = session.query(
	    Knowledge).all()
	for i in articles:
		if(i.rating<threshold):
			articles[i].delete()
			session.commit()

delete_article_by_rating(3)
#edit_article_rating(11,"food")
#delete_all_articles()
print(query_all_articles())	
