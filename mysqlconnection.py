from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'smartmill'

mysql = MySQL(app)


@app.route('/', methods=['POST'])
def index():
    if request.method == "POST":
        details = request.form
        user = details['user']
        message = details['message']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO feature_request(user, message) VALUES (%s, %s)",(user, message))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('session.html')


if __name__ == '__main__':
    app.run()