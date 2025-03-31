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
            database_customer_username = cur.fetchone()

            if ((database_customer_username is not None) and (username == str(database_customer_username[0]))):
                cur.execute("select password from customer where customer_name = '{}'".format(username))
                database_customer_password = cur.fetchone()

                if ((database_customer_username is not None) and (password == str(database_customer_password[0]))):
                    return redirect("/home")
                else:
                    return redirect("/login")
            else:
                cur.execute("select employee_name from employee where employee_name = '{}';".format(username))
                database_employee_username = cur.fetchone()

                if((database_employee_username is not None) and (username == str(database_employee_username[0]))):

                    cur.execute("select password from employee where employee_name = '{}';".format(username))

                    database_employee_password = cur.fetchone()

                    if ((database_employee_password is not None) and (password == str(database_employee_password[0]))):
                    
                        return redirect("/employee")
                    else:
                        return redirect("/login")
                else:
                    return redirect("/login")
 
                return redirect("/login")

        except psycopg2.Error:
            conn.rollback()
            return "something went seriously wrong"

    return render_template("login.html")

@app.route("/home", methods=["POST", "GET"])
def customer_view():
    if request.method == "POST":
        try:
            cur.execute("insert into hotel_chain values('{}', {});".format(request.form["chain_name"], request.form["num_hotels"]))
            conn.commit()
        except psycopg2.Error:
            conn.rollback()
            return "something went seriously wrong"

        return redirect("/home")
    else:
        try:
            cur.execute("select * from hotel_chain")
            hotel_chains = cur.fetchall()
            cur.execute("select * from hotel")
            hotels = cur.fetchall()
        except psycopg2.Error:
            conn.rollback()
            return "something went seriously wrong"

        return render_template("customer_view.html", hotels=hotels, hotel_chains=hotel_chains)

@app.route("/employee", methods=["POST", "GET"])
def employee_view():
    if request.method == "POST":
        booking_entrie = request.form["customer_id"]

        try:
            cur.execute("select booking_id from booking where customer_id = '{}'".format(request.form["customer_id"]))
            booking_id = cur.fetchone()

            if ((booking_id is not None) and (request.form["booking_id"] == str(booking_id[0]))):
                print("GOT HERE")
            else:
                return redirect("/employee")
        except psycopg2.Error:
            conn.rollback()
            return "something went seriously wrong"

    return render_template("employee_view.html")

@app.route("/register", methods=["POST", "GET"])
def register():
    return render_template("register.html")

@app.route("/", methods=["POST", "GET"])
def index():
    return redirect("/login")
'''    
    if request.method == "POST":
        try:
            cur.execute("insert into hotel_chain values('{}', {});".format(request.form["chain_name"], request.form["num_hotels"]))
            conn.commit()
        except psycopg2.Error:
            conn.rollback()
            return "something went seriously wrong"

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
'''

@app.route("/deletechain/<string:id>")
def delete_chain(id):
	try:
		cur.execute("delete from hotel_chain where chain_name = '{}';".format(id))
	except psycopg2.Error as e:
		print(e)
		conn.rollback()

	return redirect("/")

@app.route("/deleteroom/<int:id>")
def delete_room(id):
	try:
		cur.execute("delete from room where room_id = {};".format(id))
	except psycopg2.Error as e:
		print(e)
		conn.rollback()

	return redirect("/")

@app.route("/editroom/<int:id>", methods=["GET", "POST"])
def edit_room(id):
	if request.method == "POST":
		try:
			cur.execute("update room set expandable='{}', price={}, capacity={}, view='{}' where room_id={}".format("false" if request.form["expandable"] is None else request.form["expandable"], request.form["price"], request.form["capacity"], request.form["view"], id))
		except:
			conn.rollback()

		return redirect("/")
	else:
		try:
			cur.execute("select * from room where room_id={}".format(id))
			room = cur.fetchone()
		except psycopg2.Error:
			conn.rollback()
			return "something went seriously wrong"

		return render_template("edit_room.html", room=room)

@app.route("/editchain/<string:id>", methods=["GET", "POST"])
def edit_chain(id):
	if request.method == "POST":
		try:
			cur.execute("update hotel_chain set num_hotels={} where chain_name='{}'".format(request.form["num_hotels"], id))
		except psycopg2.Error as e:
			print("something went seriously wrong")
			print(e)

			conn.rollback()

		return redirect("/")
	else:
		try:
			cur.execute("select * from hotel_chain where chain_name='{}'".format(id))
			chain = cur.fetchone()
		except psycopg2.Error:
			conn.rollback()
			return "something went seriously wrong"

		return render_template("edit_chain.html", chain=chain)


@app.route("/results-customer")
def show_results_customer():

	start = request.args.get("start_date")
	end = request.args.get("end_date")
	capacity = request.args.get("capacity")
	total = request.args.get("total_capacity")
	chain = request.args.get("chain")
	loc = request.args.get("location")
	price = request.args.get("price")
	view = request.args.get("view")
	expandable = request.args.get("expandable")

	try:
		if (int(request.args.get("capacity")) < 1 or int(request.args.get("capacity")) > 9):
			return "The minimum capacity for a room is 1 and the maximum capacity for a room is 9."

		if (int(request.args.get("price")) < 0):
			return "Please enter a positive value under price."

		q = '''
					select * from room natural join hotel where room.chain_name=hotel.chain_name and room.chain_name='{}'
						and capacity={} and room.hotel_address='{}' and price<={} and view='{}' and expandable='{}';				
					'''.format(chain, capacity, loc, price, view, "false" if expandable is None else expandable)

		cur.execute(q) 
		print(q)

		res = cur.fetchall()

		print(res)

	except psycopg2.Error as e:
		print(e)
		conn.rollback()
		return "something went seriously wrong"

	return render_template("results_customer.html", results=res)

@app.route("/book", methods=["POST"])
def book():
	room_id = request.args.get("room_id")

	# add query here to make a new booking

	return render_template("done_booking.html")


@app.route("/results-employee")
def show_results_employee():

	start = request.args.get("start_date")
	end = request.args.get("end_date")
	capacity = request.args.get("capacity")
	total = request.args.get("total_capacity")
	chain = request.args.get("chain")
	loc = request.args.get("location")
	price = request.args.get("price")
	view = request.args.get("view")
	expandable = request.args.get("expandable")

	try:
		if (int(request.args.get("capacity")) < 1 or int(request.args.get("capacity")) > 9):
			return "The minimum capacity for a room is 1 and the maximum capacity for a room is 9."

		if (int(request.args.get("price")) < 0):
			return "Please enter a positive value under price."

		q = '''
					select * from room natural join hotel where room.chain_name=hotel.chain_name and room.chain_name='{}'
						and capacity={} and room.hotel_address='{}' and price<={} and view='{}' and expandable='{}';				
					'''.format(chain, capacity, loc, price, view, "false" if expandable is None else expandable)

		cur.execute(q) 
		print(q)

		res = cur.fetchall()

		print(res)

	except psycopg2.Error as e:
		print(e)
		conn.rollback()
		return "something went seriously wrong"

	return render_template("results_customer.html", results=res)



if __name__ == "__main__":
	with get_db_conn() as conn:
		with conn.cursor() as cur:
			app.run(debug=True)
