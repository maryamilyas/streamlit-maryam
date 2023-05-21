# # streamlit_app.py
#
# import streamlit as st
#
# # Initialize connection.
# conn = st.experimental_connection('snowpark')
#
# # Load the table as a dataframe using the Snowpark Session.
# @st.cache_data
# def load_table():
#     with conn.safe_session() as session:
#         return session.table('mytable').to_pandas()
#
# df = load_table()
#
# # Print results.
# for row in df.itertuples():
#     st.write(f"{row.NAME} has a :{row.PET}:")

# streamlit_app.py

# import snowflake.connector
# import streamlit as st
#
#
# def fetch_data_from_snowflake(table_name):
#     # Retrieve Snowflake connection details from secrets.toml
#     snowflake_config = st.secrets.connections.snowpark
#
#     # Connect to Snowflake
#     conn = snowflake.connector.connect(
#         user=snowflake_config["user"],
#         password=snowflake_config["password"],
#         account=snowflake_config["account"],
#         warehouse=snowflake_config["warehouse"],
#         database=snowflake_config["database"],
#         schema=snowflake_config["schema"],
#     )
#
#     # Execute query to fetch data
#     query = f"SELECT * FROM {table_name}"
#     cursor = conn.cursor()
#     cursor.execute(query)
#
#     # Retrieve column names
#     column_names = [desc[0] for desc in cursor.description]
#
#     # Retrieve rows
#     rows = cursor.fetchall()
#
#     # Close connection
#     conn.close()
#
#     # Display data in Streamlit table
#     st.table(rows, column_names)
#
#
# # Streamlit app
# def main():
#     st.title("Data Viewer")
#
#     # Input for table name
#     table_name = st.text_input("Table Name")
#
#     # Fetch and display data when the button is clicked
#     if st.button("Fetch Data"):
#         fetch_data_from_snowflake(table_name)
#
#
# if __name__ == "__main__":
#     main()

# import snowflake.connector
# import streamlit as st
#
#
# def fetch_data_from_snowflake(table_name):
#     # Retrieve Snowflake connection details from secrets.toml
#     snowflake_config = st.secrets.connections.snowpark
#
#     # Connect to Snowflake
#     conn = snowflake.connector.connect(
#         user=snowflake_config["user"],
#         password=snowflake_config["password"],
#         account=snowflake_config["account"],
#         warehouse=snowflake_config["warehouse"],
#         database=snowflake_config["database"],
#         schema=snowflake_config["schema"],
#     )
#
#     # Execute query to fetch data
#     query = f"SELECT * FROM {table_name}"
#     cursor = conn.cursor()
#     cursor.execute(query)
#
#     # Retrieve column names
#     column_names = [desc[0] for desc in cursor.description]
#
#     # Retrieve rows
#     rows = cursor.fetchall()
#
#     # Close connection
#     conn.close()
#
#     # Display data in Streamlit table
#     st.table(rows, column_names)
#
#
# # Streamlit app
# def main():
#     st.title("Data Viewer")
#
#     # Input for table name
#     table_name = st.text_input("Table Name")
#
#     # Fetch and display data when the button is clicked
#     if st.button("Fetch Data"):
#         fetch_data_from_snowflake(table_name)
#
#
# if __name__ == "__main__":
#     main()


# import streamlit as st
#
# # Initialize connection.
# conn = st.experimental_connection('snowpark')
#
# # Perform query.
# df = conn.query(
#     "SELECT * FROM EMISSION_FACTORS_DATABASES.PUBLIC.ELECTRICITY_CONSUMTION_FACTOR_CO2 WHERE COUNTRY = 'Belgium' AND YEAR = '2020';",
#     ttl=600)
#
# # Print results.
# for row in df.itertuples():
#     st.write(f"{row.COUNTRY} - {row.YEAR}: {row.VALUE}")

# import snowflake.connector
# import streamlit as st
# import pandas as pd
#
#
# def fetch_data_from_snowflake(table_name):
#     # Retrieve Snowflake connection details from secrets.toml
#     snowflake_config = st.secrets.connections.snowpark
#
#     # Connect to Snowflake
#     conn = snowflake.connector.connect(
#         user=snowflake_config["user"],
#         password=snowflake_config["password"],
#         account=snowflake_config["account"],
#         warehouse=snowflake_config["warehouse"],
#         database=snowflake_config["database"],
#         schema=snowflake_config["schema"],
#     )
#
#     # Execute query to fetch data
#     query = f"SELECT * FROM {table_name}"
#     cursor = conn.cursor()
#     cursor.execute(query)
#
#     # Retrieve column names
#     column_names = [desc[0] for desc in cursor.description]
#
#     # Retrieve rows
#     rows = cursor.fetchall()
#
#     # Close connection
#     conn.close()
#
#     # Create a Pandas DataFrame
#     df = pd.DataFrame(rows, columns=column_names)
#
#     return df
#
#
# # Streamlit app
# def main():
#     st.title("Data Viewer")
#
#     # Input for table name
#     table_name = st.text_input("Table Name")
#
#     # Fetch and display data when the button is clicked
#     if st.button("Fetch Data"):
#         data = fetch_data_from_snowflake(table_name)
#         st.dataframe(data)
#
#
# if __name__ == "__main__":
#     main()

# import snowflake.connector
# import streamlit as st
# import pandas as pd
#
#
# @st.cache_data(ttl=None)  # Cache data until app is refreshed
# def fetch_data_from_snowflake(_snowflake_config, table_name):
#     # Connect to Snowflake
#     conn = snowflake.connector.connect(
#         user=_snowflake_config["user"],
#         password=_snowflake_config["password"],
#         account=_snowflake_config["account"],
#         warehouse=_snowflake_config["warehouse"],
#         database=_snowflake_config["database"],
#         schema=_snowflake_config["schema"],
#     )
#
#     # Execute query to fetch data
#     query = f"SELECT * FROM {table_name}"
#     cursor = conn.cursor()
#     cursor.execute(query)
#
#     # Retrieve column names
#     column_names = [desc[0] for desc in cursor.description]
#
#     # Retrieve rows
#     rows = cursor.fetchall()
#
#     # Close connection
#     conn.close()
#
#     # Create DataFrame
#     df = pd.DataFrame(rows, columns=column_names)
#     return df
#
#
# # Streamlit app
# def main():
#     st.title("Data Viewer")
#
#     # Retrieve Snowflake connection details from secrets.toml
#     snowflake_config = st.secrets.connections.snowpark
#
#     # Input for table name
#     table_name = st.text_input("Table Name")
#
#     # Fetch and display data when the button is clicked
#     if st.button("Fetch Data"):
#         df = fetch_data_from_snowflake(snowflake_config, table_name)
#         st.dataframe(df)
#
#
# if __name__ == "__main__":
#     main()

