from bincom import db
from flask import current_app as app, jsonify, render_template, request
from bincom.forms import DropForm, PollingUnitForm
from bincom.models import PU_RESULTS # AGENT_NAME, LGA, PARTY, POLLING_UNIT, LGA_RESULTS, STATE, WARD
from bincom.schema import PARTY_SCHEMA, PU_RESULTS_SCHEMA, LGA_SCHEMA, LGA_RESULTS_SCHEMA, STATE_SCHEMA, USERS_SCHEMA, POLLING_UNIT_SCHEMA, WARD_SCHEMA
from bincom.files.Loaders import Loaders

manyUsers = USERS_SCHEMA(many=True)
manyPU = PU_RESULTS_SCHEMA(many=True)
manyLGA = LGA_SCHEMA(many=True)
manyLGAResult = LGA_RESULTS_SCHEMA(many=True)
manyParty = PARTY_SCHEMA(many=True)
manyPOLLING = POLLING_UNIT_SCHEMA(many=True)
manySTATE = STATE_SCHEMA(many=True)
manyWARD = WARD_SCHEMA(many=True)

@app.before_first_request
def load():
    db.create_all()
    Loaders.load_lga()
    Loaders.load_lga_result()
    Loaders.load_party()
    Loaders.load_polling()
    Loaders.load_polling_unit()
    Loaders.load_state()
    Loaders.load_users()
    Loaders.load_ward()

    return

@app.route('/polling_unit_result', methods=['GET'])
def polling_unit_results():
    results = PU_RESULTS.query.all()
    return jsonify(manyPU.dump(results)), 200

@app.route('/polling_unit_result/<string:polling_unit_uniqueid>', methods=['GET'])
def polling_unit_result(polling_unit_uniqueid):
    results = PU_RESULTS.query.filter_by(polling_unit_uniqueid=polling_unit_uniqueid).all()
    # total = len(results)
    obj = {}
    for res in results:
        if res.party_abbreviation in obj:
            obj[res.party_abbreviation] += res.party_score
        else:
            obj[res.party_abbreviation] = res.party_score

    # obj = {
    #     'data': manyPU.dump(results),
    #     'total votes': total,
    #     'polling unit uniqueid': polling_unit_uniqueid
    # }
    return jsonify(obj), 200

# @app.route('/lga_result', methods=['GET'])
# def lga_result():
#     result = LGA_RESULTS.query.all()
#     return jsonify(manyLGAResult.dump(result)), 200


@app.route('/lga_result', methods=['GET', 'POST'])
def lga_result():
    form = DropForm()
    if request.method == 'POST':
        result = PU_RESULTS.query.filter_by()
        sel = request.form.get('sel')
        return jsonify(sel)

    return render_template('lga.html', form=form)

@app.route('/polling_unit', methods=['GET', 'POST'])
def polling_unit():
    form = PollingUnitForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            polling_unit_uniqueid = form.polling_unit_uniqueid.data
            party = form.party.data
            party_score = form.party_score.data
            entered_by_user = form.entered_by_user.data
            date_entered = form.date_entered.data
            print(date_entered)
            user_ip_address = form.user_ip_address.data

            result = PU_RESULTS(polling_unit_uniqueid=polling_unit_uniqueid, party_abbreviation=party, party_score=party_score, entered_by_user=entered_by_user, date_entered=date_entered, user_ip_address=user_ip_address)
            db.session.add(result)
            db.session.commit()

            return jsonify('Result added successfully')

    return render_template('polling_unit.html', form=form)