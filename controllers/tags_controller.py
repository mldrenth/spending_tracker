from flask import Flask, render_template, redirect, request
from flask import Blueprint
from models.tag import Tag
import repositories.tag_repository as tag_repository

tags_blueprint = Blueprint("tags", __name__)

#New
#Get 
@tags_blueprint.route("/tags/new")
def new_tag():
    return render_template('tags/new.html', title = "Create New Tag")

#POST
@tags_blueprint.route("/tags", methods=['POST'])
def create_tag():
    name = request.form["name"]
    active = "active" in request.form.keys()
    tag = Tag(name, active)
    tag_repository.save(tag)
    return redirect('/')

@tags_blueprint.route("/tags/<id>/edit")
def edit_tag(id):
    tag = tag_repository.select(id)
    return render_template('tags/edit.html', title = "Edit Tag", tag = tag)

@tags_blueprint.route("/tags/<id>", methods = ['POST'])
def update_tag(id):
    name = request.form['name']
    active = "active" in request.form.keys()
    tag = Tag(name,active,id)
    tag_repository.update(tag)
    return redirect('/')
