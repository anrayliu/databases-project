from app import get_db_conn


conn = get_db_conn()

cur = conn.cursor()

cur.execute('set search_path to "public";')

cur.execute("drop table if exists hotel_chain;")

cur.execute('''create table hotel_chain (
                    chain_name varchar(30),
                    num_hotels int,
                    primary key(chain_name)
                );
            ''')

cur.execute('''
insert into hotel_chain values('Ottawa Hotels', 5);
insert into hotel_chain values('Bob Hotels', 100);
insert into hotel_chain values('123 hotel w me', 1000);
insert into hotel_chain values('im baked hotels', 1);
''')

cur.execute("drop table if exists chain_addresses;")

cur.execute('''create table chain_addresses (
                    chain_name varchar(30),
                    central_address varchar(30)
                );
            ''')

cur.execute('''
insert into chain_addresses values('Ottawa Hotels', '239 Rideau Street');
insert into chain_addresses values('Bob Hotels', '35 Elgin Street');
insert into chain_addresses values('123 hotel w me', '555 Dundurn Avenue');
insert into chain_addresses values('im baked hotels', '53 Sandy Hill Street');
''')

cur.execute("drop table if exists chain_emails;")

cur.execute('''create table chain_emails (
                    chain_name varchar(30),
                    central_email varchar(30)
                );
            ''')

cur.execute('''
insert into chain_emails values('Ottawa Hotels', 'otthotels@gmail.com');
insert into chain_emails values('Bob Hotels', 'bobhotels@hotmail.com');
insert into chain_emails values('123 hotel w me', '123.hotelwme@gmail.com');
insert into chain_emails values('im baked hotels', 'imbaked.hotels@yahoo.com');
''')

cur.execute("drop table if exists chain_phone_num;")

cur.execute('''create table chain_phone_num (
                    chain_name varchar(30),
                    central_phone_num varchar(30)
                );
            ''')

cur.execute('''
insert into chain_phone_num values('Ottawa Hotels', '735-274-9264');
insert into chain_phone_num values('Bob Hotels', '639-265-8368');
insert into chain_phone_num values('123 hotel w me', '385-648-5746');
insert into chain_phone_num values('im baked hotels', '284-597-0004');
''')

cur.execute("drop table if exists hotel;")

cur.execute('''create table hotel (
                    email varchar(30),
                    rating int,
                    num_rooms int,
                    hotel_address varchar(30),
                    chain_name varchar(30),
                    manager varchar(30)
                );
            ''')

cur.execute('''
insert into hotel values('otthotel.sandyhill@gmail.com', 4, 100, '303 Sandy Street', 'Ottawa Hotels', 'John Dosely');
insert into hotel values('bobinthecity@gmail.com', 2, 20, '333 Bresserer Street', 'Bob Hotels', 'Sammy Ross');
insert into hotel values('123.trto@gmail.com', 5, 50, '59 Main Street', '123 hotel w me', 'Elisha Travers');
insert into hotel values('bakedInBurlington@gmail.com', 4, 70, '35 Lakeshore Drive', 'im baked hotels', 'Manny Stevens');
''')

cur.execute("drop table if exists hotel_phone_num;")

cur.execute('''create table hotel_phone_num (
                    chain_name varchar(30),
                    hotel_address varchar(30),
                    phone_num varchar(30)
                );
            ''')

cur.execute("drop table if exists customer;")

cur.execute('''create table customer (
                    id int,
                    customer_name varchar(30),
                    name varchar(30),
                    customer_address varchar(30),
                    date varchar(30)
                );
            ''')

cur.execute("drop table if exists employee;")

cur.execute('''create table employee (
                    employee_name varchar(30),
                    employee_address varchar(30),
                    ssn int
                );
            ''')


conn.commit()

cur.close()
conn.close()


print("db init successful")
