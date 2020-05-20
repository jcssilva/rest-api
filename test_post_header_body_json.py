import requests
import json

def test_post_header_body_json():
    url = 'http://httpbin.org/post'

    # Additional hearders.
    headers = {'Content-type': 'application/json'}

    # Body.
    payload = {'key1': 1, 'key2': 'value2'}

    # Convert dict to json by json.dumps() for body data.
    resp = requests.post(url, headers=headers, data=json.dumps(payload, indent=4))

    # Validate response headers and body contents, e.g. status code.
    assert resp.status_code == 200
    resp_body = resp.json()
    assert resp_body['url'] == url

    # print response full body as text
    print(resp.text)