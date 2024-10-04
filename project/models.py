from project.app import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    text = db.Column(db.String, nullable=False)

    def __init__(self, title, text):
        self.title = title
        self.text = text
        # so why is id not added to self? - this is just for the class constructor 
        # and for initialization of the class instance;

    def __repr__(self):
        return f'<title {self.title}>'
