from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models import model_user

@app.route('/')
def index():
    users = model_user.User.get_all()
    return render_template('index.html', users = users)
# new user form page

@app.route('/user/new')
def new_user():
    
    return render_template('user_new.html', )

#add new user to database
@app.route('/user/create', methods=["post"])
def create_user():
    id = model_user.User.create(request.form)
    print(id)
    return redirect('/')

# show user info
@app.route('/user/<int:id>')
def show_user(id):
    user = model_user.User.get_one({'id': id})
    return render_template('user_show.html', user = user)

#form for edit user
@app.route('/user/<int:id>/edit')
def edit_user(id):
    context = {
        "user" : model_user.User.get_one({'id': id})
    }
    
    return render_template('user_edit.html', **context)

#update the user(do the edit)
@app.route('/user/<int:id>/update', methods=["post"])
def update_user(id):
    data = {
        **request.form,
        "id": id
    }
    model_user.User.update_one(data)
    return redirect(f"/user/{id}")


#delete user
@app.route('/user/<int:id>/delete')
def delete_user(id):
    model_user.User.delete_one({'id': id})
    return redirect('/')