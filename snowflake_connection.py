import snowflake.connector
import pandas as pd

def fetch_data_from_snowflake(_snowflake_config, query):
    """
    Fetch data from Snowflake using the provided configuration and query.

    Args:
        snowflake_config (dict): A dictionary containing the Snowflake connection information.
        query (str): The SQL query to execute.

    Returns:
        pandas.DataFrame: The result of the query as a DataFrame.
    """
    # Connect to Snowflake
    conn = snowflake.connector.connect(
        user=_snowflake_config["user"],
        password=_snowflake_config["password"],
        account=_snowflake_config["account"],
        database=_snowflake_config["database"],
        schema=_snowflake_config["schema"],
        warehouse=_snowflake_config["warehouse"],
    )

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