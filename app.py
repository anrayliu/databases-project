import os
import psycopg2
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

def get_db_conn():
	conn = psycopg2.connect(database="defaultdb",
							host="pg-147bd20e-databases-project.h.aivencloud.com",
							port="17637",
							user=os.environ["DB_USERNAME"],
							password=os.environ["DB_PASSWORD"])
	return conn

@app.route("/", methods=["POST", "GET"])
def index():
	if request.method == "POST":
		conn = get_db_conn()
		cur = conn.cursor()
		cur.execute(f"insert into public.hotel_chain values('{request.form["chain_name"]}', {request.form["num_hotels"]});")
		conn.commit()
		cur.close()
		conn.close()
		return redirect("/")

	else:
		conn = get_db_conn()
		cur = conn.cursor()
		cur.execute("select * from public.hotel_chain")
		hotel_chains = cur.fetchall()
		cur.close()
		conn.close()

		return render_template("index.html", hotel_chains=hotel_chains)


if __name__ == "__main__":
	app.run()