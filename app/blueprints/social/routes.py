from . import bp
from app.models import User
from flask import render_template, flash, redirect, url_for
from app.forms import AddMarvelCharacterForm, AddDrinkForm
from app.models import MarvelCharacter, AddDrinks
from flask_login import current_user
from flask_login import login_required


@bp.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.jinja', user=user)

@bp.route('/user/adddrink', methods=['GET', 'POST'])
# @login_required
def adddrink():
    form = AddDrinkForm()
    if form.validate_on_submit():
        drink = AddDrinks(idDrink=form.idDrink.data, strDrink=form.strDrink.data, strDrinkThumb=form.strDrinkThumb.data, owner_id=current_user.token)
        drink.commit()
        flash(f'Drink added', 'success')
        return redirect(url_for('social.user', username=current_user.username))
    return render_template('addDrink.jinja', title= 'addDrink', form=form)

@bp.route('/user/<username>/drinks')
# @login_required
def drinks(username):
    user = User.query.filter_by(username=username).first_or_404()
    drinks = AddDrinks.query.filter_by(owner_id=user.token).all()
    print(drinks)
    return render_template('userDrinks.jinja', user=user, drinks=drinks)

@bp.route('/user/addcharacter', methods=['GET', 'POST'])
# @login_required
def addcharacter():
    form = AddMarvelCharacterForm()
    if form.validate_on_submit():
        character = MarvelCharacter(name=form.name.data, description=form.description.data, comics_appeared_in=form.comics_appeared_in.data, super_power=form.super_power.data, owner_id=current_user.token)
        character.commit()
        flash(f'Character added', 'success')
        return redirect(url_for('social.user', username=current_user.username))
    return render_template('addMarvelCharacter.jinja', title= 'addMarvelCharacter', form=form)

@bp.route('/user/<username>/characters')
# @login_required
def characters(username):
    user = User.query.filter_by(username=username).first_or_404()
    characters = MarvelCharacter.query.filter_by(owner_id=user.token).all()
    return render_template('user.jinja', user=user, characters=characters)