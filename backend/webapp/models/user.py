from webapp.extensions import db 


class User(db.Model): 
    __tablename__ = 'user'
    # Define attributes 
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), nullable=False)
    firstname = db.Column(db.String(150), nullable=False)
    lastname = db.Column(db.String(150), nullable=False)
    bio = db.Column(db.String(250), server_default='')
    # TODO: Add a table for year in school
    # year_in_school

    # course_of_study = db.Column(db.Integer, db.ForeignKey('course_of_study.id'))
    course_of_study_id = db.Column(db.Integer, db.ForeignKey('course_of_study.id'))
    course_of_study = db.relationship('course_of_study', back_populates='users')

    user = db.relationship('study_block', backref='user', lazy=True)
    # TODO: Add relatioonship for course (course-form/ registered-courses)

    def __repr__(self): 
        return f""


db.Table('course_of_study',
    db.Column('id', db.Integer, primary_key=True),
    db.Column('title', db.String(150), nullable=False),
)
