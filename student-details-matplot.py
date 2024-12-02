import pandas as pd
import matplotlib.pyplot as plt


data = {
    'StudentID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Name': ['Vijesh', 'Mani', 'Bala', 'Manoj', 'Blesson', 'Pranav', 'Vinoth', 'Logesh', 'vishwa', 'Vishal'],
    'Maths': [85, 90, 78, 92, 88, 76, 95, 89, 83, 91],
    'Science': [89, 94, 84, 95, 91, 80, 96, 88, 85, 93],
    'English': [78, 85, 80, 86, 82, 81, 87, 84, 83, 88],
    'History': [82, 87, 79, 90, 85, 78, 91, 86, 82, 89],
    'Geography': [80, 88, 76, 91, 84, 77, 92, 87, 81, 90]
}


df = pd.DataFrame(data)

def calculate_grade(avg_mark):
    if avg_mark >= 90:
        return 'A'
    elif avg_mark >= 80:
        return 'B'
    elif avg_mark >= 70:
        return 'C'
    elif avg_mark >= 60:
        return 'D'
    else:
        return 'F'


df['Average'] = df[['Maths', 'Science', 'English', 'History', 'Geography']].mean(axis=1)
df['Grade'] = df['Average'].apply(calculate_grade)


print(df[['StudentID', 'Name', 'Maths', 'Science', 'English', 'History', 'Geography', 'Average', 'Grade']])


fig, ax = plt.subplots()


df.plot(kind='bar', x='Name', y='Average', ax=ax, color='skyblue', legend=False)


for i in range(len(df)):
    ax.text(i, df['Average'][i] + 0.5, df['Grade'][i], ha='center')

plt.title('Student Average Scores and Grades')
plt.xlabel('Student')
plt.ylabel('Average Score')
plt.ylim(0, 100)
plt.show()
