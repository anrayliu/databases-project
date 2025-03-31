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

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        try:
            cur.execute("select customer_name from customer where customer_name = '{}';".format(username))
            database_username = cur.fetchone()

            if ((database_username is not None) and (username == str(database_username[0]))):
                cur.execute("select password from customer where customer_name = '{}'".format(username))
                database_password = cur.fetchone()

                if ((database_username is not None) and (password == str(database_password[0]))):
                    return redirect("/home")
                else:
                    return redirect("/login")
            else:
                return redirect("/login")

        except psycopg2.Error:
            conn.rollback()
            return "something went seriously wrong"

    return render_template("login.html")

@app.route("/home", methods=["POST", "GET"])
def customer_view():
    if request.method == "GET":
        try:
            cur.execute("select * from hotel_chain")
            hotel_chains = cur.fetchall()
            cur.execute("select * from hotel")
            hotels = cur.fetchall()
        except psycopg2.Error:
            conn.rollback()
            return "something went seriously wrong"

        return render_template("customer_view.html", hotels=hotels, hotel_chains=hotel_chains)
    else:
        return render_template("customer_view.html")

@app.route("/register", methods=["POST", "GET"])
def register():
    return render_template("register.html")

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
			cur.execute("select * from hotel")
			hotels = cur.fetchall()
		except psycopg2.Error:
			conn.rollback()
			return "something went seriously wrong"

		return render_template("index.html", hotels=hotels, hotel_chains=hotel_chains)


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


@app.route("/results")
def show_results():

	start = request.args.get("start_date")
	end = request.args.get("end_date")
	capacity = request.args.get("capacity")
	total = request.args.get("total_capacity")
	chain = request.args.get("chain")
	loc = request.args.get("location")
	price = request.args.get("price")


	try:
		if (int(request.args.get("capacity")) < 1 or int(request.args.get("capacity")) > 9):
			conn.rollback()
			return "The minimum capacity for a room is 1 and the maximum capacity for a room is 9."

		if (int(request.args.get("price")) < 0):
			conn.rollback()
			return "Please enter a positive value under price."

		print('''
					select * from room join hotel on room.chain_name=hotel.chain_name and room.chain_name='{}'
						and hotel.num_rooms={} and room.capacity={} and hotel.hotel_address='{}' and room.price<{};				
					'''.format(chain, total, capacity, loc, price))
		cur.execute('''
					select * from room join hotel on room.chain_name=hotel.chain_name where room.chain_name='{}'
						and num_rooms={} and capacity={} and room.hotel_address='{}' and price<={};				
					'''.format(chain, total, capacity, loc, price))
		res = cur.fetchall()

	except psycopg2.Error as e:
		print(e)
		conn.rollback()
		return "something went seriously wrong"

	return render_template("results.html", results=res)


if __name__ == "__main__":
	with get_db_conn() as conn:
		with conn.cursor() as cur:
			app.run(debug=True)
