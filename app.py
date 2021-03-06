  # from datetime import datetime
# import re, smtplib
# from wtforms import Form, TextField, validators, TextAreaField
from flask import Flask, jsonify, request, flash, url_for, redirect, render_template
# from flask_sqlalchemy import SQLAlchemy
# from email.MIMEText import MIMEText
# from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
# app.config.from_pyfile('app.cfg')
app.config['DEBUG'] = True
# db = SQLAlchemy(app)
#
# class Events(db.Model):
#  __tablename__ = 'events'
#  id = db.Column('event_id', db.Integer, primary_key=True)
#  title = db.Column(db.String(100))
#  author = db.Column(db.String(100))
#  description = db.Column(db.String(200))
#  pub_date = db.Column(db.DateTime)
#
#  def __init__(self, title, author, description):
#      self.title = title
#      self.author = author
#      self.description = description
#      self.pub_date = datetime.now()
#
# class Submit(Form):
#    name = TextField()
#    email = TextField()
#    message = TextAreaField()
#
# def is_email_address_valid(author):
#  """Validate email address using regular expression."""
#  if not re.match("^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$", author):
#      return False
#  return True
# #
# def goGo(name, message, email):
#    whole = "%s <br><br><br><i>This message was from: <b>%s</b>. Their e-mail address is <b>%s</b>.</i>" % (message, name, email)
#
#    msg = MIMEMultipart('alternative')
#    msg['Subject'] = "New message from %s!" % name
#
#    part1 = MIMEText(whole, 'html')
#    msg.attach(part1)
#
#    o = smtplib.SMTP("smtp.gmail.com:587")
#    o.starttls()
#    o.login("jasonrdecastro@gmail.com", "imbeast14")
#    o.sendmail("jasonrdecastro@gmail.com", "jasonrdecastro@gmail.com", msg.as_string())
#    o.close()

@app.route('/', methods=('GET', 'POST'))
def landing():
#    form = Submit(request.form)
#    if request.method == 'POST':
#        goGo(form.name.data, form.message.data, form.email.data)
#        redirect('success')
    return render_template('index.html')#, form=form)


@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/alum')
def alum():
  return render_template('alum.html')

@app.route('/contact')
def contact():
  return render_template('contact.html')

@app.route('/pillars')
def pillars():
  return render_template('pillars.html')

@app.route('/portfolio')
def portfolio():
  return render_template('portfolio.html')

@app.route('/national')
def national():
  return render_template('national.html')

@app.route('/chapter')
def chapter():
  return render_template('chapter.html')

#@app.route('/events')
#def show_all():
#  return render_template('show_all.html')# , events=Events.query.order_by(Events.pub_date.desc()).all()  )

# @app.route('/new', methods=['GET', 'POST'])
# def new():
#    if request.method == 'POST':
#        if not request.form['title'] or not request.form['author'] or not request.form['description']:
#            flash('Please enter all the fields', 'error')

#        elif is_email_address_valid(request.form['author']):
#            flash('Please enter a valid email address', 'error')

#        else:
#            event = Events(request.form['title'],
#                               request.form['author'],
#                               request.form['description'])

#            db.session.add(event)
#            db.session.commit()

#            flash('Event was successfully submitted')

#            return redirect(url_for('show_all'))

   # return render_template('new.html')

# @app.route('/data')
# def names():
#    data = {
#        "first_names": ["John", "Jacob", "Julie", "Jennifer"],
#        "last_names": ["Connor", "Johnson", "Cloud", "Ray"]
#    }
#    return jsonify(data)
#
if __name__ == '__main__':
  app.run(debug=True)