# import snowflake.connector
# import streamlit as st
# import pandas as pd
#
#
# @st.cache_data(ttl=None)  # Cache data until app is refreshed
# def fetch_tables_from_snowflake(_snowflake_config):
#     # Connect to Snowflake
#     conn = snowflake.connector.connect(
#         user=_snowflake_config["user"],
#         password=_snowflake_config["password"],
#         account=_snowflake_config["account"],
#         warehouse=_snowflake_config["warehouse"],
#         database=_snowflake_config["database"],
#         schema=_snowflake_config["schema"],
#     )
#
#     # Retrieve table names
#     query = "SHOW TABLES"
#     cursor = conn.cursor()
#     cursor.execute(query)
#
#     # Fetch table names
#     tables = [table[1] for table in cursor.fetchall()]
#
#     # Close connection
#     conn.close()
#
#     return tables
#
#
# @st.cache_data(ttl=None)  # Cache data until app is refreshed
# def fetch_data_from_snowflake(_snowflake_config, table_name):
#     # Connect to Snowflake
#     conn = snowflake.connector.connect(
#         user=_snowflake_config["user"],
#         password=_snowflake_config["password"],
#         account=_snowflake_config["account"],
#         warehouse=_snowflake_config["warehouse"],
#         database=_snowflake_config["database"],
#         schema=_snowflake_config["schema"],
#     )
#
#     # Execute query to fetch data
#     query = f"SELECT * FROM {table_name}"
#     cursor = conn.cursor()
#     cursor.execute(query)
#
#     # Retrieve column names
#     column_names = [desc[0] for desc in cursor.description]
#
#     # Retrieve rows
#     rows = cursor.fetchall()
#
#     # Close connection
#     conn.close()
#
#     # Create DataFrame
#     df = pd.DataFrame(rows, columns=column_names)
#     return df
#
#
# # Streamlit app
# def main():
#     st.title("Data Viewer")
#
#     # Retrieve Snowflake connection details from secrets.toml
#     snowflake_config = st.secrets.connections.snowpark
#
#     # Fetch all table names
#     tables = fetch_tables_from_snowflake(snowflake_config)
#
#     # Dropdown menu to select table
#     table_name = st.selectbox("Select Table", tables)
#
#     # Fetch and display data when the button is clicked
#     if st.button("Fetch Data"):
#         df = fetch_data_from_snowflake(snowflake_config, table_name)
#
#         # Display filters for each column
#         for column in df.columns:
#             filter_type = st.selectbox(f"Filter {column}", ["None", "Dropdown", "Slicer"])
#
#             if filter_type == "Dropdown":
#                 unique_values = df[column].unique().tolist()
#                 selected_value = st.selectbox(f"Select {column}", unique_values)
#                 df = df[df[column] == selected_value]
#             elif filter_type == "Slicer":
#                 min_value = df[column].min()
#                 max_value = df[column].max()
#                 selected_range = st.slider(f"Select {column}", min_value, max_value, (min_value, max_value))
#                 df = df[(df[column] >= selected_range[0]) & (df[column] <= selected_range[1])]
#
#         # Display filtered data in DataFrame
#         st.dataframe(df)
#
#
# if __name__ == "__main__":
#     main()

# import snowflake.connector
# import streamlit as st
# import pandas as pd
#
#
# @st.cache_data(ttl=None)  # Cache data until app is refreshed
# def fetch_tables_from_snowflake(_snowflake_config):
#     # Connect to Snowflake
#     conn = snowflake.connector.connect(
#         user=_snowflake_config["user"],
#         password=_snowflake_config["password"],
#         account=_snowflake_config["account"],
#         warehouse=_snowflake_config["warehouse"],
#         database=_snowflake_config["database"],
#         schema=_snowflake_config["schema"],
#     )
#
#     # Retrieve table names
#     query = "SHOW TABLES"
#     cursor = conn.cursor()
#     cursor.execute(query)
#
#     # Fetch table names
#     tables = [table[1] for table in cursor.fetchall()]
#
#     # Close connection
#     conn.close()
#
#     return tables
#
#
# @st.cache_data(ttl=None)  # Cache data until app is refreshed
# def fetch_data_from_snowflake(_snowflake_config, table_name):
#     # Connect to Snowflake
#     conn = snowflake.connector.connect(
#         user=_snowflake_config["user"],
#         password=_snowflake_config["password"],
#         account=_snowflake_config["account"],
#         warehouse=_snowflake_config["warehouse"],
#         database=_snowflake_config["database"],
#         schema=_snowflake_config["schema"],
#     )
#
#     # Execute query to fetch data
#     query = f"SELECT * FROM {table_name}"
#     cursor = conn.cursor()
#     cursor.execute(query)
#
#     # Retrieve column names
#     column_names = [desc[0] for desc in cursor.description]
#
#     # Retrieve rows
#     rows = cursor.fetchall()
#
#     # Close connection
#     conn.close()
#
#     # Create DataFrame
#     df = pd.DataFrame(rows, columns=column_names)
#     return df
#
#
# # Streamlit app
# def main():
#     st.title("Data Viewer")
#
#     # Retrieve Snowflake connection details from secrets.toml
#     snowflake_config = st.secrets.connections.snowpark
#
#     # Fetch all table names
#     tables = fetch_tables_from_snowflake(snowflake_config)
#
#     # Dropdown menu to select schema
#     selected_schema = st.selectbox("Select Schema", snowflake_config["schema"])
#
#     # Dropdown menu to select table
#     table_name = st.selectbox("Select Table", tables)
#
#     # Fetch and display data when the button is clicked
#     if st.button("Fetch Data"):
#         # Fetch data based on the selected schema and table
#         snowflake_config["schema"] = selected_schema
#         df = fetch_data_from_snowflake(snowflake_config, table_name)
#
#         # Display filters for each column
#         for column in df.columns:
#             unique_values = df[column].unique().tolist()
#             filter_type = st.selectbox(f"Filter {column}", ["All"] + unique_values)
#
#             if filter_type != "All":
#                 df = df[df[column] == filter_type]
#
#         # Display filtered data in DataFrame
#         st.dataframe(df)
#
#
# if __name__ == "__main__":
#     main()

