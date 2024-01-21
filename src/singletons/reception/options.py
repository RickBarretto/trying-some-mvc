import screen
from entities import clinic

from ._session_options import SessionOptions
from ._patient_options import PatientOptions
from ._current_session_option import CurrentSessionOptions


class ReceptionOptions(SessionOptions, PatientOptions, CurrentSessionOptions):
    pass
