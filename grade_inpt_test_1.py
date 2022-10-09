import streamlit as st

@st.cache(allow_output_mutation=True)
def Nums():
    return []

nums = Nums()
num = st.sidebar.number_input("Input Number")
if st.sidebar.button("Add number"):
    nums.append(num)

try:
    inputs = nums
    st.table(inputs)
    st.write("Sum: ", sum(inputs))
except:
    st.title("Enter some numbers")