# import snowflake.connector
# import streamlit as st
# import pandas as pd
#
#
# @st.cache_data(ttl=None)  # Cache data until app is refreshed
# def fetch_tables_from_snowflake(_snowflake_config):
#     # Connect to Snowflake
#     conn = snowflake.connector.connect(
#         user=_snowflake_config["user"],
#         password=_snowflake_config["password"],
#         account=_snowflake_config["account"],
#         warehouse=_snowflake_config["warehouse"],
#         database=_snowflake_config["database"],
#         schema=_snowflake_config["schema"],
#     )
#
#     # Retrieve table names
#     query = "SHOW TABLES"
#     cursor = conn.cursor()
#     cursor.execute(query)
#
#     # Fetch table names
#     tables = [table[1] for table in cursor.fetchall()]
#
#     # Close connection
#     conn.close()
#
#     return tables
#
#
# @st.cache_data(ttl=None)  # Cache data until app is refreshed
# def fetch_data_from_snowflake(_snowflake_config, table_name):
#     # Connect to Snowflake
#     conn = snowflake.connector.connect(
#         user=_snowflake_config["user"],
#         password=_snowflake_config["password"],
#         account=_snowflake_config["account"],
#         warehouse=_snowflake_config["warehouse"],
#         database=_snowflake_config["database"],
#         schema=_snowflake_config["schema"],
#     )
#
#     # Execute query to fetch data
#     query = f"SELECT * FROM {table_name}"
#     cursor = conn.cursor()
#     cursor.execute(query)
#
#     # Retrieve column names
#     column_names = [desc[0] for desc in cursor.description]
#
#     # Retrieve rows
#     rows = cursor.fetchall()
#
#     # Close connection
#     conn.close()
#
#     # Create DataFrame
#     df = pd.DataFrame(rows, columns=column_names)
#     return df
#
#
# # Streamlit app
# def main():
#     st.title("Data Viewer")
#
#     # Retrieve Snowflake connection details from secrets.toml
#     snowflake_config = st.secrets.connections.snowpark
#
#     # Fetch all table names
#     tables = fetch_tables_from_snowflake(snowflake_config)
#
#     # Dropdown menu to select table
#     table_name = st.selectbox("Select Table", tables)
#
#     # Fetch and display data when the button is clicked
#     if st.button("Fetch Data"):
#         df = fetch_data_from_snowflake(snowflake_config, table_name)
#
#         # Display filters for each column
#         for column in df.columns:
#             unique_values = df[column].unique().tolist()
#             filter_type = st.selectbox(f"Filter {column}", ["All"] + unique_values)
#
#             if filter_type != "All":
#                 df = df[df[column] == filter_type]
#
#         # Display filtered data in DataFrame
#         st.dataframe(df)
#
#
# if __name__ == "__main__":
#     main()

# import snowflake.connector
# import streamlit as st
# import pandas as pd
# from streamlit.hashing import _CodeHasher
# from streamlit.report_thread import get_report_ctx
# from streamlit.server.server import Server
#
#
# # Custom SessionState class to store filter values
# class SessionState:
#     def __init__(self, **kwargs):
#         for key, val in kwargs.items():
#             setattr(self, key, val)
#
#
# def get_session_id():
#     ctx = get_report_ctx()
#     session_id = ctx.session_id
#     return session_id
#
#
# def get_session_state():
#     session_id = get_session_id()
#     session_state = getattr(Server.get_current()._session_infos, session_id).session_state
#     return session_state
#
#
# def set_session_state(**kwargs):
#     session_id = get_session_id()
#     session_state = getattr(Server.get_current()._session_infos, session_id).session_state
#     for key, val in kwargs.items():
#         setattr(session_state, key, val)
#
#
# @st.cache_data(ttl=None)  # Cache data until app is refreshed
# def fetch_tables_from_snowflake(_snowflake_config):
#     # Connect to Snowflake
#     conn = snowflake.connector.connect(
#         user=_snowflake_config["user"],
#         password=_snowflake_config["password"],
#         account=_snowflake_config["account"],
#         warehouse=_snowflake_config["warehouse"],
#         database=_snowflake_config["database"],
#         schema=_snowflake_config["schema"],
#     )
#
#     # Retrieve table names
#     query = "SHOW TABLES"
#     cursor = conn.cursor()
#     cursor.execute(query)
#
#     # Fetch table names
#     tables = [table[1] for table in cursor.fetchall()]
#
#     # Close connection
#     conn.close()
#
#     return tables
#
#
# @st.cache_data(ttl=None)  # Cache data until app is refreshed
# def fetch_data_from_snowflake(_snowflake_config, table_name):
#     # Connect to Snowflake
#     conn = snowflake.connector.connect(
#         user=_snowflake_config["user"],
#         password=_snowflake_config["password"],
#         account=_snowflake_config["account"],
#         warehouse=_snowflake_config["warehouse"],
#         database=_snowflake_config["database"],
#         schema=_snowflake_config["schema"],
#     )
#
#     # Execute query to fetch data
#     query = f"SELECT * FROM {table_name}"
#     cursor = conn.cursor()
#     cursor.execute(query)
#
#     # Retrieve column names
#     column_names = [desc[0] for desc in cursor.description]
#
#     # Retrieve rows
#     rows = cursor.fetchall()
#
#     # Close connection
#     conn.close()
#
#     # Create DataFrame
#     df = pd.DataFrame(rows, columns=column_names)
#     return df
#
#
# # Streamlit app
# def main():
#     st.title("Data Viewer")
#
#     # Retrieve Snowflake connection details from secrets.toml
#     snowflake_config = st.secrets.connections.snowpark
#
#     # Fetch all table names
#     tables = fetch_tables_from_snowflake(snowflake_config)
#
#     # Dropdown menu to select table
#     table_name = st.selectbox("Select Table", tables, key="table")
#
#     # Fetch and display data when the button is clicked
#     if st.button("Fetch Data"):
#         df = fetch_data_from_snowflake(snowflake_config, table_name)
#
#         # Retrieve session state
#         session_state = get_session_state()
#
#         # Create filters if they don't exist in session state
#         if not hasattr(session_state, "filters"):
#             session_state.filters = {}
#
#         # Display filters for each column
#         for column in df.columns:
#             unique_values = df[column].unique().tolist()
#
#             # Check if filter exists in session state
#             if column not in session_state.filters:
#                 # Default filter value
#                 session_state.filters[column] = "All"
#
#             # Update filter value based on user selection
#             filter_type = st.selectbox(f"Filter {column}", ["All"] + unique_values, key=f"filter_{column}",
#                                        index=unique_values.index(session_state.filters[column]))
#
#             # Update session state with new filter value
#             set_session_state(**{f"filters.{column}": filter_type})
#
#             # Filter data based on selected value
#             if filter_type != "All":
#                 df = df[df[column] == filter_type]
#
#         # Display filtered data in DataFrame
#         st.dataframe(df)
#
#
# if __name__ == "__main__":
#     main()

