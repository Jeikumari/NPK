import streamlit as st
import pandas as pd

# Define standard values for 100g samples
standard_values = {
    'Sample': ['Livestock Manure', 'Energy Crops', 'Harvest Remains', 'Dairy Product Waste', 'Agro Processing Waste', 'OFMSW', 'Sewage Sludge', 'Yard Trimmings'],
    'Weight (g)': [100, 100, 100, 100, 100, 100, 100, 100],
    'Nitrogen (%)': [1.5, 15, 4.1, 1.42, 3.5, 0.45, 1.43, 2.5],
    'Phosphorus (%)': [0.75, 23, 0.15, 0.45, 0.45, 0.16, 0.46, 1.76],
    'Potassium (%)': [0.55, 10, 1, 0.97, 0.25, 0.97, 0.76, 0.4]
}

df_standard = pd.DataFrame(standard_values)

# Define function to calculate NPK
def calculate_npk(sample, weight):
    standard_sample = df_standard[df_standard['Sample'] == sample].iloc[0]
    scaling_factor = weight / standard_sample['Weight (g)']
    npk_values = {
        'Nitrogen (%)': standard_sample['Nitrogen (%)'] * scaling_factor,
        'Phosphorus (%)': standard_sample['Phosphorus (%)'] * scaling_factor,
        'Potassium (%)': standard_sample['Potassium (%)'] * scaling_factor
    }
    return npk_values

# Create Streamlit application
def npk_app():
    st.title("NPK Analysis")
    st.write("Select a sample and enter the weight to get the NPK values.")
    
    sample = st.selectbox("Select Sample", df_standard['Sample'].tolist())
    weight = st.number_input("Enter Weight (g)", min_value=0.0, format="%f")
    
    if st.button("Analyze"):
        npk_values = calculate_npk(sample, weight)
        st.write(f"Nitrogen (%): {npk_values['Nitrogen (%)']}")
        st.write(f"Phosphorus (%): {npk_values['Phosphorus (%)']}")
        st.write(f"Potassium (%): {npk_values['Potassium (%)']}")
        
if __name__ == "__main__":
    npk_app()
