import random
from app import app, db, Question, Scenario

def fix_questions():
    questions = Question.query.all()
    letters = ['A', 'B', 'C', 'D']
    for q in questions:
        new_correct = random.choice(letters)
        options = {
            'A': q.option_a, 'B': q.option_b,
            'C': q.option_c, 'D': q.option_d
        }
        options[new_correct], options[q.correct_option] = options[q.correct_option], options[new_correct]
        q.option_a, q.option_b, q.option_c, q.option_d = options['A'], options['B'], options['C'], options['D']
        q.correct_option = new_correct
    db.session.commit()
    print(f"Fixed {len(questions)} questions.")

def fix_scenarios():
    scenarios = Scenario.query.all()
    letters = ['A', 'B', 'C', 'D']
    for s in scenarios:
        current = {
            'A': (s.option_a, s.outcome_a, s.points_a),
            'B': (s.option_b, s.outcome_b, s.points_b),
            'C': (s.option_c, s.outcome_c, s.points_c),
            'D': (s.option_d, s.outcome_d, s.points_d),
        }
        shuffled_letters = letters.copy()
        random.shuffle(shuffled_letters)
        new_map = {}
        for new_letter, old_letter in zip(letters, shuffled_letters):
            new_map[new_letter] = current[old_letter]

        s.option_a, s.outcome_a, s.points_a = new_map['A']
        s.option_b, s.outcome_b, s.points_b = new_map['B']
        s.option_c, s.outcome_c, s.points_c = new_map['C']
        s.option_d, s.outcome_d, s.points_d = new_map['D']
    db.session.commit()
    print(f"Fixed {len(scenarios)} scenarios.")

if __name__ == '__main__':
    with app.app_context():
        fix_questions()
        fix_scenarios()