# import snowflake.connector
# import streamlit as st
# import pandas as pd
#
#
# def fetch_tables_from_snowflake(_snowflake_config):
#     # Connect to Snowflake
#     conn = snowflake.connector.connect(
#         user=_snowflake_config["user"],
#         password=_snowflake_config["password"],
#         account=_snowflake_config["account"],
#         warehouse=_snowflake_config["warehouse"],
#         database=_snowflake_config["database"],
#         schema=_snowflake_config["schema"],
#     )
#
#     # Retrieve table names
#     query = "SHOW TABLES"
#     cursor = conn.cursor()
#     cursor.execute(query)
#
#     # Fetch table names
#     tables = [table[1] for table in cursor.fetchall()]
#
#     # Close connection
#     conn.close()
#
#     return tables
#
#
# def fetch_data_from_snowflake(_snowflake_config, table_name):
#     # Connect to Snowflake
#     conn = snowflake.connector.connect(
#         user=_snowflake_config["user"],
#         password=_snowflake_config["password"],
#         account=_snowflake_config["account"],
#         warehouse=_snowflake_config["warehouse"],
#         database=_snowflake_config["database"],
#         schema=_snowflake_config["schema"],
#     )
#
#     # Execute query to fetch data
#     query = f"SELECT * FROM {table_name}"
#     cursor = conn.cursor()
#     cursor.execute(query)
#
#     # Retrieve column names
#     column_names = [desc[0] for desc in cursor.description]
#
#     # Retrieve rows
#     rows = cursor.fetchall()
#
#     # Close connection
#     conn.close()
#
#     # Create DataFrame
#     df = pd.DataFrame(rows, columns=column_names)
#     return df
#
#
# # Streamlit app
# def main():
#     st.title("Data Viewer")
#
#     # Retrieve Snowflake connection details from secrets.toml
#     snowflake_config = st.secrets.connections.snowpark
#
#     # Fetch all table names
#     tables = fetch_tables_from_snowflake(snowflake_config)
#
#     # Dropdown menu to select table
#     table_name = st.selectbox("Select Table", tables)
#
#     # Fetch and display data when the button is clicked
#     if st.button("Fetch Data"):
#         df = fetch_data_from_snowflake(snowflake_config, table_name)
#
#         # Create a filter dictionary to store filter values
#         filters = {}
#
#         # Display filters for each column
#         for column in df.columns:
#             unique_values = df[column].unique().tolist()
#
#             # Get the filter value from the dictionary or default to "All"
#             filter_value = filters.get(column, "All")
#
#             # Update the filter value based on user selection
#             filter_value = st.selectbox(f"Filter {column}", ["All"] + unique_values, index=unique_values.index(filter_value))
#
#             # Update the filter dictionary with the new value
#             filters[column] = filter_value
#
#             # Filter the data based on the selected value
#             if filter_value != "All":
#                 df = df[df[column] == filter_value]
#
#         # Display filtered data in DataFrame
#         st.dataframe(df)
#
#
# if __name__ == "__main__":
#     main()

# import snowflake.connector
# import streamlit as st
# import pandas as pd
#
#
# def fetch_tables_from_snowflake(_snowflake_config):
#     # Connect to Snowflake
#     conn = snowflake.connector.connect(
#         user=_snowflake_config["user"],
#         password=_snowflake_config["password"],
#         account=_snowflake_config["account"],
#         warehouse=_snowflake_config["warehouse"],
#         database=_snowflake_config["database"],
#         schema=_snowflake_config["schema"],
#     )
#
#     # Retrieve table names
#     query = "SHOW TABLES"
#     cursor = conn.cursor()
#     cursor.execute(query)
#
#     # Fetch table names
#     tables = [table[1] for table in cursor.fetchall()]
#
#     # Close connection
#     conn.close()
#
#     return tables
#
#
# def fetch_data_from_snowflake(_snowflake_config, table_name):
#     # Connect to Snowflake
#     conn = snowflake.connector.connect(
#         user=_snowflake_config["user"],
#         password=_snowflake_config["password"],
#         account=_snowflake_config["account"],
#         warehouse=_snowflake_config["warehouse"],
#         database=_snowflake_config["database"],
#         schema=_snowflake_config["schema"],
#     )
#
#     # Execute query to fetch data
#     query = f"SELECT * FROM {table_name}"
#     cursor = conn.cursor()
#     cursor.execute(query)
#
#     # Retrieve column names
#     column_names = [desc[0] for desc in cursor.description]
#
#     # Retrieve rows
#     rows = cursor.fetchall()
#
#     # Close connection
#     conn.close()
#
#     # Create DataFrame
#     df = pd.DataFrame(rows, columns=column_names)
#     return df
#
#
# # Streamlit app
# def main():
#     st.title("Data Viewer")
#
#     # Retrieve Snowflake connection details from secrets.toml
#     snowflake_config = st.secrets.connections.snowpark
#
#     # Fetch all table names
#     tables = fetch_tables_from_snowflake(snowflake_config)
#
#     # Dropdown menu to select table
#     table_name = st.selectbox("Select Table", tables)
#
#     # Fetch and display data when the button is clicked
#     if st.button("Fetch Data"):
#         df = fetch_data_from_snowflake(snowflake_config, table_name)
#
#         # Create a filter dictionary to store filter values
#         filters = {}
#
#         # Display filters for each column
#         for column in df.columns:
#             unique_values = df[column].unique().tolist()
#
#             # Get the filter value from the dictionary or default to the first value in the unique values list
#             filter_value = filters.get(column, unique_values[0])
#
#             # Update the filter value based on user selection
#             filter_value = st.selectbox(f"Filter {column}", ["All"] + unique_values, index=unique_values.index(filter_value))
#
#             # Update the filter dictionary with the new value
#             filters[column] = filter_value
#
#             # Filter the data based on the selected value
#             if filter_value != "All":
#                 df = df[df[column] == filter_value]
#
#         # Display filtered data in DataFrame
#         st.dataframe(df)
#
#
# if __name__ == "__main__":
#     main()

