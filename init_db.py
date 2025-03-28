from app import get_db_conn


conn = get_db_conn()

cur = conn.cursor()

cur.execute('set search_path to "public";')

cur.execute("drop table if exists hotel_chain cascade;")

cur.execute('''create table hotel_chain (
                    chain_name varchar(30),
                    num_hotels int check (num_hotels >= 0),
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
                    central_address varchar(30),
                    CONSTRAINT PK_chain_addresses PRIMARY KEY (chain_name, central_address),
                    foreign key (chain_name) references hotel_chain(chain_name)
                );
            ''')

#cur.execute('''
#insert into chain_addresses values('Ottawa Hotels', '239 Rideau Street');
#insert into chain_addresses values('Bob Hotels', '35 Elgin Street');
#insert into chain_addresses values('123 hotel w me', '555 Dundurn Avenue');
#insert into chain_addresses values('im baked hotels', '53 Sandy Hill Street');
#''')

cur.execute("drop table if exists chain_emails;")

cur.execute('''create table chain_emails (
                    chain_name varchar(30),
                    central_email varchar(30),
                    CONSTRAINT PK_chain_emails PRIMARY KEY (chain_name, central_email),
                    foreign key (chain_name) references hotel_chain(chain_name)
                );
            ''')

#cur.execute('''
#insert into chain_emails values('Ottawa Hotels', 'otthotels@gmail.com');
#insert into chain_emails values('Bob Hotels', 'bobhotels@hotmail.com');
#insert into chain_emails values('123 hotel w me', '123.hotelwme@gmail.com');
#insert into chain_emails values('im baked hotels', 'imbaked.hotels@yahoo.com');
#''')

cur.execute("drop table if exists chain_phone_num;")

cur.execute('''create table chain_phone_num (
                    chain_name varchar(30),
                    central_phone_num varchar(30),
                    CONSTRAINT PK_chain_phone_num PRIMARY KEY (chain_name, central_phone_num),
                    foreign key (chain_name) references hotel_chain(chain_name)
                );
            ''')

#cur.execute('''
#insert into chain_phone_num values('Ottawa Hotels', '735-274-9264');
#insert into chain_phone_num values('Bob Hotels', '639-265-8368');
#insert into chain_phone_num values('123 hotel w me', '385-648-5746');
#insert into chain_phone_num values('im baked hotels', '284-597-0004');
#''')

# removed rating, num_rooms, and email from primary key

cur.execute("drop table if exists hotel cascade;")

cur.execute('''create table hotel (
                    email varchar(30),
                    rating int,
                    num_rooms int,
                    hotel_address varchar(30),
                    chain_name varchar(30),
                    manager varchar(30),
                    CONSTRAINT PK_hotel PRIMARY KEY (chain_name, hotel_address),
                    foreign key (chain_name) references hotel_chain (chain_name)
                );
            ''')

#cur.execute('''
#insert into hotel values('otthotel.sandyhill@gmail.com', 4, 100, '303 Sandy Street', 'Ottawa Hotels', 'John Dosely');
#insert into hotel values('bobinthecity@gmail.com', 2, 20, '333 Bresserer Street', 'Bob Hotels', 'Sammy Ross');
#insert into hotel values('123.trto@gmail.com', 5, 50, '59 Main Street', '123 hotel w me', 'Elisha Travers');
#insert into hotel values('bakedInBurlington@gmail.com', 4, 70, '35 Lakeshore Drive', 'im baked hotels', 'Manny Stevens');
#''')

cur.execute("drop table if exists hotel_phone_num;")

cur.execute('''create table hotel_phone_num (
                    chain_name varchar(30),
                    hotel_address varchar(30),
                    phone_num varchar(30),
                    CONSTRAINT PK_hotel_phone_num PRIMARY KEY (chain_name, hotel_address, phone_num),
                    foreign key (chain_name, hotel_address) references hotel (chain_name, hotel_address)
                );
            ''')

