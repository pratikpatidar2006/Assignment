from abc import ABC,abstractmethod

class Patient(ABC):
    def __init__(self, Patient_ID, Patient_Name, Patient_Age, Number_Days, Medicine_Charge):
        self.Patient_ID = Patient_ID
        self.Patient_Name = Patient_Name
        self.Patient_Age = Patient_Age
        self.Number_Days = Number_Days
        self.Medicine_Charge = Medicine_Charge

    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def calculate_discount(self):
        pass

    @abstractmethod
    def calculate_final_amount(self):
        pass

    @abstractmethod
    def generate_bill(self):
        pass
                 
class GeneralPatient(Patient):

    def calculate_bill(self):
        self.Consultation_Fee = 500
        self.Room_Charge = 1000 * self.Number_Days
        return self.Consultation_Fee + self.Room_Charge + self.Medicine_Charge

    def calculate_discount(self):
        self.Discount = 0
        return self.Discount

    def calculate_final_amount(self):
        total = self.calculate_bill()
        discount = self.calculate_discount()
        self.Final = total - discount
        return self.Final

    def generate_bill(self):
        self.Final = self.calculate_final_amount()

        print("""========================================
            PATIENT BILL
========================================""")

        print("Patient ID       :", self.Patient_ID)
        print("Patient Name     :", self.Patient_Name)
        print("Patient Age      :", self.Patient_Age)
        print("Patient Type     :", "General")
        print()

        print("Consultation Fee :", self.Consultation_Fee)
        print("Room Charges     :", self.Room_Charge)
        print("Medicine Charges :", self.Medicine_Charge)
        print()

        print("-----------------------------------------------")
        print("Total Hospital Bill :", self.Final)
        print("Bill Status         : GENERATED")
        
class EmergencyPatient(Patient):
    def calculate_bill(self):
        self.Consultation_Fee = 500
        self.Room_Charge = 1000 * self.Number_Days
        self.emerg=500
        return self.Consultation_Fee + self.Room_Charge + self.Medicine_Charge

    def calculate_discount(self):
        self.Discount = 0
        return self.Discount

    def calculate_final_amount(self):
        total = self.calculate_bill()
        discount = self.calculate_discount()
        self.Final = total - discount
        return self.Final

    def generate_bill(self):
        self.Final = self.calculate_final_amount()

        print("""========================================
            PATIENT BILL
========================================""")

        print("Patient ID       :", self.Patient_ID)
        print("Patient Name     :", self.Patient_Name)
        print("Patient Age      :", self.Patient_Age)
        print("Patient Type     :", "Emergency")
        print()

        print("Consultation Fee :", self.Consultation_Fee)
        print("Room Charges     :", self.Room_Charge)
        print("Medicine Charges :", self.Medicine_Charge)
        print("Emergency Charges:", self.emerg)
        print()

        print("-----------------------------------------------")
        print("Total Hospital Bill :", self.Final)
        print("Bill Status         : GENERATED")

class InsurancePatient(Patient):
    def calculate_bill(self):
        self.Consultation_Fee = 500
        self.Room_Charge = 1000 * self.Number_Days
        return self.Consultation_Fee + self.Room_Charge + self.Medicine_Charge

    def calculate_discount(self):
        self.Discount = 0.70*self.calculate_bill()
        return self.Discount

    def calculate_final_amount(self):
        self.total = self.calculate_bill()
        discount = self.calculate_discount()
        self.Final = self.total - discount
        return self.Final

    def generate_bill(self):
        self.Final = self.calculate_final_amount()

        print("""========================================
            PATIENT BILL
========================================""")

        print("Patient ID       :", self.Patient_ID)
        print("Patient Name     :", self.Patient_Name)
        print("Patient Age      :", self.Patient_Age)
        print("Patient Type     :", "Insurance")
        print()

        print("Consultation Fee :", self.Consultation_Fee)
        print("Room Charges     :", self.Room_Charge)
        print("Medicine Charges :", self.Medicine_Charge)
        print()
        print("Insurance Cover : 70 %")
        print("Insurance Amonut :",self.Discount)
        print("Patient Payable :",self.total-self.Discount)
        print("-----------------------------------------------")
        print("Total Hospital Bill :", self.Final)
        print("Bill Status         : GENERATED")

