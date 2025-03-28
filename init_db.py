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
insert into hotel_chain values('Comfort Stay', 100);
insert into hotel_chain values('Maximize Hotels', 1000);
insert into hotel_chain values('Klaradon', 10);
insert into hotel_chain values('Rosenblatt Hotels', 20);
''')

cur.execute("drop table if exists chain_addresses;")

cur.execute('''create table chain_addresses (
                    chain_name varchar(30),
                    central_address varchar(30),
                    CONSTRAINT PK_chain_addresses PRIMARY KEY (chain_name, central_address),
                    foreign key (chain_name) references hotel_chain(chain_name)
                );
            ''')

cur.execute('''
insert into chain_addresses values('Ottawa Hotels', '239 Rideau Street');
insert into chain_addresses values('Comfort Stay', '35 Elgin Street');
insert into chain_addresses values('Maximize Hotels', '555 Dundurn Avenue');
insert into chain_addresses values('Klaradon', '53 Sandy Hill Street');
insert into chain_addresses values('Rosenblatt Hotels', '812 Stittsville Street');
''')

cur.execute("drop table if exists chain_emails;")

cur.execute('''create table chain_emails (
                    chain_name varchar(30),
                    central_email varchar(30),
                    CONSTRAINT PK_chain_emails PRIMARY KEY (chain_name, central_email),
                    foreign key (chain_name) references hotel_chain(chain_name)
                );
            ''')

cur.execute('''
insert into chain_emails values('Ottawa Hotels', 'otthotels@gmail.com');
insert into chain_emails values('Comfort Stay', 'comfstay@hotmail.com');
insert into chain_emails values('Maximize Hotels', 'maximizehotels@gmail.com');
insert into chain_emails values('Klaradon', 'klaradon@yahoo.com');
insert into chain_emails values('Rosenblatt Hotels', 'rosenexperience@gmail.com');
''')

cur.execute("drop table if exists chain_phone_num;")

cur.execute('''create table chain_phone_num (
                    chain_name varchar(30),
                    central_phone_num varchar(30),
                    CONSTRAINT PK_chain_phone_num PRIMARY KEY (chain_name, central_phone_num),
                    foreign key (chain_name) references hotel_chain(chain_name)
                );
            ''')

cur.execute('''
insert into chain_phone_num values('Ottawa Hotels', '735-274-9264');
insert into chain_phone_num values('Comfort Stay', '639-265-8368');
insert into chain_phone_num values('Maximize Hotels', '385-648-5746');
insert into chain_phone_num values('Klaradon', '284-597-0004');
insert into chain_phone_num values('Rosenblatt Hotels', '338-893-8184');
''')

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

cur.execute('''
insert into hotel values('otthotel.sandyhill@gmail.com', 4, 100, '303 Sandy Street', 'Ottawa Hotels', 'John Dosely');
insert into hotel values('otthotel.gatineau@gmail.com', 3, 80, '402 Tremblent Way', 'Ottawa Hotels', 'Jane Dosely');
insert into hotel values('otthotel.elgin@gmail.com', 2, 20, '45 Elgin Street', 'Ottawa Hotels', 'Luke Peters');
insert into hotel values('otthotel.rideau@gmail.com', 3, 100, '201 Rideau Street', 'Ottawa Hotels', 'Victor Matthews');
insert into hotel values('otthotel.kanata@gmail.com', 3, 80, '39 Snow Drive', 'Ottawa Hotels', 'Joshua Kayley');
insert into hotel values('otthotel.stittsville@gmail.com', 2, 50, '17 Autumn Street', 'Ottawa Hotels', 'Anray Liu');
insert into hotel values('otthotel.westOtt@gmail.com', 4, 50, '92 Pineview Crescent', 'Ottawa Hotels', 'Willard Hickling');
insert into hotel values('otthotel.urbandale@gmail.com', 2, 10, '14 Pleasant Park Road', 'Ottawa Hotels', 'Roberto Haisty');


