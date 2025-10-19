import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.metrics import classification_report
class MyDecisionTree:
    def __init__(self):
        self.df = pd.read_csv('sleep_health.csv')
        disorder_map = {
            'No Disorder': 0,
            'Insomnia': 1,
            'Sleep Apnea': 2
        }
        self.df['Sleep Disorder'] = self.df['Sleep Disorder'].map(disorder_map)
        self.X = self.df.drop(['Sleep Disorder'], axis='columns')
        self.y = self.df['Sleep Disorder']
        self.seedValue = 1
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.tree = DecisionTreeClassifier()
        self.tree = DecisionTreeClassifier(class_weight={0: 1, 1: 3, 2: 3})
        self.y_hat = None
        self.cm = None


    def updateSeed(self, newValue):
        self.seedValue = newValue

    def trainData(self):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, self.y, test_size=0.1, random_state=self.seedValue, stratify=self.y
        )

        self.tree.fit(self.X_train, self.y_train)
        print("Model trained successfully!")

    def makePrediction(self, gender, age, sleep_duration, quality_of_sleep, physical_activity, stress_level,
                       bmi_category, blood_pressure, heart_rate, daily_steps):

        input_data = {
            'Gender': gender,
            'Age': age,
            'Sleep Duration': sleep_duration,
            'Quality of Sleep': quality_of_sleep,
            'Physical Activity Level': physical_activity,
            'Stress Level': stress_level,
            'BMI Category': bmi_category,
            'Blood Pressure': blood_pressure,
            'Heart Rate': heart_rate,
            'Daily Steps': daily_steps
        }

        input_df = pd.DataFrame([input_data])

        print("Input Data for Prediction:\n", input_df)
        prediction = self.tree.predict(input_df)
        print("Raw Prediction Result:", prediction)

        if prediction[0] == -1:
            return "No sleep disorder detected."
        elif prediction[0] == 0:
            return "No Disorder"
        elif prediction[0] == 1:
            return "Insomnia"
        elif prediction[0] == 2:
            return "Sleep Apnea"
        else:
            return "Unknown Disorder"

    def testData(self):
        if self.tree is None or not hasattr(self.tree, "tree_"):
            raise ValueError("Model is not trained. Please call trainData() first.")

        self.y_hat = self.tree.predict(self.X_test)

        print("Unique labels in the test set:", set(self.y_test))

        unique_labels = set(self.y_test)
        if len(unique_labels) < 2:
            raise ValueError("Only one class present in the test data. Cannot evaluate model.")


        print('Here')
        print(self.X_test)
        accuracy = accuracy_score(self.y_test, self.y_hat)
        print(f"Accuracy: {int(accuracy * 100) / 100.0:.2f}")

        cm = confusion_matrix(self.y_test, self.y_hat)
        return cm, accuracy_score(self.y_test, self.y_hat)

    def readCategories(self):
        result = ''
        index = 0
        setOfCategories = set(self.y)

        for catName in sorted(setOfCategories):
            if index > 0:
                result += " / "

            if catName == 0:
                result += "No Disorder"
            elif catName == 1:
                result += "Insomnia"
            elif catName == 2:
                result += "Sleep Apnea"

            index += 1

        return result


