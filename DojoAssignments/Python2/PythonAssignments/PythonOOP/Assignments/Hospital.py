import itertools
from types import *


class Patient(object):
    def __init__(self, name, allergies):
        self.patient_number = int(id(itertools.count().next))
        self.name = name
        self.allergies = allergies
        self.bed_number = None
        print (self.patient_number, self.name, self.allergies, self.bed_number)
        return


patient = Patient('bob', 'sulfa')
patient1 = Patient('bill', 'penicillin')

class Hospital(object):
    def __init__(self, name, capacity):
        self.patients = []
        self.name = name
        self.capacity = int(capacity)
        print(self.patients, self.name, self.capacity)
        return

    def admit(self, patient ):
        print(patient)
        patients = self.patients.extend([1,2,3])
        print(patients)
        print(type(patients))
        print(type(self.patients))
        return
    def discharge(self):
        return



hospital = Hospital('St. Elsewhere', 3050)
hospital.admit(patient.name)
hospital.admit(patient1.name)
