#!/usr/bin/python3
import requests

def setup():
    #DROP TABLE
    return 0

def test_listpeople():
    payload = {'course': 'cs61a'}
    r = requests.get('http://sarin.ocf.berkeley.edu:5000/listpeople', params=payload)
    print('61a', r.json())
    payload = {'course': 'cs61b'}
    r = requests.get('http://sarin.ocf.berkeley.edu:5000/listpeople', params=payload)
    print('61b', r.json())
    payload = {'course': 'cs70'}
    r = requests.get('http://sarin.ocf.berkeley.edu:5000/listpeople', params=payload)
    print('70', r.json())
    payload = {'course': 'cs61c'}
    r = requests.get('http://sarin.ocf.berkeley.edu:5000/listpeople', params=payload)
    print('61c', r.json())
    payload = {'course': 'math110'}
    r = requests.get('http://sarin.ocf.berkeley.edu:5000/listpeople', params=payload)
    print('110', r.json())
    
    return 0

def test_listcourses():
    payload = {'uname': 'awelty'}
    r = requests.get('http://sarin.ocf.berkeley.edu:5000/listcourses', params=payload)
    print('awelty', r.json())
    payload = {'uname': 'bzh'}
    r = requests.get('http://sarin.ocf.berkeley.edu:5000/listcourses', params=payload)
    print('bzh', r.json())
    payload = {'uname': 'mdcha'}
    r = requests.get('http://sarin.ocf.berkeley.edu:5000/listcourses', params=payload)
    print('mdcha', r.json())
    payload = {'uname': 'keur'}
    r = requests.get('http://sarin.ocf.berkeley.edu:5000/listcourses', params=payload)
    print('keur', r.json())
    payload = {'uname': 'bad'}
    r = requests.get('http://sarin.ocf.berkeley.edu:5000/listcourses', params=payload)
    print('bad', r.json())
    return 0

def test_addcourse():
    payload = {'uname': 'awelty', 'course': 'cs61a'}
    r = requests.post('http://sarin.ocf.berkeley.edu:5000/addcourse', params=payload)
    payload = {'uname': 'awelty', 'course': 'cs61b'}
    r = requests.post('http://sarin.ocf.berkeley.edu:5000/addcourse', params=payload)
    payload = {'uname': 'awelty', 'course': 'cs61a'}
    r = requests.post('http://sarin.ocf.berkeley.edu:5000/addcourse', params=payload)
    payload = {'uname': 'bzh', 'course': 'cs61a'}
    r = requests.post('http://sarin.ocf.berkeley.edu:5000/addcourse', params=payload)
    payload = {'uname': 'bzh', 'course': 'cs61b'}
    r = requests.post('http://sarin.ocf.berkeley.edu:5000/addcourse', params=payload)
    payload = {'uname': 'keur', 'course': 'cs61a'}
    r = requests.post('http://sarin.ocf.berkeley.edu:5000/addcourse', params=payload)
    payload = {'uname': 'keur', 'course': 'cs61c'}
    r = requests.post('http://sarin.ocf.berkeley.edu:5000/addcourse', params=payload)
    payload = {'uname': 'keur', 'course': 'cs70'}
    r = requests.post('http://sarin.ocf.berkeley.edu:5000/addcourse', params=payload)
    payload = {'uname': 'mdcha', 'course': 'cs70'}
    r = requests.post('http://sarin.ocf.berkeley.edu:5000/addcourse', params=payload)
    return 0

def test_removecourse():
    payload = {'uname': 'keur', 'course': 'cs70'}
    r = requests.post('http://sarin.ocf.berkeley.edu:5000/removecourse', params=payload)
    payload = {'uname': 'keur', 'course': 'cs61a'}
    r = requests.post('http://sarin.ocf.berkeley.edu:5000/removecourse', params=payload)
    return 0

test_addcourse()
test_removecourse()
test_listcourses()
test_listpeople()
