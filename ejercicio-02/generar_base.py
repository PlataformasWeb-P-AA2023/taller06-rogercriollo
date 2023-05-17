from sqlalchemy import create_engine

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine('sqlite:///paises.db')

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


from sqlalchemy import Column, Integer, String


class Country(Base):
    __tablename__ = 'Countries'
    
    geoname_id = Column(Integer, primary_key=True)
    name = Column(String(500))
    capital = Column(String(500))
    continent = Column(String(500))
    dial = Column(String(500))
    itu = Column(String(500))
    languages = Column(String(500))
    is_independent = Column(String(500))

    def _repr_(self):
        return "País: geoname_id=%s name=%s capital:%s continent=%s dial:%s itu:%s languages:%s is_independent:%s" % (
                          self.geoname_id,
                          self.name,
                          self.capital,
                          self.continent,
                          self.dial,
                          self.itu,
                          self.languages,
                          self.is_independent)


Base.metadata.create_all(engine)
    





