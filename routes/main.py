from flask import Blueprint, jsonify, render_template_string

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """Main index route"""
    return jsonify({
        'message': 'Welcome to Flask Boilerplate API',
        'version': '1.0.0',
        'status': 'running'
    })

@main_bp.route('/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': '2024-01-01T00:00:00Z'
    })

@main_bp.route('/docs')
def api_docs():
    """API documentation endpoint"""
    return jsonify({
        'endpoints': {
            'GET /': 'Welcome message',
            'GET /health': 'Health check',
            'GET /api/users': 'Get all users',
            'POST /api/users': 'Create new user',
            'GET /api/users/<id>': 'Get user by ID',
            'PUT /api/users/<id>': 'Update user',
            'DELETE /api/users/<id>': 'Delete user',
            'GET /api/posts': 'Get all posts',
            'POST /api/posts': 'Create new post',
            'GET /api/posts/<id>': 'Get post by ID',
            'PUT /api/posts/<id>': 'Update post',
            'DELETE /api/posts/<id>': 'Delete post'
        }
    }) 