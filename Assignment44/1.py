from abc import ABC, abstractmethod
import random


class Payment(ABC):

    @abstractmethod
    def validate_payment(self):
        pass

    @abstractmethod
    def calculate_processing_fee(self):
        pass

    @abstractmethod
    def authenticate_payment(self):
        pass

    @abstractmethod
    def process_payment(self):
        pass

    @abstractmethod
    def generate_receipt(self):
        pass


class UPIPayment(Payment):

    def validate_payment(self):
        self.upi_id = input("Enter UPI ID : ")
        self.upi_pin = input("Enter UPI PIN : ")
        return "Payment details validated successfully."

    def calculate_processing_fee(self):
        self.processing_fee = self.amount * 0 / 100
        return self.processing_fee

    def authenticate_payment(self):
        return "Authentication successful."

    def process_payment(self):
        return "Payment processed successfully."

    def generate_receipt(self):
        print("\n========== PAYMENT PROCESSING ==========")
        print("Customer Name  :", self.customer_name)
        print("Order ID       :", self.order_id)
        print("Payment Method : UPI")
        print("Order Amount   : Rs.", self.amount)
        print("Processing Fee : Rs.", self.calculate_processing_fee())
        print("Final Amount   : Rs.", self.amount + self.processing_fee)
        print(self.validate_payment())
        print(self.authenticate_payment())
        print(self.process_payment())
        print("Transaction ID :", self.transaction_id)
        print("Payment Status : SUCCESS")


class CreditCardPayment(Payment):

    def validate_payment(self):
        self.card_number = input("Enter Card Number : ")
        self.card_holder = input("Enter Card Holder Name : ")
        self.cvv = input("Enter CVV : ")
        self.expiry = input("Enter Expiry Date : ")
        return "Payment details validated successfully."

    def calculate_processing_fee(self):
        self.processing_fee = self.amount * 2 / 100
        return self.processing_fee

    def authenticate_payment(self):
        return "Authentication successful."

    def process_payment(self):
        return "Payment processed successfully."

    def generate_receipt(self):
        print("\n========== PAYMENT PROCESSING ==========")
        print("Customer Name  :", self.customer_name)
        print("Order ID       :", self.order_id)
        print("Payment Method : Credit Card")
        print("Order Amount   : Rs.", self.amount)
        print("Processing Fee : Rs.", self.calculate_processing_fee())
        print("Final Amount   : Rs.", self.amount + self.processing_fee)
        print(self.validate_payment())
        print(self.authenticate_payment())
        print(self.process_payment())
        print("Transaction ID :", self.transaction_id)
        print("Payment Status : SUCCESS")


class DebitCardPayment(Payment):

    def validate_payment(self):
        self.card_number = input("Enter Card Number : ")
        self.card_holder = input("Enter Card Holder Name : ")
        self.cvv = input("Enter CVV : ")
        self.expiry = input("Enter Expiry Date : ")
        return "Payment details validated successfully."

    def calculate_processing_fee(self):
        self.processing_fee = self.amount * 1 / 100
        return self.processing_fee

    def authenticate_payment(self):
        return "Authentication successful."

    def process_payment(self):
        return "Payment processed successfully."

    def generate_receipt(self):
        print("\n========== PAYMENT PROCESSING ==========")
        print("Customer Name  :", self.customer_name)
        print("Order ID       :", self.order_id)
        print("Payment Method : Debit Card")
        print("Order Amount   : Rs.", self.amount)
        print("Processing Fee : Rs.", self.calculate_processing_fee())
        print("Final Amount   : Rs.", self.amount + self.processing_fee)
        print(self.validate_payment())
        print(self.authenticate_payment())
        print(self.process_payment())
        print("Transaction ID :", self.transaction_id)
        print("Payment Status : SUCCESS")


class NetBankingPayment(Payment):

    def validate_payment(self):
        self.bank_name = input("Enter Bank Name : ")
        self.account_number = input("Enter Account Number : ")
        self.customer_id = input("Enter Customer ID : ")
        return "Payment details validated successfully."

    def calculate_processing_fee(self):
        self.processing_fee = self.amount * 0.5 / 100
        return self.processing_fee

    def authenticate_payment(self):
        return "Authentication successful."

    def process_payment(self):
        return "Payment processed successfully."

    def generate_receipt(self):
        print("\n========== PAYMENT PROCESSING ==========")
        print("Customer Name  :", self.customer_name)
        print("Order ID       :", self.order_id)
        print("Payment Method : Net Banking")
        print("Order Amount   : Rs.", self.amount)
        print("Processing Fee : Rs.", self.calculate_processing_fee())
        print("Final Amount   : Rs.", self.amount + self.processing_fee)
        print(self.validate_payment())
        print(self.authenticate_payment())
        print(self.process_payment())
        print("Transaction ID :", self.transaction_id)
        print("Payment Status : SUCCESS")


