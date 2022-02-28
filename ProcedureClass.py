#3) ProcedureClass.py - write a class named Procedure that represents a medical procedure that has
# been performed on a patient. The Procedure class should have the following attributes 
# Name of the procedure, Date of the procedure, Name of the practitioner who performed the procedure,
#Charges for the procedure and patient ID. The Procedure class’s __init__ method should accept an argument
#for each attribute. The Procedure class should have accessor methods only for each attribute.

class Procedure: 
    def __init__(self, procedure_name, procedure_date, practicioner_name, procedure_charges, patient_ID):
         self.procedure_name = procedure_name
         self.procedure_date = procedure_date
         self.practicioner_name = practicioner_name
         self.procedure_charges = procedure_charges
         self.patient_ID = patient_ID

    def set_procedure_name(self, procedure_name):
        self.procedure_name = procedure_name
    
    def set_procedure_date(self, procedure_date):
        self.procedure_date = procedure_date
    
    def set_practicioner_name(self, practicioner_name):
        self.practicioner_name = practicioner_name
    
    def set_procedure_charges(self, procedure_charges):
        self.procedure_charges = procedure_charges
    
    def set_patient_ID(self, patient_ID):
        self.patient_ID = patient_ID
    
    def get_prodedure_name(self):
        return self.procedure_name
    
    def get_procedure_date(self):
        return self.procedure_date

    def get_practioner_name(self):
        return self.practicioner_name
    
    def get_procedure_charges(self):
        return self.procedure_charges
    
    def get_patient_ID(self):
        return self.patient_ID
