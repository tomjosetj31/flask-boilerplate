# Flask Boilerplate

A modern Flask boilerplate template with SQLAlchemy, Alembic migrations, and a clean project structure.

## Features

- **Flask 3.0** with application factory pattern
- **SQLAlchemy** ORM with Flask-SQLAlchemy
- **Alembic** for database migrations
- **Flask-Migrate** integration
- **CORS** support
- **Marshmallow** for serialization
- **Blueprint** architecture
- **Error handling** middleware
- **Environment configuration** with dotenv
- **Testing** setup with pytest
- **Code formatting** with Black
- **Linting** with flake8
- **Docker** support with PostgreSQL and Redis

## Project Structure

```
flask-boilerplate/
├── app.py                 # Main application factory
├── requirements.txt       # Python dependencies
├── alembic.ini           # Alembic configuration
├── env.example           # Environment variables example
├── README.md             # Project documentation
├── config.py             # Configuration classes
├── manage.py             # Management commands
├── setup.py              # Automated setup script
├── demo.py               # Demo script
├── Dockerfile            # Docker configuration
├── docker-compose.yml    # Docker Compose setup
├── Makefile              # Development commands
├── .gitignore            # Git ignore rules
├── models/               # SQLAlchemy models
│   ├── __init__.py
│   ├── user.py          # User model
│   └── post.py          # Post model
├── routes/               # Flask blueprints
│   ├── __init__.py
│   ├── main.py          # Main routes
│   └── api.py           # API routes
├── migrations/           # Alembic migrations
│   ├── __init__.py
│   ├── env.py           # Migration environment
│   └── script.py.mako   # Migration template
└── tests/               # Test suite
    ├── __init__.py
    └── test_api.py      # API tests
```

## Quick Start

### Option 1: Docker (Recommended)

```bash
# Clone the repository
git clone <repository-url>
cd flask-boilerplate

# Start with Docker Compose
docker-compose up -d

# The application will be available at http://localhost:8000
```

### Option 2: Local Development

```bash
# Clone the repository
git clone <repository-url>
cd flask-boilerplate

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy environment example
cp env.example .env

# Edit .env file with your configuration
# SECRET_KEY=your-secret-key-here
# DATABASE_URL=sqlite:///app.db

# Initialize database
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

# Run the application
python app.py
# or
flask run
```

The application will be available at `http://localhost:5000` (local) or `http://localhost:8000` (Docker)

## API Endpoints

### Main Routes
- `GET /` - Welcome message
- `GET /health` - Health check
- `GET /docs` - API documentation

### User Management
- `GET /api/users` - Get all users
- `POST /api/users` - Create new user
- `GET /api/users/<id>` - Get user by ID
- `PUT /api/users/<id>` - Update user
- `DELETE /api/users/<id>` - Delete user

### Post Management
- `GET /api/posts` - Get all posts
- `POST /api/posts` - Create new post
- `GET /api/posts/<id>` - Get post by ID
- `PUT /api/posts/<id>` - Update post
- `DELETE /api/posts/<id>` - Delete post

## API Usage Examples

### Create a User

```bash
curl -X POST http://localhost:8000/api/users \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "email": "john@example.com",
    "password": "secure_password",
    "first_name": "John",
    "last_name": "Doe"
  }'
```

### Create a Post

```bash
curl -X POST http://localhost:8000/api/posts \
  -H "Content-Type: application/json" \
  -d '{
    "title": "My First Post",
    "content": "This is the content of my first post.",
    "slug": "my-first-post",
    "author_id": 1,
    "is_published": true
  }'
```

### Get All Users

```bash
curl http://localhost:8000/api/users
```

## Database Migrations

### Creating a New Migration

```bash
# After modifying models
flask db migrate -m "Add new field to user model"
```

### Applying Migrations

```bash
# Apply all pending migrations
flask db upgrade

# Downgrade to previous version
flask db downgrade
```

### Migration History

```bash
# View migration history
flask db history

# View current migration
flask db current
```

## Development

### Code Formatting

```bash
# Format code with Black
black .

# Check formatting
black --check .
```

### Linting

```bash
# Run flake8 linter
flake8 .
```

### Testing

```bash
# Run tests
pytest

# Run tests with coverage
pytest --cov=.
```

## Models

### User Model

The User model includes:
- Username and email (unique)
- Password hashing with Werkzeug
- First and last name
- Active status and admin flag
- Timestamps for creation and updates

### Post Model

The Post model includes:
- Title, content, and slug
- Publication status
- Author relationship to User
- Timestamps for creation and updates

## Configuration

### Environment Variables

- `SECRET_KEY` - Flask secret key for sessions
- `DATABASE_URL` - Database connection string
- `FLASK_ENV` - Flask environment (development/production)
- `FLASK_DEBUG` - Enable/disable debug mode

### Database Support

The boilerplate supports multiple databases:
- **SQLite** (default for development)
- **PostgreSQL** (recommended for production)
- **MySQL**

## Docker Support

### Quick Start with Docker

```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

### Docker Services

- **Web**: Flask application on port 8000
- **Database**: PostgreSQL on port 5432
- **Redis**: Redis cache on port 6379

### Port Configuration

The Docker setup uses port 8000 for the web service to avoid conflicts with AirPlay on macOS. If you need to use a different port, modify the `docker-compose.yml` file.

## Production Deployment

### Using Gunicorn

```bash
# Install gunicorn
pip install gunicorn

# Run with gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Environment Setup

```bash
# Set production environment variables
export FLASK_ENV=production
export FLASK_DEBUG=False
export DATABASE_URL=postgresql://user:pass@localhost/dbname
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Run linting and formatting
6. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support and questions, please open an issue on the GitHub repository. 