import entity
from app import start
from app.populate import populate


if __name__ == "__main__":
    clinic = entity.Clinic()
    populate(clinic)
    start(clinic)
