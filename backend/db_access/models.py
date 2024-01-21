from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class TambolaTicket(db.Model):
    __tablename__ = 'tambola_tickets'
    id = db.Column(db.Integer, primary_key=True)
    ticket_data = db.Column(db.JSON)
