from flask import Flask, render_template

#create flask object
app = Flask(__name__)

#decorater for homepage and about page
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about/')
def about():
    return render_template('about.html')

#case 1
#when you execute python file , python assigns __name__ == '__main__' to the file
if __name__ == '__main__':
    app.run(debug=True)      

#'case 2'
#when you import script into another script  , __name__ == 'name of file'
#in this page there is no run, so we can control over the script using this line