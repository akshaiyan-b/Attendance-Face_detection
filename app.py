import streamlit as st
import pandas as pd
import time 
from datetime import datetime
import os 

ts = time.time()
date = datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
timestamp = datetime.fromtimestamp(ts).strftime("%H:%M-%S")

# Construct the filename based on the current date
attendance_filename = "Attendance/Attendance_" + date + ".csv"


if not os.path.exists(attendance_filename):
    columns = ["Name", "Status"]  
    data = []  
    df = pd.DataFrame(data, columns=columns)
else:
    df = pd.read_csv(attendance_filename)

# Streamlit code
st.write("Attendance Data:")
st.dataframe(df.style.highlight_max(axis=0))

count = 0  

if count == 0:
    st.write("Count is zero")
elif count % 3 == 0 and count % 5 == 0:
    st.write("FizzBuzz")
elif count % 3 == 0:
    st.write("Fizz")
elif count % 5 == 0:
    st.write("Buzz")
else:
    st.write(f"Count: {count}")
