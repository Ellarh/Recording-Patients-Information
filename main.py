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

record_again = True
while record_again:
  name = input("Patient's name: ")
  age = int(input("Patient's age: "))
  nation = input("Nationality: ")
  state = input("State of Origin: ")
  marital = input("Marital status: ")
  gender = input("Gender: ")
  purpose = input("Purpose of visit: ")
  next_visit = input("Next visit date: ")
  
  def new_patients_info(name, age, nation, state, marital, gender, purpose, next_visit):
    new_info = {}
    new_info["Name"] = name
    new_info["Age"] = age
    new_info["Nationality"] = nation
    new_info["State of Origin"] = state
    new_info["Marital Status"] = marital
    new_info["Gender"] = gender
    new_info["Purpose of Visit"] = purpose
    new_info["Next Visit date"] = next_visit
    patients_info.append(new_info)
  

  another_patient = input("Will you need to record another patient? 'Yes' or 'No'?  ").lower()
  if another_patient == 'no':
    new_patients_info(name, age, nation, state, marital, gender, purpose, next_visit)
    print(patients_info)
    record_again = False
  else:
    new_patients_info(name, age, nation, state, marital, gender, purpose, next_visit)