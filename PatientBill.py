#4) The program should then display a well formatted report showing all the patient information, 
#information about the procedures they had and total charges. Be sure the patient is being charged 
#for only those procedures that they had (HINT: match patient_id). Total charges should be calculated
#by adding all the charges of the procedures. If the patient is a veteran, they get 40% off their total charge
import PatientClass as pt
import ProcedureClass as pr

def main():
    
    patient_ID = '1'
    name = 'Matt Jones'
    address = '123 Main st, Waco TX 76706'
    phone = '254-555-7415'
    veteran_status = True
    patient = pt.Patient(patient_ID, name, address, phone, veteran_status)


    procedure1 = pr.Procedure('Physical Exam','2/15/2022', 'Dr. Irvine', '250', '1')
    procedure2 = pr.Procedure('MRI','2/15/2022', 'Dr. Hamilton', '1500', '1')
    procedure3 = pr.Procedure('MRI','2/17/2022', 'Dr. Drey', '1200', '2')


    print('*** Patient Bill ***')
    print('Name:', patient.get_name())
    print('Address:', patient.get_address())
    print('Phone:', patient.get_phone() + '\n')
    
    print('Procedure:', procedure1.get_prodedure_name())
    print('Date:', procedure1.get_procedure_date())
    print('Practioner:', procedure1.get_practioner_name())
    charge1 = float(procedure1.get_procedure_charges())
    print('Charge: $', "{:.2f}".format(charge1) + '\n')

    print('Procedure:', procedure2.get_prodedure_name())
    print('Date:', procedure2.get_procedure_date())
    print('Practioner:', procedure2.get_practioner_name())
    charge2 = float(procedure2.get_procedure_charges())
    print('Charge: $', "{:.2f}" and "{:,}".format(charge2) + '\n')
    
    charge3 = float(procedure3.get_procedure_charges())
    
    total_charge = charge1 + charge2 

    if veteran_status == True:
        total_charge = total_charge * .60
    

    print('Total Charges: $', "{:.2f}".format(total_charge))

main()


