stud_score = {
    "ram": 90.10,
    "arun": 91.50,
    "kalai": 92.20,
    "maha": 90.50
}

topstud = ""
topscore = -1

for stud, score in stud_score.items():
    if score > topscore:
        topscore = score
        topstud = stud

print(f"The {topstud} is the student with a highest score of: {topscore}")