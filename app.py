from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define database model
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    image_url = db.Column(db.String(500), nullable=False)
    link = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f"Project('{self.title}', '{self.description}')"

# Initialize database
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    #projects = Project.query.all()  # Fetch all projects from database
    return render_template('index.html') #, projects=projects)

# About Page Route
@app.route('/about')
def about():
    return render_template('about.html')

# Sample project data
project_list = [
    {
        "title": "Object Detection with YOLOv8",
        "description": "A deep learning-based object detection project using YOLOv8 on Jetson Nano.",
        "link": "https://github.com/your-repo/object-detection",
        #"image_url": "static/images/yolo_project.jpg"
    },
    {
        "title": "Visual SLAM with Stereo Camera",
        "description": "A ROS 2-based SLAM navigation system using a stereo camera and Jetson Orin Nano.",
        "link": "https://github.com/your-repo/visual-slam",
        #"image_url": "static/images/slam_project.jpg"
    },
    {
        "title": "Autonomous Robot in Gazebo",
        "description": "A differential drive robot simulation in Gazebo with Nav2 for autonomous path planning.",
        "link": "https://github.com/your-repo/gazebo-nav2",
        #"image_url": "static/images/robot_project.jpg"
    }
]


# Projects Page Route
@app.route('/projects')
def projects():
    #projects = Project.query.all()
    print("Projects type:", type(project_list))  # Check if it's a list
    print("Projects data:", project_list) 
    return render_template('projects.html', projects=project_list)

# Contact Page Route
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)

