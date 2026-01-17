from flask import Flask, render_template
import app1
import app2
import app3
import app4

app = Flask(__name__)
application = app

# Main menu route
@app.route('/')
def main_menu():
    return render_template('index.html')

# Register the app routes
@app.route('/app1', methods=['GET', 'POST'])
def run_app1():
    return app1.app1()

@app.route('/app2', methods=['GET', 'POST'])
def run_app2():
    return app2.app2()

@app.route('/app3', methods=['GET', 'POST'])
def run_app3():
    return app3.app3()

@app.route('/app4', methods=['GET', 'POST'])
def run_app4():
    return app4.app4()


if __name__ == '__main__':
    app.run(debug=True)
