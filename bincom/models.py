from datetime import datetime
from bincom import db

class AGENT_NAME(db.Model):
    __tablename__ = 'agentname'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(255), nullable=False)
    lastname = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, default='default@demo.com')
    phone = db.Column(db.String(15), nullable=False)
    pollingunit_uniqueid = db.Column(db.Integer, nullable=False)

class LGA_RESULTS(db.Model):
    __tablename__ =  'announced_lga_results'
    id = db.Column(db.Integer, primary_key=True)
    lga_name = db.Column(db.String(50), nullable=False)
    party_abbreviation = db.Column(db.String(4), nullable=False)
    party_score = db.Column(db.Integer, nullable=False)
    entered_by_user = db.Column(db.String(50), nullable=False)
    date_entered = db.Column(db.DateTime(120), nullable=False, default=datetime.utcnow)
    user_ip_address = db.Column(db.String(50), nullable=False)

class PU_RESULTS(db.Model):
    __tablename__ = 'announced_pu_results'
    id = db.Column(db.Integer, primary_key=True)
    polling_unit_uniqueid = db.Column(db.String(50), nullable=False)
    party_abbreviation = db.Column(db.String(4), nullable=False)
    party_score = db.Column(db.Integer, nullable=False)
    entered_by_user = db.Column(db.String(50), nullable=False)
    date_entered = db.Column(db.DateTime(120), nullable=False, default=datetime.utcnow)
    user_ip_address = db.Column(db.String(50), nullable=False)

class STATE_RESULTS(db.Model): 
    __tablename__ = 'announced_state_results'
    id = db.Column(db.Integer, primary_key=True)
    state_name = db.Column(db.String(50), nullable=False)
    party_abbreviation = db.Column(db.String(4), nullable=False)
    party_score = db.Column(db.Integer, nullable=False)
    entered_by_user = db.Column(db.String(50), nullable=False)
    date_entered = db.Column(db.DateTime(120), nullable=False, default=datetime.utcnow)
    user_ip_address = db.Column(db.String(50), nullable=False)

class WARD_RESULTS(db.Model):
    __tablename__ =  'announced_ward_results'
    id = db.Column(db.Integer, primary_key=True)
    ward_name = db.Column(db.String(50), nullable=False)
    party_abbreviation = db.Column(db.String(4), nullable=False)
    party_score = db.Column(db.Integer, nullable=False)
    entered_by_user = db.Column(db.String(50), nullable=False)
    date_entered = db.Column(db.DateTime(120), nullable=False, default=datetime.utcnow)
    user_ip_address = db.Column(db.String(50), nullable=False)

class PARTY(db.Model):
    __tablename__ = 'party'
    id = db.Column(db.Integer, primary_key=True)
    partyid = db.Column(db.String(11), nullable=False)
    partyname = db.Column(db.String(11), nullable=False)

class POLLING_UNIT(db.Model):
    __tablename__ = 'polling_unit'
    id = db.Column(db.Integer, primary_key=True)
    polling_unit_id = db.Column(db.Integer)
    ward_id = db.Column(db.Integer)
    lga_id = db.Column(db.Integer)
    uniquewardid = db.Column(db.Integer)
    polling_unit_number = db.Column(db.String(50))
    polling_unit_name = db.Column(db.String(50))
    polling_unit_description = db.Column(db.Text)
    lat = db.Column(db.String(255))
    long = db.Column(db.String(255))
    entered_by_user = db.Column(db.String(50), nullable=False)
    date_entered = db.Column(db.DateTime(120), nullable=False, default=datetime.utcnow)
    user_ip_address = db.Column(db.String(50), nullable=False)

class WARD(db.Model):
    __tablename__ = 'ward'
    id = db.Column(db.Integer, primary_key=True)
    ward_id = db.Column(db.Integer, nullable=False)
    ward_name = db.Column(db.String(50), nullable=False)
    lga_id = db.Column(db.Integer, nullable=False)
    ward_description = db.Column(db.Text, nullable=False)
    entered_by_user = db.Column(db.String(50), nullable=False)
    date_entered = db.Column(db.DateTime(120), nullable=False, default=datetime.utcnow)
    user_ip_address = db.Column(db.String(50), nullable=False)

class STATE(db.Model):
    __tablename__ = 'state'
    id = db.Column(db.Integer, primary_key=True)
    state_name = db.Column(db.String(255), nullable=False)

class LGA(db.Model):
    __tablename__ = 'lga'
    id = db.Column(db.Integer, primary_key=True)
    lga_id = db.Column(db.Integer)
    lga_name = db.Column(db.String(50), nullable=False)
    state_id = db.Column(db.Integer, nullable=False)
    lga_description = db.Column(db.Text, nullable=False)
    entered_by_user = db.Column(db.String(50), nullable=False)
    date_entered = db.Column(db.DateTime(120), nullable=False, default=datetime.utcnow)
    user_ip_address = db.Column(db.String(50), nullable=False)