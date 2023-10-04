import snowflake.connector
import pandas as pd
from snowflake_secrets import SNOWFLAKE_CONFIG

def fetch_data_from_snowflake(snowflake_config, query):
    """
    Fetch data from Snowflake using the provided configuration and query.

    Args:
        snowflake_config (dict): A dictionary containing the Snowflake connection information.
        query (str): The SQL query to execute.

    Returns:
        pandas.DataFrame: The result of the query as a DataFrame.
    """
    # Connect to Snowflake
    conn = snowflake.connector.connect(**SNOWFLAKE_CONFIG)


    # Execute query and fetch results
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()

    # Convert results to DataFrame
    columns = [col[0] for col in cursor.description]
    df = pd.DataFrame(data, columns=columns)

    # Close connection
    conn.close()

    return df