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


def is_it_email(email_add):
    email_add = email_add
    if '@' in email_add:
        return True
    else:
        print('You forgot the @')
        return False
    # make sure that the input at least looks like an email


def rep_check_call(email):
    email = email
    url = 'https://emailrep.io/'+ email
    # as specified in API docs query must be done via HTTPS

    headers = {"Key": '*** redacted ****',
               "User-Agent": 'Email Info Check for School Project',
               }

    response = requests.get(url, headers=headers)
    while True:
        full_report = input('F - for a full report\nS - for a short report')
        if full_report in ['f', 'F']:
            print(response.text)
            break
            # print the jason data from emailrep.io as a text dump to the screen
        elif full_report in ['s', 'S']:
            short = response.json()
            print(short)
            print('EMAIl:' + short['email'])
            print('SKETCHY:' + short['details']['malicious_activity'])
            print('BREACHED DATA:'+ short['details']['data_breach'])
            print('LEAKED CREDS:' + short['details']['credentials_leaked'])
            break


def title():
    print("""
    -------------------------
    |  E.MAIL INFO CHECKER  |
    |   pwnd? or sketchy?   |
    -------------------------
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

