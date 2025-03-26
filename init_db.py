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


cur.execute("drop table if exists booking;")

cur.execute('''create table booking (
                    customer_id int,
                    booking_id int,
                    renting_id int,
                    constraint pk_booking primary key (customer_id, booking_id),
                    foreign key (customer_id) references customer (id),
                    foreign key (renting_id) references renting (renting_id)
                );
            ''')

cur.execute("drop table if exists renting;")

cur.execute('''create table renting (
                    customer_id int,
                    ssn int,
                    renting_id int,
                    booking_id int,
                    constraint pk_renting primary key (customer_id, renting_id),
                    foreign key (customer_id) references customer (id),
                    foreign key (ssn) references employee (ssn),
                    foreign key (booking_id) references booking (booking_id)
                );
            ''')

cur.execute("drop table if exists works_at;")

cur.execute('''create table works_at (
                    chain_name varchar(30),
                    hotel_address varchar(30),
                    ssn int, 
                    role varchar(30),
                    constraint pk_works_at primary key (chain_name, hotel_address, ssn),
                    foreign key (chain_name) references hotel_chain (chain name),
                    foreign key (hotel_address) references hotel (hotel_address),
                    foreign key (ssn) references employee (ssn)
                );
            ''')

cur.execute("drop table if exists room;")

cur.execute('''create table room (
                    hotel_address varchar(30),
                    chain_name varchar(30),
                    expandable boolean,
                    price float unsigned,
                    capacity int,
                    view varchar(30),
                    constraint pk_room primary key (hotel_address, chain_name, expandable, price, capacity, view),
                    constraint chk_view check (frequecy in ('mountain', 'ocean')),
                    foreign key (chain_name) references hotel_chain (chain_name),
                    foreign key (hotel_address) references hotel (hotel_address)
                );
            ''')

cur.execute("drop table if exists amenities;")

cur.execute('''create table amenities (
                    chain_name varchar(30),
                    hotel_address varchar(30),
                    amenity varchar(30),
                    constraint pk_amenities primary key (chain_name, hotel_address, amenity),
                    foreign key (chain_name) references hotel_chain (chain_name),
                    foreign key (hotel_address) references hotel (hotel_address)
                );
            ''')

cur.execute("drop table if exists damage;")

cur.execute('''create table damage (
                    chain_name varchar(30),
                    hotel_address varchar(30),
                    damage varchar(30),
                    constraint pk_damage primary key (chain_name, hotel_address, damage),
                    foreign key (chain_name) references hotel_chain (chain_name),
                    foreign key (hotel_address) references hotel (hotel_address)
                );
            ''')

cur.execute("drop table if exists booking_history;")

cur.execute('''create table booking_history (
                    booking_id int,
                    past_booking_id int,
                    constraint pk_booking_history primary key (booking_id, past_booking_id),
                    foreign key (booking_id) references booking (booking_id),
                    foreign key (past_booking_id) references booking (booking_id)
                );
            ''')

cur.execute("drop table if exists renting_history;")

cur.execute('''create table renting_history (
                    renting_id int,
                    past_renting_id int,
                    constraint pk_renting_history primary key (renting_id, past_renting_id),
                    foreign key (renting_id) references renting (renting_id),
                    foreign key (past_renting_id) references renting (renting_id)
                );
            ''')

conn.commit()

cur.close()
conn.close()


print("db init successful")
