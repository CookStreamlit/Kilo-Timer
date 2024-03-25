import streamlit as st

# Set favicon URL
favicon_url = "https://cdn0.iconfinder.com/data/icons/food-4-13/48/181-512.png" 

# Set page config with favicon
st.set_page_config(page_title="Kilo Timer", page_icon=favicon_url)

def calculate_cook_time(cook_time_per_kilo, actual_kilo):
    total_cook_time = cook_time_per_kilo * actual_kilo
    hours = total_cook_time // 60
    minutes = total_cook_time % 60
    return hours, minutes

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0/9.0

def celsius_to_fahrenheit(celsius):
    return (celsius * 9.0/5.0) + 32
    
def main():
    st.title('Meat Kilo Cook Time Calculator')
    
    cook_time_per_kilo = st.number_input('Cook Time per Kilo as instructed on packet (in minutes)', min_value=1)
    actual_kilo = st.number_input('Actual Weight of Meat (in kilos)', min_value=0.1)

    if st.button('Calculate Cook Time'):
        hours, minutes = calculate_cook_time(cook_time_per_kilo, actual_kilo)
        if hours > 0:
            st.success(f'Cook Time: {int(hours)} hours and {int(minutes)} minutes')
        else:
            st.success(f'Cook Time: {int(minutes)} minutes')

     st.markdown("---")

    temp_unit = st.radio("Select temperature unit:", ("Fahrenheit", "Celsius"))

    if temp_unit == "Fahrenheit":
        fahrenheit_temp = st.number_input("Enter temperature in Fahrenheit:")
        celsius_temp = fahrenheit_to_celsius(fahrenheit_temp)
        st.write("Temperature in Celsius:", round(celsius_temp, 2))
    else:
        celsius_temp = st.number_input("Enter temperature in Celsius:")
        fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
        st.write("Temperature in Fahrenheit:", round(fahrenheit_temp, 2))

if __name__ == '__main__':
    main()

