from flask import Blueprint, jsonify
from flask import request
from app import db
from app.mod_note.model import Note
from flask_jwt import jwt_required, current_identity


mod_note = Blueprint('note', __name__, url_prefix='/api')


@mod_note.route('/note', methods=['GET'])
@jwt_required()
def get_notes():
    notes = Note.query.filter_by(user_id=current_identity.id).all()
    return jsonify(notes=[n.serialize() for n in notes]), 200


@mod_note.route('/note', methods=['POST'])
@jwt_required()
def post_note():
    data = request.get_json(True)
    note = Note(data['title'], data['content'], data['category_id'], current_identity.id)
    db.session.add(note)
    db.session.commit()
    return jsonify(message="Note created"), 201


@mod_note.route('/note/<int:note_id>', methods=['GET'])
@jwt_required()
def get_note(note_id):
    note = Note.query.filter_by(id=note_id).first()
    if note:
        return jsonify(note.serialize()), 200
    return jsonify(status="Not found"), 404


@mod_note.route('/note/<int:note_id>', methods=['DELETE'])
@jwt_required()
def delete_note(note_id):
    note = Note.query.filter_by(id=note_id).first()
    if note and not note.is_owned_by(current_identity.id):
        return jsonify(error="You can only delete your notes"), 403
    if note:
        db.session.remove(note)
        db.session.commit()
        return jsonify(status="Note removed"), 200
    return jsonify(status="Not found"), 404


@mod_note.route('/note/<int:note_id>', methods=['PUT'])
@jwt_required
def update_note(note_id):
    data = request.get_json(True)
    note = Note.query.filter_by(id=note_id).first()
    if not note:
        return jsonify(status="Not found"), 404
    if data['title'] and len(data['title']) > 0:
        note.title = data['title']
    if data['content'] and len(data['content']):
        note.content = data['content']
    if data['category_id'] and len(data['category_id']) > 0:
        note.category_id = data['category_id']

    db.session.update(note)