class WalletPayment(Payment):

    def validate_payment(self):
        self.wallet_name = input("Enter Wallet Name : ")
        self.mobile_number = input("Enter Mobile Number : ")
        self.wallet_pin = input("Enter Wallet PIN : ")
        return "Payment details validated successfully."

    def calculate_processing_fee(self):
        self.processing_fee = self.amount * 1.5 / 100
        return self.processing_fee

    def authenticate_payment(self):
        return "Authentication successful."

    def process_payment(self):
        return "Payment processed successfully."

    def generate_receipt(self):
        print("\n========== PAYMENT PROCESSING ==========")
        print("Customer Name  :", self.customer_name)
        print("Order ID       :", self.order_id)
        print("Payment Method : Wallet")
        print("Order Amount   : Rs.", self.amount)
        print("Processing Fee : Rs.", self.calculate_processing_fee())
        print("Final Amount   : Rs.", self.amount + self.processing_fee)
        print(self.validate_payment())
        print(self.authenticate_payment())
        print(self.process_payment())
        print("Transaction ID :", self.transaction_id)
        print("Payment Status : SUCCESS")


payments = []


while True:

    print("""
============================================================
                 ONLINE PAYMENT SYSTEM
============================================================

1. Make Payment
2. View Payment Details
3. Exit
""")

    choice = int(input("Enter your choice : "))

    if choice == 1:

        customer_name = input("Customer Name : ")
        order_id = input("Order ID : ")
        amount = float(input("Order Amount : "))

        print("""
Select Payment Method

1. UPI
2. Credit Card
3. Debit Card
4. Net Banking
5. Wallet
""")

        ch = int(input("Enter your choice : "))

        if ch == 1:

            payment = UPIPayment()

            payment.customer_name = customer_name
            payment.order_id = order_id
            payment.amount = amount
            payment.transaction_id = "TXN" + str(random.randint(100000, 999999))

            payment.generate_receipt()
            payments.append(payment)

        elif ch == 2:

            payment = CreditCardPayment()

            payment.customer_name = customer_name
            payment.order_id = order_id
            payment.amount = amount
            payment.transaction_id = "TXN" + str(random.randint(100000, 999999))

            payment.generate_receipt()
            payments.append(payment)

        elif ch == 3:

            payment = DebitCardPayment()

            payment.customer_name = customer_name
            payment.order_id = order_id
            payment.amount = amount
            payment.transaction_id = "TXN" + str(random.randint(100000, 999999))

            payment.generate_receipt()
            payments.append(payment)

        elif ch == 4:

            payment = NetBankingPayment()

            payment.customer_name = customer_name
            payment.order_id = order_id
            payment.amount = amount
            payment.transaction_id = "TXN" + str(random.randint(100000, 999999))

            payment.generate_receipt()
            payments.append(payment)

        elif ch == 5:

            payment = WalletPayment()

            payment.customer_name = customer_name
            payment.order_id = order_id
            payment.amount = amount
            payment.transaction_id = "TXN" + str(random.randint(100000, 999999))

            payment.generate_receipt()
            payments.append(payment)

        else:
            print("Invalid payment method.")

    elif choice == 2:

        order_id = input("Enter Order ID : ")

        found = False

        for payment in payments:

            if payment.order_id == order_id:
                print(payment)
                print("\n========== PAYMENT DETAILS ==========")
                print("Order ID       :", payment.order_id)
                print("Customer Name  :", payment.customer_name)
                print("Order Amount   :", payment.amount)
                print("Processing Fee :", payment.processing_fee)
                print("Final Amount   :", payment.amount + payment.processing_fee)
                print("Transaction ID :", payment.transaction_id)
                print("Payment Status : SUCCESS")

                found = True
                break

        if found == False:
            print("Payment record not found.")

    elif choice == 3:

        print("Thank you for using Online Payment System.")
        break

    else:
        print("Invalid choice.")