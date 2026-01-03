import streamlit as s
a = s.number_input("Enter Dollars $", min_value = 1)
s.write(f"Indian currency for {a} dollars is {a*90} rupees")
a = s.number_input("Enter Pounds ", min_value = 1)
s.write(f"Indian currency for {a} pounds is {a*121} rupees")
a = s.number_input("Enter Euro ", min_value = 1)
s.write(f"Indian currency for {a} euro is {a*105} rupees")


