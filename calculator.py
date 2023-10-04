from snowflake_connection import fetch_data_from_snowflake
import streamlit as st
import numpy as np
import plotly.graph_objects as go


class NetZeroCalculator:
    """
    NetZeroCalculator is a class that performs calculations related to carbon footprint and displays the results.
    """
    @st.cache_data(ttl=None)
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
        emission_factory_query = f"select value from public.electricity_consumtion_factor_co2 where country like '{hq_location}' and year = 2020"
        emission_factor_electricity = fetch_data_from_snowflake(snowflake_config, emission_factory_query)
        emission_factor_electricity=float(emission_factor_electricity['VALUE'][0])
        
        # Store DataFrame in Session State
        st.session_state.emission_factor_electricity = emission_factor_electricity
        # Placeholder calculation
        energy_footprint = electricity_consumption * emission_factor_electricity 

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

        emission_values = []
        car_quantities = transport_data['car_quantities']
        for commercial_name, car_data in car_quantities.items():
            manufacturer_name=car_data['Manufacturer']
            quantity = car_data['Quantity']
            emission_factory_query = f"""With calculation as (
                                    select AVG("Ewltp (g/km)") as "VALUE"
                                    from staging.car_emission_data
                                    where "Mh" = '{manufacturer_name}'
                                    and "Cn" = '{commercial_name}'
                                    group by "Mh", "Cn")
                                    select AVG("VALUE") as "VALUE"
                                    from calculation"""
            # Placeholder calculation
            emission_value = fetch_data_from_snowflake(snowflake_config, emission_factory_query)
            emission_value = (emission_value/1000000)*quantity
            if not emission_value.empty:
                emission_values.append(emission_value.iloc[0]['VALUE'])
        transport_footprint = distance_traveled * sum(emission_values)

        return transport_footprint
    def calculate_public_transport_footprint(self, transport_data):
        """
        Calculate the CO2 emissions based on transport data.

        Args:
            transport_data (dict): User data for transport.

        Returns:
            float: Transport footprint in CO2 emissions.
        """
        # Implement the logic to calculate CO2 emissions based on fuel consumption and distances traveled
        snowflake_config = st.secrets.connections.snowpark
        
        distance_traveled_tram = transport_data['distance_traveled_tram']
        distance_traveled_train = transport_data['distance_traveled_train']
        distance_traveled_bus = transport_data['distance_traveled_bus']
        
        
        public_transport_footprint = distance_traveled_tram * (230/1000000) + distance_traveled_train * (280/1000000) +distance_traveled_bus * (750/1000000)

        return public_transport_footprint


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
        water_footprint = water_usage['water_consumption']*0.0004

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
        
        waste_production = waste_data['waste_production']
        waste_footprint = (waste_production*0.47*0.00022)+(waste_production*0.31*0.00015)+(waste_production*0.43*0.00047)

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
        offset = offset_data['offset_amount']

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
        transport_footprint = self.calculate_transport_footprint(user_data['transport_data'])
        public_transport_footprint = self.calculate_public_transport_footprint(user_data['transport_data'])
        water_footprint = self.calculate_water_footprint(user_data['water_usage'])
        waste_footprint = self.calculate_waste_footprint(user_data['waste_data'])
        offset = self.calculate_offset(user_data['offset_data'])

        net_zero_footprint = (
                energy_footprint + transport_footprint + public_transport_footprint + #food_footprint +
                water_footprint + waste_footprint  - offset
        )
        return net_zero_footprint

    def display_results(self, net_zero_footprint, user_data):
        """
        Display the net zero footprint results.

        Args:
            net_zero_footprint (float): Net zero footprint in CO2 emissions.
            user_data (dict): User data for all categories.
        """
        
        #Data required:  
        snowflake_config = st.secrets.connections.snowpark       
        query_company_data = """
                            SELECT *
                            FROM staging.companies_goals
                            ORDER BY SECTOR
                            """
        df_company_data = fetch_data_from_snowflake(snowflake_config, query_company_data)
        sorted_countries = sorted(df_company_data['LOCATION'].unique())
        sorted_sector = sorted(df_company_data['SECTOR'].unique())
        
        st.header("Net Zero Footprint")


        # Generate and display a bar chart of emissions by category
        categories = ["Energy", "Transport","Public transport", "Water", "Waste"]
        emissions = [
            self.calculate_energy_footprint(user_data['energy_usage'],hq_location=user_data['general']['hq_country']),
            self.calculate_transport_footprint(user_data['transport_data']),
            self.calculate_public_transport_footprint(user_data['transport_data']),
            self.calculate_water_footprint(user_data['water_usage']),
            self.calculate_waste_footprint(user_data['waste_data']),
            
        ]

        # Define the color gradient
        colors = ["#445ba7", "#bfc7e2"]
        cmap = np.linspace(0, 1, len(emissions))

        fig = go.Figure(data=go.Bar(x=categories, y=emissions, marker=dict(color=cmap, colorscale=colors)))
        fig.update_layout(
            title="CO2 Emissions by Category",
            xaxis_title="Categories",
            yaxis_title="CO2 Emissions (ton)"
        )

        # Display the chart
        st.subheader("CO2 Emissions by Category")
        st.plotly_chart(fig)
        
        
        country = user_data['general']['hq_country']
        # General grah CO2 country
        emission_country = f""" select year, co2_per_capita
                        from staging.co2_data_alg
                        where country = '{country}'
                        and year > 2010"""
        snowflake_config = st.secrets.connections.snowpark
        emission_country = fetch_data_from_snowflake(snowflake_config, emission_country)
        
        # Convert 'CO2' column to decimal values
        emission_country['YEAR'] = emission_country['YEAR'].astype(int)
        emission_country['CO2_PER_CAPITA'] = emission_country['CO2_PER_CAPITA'].astype(float)


        # Filtering the DataFrame based on the selected year range
        filtered_df = emission_country[(emission_country['YEAR'] >= int(emission_country['YEAR'].min()))
                                       & (emission_country['YEAR'] <= int(emission_country['YEAR'].max()))
                                        ]

        # Plotting
        fig = go.Figure()

        # Add the scatter trace for the trendline
        fig.add_trace(go.Scatter(
            x=filtered_df['YEAR'],
            y=filtered_df['CO2_PER_CAPITA'],
            mode='lines',
            line=dict(color='#bfc7e2', width=2, shape='spline'),
            name='CO2 Emissions'
        ))

        # Configure the layout options
        layout = go.Layout(
            plot_bgcolor='rgba(0,0,0,0)',  # Set the plot background color as transparent
            paper_bgcolor='rgba(0,0,0,0)',  # Set the paper background color as transparent
            xaxis=dict(title='Year', showgrid=True, gridcolor='#e5e7eB', zeroline=False),  # Customize x-axis grid and zeroline
            yaxis=dict(title=f'CO2 Emissions (ton)',showgrid=True, gridcolor='#e5e7eB', zeroline=False),  # Customize y-axis grid and zeroline
            title=dict(text=f'Average Emissions per Year in {country}'),  # Set the title below the x-axis
        )

        # Update the figure's layout
        fig.update_layout(layout)


        # Calculate average emissions per category
        average_emissions = np.mean(emissions)

        # Compare user's emissions to average emissions
        comparison = "lower than" if net_zero_footprint < average_emissions else "higher than"

        st.subheader("Comparison to Average Emissions")
        st.write(f"Your net zero footprint (<span style='color:#38b580'>{round(net_zero_footprint, 2)}</span> tons CO2) is {comparison} the average emissions in each category.", unsafe_allow_html=True)
        st.plotly_chart(fig)
        
        st.subheader("Track Your Competitors Net-Zero Goals")
        # Add a progress bar or chart to track the user's progress

        filtered_data = df_company_data[(df_company_data['SECTOR'] == user_data['general']['business_sector']) & (df_company_data['LOCATION'] == user_data['general']['hq_country'])]

        # Get the list of competitors (excluding the current company)
        competitors = filtered_data[filtered_data['Company Name'] != 'Your Company']['Company Name'].unique()

        # Display the competitor goals
        if not filtered_data.empty:
            #for competitor in competitors:
                competitor_data = filtered_data[filtered_data['Company Name'] == competitors]
                competitor_data = competitor_data[['Company Name', 'Net-Zero Year', 'Near term - Target Status', 'Near term - Target Classification', 'Net-Zero Committed']].reset_index(drop=True).set_index('Company Name') 

                st.dataframe(competitor_data)
        
        else:
            st.write('Your competitors did not report their Net Zero Goals.')
        
        
        # Provide informative text and tips
        st.header("Personalized Recommendations")
        st.subheader("Tips for Reducing Your Carbon Footprint")
        HFC_ref_yes = user_data['energy_usage']['hfc_refrigrator']
        electricity_consumption = user_data['energy_usage']['electricity_consumption']
        distance_traveled = user_data['transport_data']['distance_traveled'] 
        def generate_carbon_footprint_tips(electricity_consumption, HFC_ref_yes, distance_traveled):
            tips = [
                    "Choose cloud providers that prioritize renewable energy sources to power their data centers.",
                    "Consider leveraging cloud-based sustainability tools and services that help monitor, analyze, and optimize your cloud resource usage for maximum efficiency and reduced environmental impact.",
                    "Educate employees, engage them in sustainability efforts, and consider offsetting emissions through carbon offset programs.",
                    "Support forest conservation initiatives and consider offsetting your emissions."
                ]

            if electricity_consumption > 65:
                tips.append("Opt for energy-efficient equipment and utilize virtualization and cloud computing to reduce energy consumption.")

            if HFC_ref_yes:
                tips.append("Buy a HFC-free refrigerant. You can find more information on it [here](https://us.eia.org/report/20200625-hfc-free-refrigerator-list/).")

            if distance_traveled > 20000:
                tips.append("Promote remote work and utilize teleconferencing to minimize commuting-related emissions.")
            return tips

        # Generate and display tips
        tips = generate_carbon_footprint_tips(electricity_consumption, HFC_ref_yes, distance_traveled)
        for tip in tips:
            st.write(f"- {tip}")
        
        st.subheader("Find Your Sustainable Supplier")
        # Load the company data from the database


        # Main page content
        # Sector and country selection
        location_index = sorted_countries.index(user_data['general']['hq_country'])
        sector_index = sorted_sector.index(user_data['general']['business_sector'])
        col1, col2 = st.columns(2)
        with col1:
            selected_sector = st.selectbox('Select Sector', sorted_sector, index=sector_index)

        with col2:
            selected_country = st.selectbox('Select Country', sorted_countries, index=location_index)

        # Filter the company data based on the selected sector and country
        filtered_data = df_company_data[(df_company_data['SECTOR'] == selected_sector) & (df_company_data['LOCATION'] == selected_country)]

        # Display the filtered data
        if not filtered_data.empty:
            
            col1, col2 = st.columns(2)
            with col1:
                show_net_zero = st.checkbox('Show Net-Zero Committed Companies')
            with col2:
                goal_type =st.checkbox('Show Long term goal')

            # Filter data based on net-zero commitment and goal type
            if show_net_zero:
                filtered_data = filtered_data[filtered_data['Net-Zero Committed'] == 'Yes']

            if not goal_type:
                filtered_data = filtered_data[['Company Name', 'Net-Zero Year', 'Near term - Target Status', 'Near term - Target Classification', 'Net-Zero Committed']].reset_index(drop=True).set_index('Company Name') 
            else:
                filtered_data = filtered_data[['Company Name', 'Net-Zero Year', 'Long term - Target Status', 'Long term - Target Classification', 'Net-Zero Committed']].reset_index(drop=True).set_index('Company Name') 

            # Display the table without the index column
            st.dataframe(filtered_data)
        
        else:
            st.write('No companies found with the selected criteria.')



        # Add personalized recommendations based on the user's emissions and categories

        # Progress tracking
        
        st.header('Data sources')
        st.write(
            "1. [Data on CO2 and Greenhouse Gas Emissions](https://github.com/owid/co2-data)\n"
            "2. [GHG Emission Factors for Electricity Consumption](https://data.jrc.ec.europa.eu/dataset/919df040-0252-4e4e-ad82-c054896e1641)\n"
            "3. [Calculating Carbon Emissions from Water](https://shorturl.at/sABCP)\n"
            "4. [CO2 emissions from new passenger cars](https://shorturl.at/sDKRX)\n"
            "5. [Climate Change - Transport](https://climatechallenge.be/nl/themas/hoe-ons-klimaatvriendelijk-verplaatsen#gebruik-het-openbaar-vervoer)\n"
            "6. [Stib-Mivb - Milieu](https://www.stib-mivb.be/article.html?_guid=008a3561-2ac1-3410-22bc-d575f8441615&l=nl)\n"
            "7. [Statbel fgov - Municipal Waste](https://statbel.fgov.be/en/themes/environment/waste-and-pollution/municipal-waste)\n"
            "8. [EFD - emission factor database](https://www.ipcc-nggip.iges.or.jp/EFDB/find_ef.php?action=detach_filter&refresh=false&filter=prop_regional&fkey=0)\n"

)