# import snowflake.connector
# import streamlit as st
# from streamlit import caching
# import pandas as pd
# from streamlit_state import session_state
#
#
# def fetch_tables_from_snowflake(_snowflake_config):
#     # Connect to Snowflake
#     conn = snowflake.connector.connect(
#         user=_snowflake_config["user"],
#         password=_snowflake_config["password"],
#         account=_snowflake_config["account"],
#         warehouse=_snowflake_config["warehouse"],
#         database=_snowflake_config["database"],
#         schema=_snowflake_config["schema"],
#     )
#
#     # Retrieve table names
#     query = "SHOW TABLES"
#     cursor = conn.cursor()
#     cursor.execute(query)
#
#     # Fetch table names
#     tables = [table[1] for table in cursor.fetchall()]
#
#     # Close connection
#     conn.close()
#
#     return tables
#
#
# def fetch_data_from_snowflake(_snowflake_config, table_name):
#     # Connect to Snowflake
#     conn = snowflake.connector.connect(
#         user=_snowflake_config["user"],
#         password=_snowflake_config["password"],
#         account=_snowflake_config["account"],
#         warehouse=_snowflake_config["warehouse"],
#         database=_snowflake_config["database"],
#         schema=_snowflake_config["schema"],
#     )
#
#     # Execute query to fetch data
#     query = f"SELECT * FROM {table_name}"
#     cursor = conn.cursor()
#     cursor.execute(query)
#
#     # Retrieve column names
#     column_names = [desc[0] for desc in cursor.description]
#
#     # Retrieve rows
#     rows = cursor.fetchall()
#
#     # Close connection
#     conn.close()
#
#     # Create DataFrame
#     df = pd.DataFrame(rows, columns=column_names)
#     return df
#
#
# # Streamlit app
# def main():
#     st.title("Data Viewer")
#
#     # Retrieve Snowflake connection details from secrets.toml
#     snowflake_config = st.secrets.connections.snowpark
#
#     # Fetch all table names
#     tables = fetch_tables_from_snowflake(snowflake_config)
#
#     # Dropdown menu to select table
#     table_name = st.selectbox("Select Table", tables, key="table")
#
#     # Fetch and display data when the button is clicked
#     if st.button("Fetch Data"):
#         df = fetch_data_from_snowflake(snowflake_config, table_name)
#
#         # Create a filter dictionary to store filter values
#         if "filters" not in session_state:
#             session_state.filters = {}
#
#         # Display filters for each column
#         for column in df.columns:
#             unique_values = df[column].unique().tolist()
#
#             # Get the filter value from the session state or default to the first value in the unique values list
#             filter_value = session_state.filters.get(column, unique_values[0])
#
#             # Update the filter value based on user selection
#             filter_value = st.selectbox(f"Filter {column}", ["All"] + unique_values,
#                                         index=unique_values.index(filter_value))
#
#             # Update the filter dictionary in the session state with the new value
#             session_state.filters[column] = filter_value
#
#             # Filter the data based on the selected value
#             if filter_value != "All":
#                 df = df[df[column] == filter_value]
#
#         # Display filtered data in DataFrame
#         st.dataframe(df)
#
#     # Clear the filters when the table selection is changed
#     if st.session_state.table != table_name:
#         session_state.filters = {}
#
#
# if __name__ == "__main__":
#     main()

# import snowflake.connector
# import streamlit as st
# import pandas as pd
# from streamlit.hashing import _CodeHasher
# from streamlit.script_runner import RerunException
# import hashlib
#
#
# def fetch_tables_from_snowflake(_snowflake_config):
#     # Connect to Snowflake
#     conn = snowflake.connector.connect(
#         user=_snowflake_config["user"],
#         password=_snowflake_config["password"],
#         account=_snowflake_config["account"],
#         warehouse=_snowflake_config["warehouse"],
#         database=_snowflake_config["database"],
#         schema=_snowflake_config["schema"],
#     )
#
#     # Retrieve table names
#     query = "SHOW TABLES"
#     cursor = conn.cursor()
#     cursor.execute(query)
#
#     # Fetch table names
#     tables = [table[1] for table in cursor.fetchall()]
#
#     # Close connection
#     conn.close()
#
#     return tables
#
#
# def fetch_data_from_snowflake(_snowflake_config, table_name):
#     # Connect to Snowflake
#     conn = snowflake.connector.connect(
#         user=_snowflake_config["user"],
#         password=_snowflake_config["password"],
#         account=_snowflake_config["account"],
#         warehouse=_snowflake_config["warehouse"],
#         database=_snowflake_config["database"],
#         schema=_snowflake_config["schema"],
#     )
#
#     # Execute query to fetch data
#     query = f"SELECT * FROM {table_name}"
#     cursor = conn.cursor()
#     cursor.execute(query)
#
#     # Retrieve column names
#     column_names = [desc[0] for desc in cursor.description]
#
#     # Retrieve rows
#     rows = cursor.fetchall()
#
#     # Close connection
#     conn.close()
#
#     # Create DataFrame
#     df = pd.DataFrame(rows, columns=column_names)
#     return df
#
#
# def persist_state(func):
#     def wrapper(*args, **kwargs):
#         hasher = _CodeHasher(func)
#         cache_key = hasher.hash(args, kwargs)
#
#         # Compute a hash key for the current state
#         state_hash = hashlib.md5(str(st.session_state).encode()).hexdigest()
#
#         # Check if the cache key is already stored in the session state
#         if cache_key not in st.session_state:
#             # If not, create a new entry with the current state hash
#             st.session_state[cache_key] = state_hash
#         elif st.session_state[cache_key] != state_hash:
#             # If the state hash has changed, clear the cache and update the state hash
#             st.session_state[cache_key] = state_hash
#             st.experimental_rerun()
#
#         # Call the function and return the result
#         return func(*args, **kwargs)
#
#     return wrapper
#
#
# # Streamlit app
# def main():
#     st.title("Data Viewer")
#
#     # Retrieve Snowflake connection details from secrets.toml
#     snowflake_config = st.secrets.connections.snowpark
#
#     # Fetch all table names
#     tables = fetch_tables_from_snowflake(snowflake_config)
#
#     # Dropdown menu to select table
#     table_name = st.selectbox("Select Table", tables, key="table")
#
#     # Fetch and display data when the button is clicked
#     if st.button("Fetch Data"):
#         df = fetch_data_from_snowflake(snowflake_config, table_name)
#
#         # Display filters for each column
#         for column in df.columns:
#             unique_values = df[column].unique().tolist()
#
#             # Get the current filter value from session state or use the first unique value
#             filter_value = st.session_state.get(f"{table_name}_{column}_filter", unique_values[0])
#
#             # Update the filter value based on user selection
#             filter_value = st.selectbox(f"Filter {column}", unique_values, index=unique_values.index(filter_value))
#
#             # Store the filter value in session state
#             st.session_state[f"{table_name}_{column}_filter"] = filter_value
#
#             # Apply the filter to the DataFrame
#             df = df[df[column] == filter_value]
#
#         # Display filtered data in DataFrame
#         st.dataframe(df)
#
#
# if __name__ == "__main__":
#     main()

