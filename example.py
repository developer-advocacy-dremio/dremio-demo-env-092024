from dremio_simple_query.connect import get_token, DremioConnection
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


## URL to Login Endpoint
login_endpoint = "http://dremio:9047/apiv2/login"

## Payload for Login
payload = {
    "userName": "alexmerced",
    "password": "Dremio2024"
}

## Get token from API
token = get_token(uri = login_endpoint, payload=payload)

## URL Dremio Software Flight Endpoint
arrow_endpoint="grpc://dremio:32010"

## Establish Client
dremio = DremioConnection(token, arrow_endpoint)

## Query Dremio
df = dremio.toPandas("""
SELECT * FROM "@alexmerced".weather
""")

print(df)

## Query Dremio
df2 = dremio.toPandas("""
SELECT * FROM "@alexmerced"."final_order_data";
""")

print(df)

# Convert the 'date' column to datetime if it's not already in that format
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Set up the matplotlib figure
plt.figure(figsize=(12, 6))

# Plotting tempmax and tempmin over time using seaborn
sns.lineplot(x='date', y='tempmax', data=df, label='Max Temperature')
sns.lineplot(x='date', y='tempmin', data=df, label='Min Temperature')

# Customize the plot
plt.title('Temperature Trends in NY City Central Park (2009-2019)')
plt.xlabel('Date')
plt.ylabel('Temperature (°F)')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

# Show the plot
plt.show()