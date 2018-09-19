"""
Bitzino
"""

from flask import Flask, jsonify, request, send_from_directory

app = Flask(__name__)

@app.route('/blackjack', methods=['POST'])
def blackjack():
    if request.method == 'POST':
        utf8 = request.form.get('utf8')
        print('utf8 = ' + utf8)
        authenticity_token = request.form.get('authenticity_token')
        print('authenticity_token = ' + authenticity_token)
        sync_token = request.form.get('blackjack_table[sync_token]')
        print('sync_token = ' + sync_token)
        client_seed = request.form.get('blackjack_table[client_seed]')
        print('client_seed = ' + client_seed)
        bet = request.form.get('blackjack_table[bet]')
        print('bet = ' + bet)
        commit = request.form.get('commit')
        print('commit = ' + commit)
        #  TODO
        resp = jsonify(success=True)
        resp.status_code = 200
        return resp
    # By default just send back game name (i.e. to GET request)
    return 'blackjack'

@app.route('/video_poker', methods=['POST'])
def video_poker():
    if request.method == 'POST':
        utf8 = request.form.get('utf8')
        print('utf8 = ' + utf8)
        authenticity_token = request.form.get('authenticity_token')
        print('authenticity_token = ' + authenticity_token)
        sync_token = request.form.get('video_poker_table[sync_token]')
        print('sync_token = ' + sync_token)
        client_seed = request.form.get('video_poker_table[client_seed]')
        print('client_seed = ' + client_seed)
        bet = request.form.get('video_poker_table[bet]')
        print('bet = ' + bet)
        commit = request.form.get('commit')
        print('commit = ' + commit)
        #  TODO
        resp = jsonify(success=True)
        resp.status_code = 200
        return resp
    # By default just send back game name (i.e. to GET request)
    return 'video_poker'

@app.route('/craps', methods=['POST'])
def craps():
    if request.method == 'POST':
        utf8 = request.form.get('utf8')
        print('utf8 = ' + utf8)
        authenticity_token = request.form.get('authenticity_token')
        print('authenticity_token = ' + authenticity_token)
        sync_token = request.form.get('craps_table[sync_token]')
        print('sync_token = ' + sync_token)
        client_seed = request.form.get('craps_table[client_seed]')
        print('client_seed = ' + client_seed)
        wagers = request.form.get('craps_table[wagers]')
        print('wagers = ' + wagers)
        bet_per_click  = request.form.get('craps_table[bet_per_click]')
        print('bet_per_click = ' + bet_per_click)
        commit = request.form.get('commit')
        print('commit = ' + commit)
        #  TODO
        resp = jsonify(success=True)
        resp.status_code = 200
        return resp
    # By default just send back game name (i.e. to GET request)
    return 'craps'

@app.route('/roulette', methods=['POST'])
def roulette():
    if request.method == 'POST':
        utf8 = request.form.get('utf8')
        print('utf8 = ' + utf8)
        authenticity_token = request.form.get('authenticity_token')
        print('authenticity_token = ' + authenticity_token)
        sync_token = request.form.get('roulette_table[sync_token]')
        print('sync_token = ' + sync_token)
        client_seed = request.form.get('roulette_table[client_seed]')
        print('client_seed = ' + client_seed)
        wagers = request.form.get('roulette_table[wagers]')
        print('wagers = ' + wagers)
        bet_per_click  = request.form.get('roulette_table[bet_per_click]')
        print('bet_per_click = ' + bet_per_click)
        commit = request.form.get('commit')
        print('commit = ' + commit)
        #  TODO
        resp = jsonify(success=True)
        resp.status_code = 200
        return resp
    # By default just send back game name (i.e. to GET request)
    return 'roulette'

@app.route('/', defaults=dict(filename=None))
@app.route('/<path:filename>', methods=['GET', 'POST'])
def index(filename):
    filename = filename or 'index.html'
    if request.method == 'GET':
        return send_from_directory('./bitzino.com', filename)
    return jsonify(request.data)

if __name__ == '__main__':
    app.run(debug=1)
