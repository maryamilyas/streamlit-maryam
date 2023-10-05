import streamlit as st
from calculator import NetZeroCalculator
from snowflake_connection import fetch_data_from_snowflake
from streamlit_utils import set_svg_background_image, add_tooltip_to_subheader

def main():
    """
    Run the Net Zero Calculator Streamlit app.

    Collects user inputs for energy usage, transport data, food choices, water usage,
    waste data, forest data, and offset data. Calculates the net zero footprint based on the inputs
    and displays the results using Streamlit.

    """
    st.markdown("<span style='color:white;font-size:48px'>ACHIEVE </span>  <span style='color:#38b580;font-size:48px'>NET ZERO</span>",unsafe_allow_html=True)
    st.write("""Welcome to our Net Zero Calculator! We understand the importance of tackling climate change 
                and achieving a sustainable future. Our user-friendly tool empowers individuals and organizations
                to calculate their carbon footprint and explore strategies to reach net zero emissions. 
                Whether you're a business, household, or individual, join us on this journey towards a greener
                  planet by using our calculator to measure, reduce, and offset your carbon footprint. 
                  Let's take meaningful action together for a more sustainable tomorrow!""")
    
    calculator = NetZeroCalculator()
    
    # Set sidebar layout
    st.sidebar.title("User Input")

    # Collect user inputs
    with st.sidebar:
        snowflake_config = st.secrets.connections.snowpark
        query_locations = f"select distinct country from public.electricity_consumtion_factor_co2 order by 1"
        df_locations = fetch_data_from_snowflake(snowflake_config, query_locations)
        # Store DataFrame in Session State
        st.session_state.df_locations = df_locations

        query_sector = f"SELECT distinct SECTOR FROM staging.COMPANIES_GOALS order by 1"
        df_sector = fetch_data_from_snowflake(snowflake_config, query_sector)
        # Store DataFrame in Session State
        st.session_state.df_locations = df_sector

        query_car_brand = f'select distinct "Mh" from staging.car_emission_data order by 1'
        df_car_brands = fetch_data_from_snowflake(snowflake_config, query_car_brand)
        # Store DataFrame in Session State
        st.session_state.query_car_brand = query_car_brand
        
        st.subheader("General Information")
        hq_country = st.selectbox("Country name of your headquarters", df_locations)
        business_sector = st.selectbox("Business sector", df_sector)
        st.markdown("""---""")

        
        st.subheader("Energy Usage")

        electricity_consumption = st.number_input("Electricity consumption (MWh per year)", value=65)

        hfc_ref_option = st.radio('Do you own a HFC-refrigerator?', ('Yes', 'No'),index=1)

        if hfc_ref_option == 'Yes':
            HFC_ref_yes = True
            HFC_ref_no = False
        else:
            HFC_ref_yes = False
            HFC_ref_no = True

        
        st.markdown("""---""")
        st.subheader("Water Usage")
        water_consumption = st.number_input("Water consumption (cubic meters per year)", value=74)
        
        st.markdown("""---""")
        st.subheader("Transport Data")
        manufacturer_name = st.multiselect("Manufacturer name of the car(s) owned or leased by the company", df_car_brands, default=["BMW AG"])
        manufacturer_name_tuple = tuple(manufacturer_name)

        query_commercial_name = f"""select distinct "Cn", "Mh"
                                    from staging.car_emission_data 
                                    where "Mh" in {str(manufacturer_name_tuple).replace(",)", ")")} 
                                    and "Cn" <> '116D' order by 1""" 
        df_car_data = fetch_data_from_snowflake(snowflake_config, query_commercial_name)

        df_commercial_name = df_car_data[['Cn', 'Mh']].drop_duplicates().reset_index(drop=True)

        commercial_name = st.multiselect("Commercial name of the car(s) owned or leased by the company", df_commercial_name['Cn'], default=["116d"])

        car_quantities = {}
        for commercial in commercial_name:
            manufacturer = df_commercial_name[df_commercial_name['Cn'] == commercial]['Mh'].values[0]
            quantity = st.number_input(f"Number of {commercial} cars from {manufacturer}", value=1)
            car_quantities[commercial] = {'Manufacturer': manufacturer, 'Quantity': quantity}
        distance_traveled = st.number_input("Average distance traveled (kilometers per year)", value=20000)

        # Public transport data
        st.subheader("Public Transport Data")
        distance_traveled_tram = st.number_input("Average distance traveled by tram (kilometers per year)", value=100)
        distance_traveled_train = st.number_input("Average distance traveled by train (kilometers per year)", value=100)
        distance_traveled_bus = st.number_input("Average distance traveled by bus (kilometers per year)", value=20)

        # Private Waste data
        st.markdown("""---""")
        st.subheader("Waste Data")
        waste_production = st.number_input("Waste production (kilograms per year)", value=800)

        st.markdown("""---""")

        st.subheader("Offset Data")
        offset_amount = st.number_input("Offset amount (tons of CO2 offset)", value=0)
    #User data for energy usage
    user_data = {
        'general': {
            'hq_country': hq_country,
            'business_sector': business_sector
        },  # User data for country and sector
        'energy_usage': {
            'electricity_consumption': electricity_consumption,
            'hfc_refrigrator': HFC_ref_yes
        },  # User data for energy usage
        'transport_data': {
            'manufacturer_name':manufacturer_name,
            'commercial_name':commercial_name,
            'car_quantities': car_quantities,
            'distance_traveled': distance_traveled,
            'distance_traveled_tram' : distance_traveled_tram,
            'distance_traveled_train' : distance_traveled_train,
            'distance_traveled_bus' : distance_traveled_bus
        },  # User data for transport data
        'water_usage': {
            'water_consumption': water_consumption
        },  # User data for water usage
        'waste_data': {
            'waste_production': waste_production
        },  # User data for waste production and management
            'offset_data': {
            'offset_amount': offset_amount
        }   # User data for emission offset
    }

    # Calculate net zero footprint

    
    net_zero_footprint = calculator.calculate_net_zero(user_data)

    # Display the result
    calculator.display_results(net_zero_footprint, user_data)
    set_svg_background_image("path/to/background.svg")
    add_tooltip_to_subheader("Subheader text", "Tooltip text")  