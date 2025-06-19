import pytest
from app import create_app, db
from models.user import User
from models.post import Post

@pytest.fixture
def app():
    """Create application for testing"""
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    """Create test client"""
    return app.test_client()

@pytest.fixture
def runner(app):
    """Create test runner"""
    return app.test_cli_runner()

def test_index_route(client):
    """Test main index route"""
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert 'message' in data
    assert data['message'] == 'Welcome to Flask Boilerplate API'

def test_health_check(client):
    """Test health check endpoint"""
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'

def test_api_docs(client):
    """Test API documentation endpoint"""
    response = client.get('/docs')
    assert response.status_code == 200
    data = response.get_json()
    assert 'endpoints' in data

def test_create_user(client):
    """Test user creation"""
    user_data = {
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'password123',
        'first_name': 'Test',
        'last_name': 'User'
    }
    
    response = client.post('/api/users', json=user_data)
    assert response.status_code == 201
    data = response.get_json()
    assert 'user' in data
    assert data['user']['username'] == 'testuser'
    assert data['user']['email'] == 'test@example.com'

def test_get_users(client):
    """Test getting all users"""
    response = client.get('/api/users')
    assert response.status_code == 200
    data = response.get_json()
    assert 'users' in data
    assert 'count' in data

def test_create_post(client):
    """Test post creation"""
    # First create a user
    user_data = {
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'password123'
    }
    client.post('/api/users', json=user_data)
    
    # Then create a post
    post_data = {
        'title': 'Test Post',
        'content': 'This is a test post content.',
        'slug': 'test-post',
        'author_id': 1,
        'is_published': True
    }
    
    response = client.post('/api/posts', json=post_data)
    assert response.status_code == 201
    data = response.get_json()
    assert 'post' in data
    assert data['post']['title'] == 'Test Post'

def test_get_posts(client):
    """Test getting all posts"""
    response = client.get('/api/posts')
    assert response.status_code == 200
    data = response.get_json()
    assert 'posts' in data
    assert 'count' in data 