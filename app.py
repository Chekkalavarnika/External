from flask import Flask,render_template,request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('registration.html')
@app.route('/register', methods=['POST'])
def register():
    Name=request.form['Name']
    Student_Id=request.form['Student_Id']
    Email=request.form['Email']
    Year=request.form['Year']
    return render_template(
        successful.html
        name=name
        student_id=student_id
        email=email
        year=year
    )
if__main__="__name__"
app.run(host='0.0.0.0' port=5000 debug=True)

