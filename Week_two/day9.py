#Dictionaries,empty dicitonary {}
#Example
student_scores = {
    "Ederson": 81,
    "Robertson": 95,
    "Allison": 91,
    "Sanjay": 74,
    "Precious": 88
}
student_grades = {}
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)
print(student_scores)

# dictionary inside dictionary
# nested dictionary
travel_log = [
    {
        "country": "London",
        "cities_visited": ["Derby", "Bristol", "Blackpool"],
        "Total_visited": 12
    },
    {
        "country": "Italy",
        "cities_visited": ["Rome", "Florence", "Milan"],
        "Total_visited": 10
    },
]

print(travel_log)