class CorporatePatient(Patient):  
    def calculate_bill(self):
        self.Consultation_Fee = 500
        self.Room_Charge = 1000 * self.Number_Days
        return self.Consultation_Fee + self.Room_Charge + self.Medicine_Charge

    def calculate_discount(self):
        self.Discount = 0.20*self.calculate_bill()
        return self.Discount

    def calculate_final_amount(self):
        self.total = self.calculate_bill()
        discount = self.calculate_discount()
        self.Final = self.total - discount
        return self.Final

    def generate_bill(self):
        self.Final = self.calculate_final_amount()

        print("""========================================
            PATIENT BILL
========================================""")

        print("Patient ID       :", self.Patient_ID)
        print("Patient Name     :", self.Patient_Name)
        print("Patient Age      :", self.Patient_Age)
        print("Patient Type     :", "Corporate")
        print()
        
        print("Corporate Discount:",self.Discount)
        print("Consultation Fee :", self.Consultation_Fee)
        print("Room Charges     :", self.Room_Charge)
        print("Medicine Charges :", self.Medicine_Charge)
        print("Payable Amonut   :",self.total-self.Discount)
        print()

        print("-----------------------------------------------")
        print("Total Hospital Bill :", self.Final)
        print("Bill Status         : GENERATED")
list=[]  
while True:
     print()
     print()
     print("""------------------------------------------------------------
MAIN MENU:
------------------------------------------------------------

========================================
       HOSPITAL MANAGEMENT SYSTEM
========================================

1. Register Patient
2. Generate Patient Bill
3. View Patient Bill
4. Exit
""")
     c=int(input("Enter your choice :"))
     if c==1:
         print("""------------------------------------------------------------
OPTION 1: REGISTER PATIENT
------------------------------------------------------------""")
         Patient_ID=int(input("Enter patient ID:"))
         Patient_Name=input("Enter patient name :")
         Patient_Age=int(input("Enter patient Age :"))
         print()
         print("""1. General Patient
2. Emergency Patient
3. Insurance Patient
4. Corporate Patient""") 
         ch=int(input("Enter your choice:"))
         if ch==1:
             Number_Days=int(input("Enter number of days :"))
             Medicine_Charge=int(input("Enter medicine charge :"))
             patient=GeneralPatient(Patient_ID,Patient_Name,Patient_Age,Number_Days,Medicine_Charge)
             patient.generate_bill()
             list.append(patient) 

         elif ch==2:
             Number_Days=int(input("Enter number of days :"))
             Medicine_Charge=int(input("Enter medicine charge :"))
             Emerg_charge=int(input("Enter emergency charge :"))
             patient=EmergencyPatient(Patient_ID,Patient_Name,Patient_Age,Number_Days,Medicine_Charge)
             patient.generate_bill()
             patient.Emerg_charge=Emerg_charge
             list.append(patient) 
         elif ch==3:
             Number_Days=int(input("Enter number of days :"))
             Medicine_Charge=int(input("Enter medicine charge :"))
             patient=InsurancePatient(Patient_ID,Patient_Name,Patient_Age,Number_Days,Medicine_Charge)
             patient.generate_bill()
             list.append(patient)
              
         elif ch==4:
             Number_Days=int(input("Enter number of days :"))
             Medicine_Charge=int(input("Enter medicine charge :"))
             patient=CorporatePatient(Patient_ID,Patient_Name,Patient_Age,Number_Days,Medicine_Charge)
             patient.generate_bill() 
             list.append(patient)
             
         else:
              break
     elif c == 2:
           Patient_ID = int(input("Enter Patient ID : "))
           found = False

           for patient in list:
                 if patient.Patient_ID == Patient_ID:
                     patient.generate_bill()
                     found = True
                     break

           if found==False:
                print("Patient not found.")   
                                                                       
     elif c == 3:
           Patient_ID = int(input("Enter Patient ID : "))
           found = False

           for patient in list:
                 if patient.Patient_ID == Patient_ID:
                    print("\n========== PATIENT DETAILS ==========")
                    print("Patient ID       :", patient.Patient_ID)
                    print("Patient Name     :", patient.Patient_Name)
                    print("Patient Age      :", patient.Patient_Age)
                    print("Consultation Fee :", patient.Consultation_Fee)
                    print("Room Charges     :", patient.Room_Charge)
                    print("Medicine Charges :", patient.Medicine_Charge)

                    if isinstance(patient, EmergencyPatient):
                        print("Emergency Charges:", patient.emerg)

                    if isinstance(patient, InsurancePatient):
                          print("Insurance Discount:", patient.Discount)
                          print("Patient Payable   :", patient.Final)

                    if isinstance(patient, CorporatePatient):
                          print("Corporate Discount:", patient.Discount)
                          print("Patient Payable   :", patient.Final)

                 print("------------------------------------")
                 print("Total Bill        :", patient.Final)
                 print("Bill Status       : Generated")

                 found = True
                 break

           if found==False:
             print("Patient not found.")