# import snowflake.connector
# import streamlit as st
# import pandas as pd
#
#
# @st.cache_data(ttl=None)  # Cache data until app is refreshed
# def fetch_tables_from_snowflake(_snowflake_config):
#     # Connect to Snowflake
#     conn = snowflake.connector.connect(
#         user=_snowflake_config["user"],
#         password=_snowflake_config["password"],
#         account=_snowflake_config["account"],
#         warehouse=_snowflake_config["warehouse"],
#         database=_snowflake_config["database"],
#         schema=_snowflake_config["schema"],
#     )
#
#     # Retrieve table names
#     query = "SHOW TABLES"
#     cursor = conn.cursor()
#     cursor.execute(query)
#
#     # Fetch table names
#     tables = [table[1] for table in cursor.fetchall()]
#
#     # Close connection
#     conn.close()
#
#     return tables
#
#
# @st.cache_data(ttl=None)  # Cache data until app is refreshed
# def fetch_data_from_snowflake(_snowflake_config, table_name):
#     # Connect to Snowflake
#     conn = snowflake.connector.connect(
#         user=_snowflake_config["user"],
#         password=_snowflake_config["password"],
#         account=_snowflake_config["account"],
#         warehouse=_snowflake_config["warehouse"],
#         database=_snowflake_config["database"],
#         schema=_snowflake_config["schema"],
#     )
#
#     # Execute query to fetch data
#     query = f"SELECT * FROM {table_name}"
#     cursor = conn.cursor()
#     cursor.execute(query)
#
#     # Retrieve column names
#     column_names = [desc[0] for desc in cursor.description]
#
#     # Retrieve rows
#     rows = cursor.fetchall()
#
#     # Close connection
#     conn.close()
#
#     # Create DataFrame
#     df = pd.DataFrame(rows, columns=column_names)
#     return df
#
#
# # Streamlit app
# def main():
#     st.title("Data Viewer")
#
#     # Retrieve Snowflake connection details from secrets.toml
#     snowflake_config = st.secrets.connections.snowpark
#
#     # Fetch all table names
#     tables = fetch_tables_from_snowflake(snowflake_config)
#
#     # Dropdown menu to select table
#     table_name = st.selectbox("Select Table", tables)
#
#     # Fetch and display data when the button is clicked
#     if st.button("Fetch Data"):
#         df = fetch_data_from_snowflake(snowflake_config, table_name)
#
#         # Display filters for each column
#         for column in df.columns:
#             unique_values = df[column].unique().tolist()
#             filter_type = st.selectbox(f"Filter {column}", ["All"] + unique_values)
#
#             if filter_type != "All":
#                 df = df[df[column] == filter_type]
#
#         # Display filtered data in DataFrame
#         st.dataframe(df)
#
#
# if __name__ == "__main__":
#     main()

# import snowflake.connector
# import streamlit as st
# import pandas as pd
# from streamlit.legacy_caching.hashing import _CodeHasher


# class SessionState:
#     def __init__(self, hash_funcs=None):
#         self._hasher = _CodeHasher(hash_funcs=hash_funcs)
#         self._widget_states = {}
#
#     def _get_session_id(self):
#         return st.report_thread.get_report_ctx().session_id
#
#     def _get_hashed_widget_id(self, widget_key):
#         session_id = self._get_session_id()
#         return self._hasher.hash(session_id + widget_key)
#
#     def __getitem__(self, widget_key):
#         hashed_widget_id = self._get_hashed_widget_id(widget_key)
#         if hashed_widget_id not in self._widget_states:
#             self._widget_states[hashed_widget_id] = st.session_state.get(hashed_widget_id, {})
#         return self._widget_states[hashed_widget_id]
#
#     def __setitem__(self, widget_key, value):
#         hashed_widget_id = self._get_hashed_widget_id(widget_key)
#         self._widget_states[hashed_widget_id] = value
#         st.session_state[hashed_widget_id] = value


# @st.cache_data(ttl=None)  # Cache data until app is refreshed
# def fetch_tables_from_snowflake(_snowflake_config):
#     # Connect to Snowflake
#     conn = snowflake.connector.connect(
#         user=_snowflake_config["user"],
#         password=_snowflake_config["password"],
#         account=_snowflake_config["account"],
#         warehouse=_snowflake_config["warehouse"],
#         database=_snowflake_config["database"],
#         schema=_snowflake_config["schema"],
#     )
#
#     # Retrieve table names
#     query = "SHOW TABLES"
#     cursor = conn.cursor()
#     cursor.execute(query)
#
#     # Fetch table names
#     tables = [table[1] for table in cursor.fetchall()]
#
#     # Close connection
#     conn.close()
#
#     return tables
#
#
# @st.cache_data(ttl=None)  # Cache data until app is refreshed
# def fetch_data_from_snowflake(_snowflake_config, table_name):
#     # Connect to Snowflake
#     conn = snowflake.connector.connect(
#         user=_snowflake_config["user"],
#         password=_snowflake_config["password"],
#         account=_snowflake_config["account"],
#         warehouse=_snowflake_config["warehouse"],
#         database=_snowflake_config["database"],
#         schema=_snowflake_config["schema"],
#     )
#
#     # Execute query to fetch data
#     query = f"SELECT * FROM {table_name}"
#     cursor = conn.cursor()
#     cursor.execute(query)
#
#     # Retrieve column names
#     column_names = [desc[0] for desc in cursor.description]
#
#     # Retrieve rows
#     rows = cursor.fetchall()
#
#     # Close connection
#     conn.close()
#
#     # Create DataFrame
#     df = pd.DataFrame(rows, columns=column_names)
#     return df
#
#
# # Streamlit app
# def main():
#     st.title("Data Viewer")
#
#     # Retrieve Snowflake connection details from secrets.toml
#     snowflake_config = st.secrets.connections.snowpark
#
#     # Initialize SessionState
#     state = SessionState()
#
#     # Fetch all table names
#     tables = fetch_tables_from_snowflake(snowflake_config)
#
#     # Dropdown menu to select table
#     table_name = st.selectbox("Select Table", tables)
#
#     # Fetch and display data when the button is clicked
#     if st.button("Fetch Data"):
#         df = fetch_data_from_snowflake(snowflake_config, table_name)
#
#         # Display filters for each column
#         for column in df.columns:
#             unique_values = df[column].unique().tolist()
#             filter_state = state[column]
#             filter_type = st.selectbox(f"Filter {column}", ["All"] + unique_values, index=unique_values.index(
#                 filter_state) + 1 if filter_state in unique_values else 0)
#
#             if filter_type != "All":
#                 df = df[df[column] == filter_type]
#                 state[column] = filter_type
#             else:
#                 state[column] = None
#
#         # Display filtered data in DataFrame
#         st.dataframe(df)
#
#
# if __name__ == "__main__":
#     main()

