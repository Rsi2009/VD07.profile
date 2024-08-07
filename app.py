from flask import Flask, render_template, redirect, url_for, flash, request  # Добавить импорт request
from config import Config
from forms import EditProfileForm
from models import current_user

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    form = EditProfileForm()

    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.password = form.password.data
        flash('Your profile has been updated!', 'success')
        return redirect(url_for('edit_profile'))

    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email

    return render_template('edit_profile.html', title='Edit Profile', form=form)

if __name__ == '__main__':
    app.run(debug=True)
