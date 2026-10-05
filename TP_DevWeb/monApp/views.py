from .app import app
from flask import render_template, request

@app.route('/')
def index():
    return "Hello world !"


@app.route('/about/')
def about():
    return render_template("about.html", title="R3.01 Dev Web avec Flask", name=app.config['ABOUT'])

@app.route('/contact/')
def contact():
    return render_template("contact.html", title="R3.01 Dev Web avec Flask", name=app.config['CONTACT'])

if __name__ == "__main__":
    app.run()


from flask import render_template, request

@app.route('/')
@app.route('/index/')
def index_page():
    if len(request.args) == 0:
        return render_template("index.html",title ="R3.01 Dev Web avec Flask",name="Cricri")
    else:
        param_name = request.args.get('name')
        return render_template("index.html",title="R3.01 Dev Web avec Flask",name=param_name)
