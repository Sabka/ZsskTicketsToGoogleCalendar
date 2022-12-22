from __future__ import print_function
from datetime import datetime, timedelta

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']


def write_event(event):
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())



    try:
        service = build('calendar', 'v3', credentials=creds)
        colors = service.colors().get().execute()


        d = datetime.now().date()
        tomorrow = datetime(d.year, d.month, d.day, 10) + timedelta(days=1)
        start = datetime.strptime(event.start_date + " " + event.start_time, '%d.%m.%y %H:%M').isoformat()
        end = datetime.strptime(event.end_date + " " + event.end_time, '%d.%m.%y %H:%M').isoformat()
        print(event, start, end)


        event_result = service.events().insert(calendarId='primary',
                                               body={
                                                   "summary": f'Cesta {event.train_type} vlakom z {event.start_station} do {event.end_station}',
                                                   "start": {"dateTime": start, "timeZone": 'Europe/Prague'},
                                                   "end": {"dateTime": end, "timeZone": 'Europe/Prague'},
                                                   "colorId": 6
                                               }
                                               ).execute()

        #print("created event", event_result['summary'])

    except HttpError as error:
        print('An error occurred: %s' % error)