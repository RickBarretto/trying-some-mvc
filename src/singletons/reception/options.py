import screen
from entities import clinic

from ._session_options import SessionOptions
from ._patient_options import PatientOptions

class ReceptionOptions(SessionOptions, PatientOptions):
    pass
