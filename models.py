from app import db

# Define Project model
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    image_url = db.Column(db.String(500), nullable=False)
    link = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f"Project('{self.title}', '{self.description}')"

# To create the database (run this once)
if __name__ == "__main__":
    db.create_all()

