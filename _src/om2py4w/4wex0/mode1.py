from bottle import get, post, run

@get('/')
def index():
    return '''
        <form action="/convert" method="post">
                Convert From: <input name="convert_from" type="text" />
                Convert to: <input name="convert_to" type="text" />
                Value to convert: <input name="value_to_convert" type="float" />
                <input value="Convert" type="submit" />
        </form>
    '''

@post('/convert')
def convert():
    convert_from = request.forms.get('convert_from').upper()
    convert_to = request.forms.get('convert_to').upper()
    value_to_convert = request.forms.get('value_to_convert')
    url = ('http://rate-exchange.appspot.com/currency?from=%s&to=%s&q=1') % (convert_from, convert_to)
    rate = requests.get(url).json()['v']
    converted = float(value_to_convert)*float(requests.get(url).json()['v'])

    return '''<p>Current exchange rate %s to %s is: <b>%s</b></p>
        <p>Exchange value is: <b>%s</b></p>''' % (convert_from, convert_to, rate, converted)

run(host='localhost', port=8080, debug=True)
