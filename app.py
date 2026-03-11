# app.py — Kenya Home Energy-Saving Advisor

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
        'name':             request.form['name'],
        'monthly_bill_ksh': float(request.form['monthly_bill_ksh']),
        'home_size':        request.form['home_size'],
        'bulb_type':        request.form['bulb_type'],
        'has_ac':           request.form.get('has_ac') == 'on',
        'appliance_age':    request.form['appliance_age'],
        'cooking_fuel':     request.form['cooking_fuel'],
        'has_geyser':       request.form.get('has_geyser') == 'on',
    }

    conn = get_connection()
    cursor = conn.execute(
        '''INSERT INTO households
           (name, monthly_bill_ksh, home_size, bulb_type, has_ac,
            appliance_age, cooking_fuel, has_geyser)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
        (profile['name'], profile['monthly_bill_ksh'], profile['home_size'],
         profile['bulb_type'], profile['has_ac'], profile['appliance_age'],
         profile['cooking_fuel'], profile['has_geyser'])
    )
    household_id = cursor.lastrowid

    tips = get_recommendations(profile)

    for tip in tips:
        conn.execute(
            'INSERT INTO recommendations (household_id, tip, category, priority) VALUES (?, ?, ?, ?)',
            (household_id, tip['tip'], tip['category'], tip['priority'])
        )
    conn.commit()
    conn.close()

    return render_template('results.html', name=profile['name'], tips=tips)

if __name__ == '__main__':
    app.run(debug=True)