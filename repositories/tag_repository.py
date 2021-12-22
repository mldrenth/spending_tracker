from pdb import run
from db.run_sql import run_sql

from models.tag import Tag

#CREATE
def save(tag):
    sql="INSERT INTO tags (name, active) VALUES (%s, %s) RETURNING *"
    values = [tag.name, tag.active]
    results = run_sql(sql, values)
    id = results[0]['id']
    tag.id = id
    return tag

#SELECT ALL
def select_all():
    tags = []
    sql= "SELECT * FROM tags"
    results = run_sql(sql)
    for row in results:
        tag = Tag(row['name'], row['active'], row['id'])
        tags.append(tag)
    return tags


#SELECT BY ID
def select(id):
    tag = None
    sql = "SELECT * FROM tags WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        tag = Tag(result['name'], result['active'], result['id'])
    return tag

#DELETE ALL
def delete_all():
    sql = "DELETE FROM tags"
    run_sql(sql)