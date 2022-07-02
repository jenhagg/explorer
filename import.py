import fs
import pandas as pd
import sqlite3
from pathlib import Path

root = Path.cwd() / "data"
print(root)
ofs = fs.open_fs(str(root))

conn = sqlite3.connect("tamu.db")


def create_db():
    for csv in ofs.walk.files():
        table = csv.strip("/").split(".")[0]
        with ofs.open(csv) as f:
            df = pd.read_csv(f)
            df.to_sql(table, conn, if_exists="replace", index=False)


def columns():
    cols = {}
    for csv in ofs.walk.files():
        table = csv.strip("/").split(".")[0]
        with ofs.open(csv) as f:
            df = pd.read_csv(f)
            cols[table] = df.columns
    return cols
