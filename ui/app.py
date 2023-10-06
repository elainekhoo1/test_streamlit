import streamlit as st
from itertools import permutations

def get_combinations(number):
    digits = [int(d) for d in str(number)]
    return list(set(permutations(digits)))

def main():
    st.title("4-Digit Combinations")

    number_input = st.number_input("Enter a 4-digit number:", min_value=1000, max_value=9999, step=1)

    if st.button("Get Combinations"):
        combinations = get_combinations(number_input)
        st.write(f"All possible combinations of {number_input}:")
        for combination in combinations:
            st.write("".join(str(d) for d in combination))


if __name__=='__main__': 

    main()