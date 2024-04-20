student_scores = {"Harry": 81, "Ron": 78, "Hermione": 99, "Draco": 74, "Neville": 62}

student_grades = {}
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectation"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"
print(student_grades)


console_price = {"Steam Deck": 700, "Aya neo": 800, "One X player": 900}

console_type = {}
for console in console_price:
    price = console_price[console]
    if price > 800:
        console_type[console] = "Expensive"
    elif price > 700:
        console_type[console] = "Reasonable price"
    else:
        console_type[console] = "Good Deal"
print(console_type)

# nested list and dictionary

travel_log = {"Ghana": {"cities_visited": ["Accra", "Kumasi", "Tamale"]}, "USA": {"cities_visited": ["Ohio", "Indiana", "Virginia", "Maryland", "Illinois", "Wisconsin", "Tennessee", "Washington DC"]}}
print(travel_log)



