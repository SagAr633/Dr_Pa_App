from decouple import config
from google.oauth2 import service_account
import googleapiclient.discovery
import datetime
from Patients.models import BookAppointment

CAL_ID = config('CAL_ID')
SCOPES = ['https://www.googleapis.com/auth/calendar']
SERVICE_ACCOUNT_FILE = './google-credentials.json'


def test_calendar():
    print("RUNNING TEST_CALENDAR()")

    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = googleapiclient.discovery.build('calendar', 'v3', credentials=credentials)

    # CREATE A NEW EVENT
    new_event = {
        'summary': "New Appointment Scheduled",
        'location': 'Calicut, Kerala,India',
        'hospital': 'MIMS Calicut',
        'start': {
            'date': f"{datetime.date.today()}",
            'timeZone': 'America/New_York',
        },
        'end': {
            'date': f"{datetime.date.today() + datetime.timedelta(minutes=45)}",
            'timeZone': 'America/New_York',
        },
    }
    service.events().insert(calendarId=CAL_ID, body=new_event).execute()
    print('Event created')

    # GET ALL EXISTING EVENTS
    events_result = service.events().list(calendarId=CAL_ID, maxResults=2500).execute()
    events = events_result.get('items', [])

    # LOG THEM ALL OUT IN DEV TOOLS CONSOLE
    for e in events:
        print(e)

    # uncomment the following lines to delete each existing item in the calendar
    # event_id = e['id']
    # service.events().delete(calendarId=CAL_ID, eventId=event_id).execute()

    return events
