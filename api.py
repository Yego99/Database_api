from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

#Function to connect to database
def get_db_connection():
    conn = sqlite3.connect('timesheet_data.db')
    conn.row_factory = sqlite3.Row  # This allows us to return rows as dictionaries
    return conn

#Serve HTML page
@app.route('/')
def index():
    return render_template('fe.HTML')

#End point 1: Get all entries from db
@app.route('/timesheet_entries', methods=['GET'])
def get_all_entries():
    conn = get_db_connection()
    timesheets = conn.execute('SELECT * FROM timesheets').fetchall()
    conn.close()
    # Convert rows into a list of dictionaries
    return jsonify([dict(row) for row in timesheets])
 
#End point 2: Get timesheets by client parameter based
@app.route('/timesheet_entries/<client>', methods=['GET'])
def get_timesheets_by_client(client):
    conn = get_db_connection()
    timesheets = conn.execute('SELECT * FROM timesheets WHERE client = ?', (client,)).fetchall()
    conn.close()
    # Convert rows into a list of dictionaries
    return jsonify([dict(row) for row in timesheets])
    
#End point 3: Create a new timesheet entry
@app.route('/timesheet_entries', methods=['POST'])
def create_entry():
    new_entry = request.get_json()
    # Extract data from JSON payload
    name = new_entry.get('name')
    client = new_entry.get('client')
    hours = new_entry.get('hours')
    billable_rate = new_entry.get('Billable Rate')
    billable_amount = new_entry.get('billable_amount')
# Insert into database
    conn = get_db_connection()
    conn.execute('''
        INSERT INTO timesheets (name, client, hours, "Billable Rate", billable_amount)
        VALUES (?, ?, ?, ?, ?)
    ''', (name, client, hours, billable_rate, billable_amount))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Timesheet entry created successfully!'}), 201

#For search bar look ups
@app.route('/timesheet_entries/search', methods=['GET'])
def search_by_client():
    client = request.args.get('client')  # Get the 'client' query parameter
    conn = get_db_connection()
    timesheets = conn.execute('SELECT * FROM timesheets WHERE client = ?', (client,)).fetchall()
    conn.close()
    return jsonify([dict(row) for row in timesheets])



if __name__ == '__main__':
    app.run(debug=True)




















