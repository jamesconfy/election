# from bincom import db
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, IntegerField, StringField, DateField
from wtforms.validators import DataRequired, Optional
from bincom.models import LGA, PARTY, POLLING_UNIT

# db.create_all()

lga = LGA.query.all()
data = []
for val in lga:
    data.append(val.lga_id)

party = PARTY.query.all()
data1 = []
for val in party:
    data1.append(val.partyname)

pollingunitid = POLLING_UNIT.query.all()
data2 = []
for val in pollingunitid:
    data2.append(val.polling_unit_id)

class DropForm(FlaskForm):
    sel = SelectField('Local Government ID', validate_choice=data, choices=data, validators=[DataRequired()])
    submit = SubmitField('submit')

class PollingUnitForm(FlaskForm):
    polling_unit_uniqueid = SelectField('Polling Unit ID', validators=[DataRequired()], validate_choice=set(data2), choices=set(data2))
    party = SelectField('Party', validate_choice=data1, choices=data1, validators=[DataRequired()])
    party_score = IntegerField('Party Score', validators=[DataRequired()])
    entered_by_user = StringField('Entered By', validators=[Optional()])
    date_entered = DateField('Date Entered', validators=[Optional()])
    user_ip_address = StringField('User IP Address', validators=[Optional()])
    submit = SubmitField('submit')