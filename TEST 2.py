def payroll_system():
    while True:
        # Number of workers
        workers_input = input("How many workers does your company have: ").strip()
        if not workers_input.isdigit():
            print("Please type a valid whole number of workers")
            continue
        num_workers = int(workers_input)
        if num_workers == 0:
            print("You don't have any workers in your company")
            return

        total_paid = 0

        for emp_num in range(1, num_workers + 1):
            print("\n" + "-" * 50)
            # Employee Name
            while True:
                name = input(f"Employee number {emp_num} name: ").strip()
                if name == "":
                    print("We can't have a blank name")
                else:
                    break

            # Hourly Rate
            while True:
                hourly_rate = input(f"What is the hourly rate of {name}: ").strip()
                try:
                    hourly_rate = float(hourly_rate)
                    if hourly_rate < 1:
                        print("You should rate properly your workers")
                        continue
                    break
                except ValueError:
                    print("Invalid hourly rate, please try again")

            # Hours Worked
            while True:
                hours_worked = input(f"How many hours did {name} work: ").strip()
                try:
                    hours_worked = float(hours_worked)
                    if hours_worked < 0:
                        print("We only accept positive and zero number of hours of work")
                        continue
                    break
                except ValueError:
                    print("Invalid number of hours work, please try again")

            # Overtime Hours
            while True:
                overtime_hours = input(f"Total hours of Overtime: ").strip()
                try:
                    overtime_hours = float(overtime_hours)
                    if overtime_hours < 0:
                        print("We only accept positive and zero number of hours of overtime")
                        continue
                    break
                except ValueError:
                    print("Invalid number of hours work, please try again")

            # Late Hours
            while True:
                late_hours = input(f"Total hours of late: ").strip()
                try:
                    late_hours = float(late_hours)
                    if late_hours < 0:
                        print("We only accept positive and zero number of hours of late")
                        continue
                    break
                except ValueError:
                    print("Invalid number of hours work, please try again")

            # Computations
            overtime_pay = (hourly_rate / 8) * overtime_hours
            deduction = late_hours * hourly_rate
            total_salary = (hourly_rate * hours_worked) + overtime_pay - deduction

            total_paid += total_salary

            # Payroll Summary
            print("\nPayroll Summary of Employee No:{}- {}".format(emp_num, name))
            print(f"Employee Number: {emp_num}")
            print(f"Employee Name: {name}")
            print(f"Hourly Rate: PHP {hourly_rate:.2f}")
            print(f"Total hours work: {hours_worked:.1f} hours")
            print(f"Total hours of overtime: {overtime_hours:.1f} hours")
            print(f"Overtime Payment of {name} is: PHP {overtime_pay:.2f}")
            print(f"Total hours of late: {late_hours:.1f} hours")
            print(f"Total deduction of {name}: PHP {deduction:.2f}")
            print(f"Total Salary of {name} is: PHP {total_salary:.2f}")

        print(f"\nTotal Salary Paid to {num_workers} Workers is: {total_paid:.2f}")

        # Process another payroll?
        while True:
            another = input("\nWould you like to process another payroll? Y/N: ").strip().upper()
            if another not in ("Y", "N"):
                print("Invalid input, please try again either Y or N")
            elif another == "N":
                print("Exiting program")
                return
            else:
                break


# Run the payroll system
print("Simple Company Payroll System")
payroll_system()
