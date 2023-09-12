from project import db, create_app, models

# Initialize the Flask app
app = create_app()


# Create the database tables
with app.app_context():
    db.create_all()