cur.execute("drop table if exists customer cascade;")

cur.execute('''create table customer (
                    id int,
                    customer_name varchar(30),
                    name varchar(30),
                    customer_address varchar(30),
                    date varchar(30),
                    PRIMARY KEY(id)
                );
            ''')

cur.execute("drop table if exists employee cascade;")

cur.execute('''create table employee (
                    employee_name varchar(30),
                    employee_address varchar(30),
                    ssn int,
                    PRIMARY KEY(ssn)
                );
            ''')


# why is renting_id in booking?
# removed:
# renting_id int,
# foreign key (renting_id) references renting (renting_id)

cur.execute("drop table if exists booking cascade;")

cur.execute('''create table booking (
                    customer_id int,
                    booking_id int,
                    constraint pk_booking primary key (customer_id, booking_id),
                    foreign key (customer_id) references customer (id)
                );
            ''')

# also removed booking_id from renting
# removed:
# booking_id int,
# foreign key (booking_id) references booking (booking_id)

cur.execute("drop table if exists renting cascade;")

cur.execute('''create table renting (
                    customer_id int,
                    ssn int,
                    renting_id int,
                    constraint pk_renting primary key (customer_id, renting_id),
                    foreign key (customer_id) references customer (id),
                    foreign key (ssn) references employee (ssn)
                );
            ''')

cur.execute("drop table if exists works_at;")

cur.execute('''create table works_at (
                    chain_name varchar(30),
                    hotel_address varchar(30),
                    ssn int, 
                    role varchar(30),
                    constraint pk_works_at primary key (chain_name, hotel_address, ssn),
                    foreign key (chain_name, hotel_address) references hotel (chain_name, hotel_address),
                    foreign key (ssn) references employee (ssn)
                );
            ''')

cur.execute("drop table if exists room;")

cur.execute('''create table room (
                    hotel_address varchar(30),
                    chain_name varchar(30),
                    expandable boolean,
                    price float check (price >= 0),
                    capacity int,
                    view varchar(30),
                    constraint pk_room primary key (hotel_address, chain_name, expandable, price, capacity, view),
                    constraint chk_view check (view = 'mountain' or view = 'ocean'),
                    foreign key (chain_name, hotel_address) references hotel (chain_name, hotel_address)
                );
            ''')

cur.execute("drop table if exists amenities;")

cur.execute('''create table amenities (
                    chain_name varchar(30),
                    hotel_address varchar(30),
                    amenity varchar(30),
                    constraint pk_amenities primary key (chain_name, hotel_address, amenity),
                    foreign key (chain_name, hotel_address) references hotel (chain_name, hotel_address)
                );
            ''')

cur.execute("drop table if exists damage;")

cur.execute('''create table damage (
                    chain_name varchar(30),
                    hotel_address varchar(30),
                    damage varchar(30),
                    constraint pk_damage primary key (chain_name, hotel_address, damage),
                    foreign key (chain_name, hotel_address) references hotel (chain_name, hotel_address)
                );
            ''')

cur.execute("drop table if exists booking_history;")

cur.execute('''create table booking_history (
                    customer_id int,
                    booking_id int,
                    past_booking_id int,
                    constraint pk_booking_history primary key (customer_id, booking_id, past_booking_id),
                    foreign key (customer_id, booking_id) references booking (customer_id, booking_id),
                    foreign key (customer_id, past_booking_id) references booking (customer_id, booking_id)
                );
            ''')

cur.execute("drop table if exists renting_history;")

cur.execute('''create table renting_history (
                    customer_id int,
                    renting_id int,
                    past_renting_id int,
                    constraint pk_renting_history primary key (customer_id, renting_id, past_renting_id),
                    foreign key (customer_id, renting_id) references renting (customer_id, renting_id),
                    foreign key (customer_id, past_renting_id) references renting (customer_id, renting_id)
                );
            ''')

conn.commit()

cur.close()
conn.close()


print("db init successful")
