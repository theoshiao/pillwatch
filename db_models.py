class Pill(db.Model): 
    __tablename__ = 'pills'
    pill_id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String(100), nullable=False) 
    generic_name = db.Column(db.String(100), nullable=False) 
    description = db.Column(db.Text)
