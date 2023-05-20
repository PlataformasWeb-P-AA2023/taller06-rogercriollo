import requests

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from generar_base   import Country,engine

Session = sessionmaker(bind=engine)
session = Session()

x = requests.get('https://pkgstore.datahub.io/core/country-codes/country-codes_json/data/616b1fb83cbfd4eb6d9e7d52924bb00a/country-codes_json.json')

# print(x.json())

print("testing " , x.json()[0]["CLDR display name"])

for c in x.json():
    newd = Country( 
        

        geoname_id = c["Geoname ID"],
        name =  c["CLDR display name"],
        capital =  c["Capital"],
        continent = c["Continent"],
        dial = c["Dial"],
        itu =  c["ITU"],
        languages =  c["Languages"],
        is_independent =  c["is_independent"]

    )
    print()
    session.add(newd)

    print(newd.name)

session.commit()