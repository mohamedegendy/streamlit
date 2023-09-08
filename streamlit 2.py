import streamlit as st
st.write("wellcome code")
st.write("mohamed el gendy")
import numpy as np

def calculate_mean(degrees):
    mean = np.mean(degrees)
    return mean

def main():
    st.title("Student Degree Mean Calculator")
    st.write("Enter the degrees of students to calculate the mean.")

    # Input degrees
    degrees = st.text_input("Enter degrees (comma-separated)")

    if degrees:
        # Convert input string to a list of numbers
        degrees_list = [float(x.strip()) for x in degrees.split(',')]

        if len(degrees_list) > 0:
            # Calculate mean
            mean = calculate_mean(degrees_list)
            st.write("Mean:", mean)

if __name__ == "__main__":
    main()