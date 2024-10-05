# GPA scale for reference
GPA_SCALE = [
    (97, 100, 4.00, "A+"),
    (93, 96, 4.00, "A"),
    (89, 92, 3.70, "A-"),
    (84, 88, 3.30, "B+"),
    (80, 83, 3.00, "B"),
    (76, 79, 2.70, "B-"),
    (73, 75, 2.30, "C+"),
    (70, 72, 2.00, "C"),
    (67, 69, 1.70, "C-"),
    (64, 66, 1.30, "D+"),
    (60, 63, 1.00, "D"),
    (0, 59, 0.00, "F")
]
students = {
    13560901: {
        "name": "Ahmed",
        "gpa": 3.9,
        "grades": {
            "Biology": {"gpa": 4.0, "grade": "A", "mark": 96},
            "Chemistry": {"gpa": 3.7, "grade": "A-", "mark": 90},
            "English": {"gpa": 4.0, "grade": "A+", "mark": 100},
            "History": {"gpa": 4.0, "grade": "A+", "mark": 99},
            "Math": {"gpa": 3.7, "grade": "A-", "mark": 91},
            "Physics": {"gpa": 4.0, "grade": "A+", "mark": 98},
        },
        "points": 70.2,
    },
    13560902: {
        "name": "Mohammed",
        "gpa": 3.95,
        "grades": {
            "Biology": {"gpa": 4.0, "grade": "A", "mark": 94},
            "Chemistry": {"gpa": 4.0, "grade": "A+", "mark": 97},
            "English": {"gpa": 4.0, "grade": "A+", "mark": 98},
            "History": {"gpa": 4.0, "grade": "A+", "mark": 100},
            "Math": {"gpa": 3.7, "grade": "A-", "mark": 91},
            "Physics": {"gpa": 4.0, "grade": "A", "mark": 95},
        },
        "points": 71.1,
    },
    13560903: {
        "name": "Ali",
        "gpa": 3.95,
        "grades": {
            "Biology": {"gpa": 4.0, "grade": "A", "mark": 93},
            "Chemistry": {"gpa": 4.0, "grade": "A", "mark": 93},
            "English": {"gpa": 4.0, "grade": "A", "mark": 96},
            "History": {"gpa": 3.7, "grade": "A-", "mark": 92},
            "Math": {"gpa": 4.0, "grade": "A", "mark": 95},
            "Physics": {"gpa": 4.0, "grade": "A+", "mark": 98},
        },
        "points": 71.1,
    },
    13560904: {
        "name": "Hossam",
        "gpa": 3.95,
        "grades": {
            "Biology": {"gpa": 4.0, "grade": "A+", "mark": 97},
            "Chemistry": {"gpa": 4.0, "grade": "A", "mark": 95},
            "English": {"gpa": 3.7, "grade": "A-", "mark": 91},
            "History": {"gpa": 4.0, "grade": "A+", "mark": 98},
            "Math": {"gpa": 4.0, "grade": "A", "mark": 96},
            "Physics": {"gpa": 4.0, "grade": "A", "mark": 95},
        },
        "points": 71.1,
    },
    13560905: {
        "name": "Youssef",
        "gpa": 4.0,
        "grades": {
            "Biology": {"gpa": 4.0, "grade": "A+", "mark": 98},
            "Chemistry": {"gpa": 4.0, "grade": "A+", "mark": 100},
            "English": {"gpa": 4.0, "grade": "A", "mark": 96},
            "History": {"gpa": 4.0, "grade": "A+", "mark": 100},
            "Math": {"gpa": 4.0, "grade": "A", "mark": 96},
            "Physics": {"gpa": 4.0, "grade": "A+", "mark": 100},
        },
        "points": 72.0,
    },
    13560906: {
        "name": "Marwan",
        "gpa": 3.33,
        "grades": {
            "Biology": {"gpa": 4.0, "grade": "A+", "mark": 98},
            "Chemistry": {"gpa": 3.3, "grade": "B+", "mark": 85},
            "English": {"gpa": 4.0, "grade": "A", "mark": 96},
            "History": {"gpa": 1.0, "grade": "D", "mark": 60},
            "Math": {"gpa": 3.7, "grade": "A-", "mark": 91},
            "Physics": {"gpa": 4.0, "grade": "A", "mark": 94},
        },
        "points": 60.0,
    },
    13560907: {
        "name": "Kareem",
        "gpa": 3.05,
        "grades": {
            "Biology": {"gpa": 2.0, "grade": "C", "mark": 70},
            "Chemistry": {"gpa": 3.3, "grade": "B+", "mark": 88},
            "English": {"gpa": 2.3, "grade": "C+", "mark": 75},
            "History": {"gpa": 3.3, "grade": "B+", "mark": 88},
            "Math": {"gpa": 3.7, "grade": "A-", "mark": 91},
            "Physics": {"gpa": 3.7, "grade": "A-", "mark": 90},
        },
        "points": 54.9,
    },
    13560908: {
        "name": "Marco",
        "gpa": 2.55,
        "grades": {
            "Biology": {"gpa": 3.7, "grade": "A-", "mark": 91},
            "Chemistry": {"gpa": 3.7, "grade": "A-", "mark": 90},
            "English": {"gpa": 1.0, "grade": "D", "mark": 61},
            "History": {"gpa": 1.3, "grade": "D+", "mark": 66},
            "Math": {"gpa": 3.3, "grade": "B+", "mark": 87},
            "Physics": {"gpa": 2.3, "grade": "C+", "mark": 73},
        },
        "points": 45.9,
    },
    13560909: {
        "name": "Hani",
        "gpa": 3.0,
        "grades": {
            "Biology": {"gpa": 1.7, "grade": "C-", "mark": 67},
            "Chemistry": {"gpa": 2.3, "grade": "C+", "mark": 73},
            "English": {"gpa": 4.0, "grade": "A", "mark": 95},
            "History": {"gpa": 2.3, "grade": "C+", "mark": 73},
            "Math": {"gpa": 3.7, "grade": "A-", "mark": 89},
            "Physics": {"gpa": 4.0, "grade": "A+", "mark": 99},
        },
        "points": 54.0,
    },
    13560910: {
        "name": "Khaled",
        "gpa": 3.28,
        "grades": {
            "Biology": {"gpa": 3.3, "grade": "B+", "mark": 85},
            "Chemistry": {"gpa": 3.0, "grade": "B", "mark": 83},
            "English": {"gpa": 1.7, "grade": "C-", "mark": 68},
            "History": {"gpa": 4.0, "grade": "A+", "mark": 99},
            "Math": {"gpa": 3.7, "grade": "A-", "mark": 90},
            "Physics": {"gpa": 4.0, "grade": "A+", "mark": 99},
        },
        "points": 59.1,
    },
}

