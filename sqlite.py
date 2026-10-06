import sqlite3
from pathlib import Path

dbName = "cookies.sqlite"

users = Path(r"C:\Users")

for user in users.iterdir():
    profiles = (
        user
        / "AppData"
        / "Roaming"
        / "Mozilla"
        / "Firefox"
        / "Profiles"
    )
    
    if not profiles.is_dir():
        continue


    for profile in profiles.iterdir():
        dbPath = profile / dbName

        if dbPath.is_file():
            print(f"Found: {dbPath}")
        else:
            continue
        
        #https://docs.python.org/3/library/sqlite3.html#sqlite3-tutorial
        #https://www.w3schools.com/python/ref_module_sqlite3.asp
        
        con = sqlite3.connect(dbPath)
        cur = con.cursor()
        cur.execute("SELECT host, name, value FROM 'moz_cookies'")
        rows = cur.fetchall()
        
        
        for host, name, value in rows:
            print(f"Host: {host}, Cookie Name: {name} Cookie Value: {value}\n")
        
        con.close()