# import snowflake.connector
# import streamlit as st
# import pandas as pd
#
#
# # Function to fetch table names from Snowflake
# @st.cache(ttl=None)
# def fetch_tables_from_snowflake(_snowflake_config):
#     # Connect to Snowflake
#     conn = snowflake.connector.connect(
#         user=_snowflake_config["user"],
#         password=_snowflake_config["password"],
#         account=_snowflake_config["account"],
#         warehouse=_snowflake_config["warehouse"],
#         database=_snowflake_config["database"],
#         schema=_snowflake_config["schema"],
#     )
#
#     # Retrieve table names
#     query = "SHOW TABLES"
#     cursor = conn.cursor()
#     cursor.execute(query)
#
#     # Fetch table names
#     tables = [table[1] for table in cursor.fetchall()]
#
#     # Close connection
#     conn.close()
#
#     return tables
#
#
# # Function to fetch data from Snowflake
# @st.cache(ttl=None)
# def fetch_data_from_snowflake(_snowflake_config, table_name):
#     # Connect to Snowflake
#     conn = snowflake.connector.connect(
#         user=_snowflake_config["user"],
#         password=_snowflake_config["password"],
#         account=_snowflake_config["account"],
#         warehouse=_snowflake_config["warehouse"],
#         database=_snowflake_config["database"],
#         schema=_snowflake_config["schema"],
#     )
#
#     # Execute query to fetch data
#     query = f"SELECT * FROM {table_name}"
#     cursor = conn.cursor()
#     cursor.execute(query)
#
#     # Retrieve column names
#     column_names = [desc[0] for desc in cursor.description]
#
#     # Retrieve rows
#     rows = cursor.fetchall()
#
#     # Close connection
#     conn.close()
#
#     # Create DataFrame
#     df = pd.DataFrame(rows, columns=column_names)
#     return df
#
#
# # Streamlit app
# def main():
#     st.title("Data Viewer")
#
#     # Retrieve Snowflake connection details from secrets.toml
#     snowflake_config = st.secrets.connections.snowpark
#
#     # Fetch all table names
#     tables = fetch_tables_from_snowflake(snowflake_config)
#
#     # Initialize session state
#     if 'count' not in st.session_state:
#         st.session_state.count = 0
#     if "filter_state" not in st.session_state:
#         st.session_state.filter_state = {}
#
#     # Dropdown menu to select table
#     table_name = st.selectbox("Select Table", tables)
#
#     # Fetch and display data when the button is clicked
#     if st.button("Fetch Data"):
#         df = fetch_data_from_snowflake(snowflake_config, table_name)
#
#         # Display filters for each column
#         for column in df.columns:
#             unique_values = df[column].unique().tolist()
#             options = unique_values.copy()
#             if len(unique_values) > 1:
#                 options.insert(0, "All")
#
#             filter_type = st.selectbox(f"Filter {column}", options,
#                                        index=options.index(st.session_state.filter_state.get(column))
#                                        if st.session_state.filter_state.get(column) is not None else 0)
#
#             if filter_type != "All":
#                 st.session_state.filter_state[column] = filter_type
#             else:
#                 st.session_state.filter_state.pop(column, None)
#
#         # Apply filters to DataFrame
#         filtered_df = df.copy()
#         for column, value in st.session_state.filter_state.items():
#             if value is not None:
#                 filtered_df = filtered_df[filtered_df[column] == value]
#
#                 # Display filtered data in DataFrame
#                 st.dataframe(filtered_df)
#
#                 # Increment count by 1
#                 st.session_state.count += 1
#
#         # Display the current count
#         st.write("Count =", st.session_state.count)
#
#
# if __name__ == "__main__":
#     main()

# import snowflake.connector
# import streamlit as st
# import pandas as pd
#
#
# @st.cache_data(ttl=None)  # Cache data until app is refreshed
# def fetch_tables_from_snowflake(_snowflake_config):
#     # Connect to Snowflake
#     conn = snowflake.connector.connect(
#         user=_snowflake_config["user"],
#         password=_snowflake_config["password"],
#         account=_snowflake_config["account"],
#         warehouse=_snowflake_config["warehouse"],
#         database=_snowflake_config["database"],
#         schema=_snowflake_config["schema"],
#     )
#
#     # Retrieve table names
#     query = "SHOW TABLES"
#     cursor = conn.cursor()
#     cursor.execute(query)
#
#     # Fetch table names
#     tables = [table[1] for table in cursor.fetchall()]
#
#     # Close connection
#     conn.close()
#
#     return tables
#
#
# @st.cache_data(ttl=None)  # Cache data until app is refreshed
# def fetch_data_from_snowflake(_snowflake_config, table_name):
#     # Connect to Snowflake
#     conn = snowflake.connector.connect(
#         user=_snowflake_config["user"],
#         password=_snowflake_config["password"],
#         account=_snowflake_config["account"],
#         warehouse=_snowflake_config["warehouse"],
#         database=_snowflake_config["database"],
#         schema=_snowflake_config["schema"],
#     )
#
#     # Execute query to fetch data
#     query = f"SELECT * FROM {table_name}"
#     cursor = conn.cursor()
#     cursor.execute(query)
#
#     # Retrieve column names
#     column_names = [desc[0] for desc in cursor.description]
#
#     # Retrieve rows
#     rows = cursor.fetchall()
#
#     # Close connection
#     conn.close()
#
#     # Create DataFrame
#     df = pd.DataFrame(rows, columns=column_names)
#     return df
#
#
# # Streamlit app
# def main():
#     st.title("Data Viewer")
#
#     # Retrieve Snowflake connection details from secrets.toml
#     snowflake_config = st.secrets.connections.snowpark
#
#     # Fetch all table names
#     tables = fetch_tables_from_snowflake(snowflake_config)
#
#     # Initialize session state
#     if "filter_state" not in st.session_state:
#         st.session_state.filter_state = {}
#
#     # Dropdown menu to select table
#     table_name = st.selectbox("Select Table", tables)
#
#     # Fetch and display data when the button is clicked
#     if st.button("Fetch Data"):
#         df = fetch_data_from_snowflake(snowflake_config, table_name)
#
#         # Display filters for each column
#         for column in df.columns:
#             unique_values = df[column].unique().tolist()
#             options = unique_values.copy()
#             if len(unique_values) > 1:
#                 options.insert(0, "All")
#
#             filter_type = st.selectbox(f"Filter {column}", options,
#                                        index=options.index(st.session_state.filter_state.get(column))
#                                        if st.session_state.filter_state.get(column) is not None else 0)
#
#             if filter_type != "All":
#                 st.session_state.filter_state[column] = filter_type
#             else:
#                 st.session_state.filter_state[column] = None
#
#         # Apply filters to DataFrame
#         filtered_df = df.copy()
#         for column, value in st.session_state.filter_state.items():
#             if value is not None:
#                 filtered_df = filtered_df[filtered_df[column] == value]
#
#         # Display filtered data in DataFrame
#         st.dataframe(filtered_df)
#
#
# if __name__ == "__main__":
#     main()

