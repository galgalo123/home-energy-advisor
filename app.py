from flask import Flask, render_template, request
from database import get_connection, create_tables
from rule_engine import get_recommendations

app = Flask(__name__)
create_tables()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    profile = {
        'name': request.form['name'],
        'monthly_bill': float(request.form['monthly_bill']),
        'home_size': request.form['home_size'],
        'bulb_type': request.form['bulb_type'],
        'has_ac': request.form.get('has_ac') == 'on',
        'appliance_age': request.form['appliance_age']
    }

    conn = get_connection()
    cursor = conn.execute(
        'INSERT INTO households (name, monthly_bill, home_size, bulb_type, has_ac, appliance_age) VALUES (?,?,?,?,?,?)',
        (profile['name'], profile['monthly_bill'], profile['home_size'],
         profile['bulb_type'], profile['has_ac'], profile['appliance_age'])
    )
    household_id = cursor.lastrowid

    tips = get_recommendations(profile)

    for tip in tips:
        conn.execute('INSERT INTO recommendations (household_id, tip) VALUES (?,?)',
                     (household_id, tip))
    conn.commit()
    conn.close()

    return render_template('results.html', name=profile['name'], tips=tips)

if __name__ == '__main__':
    app.run(debug=True)