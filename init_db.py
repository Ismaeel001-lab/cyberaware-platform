from app import app, db
from seed_questions import seed as seed_questions
from seed_lessons import seed as seed_lessons
from seed_scenarios import seed as seed_scenarios

with app.app_context():
    db.create_all()
    print("Tables created.")

seed_questions()
seed_lessons()
seed_scenarios()