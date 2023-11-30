from calendar_setup import get_calendar_service

def list_events():
    calendar_service = get_calendar_service()
    events_result = calendar_service.events().list(calendarId='primary', timeMin='2023-01-01T00:00:00Z',
                                                  maxResults=10, singleEvents=True,
                                                  orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No hay eventos próximos.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(f"ID: {event['id']}, Título: {event['summary']}, Comienza en: {start}")

if __name__ == '__main__':
    list_events()
