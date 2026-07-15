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
from app import app, db
from seed_questions import seed as seed_questions
from seed_lessons import seed as seed_lessons
from seed_scenarios import seed as seed_scenarios
from app import User

with app.app_context():
    db.create_all()
    print("Tables created.")

seed_questions()
seed_lessons()
seed_scenarios()

# Ensure admin account is set
with app.app_context():
    admin_user = User.query.filter_by(email='shehuwaliismail@gmail.com').first()
    if admin_user:
        admin_user.is_admin = True
        db.session.commit()
        print(f"Admin privileges set for {admin_user.full_name}")
    else:
        print("Admin email not found yet — register on the live site first, then redeploy.")