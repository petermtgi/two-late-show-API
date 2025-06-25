from server.app import create_app, db
from server.models import Guest

app = create_app()

with app.app_context():
    g1 = Guest(name="Peter Mutua")
    g2 = Guest(name="Claude Otieno")

    db.session.add_all([g1, g2])
    db.session.commit()
    print("Seeded guests!")
