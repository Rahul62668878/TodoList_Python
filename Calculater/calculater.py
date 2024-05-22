class Calculater:
    def __init__(self):
        pass

    def addition(self, *args):
        result = sum(args)
        return result

    def substration(self, *args):
        result = args[0]
        for num in args[1:]:
            result -= num
        return result

    def multiplication(self, *args):
        result = 1
        for num in args:
            result *= num
        return result

    def division(self, *args):
        if 0 in args[1:]:
            print("cannot divide by zero")
            return
        result = args[0]
        for num in args[1:]:
            result /= num
        return result

    def show_option(self):
        print("Select operations:")
        print("1. Addition")
        print("2. substraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

    def run(self):

        while True:
            self.show_option()
            choice = input("Enter your choice: ")
            if not choice in "5":
                nums = [float(x) for x in input("enter a number separated by space:  ").split()]

            if choice == "1":
                print("Result:", self.addition(*nums))
            elif choice == "2":
                print("Result: ", self.substration(*nums))
            elif choice == "3":
                print("Result: ", self.multiplication(*nums))
            elif choice == "4":
                print("Result: ", self.division(*nums))
            elif choice == "5":
                break
            else:
                print("enter a valid choice")


calc = Calculater()
calc.run()