tutorials = {
    "Biology": "www.examplecollege.edu.eg/tutorials/biology",
    "Chemistry": "www.examplecollege.edu.eg/tutorials/chemistry",
    "English": "www.examplecollege.edu.eg/tutorials/english",
    "History": "www.examplecollege.edu.eg/tutorials/history",
    "Math": "www.examplecollege.edu.eg/tutorials/math",
    "Physics": "www.examplecollege.edu.eg/tutorials/physics",
}

staff = {
    "Biology": {
        "Doctor": "biologydoctor@ecollege.edu.eg",
        "Assistant": "biologyassist@ecollege.edu.eg",
    },
    "Chemistry": {
        "Doctor": "chemistrydoctor@ecollege.edu.eg",
        "Assistant": "chemistryassist@ecollege.edu.eg",
    },
    "English": {
        "Doctor": "englishdoctor@ecollege.edu.eg",
        "Assistant": "englishassist@ecollege.edu.eg",
    },
    "History": {
        "Doctor": "historydoctor@ecollege.edu.eg",
        "Assistant": "historyassist@ecollege.edu.eg",
    },
    "Math": {
        "Doctor": "mathdoctor@ecollege.edu.eg",
        "Assistant": "mathassist@ecollege.edu.eg",
    },
    "Physics": {
        "Doctor": "physicsdoctor@ecollege.edu.eg",
        "Assistant": "physicsassist@ecollege.edu.eg",
    },
}