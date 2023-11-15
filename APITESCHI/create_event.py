from datetime import datetime
from calendar_setup import get_calendar_service
import time

def create_event():
    date_Inicio = datetime(2023, 11, 4, 12, 0)
    date_Final = datetime(2023, 11, 4, 11, 0)
    event_title = 'Evento de ejemplo'
    time.sleep(0.5)
    event_desc = 'Prueba de creación de eventos en Google Calendar'
    time.sleep(0.5)
    start_date = date_Inicio.isoformat()
    end_date = date_Final.isoformat()
    calendar_service = get_calendar_service() 
    event_result = calendar_service.events().insert(calendarId='primary',
        body={
            "summary": event_title,
            "description": event_desc,
            "start": {"dateTime": start_date, "timeZone": 'America/Mexico_City'},
            "end": {"dateTime": end_date, "timeZone": 'America/Mexico_City'},
        }
    ).execute()

    print("Evento creado con éxito!")
    print("ID: ", event_result['id'])
    print("Título: ", event_result['summary'])
    print("Descripción: ", event_result["description"])
    print("Empieza en: ", event_result["start"])
    print("Termina en: ", event_result["end"])


if __name__ == '__main__':
    create_event()