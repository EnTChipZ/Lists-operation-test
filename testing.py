def payroll_system():
    while True:

        workers_input = input("How many workers does your company have: ").strip()
        if not workers_input.isdigit():
            print("Please type a valid whole number of workers")
            continue
        num_workers = int(workers_input)
        if num_workers == 0:
            print("You don't have any workers in your company")
            return

        total_paid = 0
        employees = []

        for emp_num in range(1, num_workers + 1):
            print("\n" + "-" * 50)

            while True:
                name = input(f"Employee number {emp_num} name: ").strip()
                if name == "":
                    print("We can't have a blank name")
                else:
                    break


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


            overtime_pay = (hourly_rate / 8) * overtime_hours
            deduction = late_hours * hourly_rate
            total_salary = (hourly_rate * hours_worked) + overtime_pay - deduction
            total_paid += total_salary

 
            employees.append({
                "emp_num": emp_num,
                "name": name,
                "hourly_rate": hourly_rate,
                "hours_worked": hours_worked,
                "overtime_hours": overtime_hours,
                "late_hours": late_hours,
                "overtime_pay": overtime_pay,
                "deduction": deduction,
                "total_salary": total_salary
            })


            print("\nPayroll Summary of Employee No:{} - {}".format(emp_num, name))
            print(f"Employee Number: {emp_num}")
            print(f"Employee Name: {name}")
            print(f"Hourly Rate: PHP {hourly_rate:.2f}")
            print(f"Total hours work: {hours_worked:.1f} hours")
            print(f"Total hours of overtime: {overtime_hours:.1f} hours")
            print(f"Overtime Payment of {name} is: PHP {overtime_pay:.2f}")
            print(f"Total hours of late: {late_hours:.1f} hours")
            print(f"Total deduction of {name}: PHP {deduction:.2f}")
            print(f"Total Salary of {name} is: PHP {total_salary:.2f}")

        while True:
            more = input("\nDo you want to add more workers? Y/N: ").strip().upper()
            if more == "Y":
                extra = input("How many additional workers do you want to add? ").strip()
                if extra.isdigit() and int(extra) > 0:
                    extra = int(extra)
                    for i in range(extra):
                        emp_num = len(employees) + 1
                        print(f"\nAdding Extra Employee #{emp_num}")
                        name = input(f"Employee number {emp_num} name: ").strip()
                        hourly_rate = float(input(f"What is the hourly rate of {name}: "))
                        hours_worked = float(input(f"How many hours did {name} work: "))
                        overtime_hours = float(input("Total hours of Overtime: "))
                        late_hours = float(input("Total hours of late: "))

                        overtime_pay = (hourly_rate / 8) * overtime_hours
                        deduction = late_hours * hourly_rate
                        total_salary = (hourly_rate * hours_worked) + overtime_pay - deduction
                        total_paid += total_salary

                        employees.append({
                            "emp_num": emp_num,
                            "name": name,
                            "hourly_rate": hourly_rate,
                            "hours_worked": hours_worked,
                            "overtime_hours": overtime_hours,
                            "late_hours": late_hours,
                            "overtime_pay": overtime_pay,
                            "deduction": deduction,
                            "total_salary": total_salary
                        })
                        print(f"Added {name} with salary PHP {total_salary:.2f}")
                else:
                    print("Invalid number of extra workers.")
            elif more == "N":
                break
            else:
                print("Please answer Y or N")

        print(f"\nTotal Salary Paid to {len(employees)} Workers is: {total_paid:.2f}")

        while True:
            another = input("\nWould you like to process another payroll? Y/N: ").strip().upper()
            if another not in ("Y", "N"):
                print("Invalid input, please try again either Y or N")
            elif another == "N":
                print("Exiting program")
                return
            else:
                break

print("Simple Company Payroll System")
payroll_system()
