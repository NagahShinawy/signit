"""
Service Entry Point
"""

from profiles.app import create_app

app = create_app("profiles.config.develop")

if __name__ == "__main__":
    app.run()
