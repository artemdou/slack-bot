import requests

def send_slack_message(webhook, message):
    payload = '{"text": "%s"}' % message
    response = requests.post(webhook, 
                            data=payload.encode("utf-8"))
    print(response.text)


