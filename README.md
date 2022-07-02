# explorer

## setup

Initial setup

```bash
git clone https://github.com/jenhagg/explorer.git
cd explorer
mkdir data
cp -r ../PowerSimData/powersimdata/network/usa_tamu/data data/
```

The import the csv files into a sqlite database (it will be called `tamu.db` by default)
```bash
python -m venv .env
source .env/bin/activate
pip install -r requirements.txt
python import.py
```

Now run the following to start the datasette server and navigate to localhost with the
given port (mine is `localhost:8001`)

```bash
datasette tamu.db
```
