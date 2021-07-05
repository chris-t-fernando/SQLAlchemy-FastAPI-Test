import requests
import json
import logging, sys
logging.basicConfig(stream=sys.stderr, level=logging.INFO)


# use case 1
def useCaseOne():
    logging.info('=========================================')
    logging.info('starting use case one')

    params = {
        'stock_code': [ 'avh', '14d' ]
    }

    r = requests.get('http://127.0.0.1:8001/stocks', json=params)
    rjson = r.json()
    print(json.dumps(rjson, sort_keys=False, indent=4))
    logging.info('finished use case one')
    logging.info('=========================================')

useCaseOne()