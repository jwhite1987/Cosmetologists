import flask
from google.cloud import bigquery
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'credentials.json'

app = flask.Flask(__name__)

@app.route("/")
def index():
    client = bigquery.Client()
    query_job = client.query(
        """
        SELECT
        *
        FROM
        cosm-project.cosm_dataset.charlotte_data
        """
    )

    return flask.render_template('index.html', results=query_job.result())

@app.route("/ft_mill")
def ft_mill():
    return flask.render_template('ft_mill.html')

@app.route("/huntersville")
def huntersville():
    return flask.render_template('huntersville.html')

@app.route("/matthews")
def matthews():
    return flask.render_template('matthews.html')

if __name__ == "__main__":
    app.run(debug=True)
