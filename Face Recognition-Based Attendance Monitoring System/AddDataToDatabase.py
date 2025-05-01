import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL': "https://faceattendancerealtime-ffb12-default-rtdb.firebaseio.com/"
})


ref = db.reference('Students')

data = {
    "100000":
        {
            "name": "ROHAN R",
            "major": "DATA SCIENCE",
            "starting_year": 2021,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "100001":
        {
            "name": "Vinay Vinu",
            "major": "R&D",
            "starting_year": 2021,
            "total_attendance": 0,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "100002":
            {
                "name": "Likith VK",
                "major": "Cyber Security",
                "starting_year": 2021,
                "total_attendance": 0,
                "standing": "G",
                "year": 2,
                "last_attendance_time": "2022-12-11 00:54:34"
            },
    "100003":
            {
                "name": "Syed saquib",
                "major": "Investor",
                "starting_year": 2021,
                "total_attendance": 0,
                "standing": "G",
                "year": 2,
                "last_attendance_time": "2022-12-11 00:54:34"
            },
    "100004":
            {
                "name": "Sathwik pb",
                "major": "Devops or Vlsi",
                "starting_year": 2021,
                "total_attendance": 0,
                "standing": "G",
                "year": 2,
                "last_attendance_time": "2022-12-11 00:54:34"
            },
    "100005":
            {
                "name": "Saniya",
                "major": "CR",
                "starting_year": 2021,
                "total_attendance": 0,
                "standing": "G",
                "year": 3,
                "last_attendance_time": "2022-12-11 00:54:34"
            }
}

for key, value in data.items():
    ref.child(key).set(value)
