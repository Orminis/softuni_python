information = input()

companies_dict = {}

while not information == "End":
    company_name, employee_id = information.split(" -> ")

    if company_name not in companies_dict:
        companies_dict[company_name] = [employee_id]
    else:
        if employee_id not in companies_dict[company_name]:
            companies_dict[company_name].append(employee_id)

    information = input()

order_companies = sorted(companies_dict.items(), key=lambda kvp: kvp[0])

for company, employees in order_companies:
    print(company)
    for employee in employees:
        print(f"-- {employee}")
