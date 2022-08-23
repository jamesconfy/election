from marshmallow import Schema, fields

class PARTY_SCHEMA(Schema):
    id = fields.Integer(data_key='id')
    partyid = fields.Str(data_key='party id')
    partyname = fields.Str(data_key='party name')

class LGA_SCHEMA(Schema):
    id = fields.Integer(data_key='id')
    lga_id = fields.Integer(data_key='lga id')
    lga_name = fields.Str(data_key='lga name')
    state_id = fields.Integer(data_key='state id')
    lga_description = fields.Str(data_key='lga description')
    entered_by_user =fields.Str(data_key='entered by user')
    date_entered = fields.DateTime(data_key='date_entered')
    user_ip_address = fields.Str(data_key='user_ip_address')

class PU_RESULTS_SCHEMA(Schema):
    id = fields.Integer(data_key='id')
    polling_unit_uniqueid = fields.Str(data_key='polling_unit_uniqueid')
    party_abbreviation = fields.Str(data_key='party_abbreviation')
    party_score = fields.Integer(data_key='party_score')
    entered_by_user = fields.Str(data_key='entered_by_user')
    date_entered = fields.DateTime(data_key='date_entered')
    user_ip_address = fields.Str(data_key='user_ip_address')

class LGA_RESULTS_SCHEMA(Schema):
    id = fields.Integer(data_key='id')
    lga_name = fields.Str(data_key='lga name')
    party_abbreviation = fields.Str(data_key='party_abbreviation')
    party_score = fields.Integer(data_key='party_score')
    entered_by_user = fields.Str(data_key='entered_by_user')
    date_entered = fields.DateTime(data_key='date_entered')
    user_ip_address = fields.Str(data_key='user_ip_address')

class USERS_SCHEMA(Schema):
    id = fields.Integer(data_key='id')
    firstname = fields.String(data_key='first name')
    lastname = fields.String(data_key='last name')
    email = fields.String(data_key='email')
    phone =fields.String(data_key='phone number')
    pollingunit_uniqueid = fields.Integer(data_key='polling unit uniqueid')

class POLLING_UNIT_SCHEMA(Schema):
    id = fields.Integer(data_key='id')
    polling_unit_id = fields.Integer(data_key='polling unit id')
    ward_id = fields.Integer(data_key='ward id')
    lga_id = fields.Integer(data_key='lga id')
    uniquewardid = fields.Integer(data_key='unique ward id')
    polling_unit_number = fields.Str(data_key='polling unit number')
    polling_unit_name = fields.Str(data_key='polling unit name')
    polling_unit_description = fields.Str(data_key='polling unit description')
    lat = fields.Str(data_key='latitude')
    long = fields.Str(data_key='longitude')
    entered_by_user = fields.Str(data_key='entered_by_user')
    date_entered = fields.DateTime(data_key='date_entered')
    user_ip_address = fields.Str(data_key='user_ip_address')

class STATE_SCHEMA(Schema):
    id = fields.Integer(data_key='id')
    state_name = fields.Str(data_key='state name')

class WARD_SCHEMA(Schema):
    id = fields.Integer(data_key='id')
    ward_id = fields.Integer(data_key='ward id')
    ward_name = fields.Str(data_key='ward name')
    lga_id = fields.Integer(data_key='lga id')
    ward_description = fields.Str(data_key='ward description')
    entered_by_user = fields.Str(data_key='entered_by_user')
    date_entered = fields.DateTime(data_key='date_entered')
    user_ip_address = fields.Str(data_key='user_ip_address')