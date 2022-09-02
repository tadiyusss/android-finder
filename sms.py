from subprocess import check_output
import json

def sendSMS(message):
    output = check_output(["termux-sms-send", "-n", "8080", "-s", "0", message])
    result = output.decode('utf-8')
    return result

def readSMS():
    out = check_output(["termux-sms-list"])
    result = json.loads(out.decode('utf-8'))
    return result
