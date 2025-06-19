#!/usr/bin/env python3
"""
Setup script for Flask Boilerplate
"""
import os
import sys
import subprocess
from pathlib import Path

def run_command(command, description):
    """Run a shell command and handle errors"""
    print(f"Running: {description}")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✓ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ {description} failed: {e}")
        print(f"Error output: {e.stderr}")
        return False

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print("✗ Python 3.8 or higher is required")
        return False
    print(f"✓ Python {sys.version_info.major}.{sys.version_info.minor} detected")
    return True

def create_virtual_environment():
    """Create virtual environment if it doesn't exist"""
    venv_path = Path("venv")
    if venv_path.exists():
        print("✓ Virtual environment already exists")
        return True
    
    print("Creating virtual environment...")
    return run_command("python -m venv venv", "Create virtual environment")

def install_dependencies():
    """Install Python dependencies"""
    # Determine the correct pip command based on OS
    if os.name == 'nt':  # Windows
        pip_cmd = "venv\\Scripts\\pip"
    else:  # Unix/Linux/macOS
        pip_cmd = "venv/bin/pip"
    
    return run_command(f"{pip_cmd} install -r requirements.txt", "Install dependencies")

def create_env_file():
    """Create .env file from example if it doesn't exist"""
    env_file = Path(".env")
    env_example = Path("env.example")
    
    if env_file.exists():
        print("✓ .env file already exists")
        return True
    
    if env_example.exists():
        import shutil
        shutil.copy(env_example, env_file)
        print("✓ Created .env file from env.example")
        print("⚠️  Please edit .env file with your configuration")
        return True
    else:
        print("✗ env.example file not found")
        return False

def initialize_database():
    """Initialize database with Flask-Migrate"""
    # Determine the correct python command based on OS
    if os.name == 'nt':  # Windows
        python_cmd = "venv\\Scripts\\python"
    else:  # Unix/Linux/macOS
        python_cmd = "venv/bin/python"
    
    # Set Flask environment variables
    env = os.environ.copy()
    env['FLASK_APP'] = 'app.py'
    
    # Initialize migrations
    if not run_command(f"{python_cmd} -m flask db init", "Initialize database migrations"):
        return False
    
    # Create initial migration
    if not run_command(f"{python_cmd} -m flask db migrate -m 'Initial migration'", "Create initial migration"):
        return False
    
    # Apply migrations
    if not run_command(f"{python_cmd} -m flask db upgrade", "Apply database migrations"):
        return False
    
    return True

def main():
    """Main setup function"""
    print("🚀 Flask Boilerplate Setup")
    print("=" * 40)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Create virtual environment
    if not create_virtual_environment():
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        sys.exit(1)
    
    # Create .env file
    if not create_env_file():
        sys.exit(1)
    
    # Initialize database
    if not initialize_database():
        print("⚠️  Database initialization failed. You can run it manually later.")
    
    print("\n" + "=" * 40)
    print("🎉 Setup completed successfully!")
    print("\nNext steps:")
    print("1. Edit .env file with your configuration")
    print("2. Activate virtual environment:")
    if os.name == 'nt':  # Windows
        print("   venv\\Scripts\\activate")
    else:  # Unix/Linux/macOS
        print("   source venv/bin/activate")
    print("3. Run the application:")
    print("   python app.py")
    print("   or")
    print("   flask run")
    print("\nFor more information, see README.md")

if __name__ == "__main__":
    main() 