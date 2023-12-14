from flask import Flask
from datetime import datetime

import os
import pandas as pd

app = Flask(__name__)

df = pd.read_csv('exchange_rate.csv', \
    header=0, index_col=0, parse_dates=['date'], date_parser=lambda x: datetime.strptime(x, '%Y-%m-%d'))


@app.route('/')
def index():
    return df.to_json(date_format='iso')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))