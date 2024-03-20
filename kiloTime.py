import streamlit as st

def calculate_cook_time(cook_time_per_kilo, actual_kilo):
    total_cook_time = cook_time_per_kilo * actual_kilo
    hours = total_cook_time // 60
    minutes = total_cook_time % 60
    return hours, minutes

def main():
    st.title('Meat Kilo Cook Time Calculator')
    
    cook_time_per_kilo = st.number_input('Cook Time per Kilo as instructed on packet (in minutes)', min_value=1)
    actual_kilo = st.number_input('Actual Weight of Meat (in kilos)', min_value=0.1, on_change=True)

    if st.button('Calculate Cook Time') or st.session_state.actual_kilo_entered:
        hours, minutes = calculate_cook_time(cook_time_per_kilo, actual_kilo)
        if hours > 0:
            st.success(f'Cook Time: {int(hours)} hours and {int(minutes)} minutes')
        else:
            st.success(f'Cook Time: {int(minutes)} minutes')

if __name__ == '__main__':
    main()
