from queue import Queue
from flask import  Blueprint
import subprocess
import random
import time



api = Blueprint('sms_auth', __name__)

# Replace this with your device ID (use 'adb devices' command to find it)
DEVICE_ID = '33009644ada323bf'

# Create a queue to hold API requests
sms_queue = Queue()

#dictanory for the conformation of auth code
m_MapAuthCode = {}

# Create a queue to hold API requests
auth_code_queue = Queue()

# Generate a random 6-digit authentication code
def generate_auth_code():
    return str(random.randint(100000, 999999))

#testing
def generate_phone_num():
    return str(random.randint(1000000000, 9999999999))

# Send an SMS using ADB
def send_sms(phone_number, message):
        m_MapAuthCode[phone_number] = message
        adb_command = f'cd C:\\Users\\QA1\\Downloads\\platform-tools_r34.0.4-windows\\platform-tools && adb -s 33009644ada323bf shell am start -a android.intent.action.SENDTO -d sms:{phone_number} --es sms_body "{message}" && adb shell input tap 642 631 && adb shell input tap 638 1228'
        subprocess.run(adb_command, shell=True, check=True)
        # Sleep for 1 second to allow the SMS to be sent
        time.sleep(1)

#checking auth code
def check_code(phone_number,user_auth_code):
    print(m_MapAuthCode[phone_number])
    print(user_auth_code)
    if m_MapAuthCode[phone_number] == user_auth_code:
        return "Right auth code"
    else:
        return "Wrong auth code"