insert into hotel values('comfstayOttawa@hotmail.com', 2, 20, '333 Bresserer Street', 'Comfort Stay', 'Sammy Ross');
insert into hotel values('comfstayGatineau@hotmail.com', 5, 200, '154 Wrightville Way', 'Comfort Stay', 'Charlie E. Hook');
insert into hotel values('comfstayElgin@hotmail.com', 2, 100, '46 Elgin Street', 'Comfort Stay', 'Frederick Spurgin');
insert into hotel values('comfstayKanata@hotmail.com', 3, 50, '30 Qualicum Street', 'Comfort Stay', 'Milton Shwift');
insert into hotel values('comfstayLynwood@hotmail.com', 4, 25, '53 Ascot Avenue', 'Comfort Stay', 'Johnathan Rico');
insert into hotel values('comfstayWestcliffe@hotmail.com', 2, 20, '62 Seyton Drive', 'Comfort Stay', 'Frank Browser');
insert into hotel values('comfstayArlington@hotmail.com', 4, 70, '38 McClellan Road', 'Comfort Stay', 'Bertha Leamy');
insert into hotel values('comfstayMerivale@hotmail.com', 1, 10, '48 Capital Drive', 'Comfort Stay', 'Jamie Thomas');

insert into hotel values('maximizeOttawa@gmail.com', 5, 50, '59 Main Street', 'Maximize Hotels', 'Elisha Travers');
insert into hotel values('maximizeNewYork@gmail.com', 4, 120, '72 Broadway Ave', 'Maximize Hotels', 'Sarah Johnson');
insert into hotel values('maximizeParis@gmail.com', 3, 90, '15 Rue de la Paix', 'Maximize Hotels', 'Lucie Dupont');
insert into hotel values('maximizeCalifornia@gmail.com', 5, 200, '100 Sunset Blvd', 'Maximize Hotels', 'Mark Thompson');
insert into hotel values('maximizeLondon@gmail.com', 4, 150, '47 Oxford Street', 'Maximize Hotels', 'Emma Parker');
insert into hotel values('maximizeTokyo@gmail.com', 3, 110, '300 Shibuya Crossing', 'Maximize Hotels', 'Hiroshi Tanaka');
insert into hotel values('maximizeMountainLodge@gmail.com', 5, 180, '100 Mountain View Road', 'Maximize Hotels', 'James Mitchell');
insert into hotel values('maximizeCoastalEscape@gmail.com', 4, 130, '21 Beachside Drive', 'Maximize Hotels', 'Nina Williams');

insert into hotel values('klaradonBurlington@gmail.com', 4, 70, '35 Lakeshore Drive', 'Klaradon', 'Manny Stevens');
insert into hotel values('klaradonWaterdown@gmail.com', 3, 20, '35 Humphrey Drive', 'Klaradon', 'Matthew Boyle');
insert into hotel values('klaradonToronto@gmail.com', 3, 85, '45 Queen Street', 'Klaradon', 'Lisa Green');
insert into hotel values('klaradonVancouver@gmail.com', 5, 150, '120 Pacific Blvd', 'Klaradon', 'John Harris');
insert into hotel values('klaradonOttawa@gmail.com', 4, 100, '60 Elgin Street', 'Klaradon', 'Rachel Adams');
insert into hotel values('klaradonCalgary@gmail.com', 3, 95, '10 Calgary Road', 'Klaradon', 'David Brown');
insert into hotel values('klaradonMontreal@gmail.com', 5, 130, '75 Saint Catherine Street', 'Klaradon', 'Jessica Lee');
insert into hotel values('klaradonQuebecCity@gmail.com', 4, 110, '22 Old Port Road', 'Klaradon', 'Michael Roberts');

insert into hotel values('rosenblatToronto@gmail.com', 5, 70, '812 Stittsville Street', 'Rosenblatt Hotels', 'Atom Rosenblatt');
insert into hotel values('rosenblattVancouver@gmail.com', 4, 120, '214 Granville Street', 'Rosenblatt Hotels', 'Sophie Cohen');
insert into hotel values('rosenblattMontreal@gmail.com', 3, 80, '67 Crescent Street', 'Rosenblatt Hotels', 'Daniel Kim');
insert into hotel values('rosenblattCalgary@gmail.com', 5, 150, '98 16th Avenue NW', 'Rosenblatt Hotels', 'Lena Patel');
insert into hotel values('rosenblattOttawa@gmail.com', 4, 100, '45 Wellington Street', 'Rosenblatt Hotels', 'Matthew Davis');
insert into hotel values('rosenblattQuebecCity@gmail.com', 3, 90, '50 Rue Saint-Jean', 'Rosenblatt Hotels', 'Chloe Lee');
insert into hotel values('rosenblattEdmonton@gmail.com', 5, 180, '123 Jasper Avenue', 'Rosenblatt Hotels', 'Ethan Smith');
insert into hotel values('rosenblattWinnipeg@gmail.com', 4, 110, '550 Main Street', 'Rosenblatt Hotels', 'Olivia Martinez');
''')

cur.execute("drop table if exists hotel_phone_num;")

cur.execute('''create table hotel_phone_num (
                    chain_name varchar(30),
                    hotel_address varchar(30),
                    phone_num varchar(30),
                    CONSTRAINT PK_hotel_phone_num PRIMARY KEY (chain_name, hotel_address, phone_num),
                    foreign key (chain_name, hotel_address) references hotel (chain_name, hotel_address)
                );
            ''')
cur.execute('''
insert into hotel_phone_num values('Ottawa Hotels', '303 Sandy Street', '264-817-7492');
insert into hotel_phone_num values('Ottawa Hotels', '402 Tremblent Way', '613-256-4923');
insert into hotel_phone_num values('Ottawa Hotels', '45 Elgin Street', '613-489-2841');
insert into hotel_phone_num values('Ottawa Hotels', '201 Rideau Street', '613-578-9124');
insert into hotel_phone_num values('Ottawa Hotels', '39 Snow Drive', '613-638-2947');
insert into hotel_phone_num values('Ottawa Hotels', '17 Autumn Street', '613-725-3691');
insert into hotel_phone_num values('Ottawa Hotels', '92 Pineview Crescent', '613-381-6745');
insert into hotel_phone_num values('Ottawa Hotels', '14 Pleasant Park Road', '613-502-9832');

