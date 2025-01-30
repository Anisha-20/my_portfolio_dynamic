# Create and activate a virtual environment (optional but recommended)
python3 -m venv portfolio-env
source portfolio-env/bin/activate  # On Windows, use portfolio-env\Scripts\activate

# Install Flask and other dependencies
pip install flask flask_sqlalchemy

# Install additional packages for frontend (like Jinja2 for templating, which is included with Flask)
pip install flask-bootstrap

