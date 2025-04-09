from app import create_app
from app.models import db

app = create_app()

with app.app_context():
    print("✅ Inside app context")
    db.create_all()
    print("✅ Tables created successfully!")