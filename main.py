from flask import Flask, render_template, url_for

app = Flask(__name__)

# здесь будут браться значения из базы данных в будущем

activity_list = [ 
    100, 150, 240, 200, 150
 ] 

@app.route('/')
def hello():
    return render_template('main.html', title = "Main page", activity_list = activity_list) 

@app.route('/pomodoro')
def pomodoro_timer():
    return render_template('pomodoro.html', title = "Pomodoro")

if __name__ == '__main__':
    app.run(debug=True)