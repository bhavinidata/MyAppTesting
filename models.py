from .app import db


class TempTableData(db.Model):
    __tablename__ = 'my_temp_table'

    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(64))
    lname = db.Column(db.String(64))

    def __repr__(self):
        return '<TempTableData %r>' % (self.name)