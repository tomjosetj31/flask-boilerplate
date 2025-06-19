#!/usr/bin/env python3
"""
Demo script for Flask Boilerplate
This script demonstrates the basic functionality of the boilerplate
"""
import requests
import json
import time

BASE_URL = "http://localhost:8000"

def print_response(response, description):
    """Print formatted response"""
    print(f"\n{'='*50}")
    print(f"{description}")
    print(f"{'='*50}")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")

def demo_api():
    """Demonstrate the API functionality"""
    print("🚀 Flask Boilerplate Demo")
    print("Make sure the Flask application is running on http://localhost:8000")
    print("You can start it with: docker-compose up -d")
    
    # Wait for user to start the server
    input("\nPress Enter when the Flask app is running...")
    
    try:
        # Test health check
        response = requests.get(f"{BASE_URL}/health")
        print_response(response, "Health Check")
        
        # Test API docs
        response = requests.get(f"{BASE_URL}/docs")
        print_response(response, "API Documentation")
        
        # Create a user
        user_data = {
            "username": "demo_user",
            "email": "demo@example.com",
            "password": "demo_password",
            "first_name": "Demo",
            "last_name": "User"
        }
        
        response = requests.post(f"{BASE_URL}/api/users", json=user_data)
        print_response(response, "Create User")
        
        if response.status_code == 201:
            user_id = response.json()['user']['id']
            
            # Get all users
            response = requests.get(f"{BASE_URL}/api/users")
            print_response(response, "Get All Users")
            
            # Get specific user
            response = requests.get(f"{BASE_URL}/api/users/{user_id}")
            print_response(response, "Get Specific User")
            
            # Create a post
            post_data = {
                "title": "Demo Post",
                "content": "This is a demo post created by the demo script.",
                "slug": "demo-post",
                "author_id": user_id,
                "is_published": True
            }
            
            response = requests.post(f"{BASE_URL}/api/posts", json=post_data)
            print_response(response, "Create Post")
            
            if response.status_code == 201:
                post_id = response.json()['post']['id']
                
                # Get all posts
                response = requests.get(f"{BASE_URL}/api/posts")
                print_response(response, "Get All Posts")
                
                # Get specific post
                response = requests.get(f"{BASE_URL}/api/posts/{post_id}")
                print_response(response, "Get Specific Post")
                
                # Update post
                update_data = {
                    "title": "Updated Demo Post",
                    "is_published": False
                }
                
                response = requests.put(f"{BASE_URL}/api/posts/{post_id}", json=update_data)
                print_response(response, "Update Post")
                
                # Delete post
                response = requests.delete(f"{BASE_URL}/api/posts/{post_id}")
                print_response(response, "Delete Post")
                
                # Delete user
                response = requests.delete(f"{BASE_URL}/api/users/{user_id}")
                print_response(response, "Delete User")
        
        print("\n🎉 Demo completed successfully!")
        print("The Flask Boilerplate is working correctly!")
        
    except requests.exceptions.ConnectionError:
        print("❌ Error: Could not connect to the Flask application.")
        print("Make sure the application is running on http://localhost:8000")
        print("Start it with: docker-compose up -d")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    demo_api() 