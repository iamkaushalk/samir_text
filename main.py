from flask import Flask, render_template, request, session, redirect
from flask_socketio import SocketIO, emit
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config[ 'SECRET_KEY' ] = 'key'
socketio = SocketIO( app )
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost/smartmill'
db = SQLAlchemy(app)

class Message(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  user = db.Column(db.String(12), nullable=False)
  message = db.Column(db.String(255), nullable=False)

@app.route( '/session' , methods = ['GET', 'POST'])
def hello():
      if(request.method=='POST'):
        user = request.form.get('user')
        msg = request.form.get('msg')
        entry = Message( name=name, message=msg )
        db.session.add(entry)
        db.session.commit()
      return render_template( 'session.html' )  

def messageRecived():
  print( 'message was received!!!' )

@socketio.on( 'my event' )
def handle_my_custom_event( json ):
  print( 'recived my event: ' + str( json ) )
  socketio.emit( 'my response', json, callback=messageRecived )

if __name__ == '__main__':
  socketio.run( app, debug = True )