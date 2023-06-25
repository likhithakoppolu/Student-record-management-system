from flask import Flask, render_template, redirect, request


app = Flask(__name__)

# MySQL database configuration
db_config = {
    'user': 'your_username',
    'password': 'your_password',
    'host': 'localhost',
    'database': 'your_database',
    'raise_on_warnings': True
}

# Home page
@app.route('/')
def index():
    return render_template('index.html')

# Student Details page
@app.route('/studentdetails')
def studentdetails():
    try:
        # Connect to the MySQL database
        conn = mysql.connector.connect(**db_config)

        # Create a cursor object to interact with the database
        cursor = conn.cursor()

        # Execute a SQL query to fetch student details from the database
        query = "SELECT * FROM students"
        cursor.execute(query)

        # Fetch all the rows returned by the query
        students = cursor.fetchall()

        # Close the cursor and connection
        cursor.close()
        conn.close()

        # Render the studentdetails.html template with the fetched student details
        return render_template('studentdetails.html', students=students)
    except mysql.connector.Error as error:
        print("Error while connecting to MySQL:", error)
        # Handle the error in an appropriate way

# Exams page
@app.route('/exams')
def exams():
    # Perform any additional logic here
    return render_template('exams.html')

# Results page
@app.route('/results')
def results():
    # Perform any additional logic here
    return render_template('results.html')

# Materials page
@app.route('/materials')
def materials():
    # Perform any additional logic here
    return render_template('materials.html')

if __name__ == '__main__':
    app.run(debug=True)
