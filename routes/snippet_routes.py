from flask import Blueprint, request, jsonify
from models import db, Snippet
from datetime import datetime

snippet_bp = Blueprint('snippets', __name__)

@snippet_bp.route('/users/<string:user_id>/snippets', methods=['POST'])
def create_or_update_snippet(user_id):
    data = request.get_json()
    name = data.get('snippet_name')
    language = data.get('language')
    content = data.get('code_content')

    snippet = Snippet.query.filter_by(user_id=user_id, snippet_name=name).first()

    if snippet:
        snippet.language = language
        snippet.code_content = content
        snippet.updated_at = datetime.utcnow()
    else:
        snippet = Snippet(user_id=user_id, snippet_name=name, language=language, code_content=content)
        db.session.add(snippet)

    db.session.commit()

    return jsonify({
        "user_id": user_id,
        "snippet_name": snippet.snippet_name,
        "language": snippet.language,
        "code_content": snippet.code_content,
        "created_at": snippet.created_at,
        "updated_at": snippet.updated_at
    })

@snippet_bp.route('/users/<string:user_id>/snippets', methods=['GET'])
def list_snippets(user_id):
    snippets = Snippet.query.filter_by(user_id=user_id).all()
    return jsonify([
        {
            "snippet_name": s.snippet_name,
            "language": s.language,
            "updated_at": s.updated_at
        } for s in snippets
    ])

@snippet_bp.route('/users/<string:user_id>/snippets/<string:snippet_name>', methods=['GET'])
def get_snippet(user_id, snippet_name):
    snippet = Snippet.query.filter_by(user_id=user_id, snippet_name=snippet_name).first()
    if snippet:
        return jsonify({
            "snippet_name": snippet.snippet_name,
            "language": snippet.language,
            "code_content": snippet.code_content,
            "created_at": snippet.created_at,
            "updated_at": snippet.updated_at
        })
    return jsonify({"error": "Snippet not found"}), 404

@snippet_bp.route('/users/<string:user_id>/snippets/<string:snippet_name>', methods=['DELETE'])
def delete_snippet(user_id, snippet_name):
    snippet = Snippet.query.filter_by(user_id=user_id, snippet_name=snippet_name).first()
    if snippet:
        db.session.delete(snippet)
        db.session.commit()
        return '', 204
    return jsonify({"error": "Snippet not found"}), 404
