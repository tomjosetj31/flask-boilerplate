#!/usr/bin/env python3
"""
Management script for Flask application
"""
import os
import sys
from flask.cli import FlaskGroup
from app import create_app, db
from models.user import User
from models.post import Post

app = create_app()
cli = FlaskGroup(create_app=create_app)

@cli.command("init-db")
def init_db():
    """Initialize the database."""
    with app.app_context():
        db.create_all()
        print("Database initialized!")

@cli.command("create-admin")
def create_admin():
    """Create an admin user."""
    with app.app_context():
        username = input("Enter admin username: ")
        email = input("Enter admin email: ")
        password = input("Enter admin password: ")
        
        # Check if user already exists
        if User.query.filter_by(username=username).first():
            print("User already exists!")
            return
        
        admin = User(
            username=username,
            email=email,
            password=password
        )
        admin.is_admin = True
        
        db.session.add(admin)
        db.session.commit()
        print(f"Admin user '{username}' created successfully!")

@cli.command("create-user")
def create_user():
    """Create a regular user."""
    with app.app_context():
        username = input("Enter username: ")
        email = input("Enter email: ")
        password = input("Enter password: ")
        first_name = input("Enter first name (optional): ")
        last_name = input("Enter last name (optional): ")
        
        # Check if user already exists
        if User.query.filter_by(username=username).first():
            print("User already exists!")
            return
        
        user = User(
            username=username,
            email=email,
            password=password,
            first_name=first_name if first_name else None,
            last_name=last_name if last_name else None
        )
        
        db.session.add(user)
        db.session.commit()
        print(f"User '{username}' created successfully!")

@cli.command("list-users")
def list_users():
    """List all users."""
    with app.app_context():
        users = User.query.all()
        if not users:
            print("No users found.")
            return
        
        print("\nUsers:")
        print("-" * 50)
        for user in users:
            print(f"ID: {user.id}")
            print(f"Username: {user.username}")
            print(f"Email: {user.email}")
            print(f"Admin: {user.is_admin}")
            print(f"Active: {user.is_active}")
            print("-" * 50)

@cli.command("list-posts")
def list_posts():
    """List all posts."""
    with app.app_context():
        posts = Post.query.all()
        if not posts:
            print("No posts found.")
            return
        
        print("\nPosts:")
        print("-" * 50)
        for post in posts:
            print(f"ID: {post.id}")
            print(f"Title: {post.title}")
            print(f"Slug: {post.slug}")
            print(f"Author: {post.author.username if post.author else 'Unknown'}")
            print(f"Published: {post.is_published}")
            print("-" * 50)

@cli.command("shell")
def shell():
    """Start a Python shell with Flask app context."""
    import code
    with app.app_context():
        code.interact(local=locals())

if __name__ == '__main__':
    cli() 