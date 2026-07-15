import secrets
import string
import os
from dotenv import load_dotenv
load_dotenv()
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-only-fallback-key-change-me')

database_url = os.environ.get('DATABASE_URL', 'sqlite:///cyberaware.db')
if database_url.startswith('postgres://'):
    database_url = database_url.replace('postgres://', 'postgresql://', 1)
app.config['SQLALCHEMY_DATABASE_URI'] = database_url

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
bcrypt = Bcrypt(app)

# ---------- MODELS ----------

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    department = db.Column(db.String(100))
    level = db.Column(db.String(20))
    is_admin = db.Column(db.Boolean, default=False)

class QuizResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    category = db.Column(db.String(50))
    score = db.Column(db.Integer)
    total_questions = db.Column(db.Integer)
    test_type = db.Column(db.String(10))
    date_taken = db.Column(db.DateTime, server_default=db.func.now())

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50), nullable=False)
    question_text = db.Column(db.Text, nullable=False)
    option_a = db.Column(db.String(255), nullable=False)
    option_b = db.Column(db.String(255), nullable=False)
    option_c = db.Column(db.String(255), nullable=False)
    option_d = db.Column(db.String(255), nullable=False)
    correct_option = db.Column(db.String(1), nullable=False)
    explanation = db.Column(db.Text)
    weight = db.Column(db.Integer, default=1)
    test_type = db.Column(db.String(10), nullable=False)
    pair_id = db.Column(db.Integer)

class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50), nullable=False, unique=True)
    title = db.Column(db.String(150), nullable=False)
    icon = db.Column(db.String(10))
    summary = db.Column(db.String(255))
    content = db.Column(db.Text, nullable=False)

class QuizAnswer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quiz_result_id = db.Column(db.Integer, db.ForeignKey('quiz_result.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    is_correct = db.Column(db.Boolean, default=False)
    weight = db.Column(db.Integer, default=1)

class Scenario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50), nullable=False)
    title = db.Column(db.String(150), nullable=False)
    icon = db.Column(db.String(10))
    story = db.Column(db.Text, nullable=False)
    option_a = db.Column(db.String(255), nullable=False)
    option_b = db.Column(db.String(255), nullable=False)
    option_c = db.Column(db.String(255), nullable=False)
    option_d = db.Column(db.String(255), nullable=False)
    outcome_a = db.Column(db.Text, nullable=False)
    outcome_b = db.Column(db.Text, nullable=False)
    outcome_c = db.Column(db.Text, nullable=False)
    outcome_d = db.Column(db.Text, nullable=False)
    points_a = db.Column(db.Integer, default=0)
    points_b = db.Column(db.Integer, default=0)
    points_c = db.Column(db.Integer, default=0)
    points_d = db.Column(db.Integer, default=0)

class ScenarioResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    scenario_id = db.Column(db.Integer, db.ForeignKey('scenario.id'), nullable=False)
    points_earned = db.Column(db.Integer)
    choice_made = db.Column(db.String(1))
    date_taken = db.Column(db.DateTime, server_default=db.func.now())

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

# ---------- BADGES ----------

BADGE_INFO = {
    "Phishing": {"name": "Phishing Defender", "icon": "🎣"},
    "Password & MFA": {"name": "Password Guardian", "icon": "🔐"},
    "Mobile Security": {"name": "Mobile Protector", "icon": "📱"},
    "Malware & Browsing": {"name": "Malware Buster", "icon": "🛡️"},
    "Social Media & Privacy": {"name": "Privacy Advocate", "icon": "🔒"},
    "Financial Scams": {"name": "Scam Spotter", "icon": "💰"},
    "Data Privacy": {"name": "Identity Protector", "icon": "🪪"},
    "Incident Response": {"name": "Rapid Responder", "icon": "🚨"},
}

def get_user_badges(user_id):
    categories = [row[0] for row in db.session.query(QuizAnswer.category).filter_by(user_id=user_id).distinct()]
    badges = []
    for cat in categories:
        answers = QuizAnswer.query.filter_by(user_id=user_id, category=cat).all()
        if not answers:
            continue
        correct = sum(1 for a in answers if a.is_correct)
        total = len(answers)
        percentage = (correct / total) * 100 if total else 0
        if percentage >= 80 and cat in BADGE_INFO:
            badges.append(BADGE_INFO[cat])
    return badges

