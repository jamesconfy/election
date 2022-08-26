from bincom import db
from bincom.models import AGENT_NAME, LGA, PARTY, POLLING_UNIT, PU_RESULTS, LGA_RESULTS, STATE, WARD
from utils import changeToDatetime, pu_unit_result, lga_list, lga_result_list, users_list, party_list, polling_unit_list, states_list, ward_list

class Loaders(object):
    def __init__(self):
         self.loaders = ''

    def load_users():
        res = AGENT_NAME.query.all()
        if not res:
            for val in users_list:
                results = AGENT_NAME(id=val[0], firstname=val[1], lastname=val[2], email=val[3], phone=val[4], pollingunit_uniqueid=val[5])
                db.session.add(results)
                db.session.commit()

        return 

    def load_polling():
        res = PU_RESULTS.query.all()
        if not res:
            for val in pu_unit_result:
                results = PU_RESULTS(id=val[0], polling_unit_uniqueid=val[1], party_abbreviation=val[2], party_score=val[3], entered_by_user=val[4], date_entered=changeToDatetime(val[5]), user_ip_address=val[6])
                db.session.add(results)
                db.session.commit()

        return 

    def load_lga():
        res = LGA.query.all()
        if not res:
            for val in lga_list:
                results = LGA(id=val[0], lga_id=val[1], lga_name=val[2], state_id=val[3], lga_description=val[4], entered_by_user=val[5], user_ip_address=val[7])
                db.session.add(results)
                db.session.commit()

        return 


    def load_lga_result():
        res = LGA_RESULTS.query.all()
        if not res:
            for val in lga_result_list:
                results = LGA_RESULTS(id=val[0], lga_name=val[1], party_abbreviation=val[2], party_score=val[3], entered_by_user=val[4], date_entered=changeToDatetime(val[5]), user_ip_address=val[6])
                db.session.add(results)
                db.session.commit()

        return 

    def load_party():
        res = PARTY.query.all()
        if not res:
            for val in party_list:
                result = PARTY(id=val[0], partyid=val[1], partyname=val[2])
                db.session.add(result)
                db.session.commit()

        return 

    def load_polling_unit():
        res = POLLING_UNIT.query.all()
        if not res:
            for val in polling_unit_list:
                result = POLLING_UNIT(id=val[0], polling_unit_id=val[1], ward_id=val[2], lga_id=val[3], uniquewardid=val[4], polling_unit_number=val[5], polling_unit_name=val[6], polling_unit_description=val[7], lat=val[8], long=val[9], entered_by_user=val[10], user_ip_address=val[12])
                db.session.add(result)
                db.session.commit()

        return 

    def load_state():
        res = STATE.query.all()
        if not res:
            for val in states_list:
                result = STATE(id=val[0], state_name=val[1])
                db.session.add(result)
                db.session.commit()

        return 

    def load_ward():
        res = WARD.query.all()
        if not res:
            for val in ward_list:
                result = WARD(id=val[0], ward_id=val[1], ward_name=val[2], lga_id=val[3], ward_description=val[4], entered_by_user=val[5], user_ip_address=val[7])
                db.session.add(result)
                db.session.commit()

        return 