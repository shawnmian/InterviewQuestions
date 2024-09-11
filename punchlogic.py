import json
from datetime import datetime

with open('PunchLogicTest.json', 'r') as file:
    data = json.load(file)

# Dictionary to store the jobs
job_dict = {}

job_meta = data['jobMeta']
for entry in job_meta:
    job = entry['job']
    rate = entry['rate']
    benefits_rate = entry['benefitsRate']

    job_dict[job] = {'rate': rate, 'benefits_rate': benefits_rate}

# Dict to store employees and their info
employee_dict = {}

employee_data = data['employeeData']
for employee_info in employee_data:
    employee_name = employee_info['employee']
    time_punches = employee_info['timePunch']

    employee_dict[employee_name] = {
        'timePunches': time_punches,
        'reg_hours': 0,
        'ot_hours': 0,
        'dt_hours': 0,
        'total_wage': 0,
        'total_benefits': 0
    }

def calculate_details(employee_dict, job_dict):
    #fxn to simplify further steps
    def calculate_hours(start_time, end_time):
        start = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
        end = datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')
        return (end - start).total_seconds() / 3600 

    # Iterate over each employee in the dictionary
    for employee, data in employee_dict.items():
        total_hours = 0
        regular_hours = 0
        overtime_hours = 0
        doubletime_hours = 0

        #run through timepunches 
        for punch in data['timePunches']:
            job = punch['job']
            start_time = punch['start']
            end_time = punch['end']

            
            job_rate_info = job_dict[job]
            rate = job_rate_info['rate']
            benefits_rate = job_rate_info['benefits_rate']

           
            hours_worked = calculate_hours(start_time, end_time)
            remaining_hours = hours_worked

            # Regular Hours: Cap at 40 hours
            if regular_hours < 40:
                regular_available = min(40 - regular_hours, remaining_hours)
                regular_hours += regular_available
                data['total_wage'] += regular_available * rate
                data['total_benefits'] += regular_available * benefits_rate
                remaining_hours -= regular_available

            # Overtime Hours: After regular hours, cap at 8 hours
            if regular_hours >= 40 and remaining_hours > 0 and overtime_hours < 8:
                overtime_available = min(8 - overtime_hours, remaining_hours)
                overtime_hours += overtime_available
                data['total_wage'] += overtime_available * rate * 1.5
                data['total_benefits'] += overtime_available * benefits_rate
                remaining_hours -= overtime_available

            # Double Time Hours: After overtime hours
            if regular_hours >= 40 and overtime_hours >= 8 and remaining_hours > 0:
                doubletime_hours += remaining_hours
                data['total_wage'] += remaining_hours * rate * 2
                data['total_benefits'] += remaining_hours * benefits_rate
                remaining_hours = 0

        # Store the calculated hours back into the employee data
        data['reg_hours'] = regular_hours
        data['ot_hours'] = overtime_hours
        data['dt_hours'] = doubletime_hours

    return employee_dict

updated_employee_data = calculate_details(employee_dict, job_dict)

# Convert updated_employee_data to the final format without time punches
final_employee_data = {}
for employee_name, details in updated_employee_data.items():
    final_employee_data[employee_name] = {
        "employee": employee_name,
        "regular": f"{details['reg_hours']}",
        "overtime": f"{details['ot_hours']}",
        "doubletime": f"{details['dt_hours']}",
        "wageTotal": f"{details['total_wage']}",
        "benefitTotal": f"{details['total_benefits']}"
    }

# Write the final_employee_data to a new JSON file
with open('final_employee_data.json', 'w') as json_file:
    json.dump(final_employee_data, json_file, indent=2)

# Print the final JSON output
print(json.dumps(final_employee_data, indent=2)) 
