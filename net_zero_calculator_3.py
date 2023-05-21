
import streamlit as st
import plotly.graph_objects as go
import numpy as np
import pandas as pd
from decimal import Decimal

import base64
import snowflake.connector

@st.cache_data(ttl=None)  # Cache data until app is refreshed
def fetch_data_from_snowflake(_snowflake_config, query):
    # Connect to Snowflake
    conn = snowflake.connector.connect(
        user=_snowflake_config["user"],
        password=_snowflake_config["password"],
        account=_snowflake_config["account"],
        warehouse=_snowflake_config["warehouse"],
        database=_snowflake_config["database"],
        schema=_snowflake_config["schema"],
    )

    # Execute query to fetch data
    
    cursor = conn.cursor()
    cursor.execute(query)

    # Retrieve column names
    column_names = [desc[0] for desc in cursor.description]

    # Retrieve rows
    rows = cursor.fetchall()

    # Close connection
    conn.close()

    # Create DataFrame
    df = pd.DataFrame(rows, columns=column_names)
    return df

class NetZeroCalculator:
    """
    NetZeroCalculator is a class that performs calculations related to carbon footprint and displays the results.
    """

    def __init__(self):
        """
        Initialize all necessary data sources and variables.
        """
        pass
    def general_data(self, general):
        """
        Calculate the CO2 emissions based on energy usage.

        Args:
            energy_usage (dict): User data for energy usage.

        Returns:
            float: Energy footprint in CO2 emissions.
        """
        # Implement the logic to calculate CO2 emissions based on energy sources and consumption
        hq_country = general['hq_country']
        business_sector = general['business_sector']

        # Placeholder calculation
        

        return hq_country,business_sector
    def calculate_energy_footprint(self, energy_usage,hq_location):
        """
        Calculate the CO2 emissions based on energy usage.

        Args:
            energy_usage (dict): User data for energy usage.

        Returns:
            float: Energy footprint in CO2 emissions.
        """
        # Implement the logic to calculate CO2 emissions based on energy sources and consumption
        snowflake_config = st.secrets.connections.snowpark
        electricity_consumption = energy_usage['electricity_consumption']
        natural_gas_consumption = energy_usage['natural_gas_consumption']
        emission_factory_query = f"select value from public.electricity_consumtion_factor_co2 where country like '{hq_location}' and year = 2020"
        emission_factor_electricity = fetch_data_from_snowflake(snowflake_config, emission_factory_query)
        emission_factor_electricity=float(emission_factor_electricity['VALUE'][0])
        
        # Store DataFrame in Session State
        st.session_state.emission_factor_electricity = emission_factor_electricity
        # Placeholder calculation
        energy_footprint = electricity_consumption * emission_factor_electricity + natural_gas_consumption * 2

        return energy_footprint

    def calculate_transport_footprint(self, transport_data):
        """
        Calculate the CO2 emissions based on transport data.

        Args:
            transport_data (dict): User data for transport.

        Returns:
            float: Transport footprint in CO2 emissions.
        """
        # Implement the logic to calculate CO2 emissions based on fuel consumption and distances traveled
        snowflake_config = st.secrets.connections.snowpark
        
        distance_traveled = transport_data['distance_traveled']
        manufacturer_name = transport_data['manufacturer_name']
        manufacturer_name_tuple = tuple(manufacturer_name)

        
        commercial_name = transport_data['commercial_name']
        commercial_name_tuple = tuple(commercial_name)
        emission_factory_query = f"""select AVG("Ewltp (g/km)") as "VALUE"
                                    from staging.car_emission_data
                                    where "Mh" in {str(manufacturer_name_tuple).replace(",)", ")")}
                                    and "Cn" in {str(commercial_name_tuple).replace(",)", ")")}
                                    order by 1"""
        # Placeholder calculation
        emission_factor_car = fetch_data_from_snowflake(snowflake_config, emission_factory_query)
        emission_factor_car=float(emission_factor_car['VALUE'][0])
        transport_footprint = distance_traveled * emission_factor_car

        return transport_footprint

    def calculate_food_footprint(self, food_choices):
        """
        Calculate the CO2 emissions based on food choices.

        Args:
            food_choices (dict): User data for food choices.

        Returns:
            float: Food footprint in CO2 emissions.
        """
        # Implement the logic to calculate CO2 emissions based on food sources and consumption patterns
        # Placeholder calculation
        food_footprint = 100

        return food_footprint

    def calculate_water_footprint(self, water_usage):
        """
        Calculate the CO2 emissions based on water usage.

        Args:
            water_usage (dict): User data for water usage.

        Returns:
            float: Water footprint in CO2 emissions.
        """
        # Implement the logic to calculate CO2 emissions based on water consumption
        # Placeholder calculation
        water_footprint = 50

        return water_footprint

    def calculate_waste_footprint(self, waste_data):
        """
        Calculate the CO2 emissions based on waste production and management.

        Args:
            waste_data (dict): User data for waste production and management.

        Returns:
            float: Waste footprint in CO2 emissions.
        """
        # Implement the logic to calculate CO2 emissions based on waste production and management
        # Placeholder calculation
        waste_footprint = 75

        return waste_footprint

    def calculate_forest_footprint(self, forest_data):
        """
        Calculate the CO2 emissions based on forest conservation and deforestation.

        Args:
            forest_data (dict): User data for forest conservation.

        Returns:
            float: Forest footprint in CO2 emissions.
        """
        # Implement the logic to calculate CO2 emissions based on forest conservation data
        # Placeholder calculation
        forest_footprint = 25

        return forest_footprint

    def calculate_offset(self, offset_data):
        """
        Calculate the required CO2 offset to achieve net-zero emissions.

        Args:
            offset_data (dict): User data for emission offset.

        Returns:
            float: Required CO2 offset.
        """
        # Implement the logic to calculate the required CO2 offset based on emission reduction projects
        # Placeholder calculation
        offset = 10

        return offset

    def calculate_net_zero(self, user_data):
        """
        Perform all calculations and return the net zero footprint.

        Args:
            user_data (dict): User data for all categories.

        Returns:
            float: Net zero footprint in CO2 emissions.
        """
        hq_country = 'Belgium'
        energy_footprint = self.calculate_energy_footprint(user_data['energy_usage'],hq_location=hq_country)
        #hq_country = self.general_data(user_data['hq_country'])
        #business_sector = self.general_data(user_data['business_sector'])
        transport_footprint = self.calculate_transport_footprint(user_data['transport_data'])
        #food_footprint = self.calculate_food_footprint(user_data['food_choices'])
        water_footprint = self.calculate_water_footprint(user_data['water_usage'])
        waste_footprint = self.calculate_waste_footprint(user_data['waste_data'])
        forest_footprint = self.calculate_forest_footprint(user_data['forest_data'])
        offset = self.calculate_offset(user_data['offset_data'])

        net_zero_footprint = (
                energy_footprint + transport_footprint + #food_footprint +
                water_footprint + waste_footprint + forest_footprint - offset
        )

        return net_zero_footprint

    def display_results(self, net_zero_footprint, user_data):
        """
        Display the net zero footprint results.

        Args:
            net_zero_footprint (float): Net zero footprint in CO2 emissions.
            user_data (dict): User data for all categories.
        """
        st.header("Net Zero Footprint")
        st.write(net_zero_footprint)

        # Generate and display a bar chart of emissions by category
        categories = ["Energy", "Transport", "Water", "Waste", "Forest"]
        emissions = [
            self.calculate_energy_footprint(user_data['energy_usage'],hq_location=user_data['general']['hq_country']),
            self.calculate_transport_footprint(user_data['transport_data']),
            #self.calculate_food_footprint(user_data['food_choices']),
            self.calculate_water_footprint(user_data['water_usage']),
            self.calculate_waste_footprint(user_data['waste_data']),
            self.calculate_forest_footprint(user_data['forest_data'])
        ]

        # Define the color gradient
        colors = ["#445ba7", "#bfc7e2"]
        cmap = np.linspace(0, 1, len(emissions))

        fig = go.Figure(data=go.Bar(x=categories, y=emissions, marker=dict(color=cmap, colorscale=colors)))
        fig.update_layout(
            title="CO2 Emissions by Category",
            xaxis_title="Categories",
            yaxis_title="CO2 Emissions (tons)"
        )

        # Display the chart
        st.subheader("CO2 Emissions by Category")
        st.plotly_chart(fig)

        # Calculate average emissions per category
        average_emissions = np.mean(emissions)

        # Compare user's emissions to average emissions
        comparison = "lower than" if net_zero_footprint < average_emissions else "higher than"

        st.subheader("Comparison to Average Emissions")
        st.write(f"Your net zero footprint is {comparison} the average emissions in each category.")

        # Provide informative text and tips
        st.subheader("Tips for Reducing Your Carbon Footprint")
        st.write("Here are some tips to help you reduce your carbon footprint:\n"
                 "- Reduce your energy consumption by using energy-efficient appliances and insulating your home.\n"
                 "- Opt for sustainable transportation options such as walking, cycling, or using public transportation.\n"
                 "- Choose plant-based meals and reduce meat consumption.\n"
                 "- Conserve water by fixing leaks and using water-efficient fixtures.\n"
                 "- Recycle and compost to minimize waste production.\n"
                 "- Support forest conservation initiatives and consider offsetting your emissions.")

        # Share results button
        st.subheader("Share Your Results")
        st.write("Share your net zero footprint and inspire others to take action!")
        # Add the necessary code to implement sharing functionality (e.g., share on social media, via email)

        # Personalized recommendations based on the results
        st.subheader("Personalized Recommendations")
        st.write(
            "Based on your results, here are some personalized recommendations to further reduce your carbon footprint:"
        )
        # Add personalized recommendations based on the user's emissions and categories

        # Progress tracking
        st.subheader("Progress Tracking")
        st.write("Track your progress towards your net zero goal:")
        # Add a progress bar or chart to track the user's progress

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"svg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

