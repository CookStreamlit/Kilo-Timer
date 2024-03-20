import streamlit as st

def calculate_cook_time(cook_time_per_kilo, actual_kilo):
    return cook_time_per_kilo * actual_kilo

def main():
    st.title('Meat Cook Time Calculator')
    
    cook_time_per_kilo = st.number_input('Cook Time per Kilo (in minutes)', min_value=1)
    actual_kilo = st.number_input('Actual Weight of Meat (in kilos)', min_value=0.1)

    if st.button('Calculate Cook Time'):
        cook_time = calculate_cook_time(cook_time_per_kilo, actual_kilo)
        st.success(f'Cook Time: {cook_time} minutes')

if __name__ == '__main__':
    main()
