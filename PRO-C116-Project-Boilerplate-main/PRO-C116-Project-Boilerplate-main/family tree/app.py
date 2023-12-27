# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "rohan" 
    age = "14" 

    return render_template('index.html' , name = name , age = age)


@app.route('/father')
def father():
    name='rohit'
    age='50'
    return render_template('father.html', name = name, age = age)
@app.route('/mother')
def mother():
    name="suman"
    age="49"
    return render_template('mother.html', name = name, age= age )

@app.route('/friend')
def friend():
    name="yadu"
    age="15"
    return render_template('friend.html', name = name, age = age)





# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