# import snowflake.connector
# import streamlit as st
# import pandas as pd
#
#
# @st.cache_data(ttl=None)  # Cache data until app is refreshed
# def fetch_tables_from_snowflake(_snowflake_config):
#     # Connect to Snowflake
#     conn = snowflake.connector.connect(
#         user=_snowflake_config["user"],
#         password=_snowflake_config["password"],
#         account=_snowflake_config["account"],
#         warehouse=_snowflake_config["warehouse"],
#         database=_snowflake_config["database"],
#         schema=_snowflake_config["schema"],
#     )
#
#     # Retrieve table names
#     query = "SHOW TABLES"
#     cursor = conn.cursor()
#     cursor.execute(query)
#
#     # Fetch table names
#     tables = [table[1] for table in cursor.fetchall()]
#
#     # Close connection
#     conn.close()
#
#     return tables
#
#
# @st.cache_data(ttl=None)  # Cache data until app is refreshed
# def fetch_data_from_snowflake(_snowflake_config, table_name):
#     # Connect to Snowflake
#     conn = snowflake.connector.connect(
#         user=_snowflake_config["user"],
#         password=_snowflake_config["password"],
#         account=_snowflake_config["account"],
#         warehouse=_snowflake_config["warehouse"],
#         database=_snowflake_config["database"],
#         schema=_snowflake_config["schema"],
#     )
#
#     # Execute query to fetch data
#     query = f"SELECT * FROM {table_name}"
#     cursor = conn.cursor()
#     cursor.execute(query)
#
#     # Retrieve column names
#     column_names = [desc[0] for desc in cursor.description]
#
#     # Retrieve rows
#     rows = cursor.fetchall()
#
#     # Close connection
#     conn.close()
#
#     # Create DataFrame
#     df = pd.DataFrame(rows, columns=column_names)
#     return df
#
#
# # Streamlit app
# def main():
#     st.title("Data Viewer")
#
#     # Retrieve Snowflake connection details from secrets.toml
#     snowflake_config = st.secrets.connections.snowpark
#
#     # Fetch all table names
#     tables = fetch_tables_from_snowflake(snowflake_config)
#
#     # Initialize session state
#     if "filter_state" not in st.session_state:
#         st.session_state.filter_state = {}
#
#     # Dropdown menu to select table
#     table_name = st.selectbox("Select Table", tables)
#
#     # Fetch and display data when the button is clicked
#     if st.button("Fetch Data"):
#         df = fetch_data_from_snowflake(snowflake_config, table_name)
#
#         # Display filters for each column
#         for column in df.columns:
#             unique_values = df[column].unique().tolist()
#             options = unique_values.copy()
#             if len(unique_values) > 1:
#                 options.insert(0, "All")
#
#             filter_type = st.selectbox(f"Filter {column}", options,
#                                        index=options.index(st.session_state.filter_state.get(column))
#                                        if st.session_state.filter_state.get(column) is not None else 0)
#
#             if filter_type != "All":
#                 st.session_state.filter_state[column] = filter_type
#             else:
#                 st.session_state.filter_state.pop(column, None)
#
#         # Apply filters to DataFrame
#         filtered_df = df.copy()
#         for column, value in st.session_state.filter_state.items():
#             if value is not None:
#                 filtered_df = filtered_df[filtered_df[column] == value]
#
#         # Display filtered data in DataFrame
#         st.dataframe(filtered_df)
#
#
# if __name__ == "__main__":
#     main()

import snowflake.connector
import streamlit as st
import pandas as pd


@st.cache_data(ttl=None)  # Cache data until app is refreshed
def fetch_tables_from_snowflake(_snowflake_config):
    # Connect to Snowflake
    conn = snowflake.connector.connect(
        user=_snowflake_config["user"],
        password=_snowflake_config["password"],
        account=_snowflake_config["account"],
        warehouse=_snowflake_config["warehouse"],
        database=_snowflake_config["database"],
        schema=_snowflake_config["schema"],
    )

    # Retrieve table names
    query = "SHOW TABLES"
    cursor = conn.cursor()
    cursor.execute(query)

    # Fetch table names
    tables = [table[1] for table in cursor.fetchall()]

    # Close connection
    conn.close()

    return tables


@st.cache_data(ttl=None)  # Cache data until app is refreshed
def fetch_data_from_snowflake(_snowflake_config, table_name):
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
    query = f"SELECT * FROM {table_name}"
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


# Streamlit app
def main():
    st.title("Data Viewer")

    # Retrieve Snowflake connection details from secrets.toml
    snowflake_config = st.secrets.connections.snowpark

    # Fetch all table names
    tables = fetch_tables_from_snowflake(snowflake_config)

    # Initialize session state
    if "filter_state" not in st.session_state:
        st.session_state.filter_state = {}
        st.session_state.df = None

    # Dropdown menu to select table
    table_name = st.selectbox("Select Table", tables)

    # Fetch and display data when the button is clicked
    if st.button("Fetch Data"):
        df = fetch_data_from_snowflake(snowflake_config, table_name)

        # Store DataFrame in Session State
        st.session_state.df = df

        # Display filters for each column
        for column in df.columns:
            unique_values = df[column].unique().tolist()
            options = unique_values.copy()
            if len(unique_values) > 1:
                options.insert(0, "All")

            filter_type = st.selectbox(f"Filter {column}", options,
                                       index=options.index(st.session_state.filter_state.get(column))
                                       if st.session_state.filter_state.get(column) is not None else 0)

            if filter_type != "All":
                st.session_state.filter_state[column] = filter_type
            else:
                st.session_state.filter_state.pop(column, None)

        # Apply filters to DataFrame
        filtered_df = df.copy()
        for column, value in st.session_state.filter_state.items():
            if value is not None:
                filtered_df = filtered_df[filtered_df[column] == value]

        # Display filtered data in DataFrame
        st.dataframe(filtered_df)


if __name__ == "__main__":
    main()
