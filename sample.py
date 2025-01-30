from app import db
from models import Project

# Add sample projects
project1 = Project(title="Web App", description="A web application built with Flask.", image_url="link-to-image", link="https://example.com")
project2 = Project(title="Machine Learning", description="A machine learning model for prediction.", image_url="link-to-image", link="https://example.com")

# Add projects to the database
db.session.add(project1)
db.session.add(project2)
db.session.commit()

# Verify the entries
print(Project.query.all())