# Streamlit app
def main():
    """
    Run the Net Zero Calculator Streamlit app.

    Collects user inputs for energy usage, transport data, food choices, water usage,
    waste data, forest data, and offset data. Calculates the net zero footprint based on the inputs
    and displays the results using Streamlit.

    """
    st.markdown("<span style='color:white;font-size:48px'>ACHIEVE </span>  <span style='color:#38b580;font-size:48px'>NET ZERO</span>",unsafe_allow_html=True)
    st.write("Welcome to our Net Zero Calculator! We understand the importance of tackling climate change and achieving a sustainable future. Our user-friendly tool empowers individuals and organizations to calculate their carbon footprint and explore strategies to reach net zero emissions. Whether you're a business, household, or individual, join us on this journey towards a greener planet by using our calculator to measure, reduce, and offset your carbon footprint. Let's take meaningful action together for a more sustainable tomorrow.")
    add_bg_from_local('logo.svg')   
    calculator = NetZeroCalculator()

    # Set sidebar layout
    st.sidebar.title("User Input")

    # Collect user inputs
    with st.sidebar:
        snowflake_config = st.secrets.connections.snowpark
        #query_locations = f"SELECT distinct location FROM staging.COMPANIES_GOALS order by 1"
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
        hq_country = st.selectbox("How many locations/sites do you have?", df_locations)
        business_sector = st.selectbox("What business sector are you in?", df_sector)

        st.subheader("Energy Usage")
        electricity_consumption = st.number_input("Electricity consumption (kWh per month)", value=1500)
        natural_gas_consumption = st.number_input("Natural gas consumption (cubic meters per year)", value=500)

        st.subheader("Transport Data")
        manufacturer_name = st.multiselect("Manufacturer name of the car(s) owned or leased by the company", df_car_brands, default=["BMW AG"])
        manufacturer_name_tuple = tuple(manufacturer_name)

        
        query_commercial_name = f"""select distinct "Cn"
                                    from staging.car_emission_data 
                                    where "Mh" in {str(manufacturer_name_tuple).replace(",)", ")")} 
                                            and "Cn" <> '116D' order by 1""" 
        st.markdown(query_commercial_name)
        df_commercial_name = fetch_data_from_snowflake(snowflake_config, query_commercial_name)

        commercial_name= st.multiselect("Commercial name of the car(s) owned or leased by the company", df_commercial_name,  default=["116d"])

        #fuel_consumption = st.number_input("Fuel consumption (liters per year)", value=1200)
        
        distance_traveled = st.number_input("Average Distance traveled (kilometers per year)", value=15000)

        #st.subheader("Food Choices")
        #meat_consumption = st.number_input("Meat consumption (kilograms per year)", value=50)
        #vegetable_consumption = st.number_input("Vegetable consumption (kilograms per year)", value=100)
        #fruit_consumption = st.number_input("Fruit consumption (kilograms per year)", value=75)

        st.subheader("Water Usage")
        water_consumption = st.number_input("Water consumption (cubic meters per year)", value=200)

        st.subheader("Waste Data")
        waste_production = st.number_input("Waste production (kilograms per year)", value=500)

        st.subheader("Forest Data")
        deforestation_area = st.number_input("Deforestation area (hectares per year)", value=2.5)

        st.subheader("Offset Data")
        offset_amount = st.number_input("Offset amount (tons of CO2 offset)", value=100)

    user_data = {
        'general': {
            'hq_country': hq_country,
            'business_sector': business_sector
              }, 
        'energy_usage': {
            'electricity_consumption': electricity_consumption,
            'natural_gas_consumption': natural_gas_consumption
        },  # User data for energy usage
        'transport_data': {
            'manufacturer_name':manufacturer_name,
            'commercial_name':commercial_name,
            'distance_traveled': distance_traveled
        },  # User data for transport
        #'food_choices': {
        #    'meat_consumption': meat_consumption,
        #    'vegetable_consumption': vegetable_consumption,
        #    'fruit_consumption': fruit_consumption
        #},  # User data for food choices
        'water_usage': {
            'water_consumption': water_consumption
        },  # User data for water usage
        'waste_data': {
            'waste_production': waste_production
        },  # User data for waste production and management
        'forest_data': {
            'deforestation_area': deforestation_area
        },  # User data for forest conservation
        'offset_data': {
            'offset_amount': offset_amount
        }  # User data for emission offset
    }

    # Calculate net zero footprint

    
    net_zero_footprint = calculator.calculate_net_zero(user_data)

    # Display the result
    calculator.display_results(net_zero_footprint, user_data)


if __name__ == '__main__':
    main()
