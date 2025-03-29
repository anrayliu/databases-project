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
		try:
			cur.execute("insert into hotel_chain values('{}', {});".format(request.form["chain_name"], request.form["num_hotels"]))
			conn.commit()
		except psycopg2.Error:
			conn.rollback()

		return redirect("/")

	else:
		try:
			cur.execute("select * from hotel_chain")
			hotel_chains = cur.fetchall()
		except psycopg2.Error:
			conn.rollback()
			return "something went seriously wrong"

		return render_template("index.html", hotel_chains=hotel_chains)


@app.route("/delete/<string:id>")
def delete(id):
	try:
		cur.execute("delete from hotel_chain where chain_name = '{}'".format(id))
	except psycopg2.Error:
		conn.rollback()

	return redirect("/")


@app.route("/edit/<string:id>", methods=["GET", "POST"])
def edit(id):
	if request.method == "POST":
		try:
			cur.execute("update hotel_chain set chain_name='{}', num_hotels='{}' where chain_name='{}'".format(request.form["chain_name"], request.form["num_hotels"], id))
		except psycopg2.Error:
			conn.rollback()

		return redirect("/")
	else:
		try:
			cur.execute("select * from hotel_chain where chain_name='{}'".format(id))
			chain = cur.fetchone()
		except psycopg2.Error:
			conn.rollback()
			return "something went seriously wrong"

		return render_template("edit.html", chain=chain)



if __name__ == "__main__":
	with get_db_conn() as conn:
		with conn.cursor() as cur:
			app.run(debug=True)