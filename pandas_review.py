import pandas

class_data = {
    "student": ["Ayush", "Zuko", "Katara", "Sokka"],
    "score": [97, 76, 98, 45],
    "attendance": [90, 60, 100, 85]
}

class_df = pandas.DataFrame(class_data)

class_df.to_csv("class_report.csv", index=False)

print(class_df.score.mean())
print(class_df.attendance.max())
class_df["passed"] = class_df["score"] > 50
print(class_df)

print(class_df[(class_df["score"]>70) & (class_df["attendance"]>80)])

print(class_df[(class_df["student"]=="Sokka") | (class_df["student"]=="Zuko")])

for index,row in class_df.iterrows():
    print(f"{row.student} scored {row.score} and has {row.attendance}% attendance.")

class_d = {row.student: row.score for (index,row) in class_df.iterrows()}
print(class_d)