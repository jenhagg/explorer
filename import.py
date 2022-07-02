import fs
import pandas as pd
import sqlite3
from pathlib import Path

root = Path.cwd() / "data"
ofs = fs.open_fs(str(root))

conn = sqlite3.connect("tamu.db")


def iter_df():
    for csv in ofs.walk.files():
        table = csv.strip("/").split(".")[0]
        with ofs.open(csv) as f:
            df = pd.read_csv(f)
            yield df, table


def create_db():
    for df, table in iter_df():
        df.to_sql(table, conn, if_exists="replace", index=False)


def columns():
    return {table: df.columns for df, table in iter_df()}


if __name__ == "__main__":
    create_db()
