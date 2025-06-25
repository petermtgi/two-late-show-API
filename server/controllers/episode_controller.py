from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from server.models import Episode, Appearance, db

bp = Blueprint('episodes', __name__)

@bp.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([episode.to_dict() for episode in episodes]), 200

@bp.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get_or_404(id)
    appearances = [appearance.to_dict() for appearance in episode.appearances]
    return jsonify({"episode": episode.to_dict(), "appearances": appearances}), 200

@bp.route('/episodes/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_episode(id):
    episode = Episode.query.get_or_404(id)
    db.session.delete(episode)
    db.session.commit()
    return jsonify({"message": "Episode deleted"}), 200