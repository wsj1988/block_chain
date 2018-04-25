# -*- coding: utf-8 -*-

import requests
import json
from pprint import pprint


def do_mine():
    URL = 'http://localhost:5001/mine'
    res = requests.get(URL)
    pprint(json.loads(res.text))


def do_new_transaction():
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        'sender': 'bea9eef3269a4eedbe8d3a61b448ba8a',
        'recipient': 'someone-other-address',
        'amount': 5
    }
    URL = 'http://localhost:5000/transactions/new'
    
    res = requests.post(URL, headers=headers, json=data)
    pprint(json.loads(res.text))


def do_get_chain():
    URL = 'http://localhost:5000/chain'
    res = requests.get(URL)
    pprint(json.loads(res.text))


def do_register():
    URL = 'http://localhost:5000/nodes/register'
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        'nodes': [URL.replace('5001', '5000') if '5001' in URL else URL.replace('5000', '5001')]
    }
    res = requests.post(URL, headers=headers, json=data)
    pprint(json.loads(res.text))


def do_resolve():
    URL = 'http://localhost:5001/nodes/resolve'
    res = requests.get(URL)
    pprint(json.loads(res.text))


if __name__ == '__main__':
    # do_mine()
    # do_new_transaction()
    # do_get_chain()
    # do_resolve()
    # do_register()
