import csv
import psycopg2

conn = psycopg2.connect("host=localhost dbname=zno_db user=postgres password = pgAdmin port=5432")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS Odata;")
query1='''
CREATE TABLE Odata(
        OUTID  TEXT,
       Birth real,
        SEXTYPENAME VARCHAR(128),
        REGNAME VARCHAR(128),
        AREANAME VARCHAR(128),
        TERNAME VARCHAR(128),
        REGTYPENAME VARCHAR(128),
        TerTypeName VARCHAR(128),
        ClassProfileNAME VARCHAR(128),
        ClassLangName VARCHAR(128),
        EONAME TEXT,
        EOTYPENAME VARCHAR(128),
        EORegName VARCHAR(128),
        EOAreaName VARCHAR(128),
        EOTerName VARCHAR(128),
        EOParent TEXT,
        UkrTest VARCHAR(128),
        UkrTestStatus VARCHAR(128),
        UkrBall100 real,
        UkrBall12 real,
        UkrBall real,
        UkrAdaptScale VARCHAR(128),
        UkrPTName TEXT,
        UkrPTRegName VARCHAR(128),
        UkrPTAreaName VARCHAR(128),
        UkrPTTerName VARCHAR(128),
        histTest VARCHAR(128),
        HistLang VARCHAR(128),
        histTestStatus VARCHAR(128),
        histBall100 real,
        histBall12 real,
        histBall real,
        histPTName TEXT,
        histPTRegName VARCHAR(128),
        histPTAreaName VARCHAR(128),
        histPTTerName VARCHAR(128),
        mathTest VARCHAR(128),
        mathLang VARCHAR(128),
        mathTestStatus VARCHAR(128),
        mathBall100 real,
        mathBall12 real,
        mathBall real,
        mathPTName TEXT,
        mathPTRegName VARCHAR(128),
        mathPTAreaName VARCHAR(128),
        mathPTTerName VARCHAR(128),
        physTest VARCHAR(128),
        physLang VARCHAR(128),
        physTestStatus VARCHAR(128),
        physBall100 real,
        physBall12 real,
        physBall real,
        physPTName TEXT,
        physPTRegName VARCHAR(128),
        physPTAreaName VARCHAR(128),
        physPTTerName VARCHAR(128),
        chemTest VARCHAR(128),
        chemLang VARCHAR(128),
        chemTestStatus VARCHAR(128),
        chemBall100 real,
        chemBall12 real,
        chemBall real,
        chemPTName TEXT,
        chemPTRegName VARCHAR(128),
        chemPTAreaName VARCHAR(128),
        chemPTTerName VARCHAR(128),
        bioTest VARCHAR(128),
        bioLang VARCHAR(128),
        bioTestStatus VARCHAR(128),
        bioBall100 real,
        bioBall12 real,
        bioBall real,
        bioPTName TEXT,
        bioPTRegName VARCHAR(128),
        bioPTAreaName VARCHAR(128),
        bioPTTerName VARCHAR(128),
        geoTest VARCHAR(128),
        geoLang VARCHAR(128),
        geoTestStatus VARCHAR(128),
        geoBall100 real,
        geoBall12 real,
        geoBall real,
        geoPTName TEXT,
        geoPTRegName VARCHAR(128),
        geoPTAreaName VARCHAR(128),
        geoPTTerName VARCHAR(128),
        engTest VARCHAR(128),
        engTestStatus VARCHAR(128),
        engBall100 real,
        engBall12 real,
        engDPALevel VARCHAR(128),
        engBall real,
        engPTName TEXT,
        engPTRegName VARCHAR(128),
        engPTAreaName VARCHAR(128),
        engPTTerName VARCHAR(128),
        fraTest VARCHAR(128),
        fraTestStatus VARCHAR(128),
        fraBall100 real,
        fraBall12 real,
        fraDPALevel VARCHAR(128),
        fraBall real,
        fraPTName TEXT,
        fraPTRegName VARCHAR(128),
        fraPTAreaName VARCHAR(128),
        fraPTTerName VARCHAR(128),
        deuTest VARCHAR(128),
        deuTestStatus VARCHAR(128),
        deuBall100 real,
        deuBall12 real,
        deuDPALevel VARCHAR(128),
        deuBall real,
        deuPTName TEXT,
        deuPTRegName VARCHAR(128),
        deuPTAreaName VARCHAR(128),
        deuPTTerName VARCHAR(128),
        spaTest VARCHAR(128),
        spaTestStatus VARCHAR(128),
        spaBall100 real,
        spaBall12 real,
        spaDPALevel VARCHAR(128),
        spaBall real,
        spaPTName TEXT,
        spaPTRegName VARCHAR(128),
        spaPTAreaName VARCHAR(128),
        spaPTTerName VARCHAR(128),
        YEAR  VARCHAR,
        PRIMARY KEY (OUTID)
);
'''
cur.execute(query1)

query2 = ''' 
SELECT REGNAME, min(physball100), YEAR
FROM Odata
WHERE physTestStatus='Зараховано'
GROUP BY REGNAME, YEAR;
'''
cur.execute(query2)

with open('zno.csv', 'w', encoding="utf-8") as result:
    writer = csv.writer(result)
    writer.writerow(['Область', 'Мінімальний бал', 'Рік'])
    row = cur.fetchone()
    while row:
        writer.writerow(row)
        row = cur.fetchone()

conn.commit()
cur.close()
conn.close()
