import csv
import psycopg2

conn = psycopg2.connect("host=localhost dbname=zno_db user=postgres password = pgAdmin port=5432")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS Odata;")
query1='''
CREATE TABLE Odata(
        OUTID  TEXT,
        Birth  VARCHAR,
        SEXTYPENAME  TEXT,
        REGNAME  TEXT,
        AREANAME  TEXT,
        TERNAME  TEXT,
        REGTYPENAME  TEXT,
        TerTypeName  TEXT,
        ClassProfileNAME  TEXT,
        ClassLangName  TEXT,
        EONAME  TEXT,
        EOTYPENAME  TEXT,
        EORegName  TEXT,
        EOAreaName  TEXT,
        EOTerName  TEXT,
        EOParent  TEXT,
        UkrTest  TEXT,
        UkrTestStatus  TEXT,
        UkrBall100  TEXT,
        UkrBall12  TEXT,
        UkrBall  TEXT,
        UkrAdaptScale  VARCHAR,
        UkrPTName  TEXT,
        UkrPTRegName  TEXT,
        UkrPTAreaName  TEXT,
        UkrPTTerName  TEXT,
        histTest  TEXT,
        HistLang  TEXT,
        histTestStatus  TEXT,
        histBall100  TEXT,
        histBall12  TEXT,
        histBall  TEXT,
        histPTName  TEXT,
        histPTRegName  TEXT,
        histPTAreaName  TEXT,
        histPTTerName  TEXT,
        mathTest  TEXT,
        mathLang  TEXT,
        mathTestStatus  TEXT,
        mathBall100  TEXT,
        mathBall12  TEXT,
        mathBall  TEXT,
        mathPTName  TEXT,
        mathPTRegName  TEXT,
        mathPTAreaName  TEXT,
        mathPTTerName  TEXT,
        physTest  TEXT,
        physLang  TEXT,
        physTestStatus  TEXT,
        physBall100  TEXT,
        physBall12  TEXT,
        physBall  TEXT,
        physPTName  TEXT,
        physPTRegName  TEXT,
        physPTAreaName  TEXT,
        physPTTerName  TEXT,
        chemTest  TEXT,
        chemLang  TEXT,
        chemTestStatus  TEXT,
        chemBall100  TEXT,
        chemBall12  TEXT,
        chemBall  TEXT,
        chemPTName  TEXT,
        chemPTRegName  TEXT,
        chemPTAreaName  TEXT,
        chemPTTerName  TEXT,
        bioTest  TEXT,
        bioLang  TEXT,
        bioTestStatus  TEXT,
        bioBall100  TEXT,
        bioBall12  TEXT,
        bioBall  TEXT,
        bioPTName  TEXT,
        bioPTRegName  TEXT,
        bioPTAreaName  TEXT,
        bioPTTerName  TEXT,
        geoTest  TEXT,
        geoLang  TEXT,
        geoTestStatus  TEXT,
        geoBall100  TEXT,
        geoBall12  TEXT,
        geoBall  TEXT,
        geoPTName  TEXT,
        geoPTRegName  TEXT,
        geoPTAreaName  TEXT,
        geoPTTerName  TEXT,
        engTest  TEXT,
        engTestStatus  TEXT,
        engBall100  TEXT,
        engBall12  TEXT,
        engDPALevel  TEXT,
        engBall  TEXT,
        engPTName  TEXT,
        engPTRegName  TEXT,
        engPTAreaName  TEXT,
        engPTTerName  TEXT,
        fraTest  TEXT,
        fraTestStatus  TEXT,
        fraBall100  TEXT,
        fraBall12  TEXT,
        fraDPALevel  TEXT,
        fraBall  TEXT,
        fraPTName  TEXT,
        fraPTRegName  TEXT,
        fraPTAreaName  TEXT,
        fraPTTerName  TEXT,
        deuTest  TEXT,
        deuTestStatus  TEXT,
        deuBall100  TEXT,
        deuBall12  TEXT,
        deuDPALevel  TEXT,
        deuBall  TEXT,
        deuPTName  TEXT,
        deuPTRegName  TEXT,
        deuPTAreaName  TEXT,
        deuPTTerName  TEXT,
        spaTest  TEXT,
        spaTestStatus  TEXT,
        spaBall100  TEXT,
        spaBall12  TEXT,
        spaDPALevel  TEXT,
        spaBall  TEXT,
        spaPTName  TEXT,
        spaPTRegName  TEXT,
        spaPTAreaName  TEXT,
        spaPTTerName  TEXT,
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
