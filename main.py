"""
Create a Python script that will meet the constraints below:
I. The program should run continuously until the user chooses to “quit”: #done
II. The program must perform an HTTP GET request to a website #done
III. The program must access JSON data from the website #done
IV. The program needs to have at least 1 function of each type below:
    i. No arguments, and no return #done
    ii. Yes argument(s), and yes return #done
Demo your code to the instructor and copy/paste it below.
"""
import requests

def prGreen(skk):
    print("\033[92m {}\033[00m" .format(skk))

def prYell(skk):
    print("\033[93m {}\033[00m" .format(skk))

def is_it_email(email_add):
    email_add = email_add
    if '@' in email_add:
        return True
    else:
        prYell('\n    Error, Not a valid email')
        return False
    # make sure that the input at least looks like an email


def rep_check_call(email):
    email = email
    url = 'https://emailrep.io/' + email
    # as specified in API docs query must be done via HTTPS
    headers = {"Key": '** REDACTED **', "User-Agent": 'Email info School Project'}
    # provide the API key as instructed in in docs for the API, with description of project
    response = requests.get(url, headers=headers)

    try:
        if (response.json())['status'] == 'fail':
            prYell('Error accessing API.\nLimit of calls may be reached.')
            return None
    except KeyError:
        pass
        # the json data will only have the key 'status' if the call fails
        # this should handle the error

    while True:
        full_report = input('F - for a full report\nS - for a short report\n: ')
        if full_report in ['f', 'F']:
            print(response.text)
            break
            # print the json data from emailrep.io as a text dump to the screen
        elif full_report in ['s', 'S']:
            short = response.json()
            # print(short)
            prGreen('EMAIl:' + short['email'])
            print()
            prYell('MALICIOUS:' + str(short['details']['malicious_activity']))
            prGreen('BREACHED DATA:' + str(short['details']['data_breach']))
            prYell('LEAKED CREDS:' + str(short['details']['credentials_leaked']))
            prGreen('DISPOSABLE: ' + str(short['details']['disposable']))
            prYell('DELIVERABLE: ' + str(short['details']['deliverable']))
            more = input('\nHit M for more details or any other key to continue')
            if more in ['m', 'M']:
                print(response.text)
                break
            # just pull out some values for a short report
            break

def title():
    prGreen("""
    --------------------------
    |  E.MAIL INFO CHECKER   |
    | is it pwnd or sketchy? |
    --------------------------
    """)

while True:
    title()
    # take an email  from user
    email_add = input('Enter email to check, or exit to quit:\n>')
    if email_add in ['quit', 'exit', 'Exit', 'Quit', 'Q', 'q', 'die']:
        break
        # quit the loop if the user wants to exit
    if is_it_email(email_add):
        rep_check_call(email_add)
        # make sure the input contains an @ then run the API call function
print('Goodbye.')

# Some disposable emails to try:
# tikaunoutoimei-2793@yopmail.com
# rapafa+of9bli2pmmpk@guerrillamailblock.com

