class Atm:

    def __init__(self, pin, balance):
        self.pin = pin
        self.balance = balance

        self.menu()

        def menu(self):
            while True:
                user_input = input("""
                    Hello! How would you like to proceed?
                    1. Enter 1 to create a PIN
                    2. Enter 2 to deposit
                    3. Enter 3 to withdraw
                    4. Enter 4 to check balance
                    5. Enter 5 to exit
                    """)

                if user_input == "1":
                    self.create_pin()
                elif user_input == "2":
                    self.deposit()
                elif user_input == "3":
                    self.withdraw()
                elif user_input == "4":
                    self.check_balance()
                elif user_input == "5":
                    print("Goodbye!")
                    break
                else:
                    print("Invalid input. Please choose a valid option.")