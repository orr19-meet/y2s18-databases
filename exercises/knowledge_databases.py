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
			session.delete(i)
			session.commit()

def query_article_by_primary_key(id):
	article=session.query(
	    Knowledge).filter_by(article_id=id).first()
	return article

def query_by_top_5():
	articles = session.query(
	    Knowledge).all()
	articles.order_by(Knowledge.rating)
	print("top 5: \n")
	for i in range (5):
		print(articles[i])

delete_all_articles()
add_article("weather", "rainbow", 10)
add_article("food", "sushi", 2)
add_article("weather", "heat", 5)
add_article("meet", "student", 1)
add_article("school", "iasa", 9)
add_article("math", "devision", 8)
add_article("shape", "heart", 9)



# query_article_by_primary_key(1).topic="rain"
# delete_article_by_topic("rainbow")
query_by_top_5()	
#delete_article_by_rating(3)
#edit_article_rating(11,"food")
#delete_all_articles()
print(query_all_articles())	
