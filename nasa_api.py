import requests
import pandas as pd
import sqlalchemy as db

# Get NASA API data
API_KEY = "M3CCsNeHMKXdjJjzrkhwfx0SEsAEOR5MCe686jvp"

url = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"

response = requests.get(url)


print(response.status_code)
print(response.text)

data = response.json()

print(response.status_code)


# Convert dictionary into pandas dataframe
df = pd.DataFrame.from_dict([data])

print(df)


# Import SQLAlchemy and create database engine
engine = db.create_engine('sqlite:///nasa.db')


# Send dataframe to SQL table
df.to_sql('apod', con=engine, if_exists='replace', index=False)


# Query database and print results
with engine.connect() as connection:
    query_result = connection.execute(
        db.text("SELECT * FROM apod;")
    ).fetchall()

    print(pd.DataFrame(query_result))