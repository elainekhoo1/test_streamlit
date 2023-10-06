import random
import streamlit as st
from itertools import permutations

def get_combinations(number):
    digits = [int(d) for d in str(number)]
    return list(set(permutations(digits)))

def main():
    st.title("4-Digit Combinations")

    number_input = st.number_input("Enter a 4-digit number:", min_value=0000, max_value=9999, step=1, value=8888)
    if st.button("Get Combinations"):
        combinations = get_combinations(number_input)
        st.write(f"All possible combinations of {number_input}:")
        for combination in combinations:
            st.write("".join(str(d) for d in combination))
        random_number = "".join(str(d) for d in random.choice(combinations))
        st.write(f"<span style='font-size: 24px'>Your lucky number for 4D today is <b>{random_number}</b></span>", unsafe_allow_html=True)

if __name__=='__main__': 

    main()