insert into hotel_phone_num values('Comfort Stay', '333 Bresserer Street', '613-495-2387');
insert into hotel_phone_num values('Comfort Stay', '154 Wrightville Way', '819-234-6723');
insert into hotel_phone_num values('Comfort Stay', '46 Elgin Street', '613-382-9248');
insert into hotel_phone_num values('Comfort Stay', '30 Qualicum Street', '613-758-4930');
insert into hotel_phone_num values('Comfort Stay', '53 Ascot Avenue', '613-849-1427');
insert into hotel_phone_num values('Comfort Stay', '62 Seyton Drive', '613-731-5284');
insert into hotel_phone_num values('Comfort Stay', '38 McClellan Road', '613-404-2397');
insert into hotel_phone_num values('Comfort Stay', '48 Capital Drive', '613-533-9054');

insert into hotel_phone_num values('Maximize Hotels', '59 Main Street', '613-501-2359');
insert into hotel_phone_num values('Maximize Hotels', '72 Broadway Ave', '212-634-7821');
insert into hotel_phone_num values('Maximize Hotels', '15 Rue de la Paix', '33-1-45-67-8923');
insert into hotel_phone_num values('Maximize Hotels', '100 Sunset Blvd', '310-556-2714');
insert into hotel_phone_num values('Maximize Hotels', '47 Oxford Street', '44-20-7984-2398');
insert into hotel_phone_num values('Maximize Hotels', '300 Shibuya Crossing', '81-3-5342-1678');
insert into hotel_phone_num values('Maximize Hotels', '100 Mountain View Road', '303-423-6781');
insert into hotel_phone_num values('Maximize Hotels', '21 Beachside Drive', '408-874-5921');

insert into hotel_phone_num values('Klaradon', '35 Lakeshore Drive', '905-324-8593');
insert into hotel_phone_num values('Klaradon', '35 Humphrey Drive', '905-876-3421');
insert into hotel_phone_num values('Klaradon', '45 Queen Street', '416-256-7283');
insert into hotel_phone_num values('Klaradon', '120 Pacific Blvd', '604-435-6019');
insert into hotel_phone_num values('Klaradon', '60 Elgin Street', '613-721-4935');
insert into hotel_phone_num values('Klaradon', '10 Calgary Road', '403-234-8721');
insert into hotel_phone_num values('Klaradon', '75 Saint Catherine Street', '514-432-9801');
insert into hotel_phone_num values('Klaradon', '22 Old Port Road', '418-762-2395');

insert into hotel_phone_num values('Rosenblatt Hotels', '812 Stittsville Street', '613-458-7632');
insert into hotel_phone_num values('Rosenblatt Hotels', '214 Granville Street', '604-378-5921');
insert into hotel_phone_num values('Rosenblatt Hotels', '67 Crescent Street', '514-294-1635');
insert into hotel_phone_num values('Rosenblatt Hotels', '98 16th Avenue NW', '403-623-8745');
insert into hotel_phone_num values('Rosenblatt Hotels', '45 Wellington Street', '613-533-2847');
insert into hotel_phone_num values('Rosenblatt Hotels', '50 Rue Saint-Jean', '418-654-9275');
insert into hotel_phone_num values('Rosenblatt Hotels', '123 Jasper Avenue', '780-412-6354');
insert into hotel_phone_num values('Rosenblatt Hotels', '550 Main Street', '204-768-4927');
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
