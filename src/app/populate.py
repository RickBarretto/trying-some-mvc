import random

import entity

def populate(clinic: entity.Clinic):

    # Adiciona sessões
    dates = [
        "13/02/2024", "27/05/2023", 
        "08/09/2022", "15/12/2021", 
        "03/04/2024", "21/07/2023"
    ]

    for date in dates:
        uid = clinic.new_session_id()
        session = entity.Session(uid, date)
        session.status = random.choice([
            entity.SessionStatus.UNBEGUN, 
            entity.SessionStatus.FINISHED
        ])

        clinic.sessions.append(session)
        clinic.last_session_id = uid

    # Adiciona pacientes
    last_cpf = "000.000.000-00"
    for _ in range(random.randint(5, 30)):
        uid = clinic.new_patient_id()
        patient = entity.Patient(
            uid, 
            new_cpf(last_cpf), 
            new_name(),
            new_extra_info()
        )

        clinic.patients.append(patient)
        clinic.last_patient_id = uid
        last_cpf = patient.cpf


def new_name():
    male_names = [
        "Bruno", "Daniel", "Felipe", "Henrique", "João", "Lucas", "Nathan",
        "Pedro", "Rafael", "Tiago", "Vinicius", "Zeca", "Bernardo", "Diego", 
        "Fabio", "Heitor", "Julio", "Enzo", "Matheus", "Otavio", "Renato", 
        "Caio", "Thiago", "Wesley", "Arthur",
    ]

    female_names = [
        "Ana", "Carla", "Eduarda", "Gabriela", "Isabela", "Karina", "Mariana",
        "Olivia", "Raquel", "Sofia", "Valeria", "Yasmin", "Alice", "Camila",
        "Elisa", "Iara", "Lara", "Diana", "Natalia", "Patricia",  "Samara",
        "Vivian", "Ximena", "Bianca", "Giovanna",
    ]

    surnames = [
        "Silva", "Santos", "Gomes", "Souza", "Costa", "Alves", "Lima", "Ferreira",
        "Ribeiro", "Oliveira", "Martins", "Rocha", "Dias", "Pereira", "Carvalho",
    ]

    name = []
    
    # Escolhe se irá usar nomes femininos ou masculinos
    if random.choice([True, False]):
        name_sample = male_names
    else:
        name_sample = female_names
    
    # Criam as partes do nome e sobrenome
    name.extend(random.choices(name_sample, k = random.randint(1, 2)))
    name.extend(random.choices(surnames, k = random.randint(1, 2)))

    return " ".join(name)


def new_cpf(last_cpf: str):
    digits = int(last_cpf.replace("-", "").replace(".", ""))
    digits += 1
    
    missing_digits = 11 - len(str(digits))
    prefix = "0" * missing_digits
    result = prefix + str(digits)

    return f"{result[0:3]}.{result[3:6]}.{result[6:9]}-{result[9:11]}"


def new_extra_info():
    allergies = [
        "Rinite alérgica", "Asma", "Conjuntivite alérgica", "Eczema", "Urticária",
        "Anafilaxia", "Lactose", "Caseína", "Ovos", "Amendoim", "Trigo", "Nozes",
        "Peixes", "Frutos do mar", "Penicilina", "Aspirina", "Iodo", "Insulina",         
        "Carbamazepina", "Diclofenaco", "Ibuprofeno", "Paracetamol", "Metronidazol",     
        "Sulfametoxazol",
    ]

    telephones = [
        "+55 (12) 34567890", "+55 (22) 98765432", "+55 (32) 67890123", 
        "+55 (42) 12345678", "+55 (52) 90123456", "+55 (62) 45678901", 
        "+55 (72) 78901234", "+55 (82) 23456789", "+55 (92) 56789012", 
        "+55 (98) 89012345", "+55 (13) 43215678", "+55 (23) 87654321", 
        "+55 (33) 78901234", "+55 (43) 21098765", "+55 (53) 65432109", 
        "+55 (63) 32165498", "+55 (73) 09876543", "+55 (83) 54321098", 
        "+55 (93) 43210987", "+55 (97) 65432109"
    ]

    patients_allergies = random.choices(allergies, k = random.randint(0, len(allergies) // 4))
    patients_telephones = random.choices(telephones, k = random.randint(1, 3))

    return [
        "Alergias: " + ", ".join(patients_allergies),
        "Contatos: " + ", ".join(patients_telephones)
    ]
