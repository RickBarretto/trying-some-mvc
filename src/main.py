from entities.clinic import Clinic
from menus.start import start_application



if __name__ == "__main__":
    
    clinic_singleton = Clinic()
    start_application(clinic_singleton)
