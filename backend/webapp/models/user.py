from webapp.extensions import db 
from webapp.models.course import Course
from webapp.models.session import Session
from webapp.models.ratings import ArticleRatings

class User(db.Model): 
    __tablename__ = 'user'
    # Define attributes 
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), nullable=False)
    firstname = db.Column(db.String(150), nullable=False)
    lastname = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(30), nullable=False)
    bio = db.Column(db.String(250), server_default='')
    # TODO: Add a table for year in school
    # year_in_school

    # course_of_study = db.Column(db.Integer, db.ForeignKey('course_of_study.id'))
    # course_of_study_id = db.Column(db.Integer, db.ForeignKey('Course_Of_Study.id'))
    # course_of_study = db.relationship('Course_Of_Study', back_populates='user')

    sessions = db.relationship('Session', back_populates='user', order_by='Session.start_time.desc()')

    article_ratings = db.relationship('ArticleRatings', back_populates='user')


    def __repr__(self): 
        return f"User<id={self.id}, email={self.email}, firstname={self.firstname}, lastname={self.lastname}>"
    

    def save(self): 
        # Save a user to a db 
        db.session.add(self)
        db.session.commit()
        db.session.refresh(self)
    
    def verify_password(self, other_password): 
        # TODO: Hash the passwords
        return self.password == other_password

    def get_courses(self): 
        return self.courses
    
    def add_course(self, code): 
        course = Course.find_by_id(code)
        self.courses.append(course)
        self.save()

    def remove_course(self, code): 
        course = Course.find_by_id(code)
        self.courses.remove(course)
        self.save()

    def get_sessions(self, course_code=None): 
        if not course_code: 
            return self.sessions
        return Session.find_course_sessions(self.id, course_code)
    
    def get_articles(self): 
        return self.article_ratings
    
    def add_rating(self, article_id, rating): 
        article_rating = ArticleRatings(user_id=self.id, article_id= article_id, rating = rating)
        self.article_ratings.append(article_rating)
        self.save()
    
    def remove_rating(self, article_id): 
        article_rating = ArticleRatings.find_by_id(self.id, article_id)
        print(article_rating)
        article_rating.remove()
        # self.article_ratings.remove(article_rating)
        # self.save()

    @classmethod
    def find_by_email(cls, email): 
        if not email: 
            return None 
        res = User.query.filter(cls.email == email).first()
        return res 

    @classmethod
    def find_by_id(cls, id): 
        if not id: 
            return None 
        try:
            res = User.query.filter(cls.id == id).first()
        except: 
            return None
        return res

    @classmethod
    def get_users(cls, limit=15): 
        res = cls.query.limit(limit).all()
        return res 
    
    @classmethod
    def remove_by_id(cls, user_id): 
        cls.query.filter(cls.id==user_id).delete()
        db.session.commit()








class Course_Of_Study(db.Model): 
    __tablename__ = 'course_of_study'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    # users = db.relationship('User')

# db.Table('course_of_study',
#     db.Column('id', db.Integer, primary_key=True),
#     db.Column('title', db.String(150), nullable=False),
# )

