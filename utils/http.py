import json
import requests


def request(method, url, headers=None, body=None, result=None):
    client = requests.Session()
    req_body = None

    if body is not None:
        req_body = json.dumps(body)

    try:
        req = requests.Request(method, url, headers=headers, data=req_body)
        prepared_req = client.prepare_request(req)
        response = client.send(prepared_req)

        if result is not None:
            try:
                response_json = response.json()
                for key, value in response_json.items():
                    setattr(result, key, value)
            except ValueError:
                pass

        response.raise_for_status()

    except Exception as e:
        return str(e)

if __name__ == '__main__':
    class Result:
        pass

    url = "https://example.com/api"
    headers = {"Content-Type": "application/json"}
    data = {"key": "value"}

    result = Result()
    error = request("POST", url, headers=headers, body=data, result=result)

    if error:
        print("Error:", error)
    else:
        print("Response:", result.__dict__)
