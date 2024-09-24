import tkinter as tk
import joblib
import numpy as np
from tkinter import messagebox
from sklearn.preprocessing import MinMaxScaler

# Loading the training model and scaler
model = joblib.load('Saved model/heart_disease_model_v1.3.joblib')
scaler = joblib.load('Saved scaler/scaler_v1.3.joblib')

# Creating the prediction function

def predict_heart_disease():
    try:
        # Getting the input values from the entry fields
        age = int(entries[0].get())
        sex = 1 if sex_var.get() == "Male" else 0
        cp = int(dropdown_vars[0].get())
        trestbps = int(entries[1].get())
        chol = int(entries[2].get())
        fbs = int(dropdown_vars[1].get())
        restecg = int(dropdown_vars[2].get())
        thalach = int(entries[3].get())
        exang = int(dropdown_vars[3].get())
        oldpeak = float(entries[4].get())
        slope = int(dropdown_vars[4].get())
        ca = int(dropdown_vars[5].get())
        thal = int(dropdown_vars[6].get())

        # Creating a numpy array with the input values
        input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

        # Normalizing the input data with the loaded scaler
        input_data_scaled = scaler.transform(input_data)

        # Making the prediction using the loaded model
        prediction = model.predict(input_data_scaled)

        # Display the prediction result
        if prediction == 0:
            message_label.config(text="You don't have heart disease.",bg="cyan", fg = 'black')
        else:
            message_label.config(text="You may have heart disease.",bg="red", fg = 'black')

    except ValueError:
        messagebox.showerror("Error", "Please enter valid input values.")

# Creating the main GUI
root = tk.Tk()
root.title("Heart Disease Prediction")
root.geometry("700x350")
root.resizable(False, False) 

boarder_frame = tk.Frame(root, bd=2, relief="solid")
boarder_frame.pack(fill="both", expand=True, padx=10, pady=10)

left_frame = tk.Frame(boarder_frame,bg="cyan", width=200)
left_frame.grid(row=0, column=0, padx=8, pady=8, sticky="ns")

right_frame = tk.Frame(boarder_frame)
right_frame.grid(row=0, column=2, padx=10, pady=10)

# Add the result message label
message_label = tk.Label(left_frame, text="Prediction will be displayed here.",bg="cyan",fg="black",wraplength=180)
message_label.pack(padx=10, pady=10)
message_label.place(relx=0.5, rely=0.5, anchor="center")

seperator = tk.Frame(boarder_frame, width=2, bg="black")
seperator.grid(row=0, column=1, sticky="ns")

# Adding Input Fields
labels = ["Age", "Sex", "Cp", "Trestbps" , "Chol" , "Fbs" , "Restecg" , "Thalach" , "Exang" , "Old peak" , "Slope" , "Ca" , "Thal"]
entries = []
dropdown_vars = []

# Creating the "Name" field seperately with increased length
tk.Label(right_frame, text="Name").grid(row=0, column=0, columnspan=2, padx=1, pady=1)
name_entry = tk.Entry(right_frame, width=40)
name_entry.grid(row=0, column=2, columnspan=4, padx=1, pady=1)

dropdown_options = {
    "Cp": ["0","1","2","3","4"],
    "Fbs": ["0","1"],
    "Restecg": ["0","1","2"],
    "Exang": ["0","1"],
    "Slope": ["0","1","2"],
    "Ca": ["0","1","2","3","4"],
    "Thal": ["0","1","2","3"]

}

# Placing the input fields on the gui
for i, label in enumerate(labels):
    row = (i // 2) + 1
    column = (i % 2) * 3
    tk.Label(right_frame, text=label).grid(row=row, column=column, padx=5, pady=5)

    if label == "Sex":
        sex_var = tk.StringVar(value="Select")
        sex_menu = tk.OptionMenu(right_frame, sex_var, "Male", "Female")
        sex_menu.grid(row=row, column=column + 1, padx=5, pady=5)
    elif label in dropdown_options:
        var = tk.StringVar(value="Select")
        menu = tk.OptionMenu(right_frame, var, *dropdown_options[label])
        menu.grid(row=row, column=column + 1, padx=5, pady=5)
        dropdown_vars.append(var)
    else:
        entry = tk.Entry(right_frame)
        entry.grid(row=row, column=column + 1, padx=5, pady=5)
        entries.append(entry)

# Adding the prediction result and submit button

# Adding a submit button
submit_button = tk.Button(right_frame, text="Submit", command=predict_heart_disease)
submit_button.grid(row=7, column=2, padx=5, pady=5)

# to run the application
root.mainloop()