def generate_temp_password(length=8):
    chars = string.ascii_letters + string.digits
    return ''.join(secrets.choice(chars) for _ in range(length))

# ---------- ROUTES ----------

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        full_name = request.form['full_name']
        email = request.form['email']
        password = request.form['password']
        department = request.form['department']
        level = request.form['level']

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already registered. Please log in instead.')
            return redirect(url_for('register'))

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        new_user = User(
            full_name=full_name,
            email=email,
            password=hashed_password,
            department=department,
            level=level
        )
        db.session.add(new_user)
        db.session.commit()

        flash('Account created successfully! Please log in.')
        return redirect(url_for('home'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()

        if user and bcrypt.check_password_hash(user.password, password):
            remember = True if request.form.get('remember') else False
            login_user(user, remember=remember)
            flash(f'Welcome back, {user.full_name}!')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid email or password. Please try again.')
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('home'))

@app.route('/dashboard')
@login_required
def dashboard():
    pre_result = QuizResult.query.filter_by(user_id=current_user.id, test_type='pre').order_by(QuizResult.date_taken.desc()).first()
    post_result = QuizResult.query.filter_by(user_id=current_user.id, test_type='post').order_by(QuizResult.date_taken.desc()).first()
    all_results = QuizResult.query.filter_by(user_id=current_user.id).order_by(QuizResult.date_taken.desc()).all()
    badges = get_user_badges(current_user.id)

    quiz_points = db.session.query(db.func.sum(QuizResult.score)).filter_by(user_id=current_user.id).scalar() or 0
    scenario_points = db.session.query(db.func.sum(ScenarioResult.points_earned)).filter_by(user_id=current_user.id).scalar() or 0
    total_points = quiz_points + scenario_points

    return render_template('dashboard.html',
                            pre_result=pre_result,
                            post_result=post_result,
                            all_results=all_results,
                            badges=badges,
                            total_points=total_points)

@app.route('/quiz/<test_type>', methods=['GET', 'POST'])
@login_required
def quiz(test_type):
    if test_type not in ['pre', 'post']:
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        questions = Question.query.filter_by(test_type=test_type).all()
        total_score = 0
        max_score = 0
        correct_count = 0

        result = QuizResult(
            user_id=current_user.id,
            category='All',
            score=0,
            total_questions=len(questions),
            test_type=test_type
        )
        db.session.add(result)
        db.session.flush()

        for q in questions:
            max_score += q.weight
            submitted = request.form.get(f'question_{q.id}')
            is_correct = (submitted == q.correct_option)
            if is_correct:
                total_score += q.weight
                correct_count += 1

            answer = QuizAnswer(
                quiz_result_id=result.id,
                user_id=current_user.id,
                category=q.category,
                is_correct=is_correct,
                weight=q.weight
            )
            db.session.add(answer)

        result.score = total_score
        db.session.commit()

        percentage = round((total_score / max_score) * 100, 1) if max_score > 0 else 0
        return render_template('quiz_result.html', score=total_score, max_score=max_score,
                                percentage=percentage, correct_count=correct_count,
                                total_questions=len(questions), test_type=test_type)

    questions = Question.query.filter_by(test_type=test_type).all()
    return render_template('quiz.html', questions=questions, test_type=test_type)

@app.route('/learn')
@login_required
def learn():
    lessons = Lesson.query.all()
    return render_template('learn.html', lessons=lessons)

@app.route('/learn/<category>')
@login_required
def lesson_detail(category):
    lesson = Lesson.query.filter_by(category=category).first_or_404()
    return render_template('lesson_detail.html', lesson=lesson)

@app.route('/scenarios')
@login_required
def scenarios_list():
    all_scenarios = Scenario.query.all()
    completed_ids = [r.scenario_id for r in ScenarioResult.query.filter_by(user_id=current_user.id).all()]
    return render_template('scenarios.html', scenarios=all_scenarios, completed_ids=completed_ids)

@app.route('/scenario/<int:scenario_id>', methods=['GET', 'POST'])
@login_required
def scenario_play(scenario_id):
    scenario = Scenario.query.get_or_404(scenario_id)

    if request.method == 'POST':
        choice = request.form.get('choice')
        points_map = {'A': scenario.points_a, 'B': scenario.points_b, 'C': scenario.points_c, 'D': scenario.points_d}
        outcome_map = {'A': scenario.outcome_a, 'B': scenario.outcome_b, 'C': scenario.outcome_c, 'D': scenario.outcome_d}
        points = points_map.get(choice, 0)
        outcome_text = outcome_map.get(choice, '')

        result = ScenarioResult(
            user_id=current_user.id,
            scenario_id=scenario.id,
            points_earned=points,
            choice_made=choice
        )
        db.session.add(result)
        db.session.commit()

        return render_template('scenario_result.html', scenario=scenario, points=points, outcome_text=outcome_text)

    return render_template('scenario_play.html', scenario=scenario)

@app.route('/leaderboard')
@login_required
def leaderboard():
    all_students = User.query.filter_by(is_admin=False).all()
    board = []
    for student in all_students:
        quiz_points = db.session.query(db.func.sum(QuizResult.score)).filter_by(user_id=student.id).scalar() or 0
        scenario_points = db.session.query(db.func.sum(ScenarioResult.points_earned)).filter_by(user_id=student.id).scalar() or 0
        total_points = quiz_points + scenario_points
        badge_count = len(get_user_badges(student.id))
        board.append({
            'user_id': student.id,
            'name': student.full_name,
            'total_points': total_points,
            'badge_count': badge_count,
            'is_you': student.id == current_user.id
        })

    board.sort(key=lambda x: x['total_points'], reverse=True)
    for i, entry in enumerate(board):
        entry['rank'] = i + 1
        entry['display_name'] = f"{entry['name']} (You)" if entry['is_you'] else entry['name']

    return render_template('leaderboard.html', board=board)

@app.route('/admin')
@login_required
def admin_dashboard():
    if not current_user.is_admin:
        flash('Access denied. Admin only.')
        return redirect(url_for('dashboard'))

    total_users = User.query.filter_by(is_admin=False).count()
    pre_results = QuizResult.query.filter_by(test_type='pre').all()
    post_results = QuizResult.query.filter_by(test_type='post').all()

    avg_pre = round(sum(r.score for r in pre_results) / len(pre_results), 1) if pre_results else 0
    avg_post = round(sum(r.score for r in post_results) / len(post_results), 1) if post_results else 0

    students_with_both = []
    all_students = User.query.filter_by(is_admin=False).all()
    for student in all_students:
        pre = QuizResult.query.filter_by(user_id=student.id, test_type='pre').order_by(QuizResult.date_taken.desc()).first()
        post = QuizResult.query.filter_by(user_id=student.id, test_type='post').order_by(QuizResult.date_taken.desc()).first()
        students_with_both.append({
            'id': student.id,
            'name': student.full_name,
            'email': student.email,
            'department': student.department,
            'level': student.level,
            'pre_score': pre.score if pre else None,
            'post_score': post.score if post else None,
            'improvement': (post.score - pre.score) if (pre and post) else None
        })

    return render_template('admin.html',
                            total_users=total_users,
                            pre_count=len(pre_results),
                            post_count=len(post_results),
                            avg_pre=avg_pre,
                            avg_post=avg_post,
                            students=students_with_both)

@app.route('/admin/delete/<int:user_id>', methods=['POST'])
@login_required
def delete_user(user_id):
    if not current_user.is_admin:
        flash('Access denied. Admin only.')
        return redirect(url_for('dashboard'))

    user_to_delete = User.query.get_or_404(user_id)
    if user_to_delete.is_admin:
        flash('Cannot delete an admin account.')
        return redirect(url_for('admin_dashboard'))

    QuizResult.query.filter_by(user_id=user_id).delete()
    db.session.delete(user_to_delete)
    db.session.commit()
    flash(f'Deleted {user_to_delete.full_name} and their quiz results.')
    return redirect(url_for('admin_dashboard'))

@app.route('/admin/reset-password/<int:user_id>', methods=['POST'])
@login_required
def reset_password(user_id):
    if not current_user.is_admin:
        flash('Access denied. Admin only.')
        return redirect(url_for('dashboard'))

    user = User.query.get_or_404(user_id)
    temp_password = generate_temp_password()
    user.password = bcrypt.generate_password_hash(temp_password).decode('utf-8')
    db.session.commit()

    flash(f'New temporary password for {user.full_name}: {temp_password} — share this with them securely.')
    return redirect(url_for('admin_dashboard'))

if __name__ == '__main__':
    app.run(debug=True)