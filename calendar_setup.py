import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/calendar']
# Obtiene el directorio actual donde se encuentra el script 'calendar_setup.py'
directorio_actual = os.path.dirname(__file__)

# Nombre del archivo que deseas leer
nombre_archivo = 'client_secret_432443295689-rcikjhqjb904okrs17gu8po6sb3mq3s8.apps.googleusercontent.com.json'

CREDENTIALS_FILE = os.path.join(directorio_actual, nombre_archivo)


def get_calendar_service():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)
    return service
