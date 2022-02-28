#2) PatientClass.py - Write a class named Patient that has the following attributes - 
#ID, name, address, phone, veteran_status (True or False). The Patient class’s __init__ method
#should accept an argument for each attribute. The Patient class should have accessor methods only for each attribute.

class Patient:
    def __init__(self,patient_ID,name,address,phone,veteran_status):
         self.patient_ID = patient_ID
         self.name = name
         self.address = address
         self.phone = phone
         self.veteran_status = veteran_status
         
    def set_ID(self, ID):
        self.ID = ID
    
    def set_name(self,name):
        self.name = name
    
    def set_adress(self,address):
        self.address = address
    
    def set_phone(self,phone):
        self.phone = phone
    
    def set_veteran_status(self, veteran_status):
        self.veteran_status = veteran_status

    def get_ID(self):
        return self.patient_ID
    
    def get_name(self):
        return self.name
    
    def get_address(self):
        return self.address
    
    def get_phone(self):
        return self.phone
    
    def get_veteran_status(self):
        return self.veteran_status


    
