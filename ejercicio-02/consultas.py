from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and 

# se importa la clase(s) del
# archivo genera_tablas
from generar_base  import Country, engine


Session = sessionmaker(bind=engine)
session = Session()


##Realizar la siguientes consultas, usar archivos separados para cada consulta.:

## Presentar todos los países del continente americano
##Presentar los países de Asía, ordenados por el atributo Dial.
##Presentar los lenguajes de cada país.
##Presentar los países ordenados por la capital, siempre que el país pertenezca a Europa
##Presentar todos los países que tengan en su cadena de nombre de país "uador" o en su cadena de capital "ito".*/


#1

countries = session.query(Country).filter(Country.continent=="AM" or Country.continent=="AS" or Country.continent=="NA" ).all()

for x in countries:
    print("%s" % (x))
    print("------")











# 2


countries = session.query(Country).filter(Country.continent=="AS" ).order_by(Country.dial).all()



for x in countries:
    print("%s" % (x))
    print("------")

# 3

countries = session.query(Country).all()
for x in countries:

    print(f"país: {x.name}  lenguajes: {x.languages}")

# 4

countries = session.query(Country).filter(Country.continent=="EU" ).order_by(Country.capital).all()


for x in countries:
    print("%s" % (x))
    print("------")


# 5

    


countries = session.query(Country).filter(or_(Country.name.like("%uador%"), Country.capital.like("%ito"))).all()


for x in countries:
    print("%s" % (x))
    print("------")