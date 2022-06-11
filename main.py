from doctor import patient_logo, info_logo

patients_info = [
    {
        "Name": "Patricia Allen",
        "Age": 25,
        "Nationality": "America",
        "State of Origin": "New York",
        "Marital Status": "Single",
        "Gender": "Female",
        "Purpose of Visit": "Chest Xray and blood pressure checks",
        "Next Visit date": "28th August, 2022",
    },
    {
        "Name": "Nicholas Carmen",
        "Age": 30,
        "Nationality": "America",
        "State of Origin": "Seattle",
        "Marital Status": "Single",
        "Gender": "Male",
        "Purpose of Visit": "Blood pressure check up and weight checks",
        "Next Visit date": "25th September, 2022",
    },
]
print(patient_logo)
print(info_logo)

def new_patients_info(name, age, nation, state, marital, gender, purpose, next_visit):
    patients_info.append({
        "Name": name,
        "Age": age,
        "Nationality": nation,
        "State of Origin": state,
        "Marital Status": marital,
        "Gender": gender,
        "Purpose of Visit": purpose,
        "Next Visit date": next_visit,
    })

while True:
    new_patients_info(
        input("Patient's name: "),
        int(input("Patient's age: ")),
        input("Nationality: "),
        input("State of Origin: "),
        input("Marital status: "),
        input("Gender: "),
        input("Purpose of visit: "),
        input("Next visit date: "),
    )
    if input(
        "Will you need to record another patient? 'Yes' or 'No'?  "
    ).lower() == 'no':
        break

print(patients_info)
