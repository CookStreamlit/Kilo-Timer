import streamlit as st

def calculate_time_per_kilo(total_time, total_distance):
    time_per_kilo = total_time / total_distance
    return time_per_kilo

def main():
    st.title("Time per Kilometer Calculator")
    st.write("This calculator helps you find the average time per kilometer based on the total time and distance.")

    total_time = st.number_input("Total Time (in minutes)", min_value=0.0, step=1.0, format="%.2f")
    total_distance = st.number_input("Total Distance (in kilometers)", min_value=0.0, step=0.1, format="%.2f")

    if st.button("Calculate"):
        if total_distance == 0:
            st.error("Total distance cannot be zero.")
        else:
            time_per_kilo = calculate_time_per_kilo(total_time, total_distance)
            st.success(f"Average Time per Kilometer: {time_per_kilo:.2f} minutes")

if __name__ == "__main__":
    main()
