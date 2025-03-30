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
                    customer_address varchar(30),
                    date varchar(30),
                    PRIMARY KEY(id)
                );
            ''')
cur.execute('''
insert into customer values('000000', 'Valentino Vinod', '720 Rideau Street', '28/03/20');
insert into customer values('000001', 'Anray Liu', '100 Rideau Street', '13/02/23');
insert into customer values('000002', 'Adam Rosenblatt', '382 Markhamm Way', '05/10/24');
insert into customer values('000003', 'Manny Matthews', '48 Blue Sky Way', '20/01/25');
insert into customer values('000004', 'Maradin Leo', '34 Wacky Street', '14/08/25');
''')


cur.execute("drop table if exists employee cascade;")

cur.execute('''create table employee (
                    employee_name varchar(30),
                    employee_address varchar(30),
                    ssn int,
                    PRIMARY KEY(ssn)
                );
            ''')

cur.execut('''
insert into employee values('John Doe', '123 Elm St', 100001234);
insert into employee values('Jane Smith', '456 Oak St', 100002345);
insert into employee values('Alice Johnson', '789 Pine St', 100003456);
insert into employee values('Bob Brown', '101 Maple St', 100004567);
insert into employee values('Charlie Davis', '202 Birch St', 100005678);
insert into employee values('Deborah Wilson', '303 Cedar St', 100006789);
insert into employee values('Edward Moore', '404 Walnut St', 100007890);
insert into employee values('Fiona White', '505 Chestnut St', 100008901);
insert into employee values('George Harris', '606 Ash St', 100009012);
insert into employee values('Hannah Clark', '707 Willow St', 100010123);
insert into employee values('Isaac Lewis', '808 Redwood St', 100011234);
insert into employee values('Jackie Scott', '909 Pinecrest St', 100012345);
insert into employee values('Kevin Martin', '101 Birchwood St', 100013456);
insert into employee values('Laura Young', '202 Oakdale St', 100014567);
insert into employee values('Michael King', '303 Maplewood St', 100015678);
insert into employee values('Nina Adams', '404 Elmwood St', 100016789);
insert into employee values('Oscar Nelson', '505 Oakview St', 100017890);
insert into employee values('Patricia Carter', '606 Ashwood St', 100018901);
insert into employee values('Quinn Mitchell', '707 Cedarwood St', 100019012);
insert into employee values('Rachel Robinson', '808 Chestnutwood St', 100020123);
insert into employee values('Samuel Clark', '909 Redwoodview St', 100021234);
insert into employee values('Tina Perez', '101 Mapleview St', 100022345);
insert into employee values('Ursula Lee', '202 Birchview St', 100023456);
insert into employee values('Victor Hall', '303 Willowview St', 100024567);
insert into employee values('Wendy Allen', '404 Pineview St', 100025678);
insert into employee values('Xander Scott', '505 Cedarview St', 100026789);
insert into employee values('Yvonne Gonzalez', '606 Oakview St', 100027890);
insert into employee values('Zane Martinez', '707 Redwoodview St', 100028901);
insert into employee values('Amelia Carter', '808 Pineview St', 100029012);
insert into employee values('Brandon Clark', '909 Ashview St', 100030123);
insert into employee values('Carmen Thompson', '101 Willowview St', 100031234);
insert into employee values('Diana Lewis', '202 Chestnutview St', 100032345);
insert into employee values('Elliot Harris', '303 Mapleview St', 100033456);
insert into employee values('Felicia Evans', '404 Oakwood St', 100034567);
insert into employee values('Graham Walker', '505 Ashwood St', 100035678);
insert into employee values('Helen Green', '606 Cedarwood St', 100036789);
insert into employee values('Ian White', '707 Redwood St', 100037890);
insert into employee values('Julia Young', '808 Pinecrest St', 100038901);
insert into employee values('Kyle Mitchell', '909 Birch St', 100039012);
insert into employee values('Lana Moore', '101 Elmwood St', 100040123);
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

cur.execute('''
insert into works_at values('Maximize Hotels', '59 Main Street', 100001234, 'Manager');
insert into works_at values('Maximize Hotels', '72 Broadway Ave', 100002345, 'Receptionist');
insert into works_at values('Maximize Hotels', '15 Rue de la Paix', 100003456, 'Housekeeping');
insert into works_at values('Maximize Hotels', '100 Sunset Blvd', 100004567, 'Security');
insert into works_at values('Maximize Hotels', '47 Oxford Street', 100005678, 'Concierge');
insert into works_at values('Maximize Hotels', '300 Shibuya Crossing', 100006789, 'Chef');
insert into works_at values('Maximize Hotels', '100 Mountain View Road', 100007890, 'Waiter');
insert into works_at values('Maximize Hotels', '21 Beachside Drive', 100008901, 'Porter');
insert into works_at values('Klaradon', '35 Lakeshore Drive', 100009012, 'Manager');
insert into works_at values('Klaradon', '35 Humphrey Drive', 100010123, 'Receptionist');
insert into works_at values('Klaradon', '45 Queen Street', 100011234, 'Housekeeping');
insert into works_at values('Klaradon', '120 Pacific Blvd', 100012345, 'Security');
insert into works_at values('Klaradon', '60 Elgin Street', 100013456, 'Concierge');
insert into works_at values('Klaradon', '10 Calgary Road', 100014567, 'Chef');
insert into works_at values('Klaradon', '75 Saint Catherine Street', 100015678, 'Waiter');
insert into works_at values('Klaradon', '22 Old Port Road', 100016789, 'Porter');
insert into works_at values('Rosenblatt Hotels', '812 Stittsville Street', 100017890, 'Manager');
insert into works_at values('Rosenblatt Hotels', '214 Granville Street', 100018901, 'Receptionist');
insert into works_at values('Rosenblatt Hotels', '67 Crescent Street', 100019012, 'Housekeeping');
insert into works_at values('Rosenblatt Hotels', '98 16th Avenue NW', 100020123, 'Security');
insert into works_at values('Rosenblatt Hotels', '45 Wellington Street', 100021234, 'Concierge');
insert into works_at values('Rosenblatt Hotels', '50 Rue Saint-Jean', 100022345, 'Chef');
insert into works_at values('Rosenblatt Hotels', '123 Jasper Avenue', 100023456, 'Waiter');
insert into works_at values('Rosenblatt Hotels', '550 Main Street', 100024567, 'Porter');
insert into works_at values('Comfort Stay', '333 Bresserer Street', 100025678, 'Manager');
insert into works_at values('Comfort Stay', '154 Wrightville Way', 100026789, 'Receptionist');
insert into works_at values('Comfort Stay', '46 Elgin Street', 100027890, 'Housekeeping');
insert into works_at values('Comfort Stay', '30 Qualicum Street', 100028901, 'Security');
insert into works_at values('Comfort Stay', '53 Ascot Avenue', 100029012, 'Concierge');
insert into works_at values('Comfort Stay', '62 Seyton Drive', 100030123, 'Chef');
insert into works_at values('Comfort Stay', '38 McClellan Road', 100031234, 'Waiter');
insert into works_at values('Comfort Stay', '48 Capital Drive', 100032345, 'Porter');
insert into works_at values('Ottawa Hotels', '402 Tremblent Way', 100033456, 'Manager');
insert into works_at values('Ottawa Hotels', '45 Elgin Street', 100034567, 'Receptionist');
insert into works_at values('Ottawa Hotels', '201 Rideau Street', 100035678, 'Housekeeping');
insert into works_at values('Ottawa Hotels', '39 Snow Drive', 100036789, 'Security');
insert into works_at values('Ottawa Hotels', '17 Autumn Street', 100037890, 'Concierge');
insert into works_at values('Ottawa Hotels', '92 Pineview Crescent', 100038901, 'Chef');
insert into works_at values('Ottawa Hotels', '14 Pleasant Park Road', 100039012, 'Waiter');
insert into works_at values('Ottawa Hotels', '550 Main Street', 100040123, 'Porter');
''')

cur.execute("drop table if exists room;")

cur.execute('''create table room (
                    room_id varchar(30),
                    hotel_address varchar(30),
                    chain_name varchar(30),
                    expandable boolean,
                    price float check (price >= 0),
                    capacity int,
                    view varchar(30),
                    constraint pk_room primary key (hotel_address, chain_name, room_id),
                    constraint chk_view check (view = 'mountain' or view = 'ocean'),
                    foreign key (chain_name, hotel_address) references hotel (chain_name, hotel_address)
                );
            ''')

cur.execute("drop table if exists amenities;")

cur.execute('''
-- Ottawa Hotels - 303 Sandy Street
insert into room values('303 Sandy Street', 'Ottawa Hotels', true, 120.00, 1, 'mountain');
insert into room values('303 Sandy Street', 'Ottawa Hotels', false, 160.00, 2, 'ocean');
insert into room values('303 Sandy Street', 'Ottawa Hotels', true, 210.00, 3, 'mountain');
insert into room values('303 Sandy Street', 'Ottawa Hotels', false, 260.00, 4, 'ocean');
insert into room values('303 Sandy Street', 'Ottawa Hotels', true, 310.00, 5, 'mountain');

-- Ottawa Hotels - 402 Tremblent Way
insert into room values('402 Tremblent Way', 'Ottawa Hotels', true, 150.00, 1, 'mountain');
insert into room values('402 Tremblent Way', 'Ottawa Hotels', false, 200.00, 2, 'ocean');
insert into room values('402 Tremblent Way', 'Ottawa Hotels', true, 250.00, 3, 'mountain');
insert into room values('402 Tremblent Way', 'Ottawa Hotels', false, 300.00, 5, 'ocean');
insert into room values('402 Tremblent Way', 'Ottawa Hotels', true, 350.00, 7, 'mountain');

-- Ottawa Hotels - 45 Elgin Street
insert into room values('45 Elgin Street', 'Ottawa Hotels', true, 180.00, 1, 'ocean');
insert into room values('45 Elgin Street', 'Ottawa Hotels', false, 230.00, 2, 'mountain');
insert into room values('45 Elgin Street', 'Ottawa Hotels', true, 280.00, 3, 'ocean');
insert into room values('45 Elgin Street', 'Ottawa Hotels', false, 330.00, 4, 'mountain');
insert into room values('45 Elgin Street', 'Ottawa Hotels', true, 380.00, 6, 'ocean');

-- Ottawa Hotels - 201 Rideau Street
insert into room values('201 Rideau Street', 'Ottawa Hotels', true, 220.00, 2, 'mountain');
insert into room values('201 Rideau Street', 'Ottawa Hotels', false, 270.00, 3, 'ocean');
insert into room values('201 Rideau Street', 'Ottawa Hotels', true, 320.00, 4, 'mountain');
insert into room values('201 Rideau Street', 'Ottawa Hotels', false, 370.00, 5, 'ocean');
insert into room values('201 Rideau Street', 'Ottawa Hotels', true, 420.00, 7, 'mountain');

-- Ottawa Hotels - 39 Snow Drive
insert into room values('39 Snow Drive', 'Ottawa Hotels', true, 210.00, 1, 'ocean');
insert into room values('39 Snow Drive', 'Ottawa Hotels', false, 260.00, 2, 'mountain');
insert into room values('39 Snow Drive', 'Ottawa Hotels', true, 310.00, 3, 'ocean');
insert into room values('39 Snow Drive', 'Ottawa Hotels', false, 360.00, 5, 'mountain');
insert into room values('39 Snow Drive', 'Ottawa Hotels', true, 410.00, 8, 'ocean');

-- Ottawa Hotels - 17 Autumn Street
insert into room values('17 Autumn Street', 'Ottawa Hotels', true, 180.00, 1, 'mountain');
insert into room values('17 Autumn Street', 'Ottawa Hotels', false, 230.00, 2, 'ocean');
insert into room values('17 Autumn Street', 'Ottawa Hotels', true, 280.00, 3, 'mountain');
insert into room values('17 Autumn Street', 'Ottawa Hotels', false, 330.00, 5, 'ocean');
insert into room values('17 Autumn Street', 'Ottawa Hotels', true, 380.00, 6, 'mountain');

-- Ottawa Hotels - 92 Pineview Crescent
insert into room values('92 Pineview Crescent', 'Ottawa Hotels', true, 190.00, 2, 'ocean');
insert into room values('92 Pineview Crescent', 'Ottawa Hotels', false, 240.00, 3, 'mountain');
insert into room values('92 Pineview Crescent', 'Ottawa Hotels', true, 290.00, 4, 'ocean');
insert into room values('92 Pineview Crescent', 'Ottawa Hotels', false, 340.00, 5, 'mountain');
insert into room values('92 Pineview Crescent', 'Ottawa Hotels', true, 390.00, 7, 'ocean');

-- Ottawa Hotels - 14 Pleasant Park Road
insert into room values('14 Pleasant Park Road', 'Ottawa Hotels', true, 200.00, 1, 'mountain');
insert into room values('14 Pleasant Park Road', 'Ottawa Hotels', false, 250.00, 2, 'ocean');
insert into room values('14 Pleasant Park Road', 'Ottawa Hotels', true, 300.00, 3, 'mountain');
insert into room values('14 Pleasant Park Road', 'Ottawa Hotels', false, 350.00, 5, 'ocean');
insert into room values('14 Pleasant Park Road', 'Ottawa Hotels', true, 400.00, 7, 'mountain');

-- Comfort Stay - 333 Bresserer Street
insert into room values('333 Bresserer Street', 'Comfort Stay', true, 120.00, 1, 'mountain');
insert into room values('333 Bresserer Street', 'Comfort Stay', false, 170.00, 2, 'ocean');
insert into room values('333 Bresserer Street', 'Comfort Stay', true, 220.00, 3, 'mountain');
insert into room values('333 Bresserer Street', 'Comfort Stay', false, 270.00, 4, 'ocean');
insert into room values('333 Bresserer Street', 'Comfort Stay', true, 320.00, 6, 'mountain');

-- Comfort Stay - 154 Wrightville Way
insert into room values('154 Wrightville Way', 'Comfort Stay', true, 130.00, 2, 'ocean');
insert into room values('154 Wrightville Way', 'Comfort Stay', false, 180.00, 3, 'mountain');
insert into room values('154 Wrightville Way', 'Comfort Stay', true, 230.00, 4, 'ocean');
insert into room values('154 Wrightville Way', 'Comfort Stay', false, 280.00, 5, 'mountain');
insert into room values('154 Wrightville Way', 'Comfort Stay', true, 330.00, 7, 'ocean');

-- Comfort Stay - 46 Elgin Street
insert into room values('46 Elgin Street', 'Comfort Stay', true, 140.00, 1, 'mountain');
insert into room values('46 Elgin Street', 'Comfort Stay', false, 190.00, 2, 'ocean');
insert into room values('46 Elgin Street', 'Comfort Stay', true, 240.00, 3, 'mountain');
insert into room values('46 Elgin Street', 'Comfort Stay', false, 290.00, 4, 'ocean');
insert into room values('46 Elgin Street', 'Comfort Stay', true, 340.00, 6, 'mountain');

-- Comfort Stay - 30 Qualicum Street
insert into room values('30 Qualicum Street', 'Comfort Stay', true, 150.00, 2, 'ocean');
insert into room values('30 Qualicum Street', 'Comfort Stay', false, 200.00, 3, 'mountain');
insert into room values('30 Qualicum Street', 'Comfort Stay', true, 250.00, 4, 'ocean');
insert into room values('30 Qualicum Street', 'Comfort Stay', false, 300.00, 5, 'mountain');
insert into room values('30 Qualicum Street', 'Comfort Stay', true, 350.00, 7, 'ocean');

-- Comfort Stay - 53 Ascot Avenue
insert into room values('53 Ascot Avenue', 'Comfort Stay', true, 160.00, 1, 'mountain');
insert into room values('53 Ascot Avenue', 'Comfort Stay', false, 210.00, 2, 'ocean');
insert into room values('53 Ascot Avenue', 'Comfort Stay', true, 260.00, 3, 'mountain');
insert into room values('53 Ascot Avenue', 'Comfort Stay', false, 310.00, 4, 'ocean');
insert into room values('53 Ascot Avenue', 'Comfort Stay', true, 360.00, 6, 'mountain');

-- Comfort Stay - 62 Seyton Drive
insert into room values('62 Seyton Drive', 'Comfort Stay', true, 170.00, 2, 'ocean');
insert into room values('62 Seyton Drive', 'Comfort Stay', false, 220.00, 3, 'mountain');
insert into room values('62 Seyton Drive', 'Comfort Stay', true, 270.00, 4, 'ocean');
insert into room values('62 Seyton Drive', 'Comfort Stay', false, 320.00, 5, 'mountain');
insert into room values('62 Seyton Drive', 'Comfort Stay', true, 370.00, 7, 'ocean');

-- Comfort Stay - 38 McClellan Road
insert into room values('38 McClellan Road', 'Comfort Stay', true, 180.00, 1, 'mountain');
insert into room values('38 McClellan Road', 'Comfort Stay', false, 230.00, 2, 'ocean');
insert into room values('38 McClellan Road', 'Comfort Stay', true, 280.00, 3, 'mountain');
insert into room values('38 McClellan Road', 'Comfort Stay', false, 330.00, 5, 'ocean');
insert into room values('38 McClellan Road', 'Comfort Stay', true, 380.00, 6, 'mountain');

-- Comfort Stay - 48 Capital Drive
insert into room values('48 Capital Drive', 'Comfort Stay', true, 190.00, 1, 'ocean');
insert into room values('48 Capital Drive', 'Comfort Stay', false, 240.00, 2, 'mountain');
insert into room values('48 Capital Drive', 'Comfort Stay', true, 290.00, 3, 'ocean');
insert into room values('48 Capital Drive', 'Comfort Stay', false, 340.00, 4, 'mountain');
insert into room values('48 Capital Drive', 'Comfort Stay', true, 390.00, 6, 'ocean');

-- Maximize Hotels - 59 Main Street
insert into room values('59 Main Street', 'Maximize Hotels', true, 150.50, 1, 'mountain');
insert into room values('59 Main Street', 'Maximize Hotels', false, 200.00, 2, 'ocean');
insert into room values('59 Main Street', 'Maximize Hotels', true, 250.00, 4, 'mountain');
insert into room values('59 Main Street', 'Maximize Hotels', false, 300.00, 6, 'ocean');
insert into room values('59 Main Street', 'Maximize Hotels', true, 350.00, 8, 'mountain');

-- Maximize Hotels - 72 Broadway Ave
insert into room values('72 Broadway Ave', 'Maximize Hotels', true, 180.00, 1, 'ocean');
insert into room values('72 Broadway Ave', 'Maximize Hotels', false, 220.00, 2, 'mountain');
insert into room values('72 Broadway Ave', 'Maximize Hotels', true, 270.00, 3, 'ocean');
insert into room values('72 Broadway Ave', 'Maximize Hotels', false, 330.00, 5, 'mountain');
insert into room values('72 Broadway Ave', 'Maximize Hotels', true, 380.00, 7, 'ocean');

-- Maximize Hotels - 15 Rue de la Paix
insert into room values('15 Rue de la Paix', 'Maximize Hotels', true, 210.00, 2, 'mountain');
insert into room values('15 Rue de la Paix', 'Maximize Hotels', false, 260.00, 3, 'ocean');
insert into room values('15 Rue de la Paix', 'Maximize Hotels', true, 310.00, 4, 'mountain');
insert into room values('15 Rue de la Paix', 'Maximize Hotels', false, 370.00, 6, 'ocean');
insert into room values('15 Rue de la Paix', 'Maximize Hotels', true, 420.00, 8, 'mountain');

-- Maximize Hotels - 100 Sunset Blvd
insert into room values('100 Sunset Blvd', 'Maximize Hotels', true, 230.00, 3, 'ocean');
insert into room values('100 Sunset Blvd', 'Maximize Hotels', false, 280.00, 4, 'mountain');
insert into room values('100 Sunset Blvd', 'Maximize Hotels', true, 330.00, 5, 'ocean');
insert into room values('100 Sunset Blvd', 'Maximize Hotels', false, 380.00, 6, 'mountain');
insert into room values('100 Sunset Blvd', 'Maximize Hotels', true, 430.00, 9, 'ocean');

-- Maximize Hotels - 47 Oxford Street
insert into room values('47 Oxford Street', 'Maximize Hotels', true, 160.00, 1, 'mountain');
insert into room values('47 Oxford Street', 'Maximize Hotels', false, 210.00, 2, 'ocean');
insert into room values('47 Oxford Street', 'Maximize Hotels', true, 260.00, 3, 'mountain');
insert into room values('47 Oxford Street', 'Maximize Hotels', false, 320.00, 5, 'ocean');
insert into room values('47 Oxford Street', 'Maximize Hotels', true, 370.00, 7, 'mountain');

-- Maximize Hotels - 300 Shibuya Crossing
insert into room values('300 Shibuya Crossing', 'Maximize Hotels', true, 270.00, 2, 'ocean');
insert into room values('300 Shibuya Crossing', 'Maximize Hotels', false, 320.00, 3, 'mountain');
insert into room values('300 Shibuya Crossing', 'Maximize Hotels', true, 370.00, 4, 'ocean');
insert into room values('300 Shibuya Crossing', 'Maximize Hotels', false, 420.00, 6, 'mountain');
insert into room values('300 Shibuya Crossing', 'Maximize Hotels', true, 470.00, 8, 'ocean');

-- Maximize Hotels - 100 Mountain View Road
insert into room values('100 Mountain View Road', 'Maximize Hotels', true, 280.00, 2, 'mountain');
insert into room values('100 Mountain View Road', 'Maximize Hotels', false, 330.00, 3, 'ocean');
insert into room values('100 Mountain View Road', 'Maximize Hotels', true, 380.00, 5, 'mountain');
insert into room values('100 Mountain View Road', 'Maximize Hotels', false, 430.00, 6, 'ocean');
insert into room values('100 Mountain View Road', 'Maximize Hotels', true, 480.00, 9, 'mountain');

-- Maximize Hotels - 21 Beachside Drive
insert into room values('21 Beachside Drive', 'Maximize Hotels', true, 190.00, 1, 'ocean');
insert into room values('21 Beachside Drive', 'Maximize Hotels', false, 240.00, 2, 'mountain');
insert into room values('21 Beachside Drive', 'Maximize Hotels', true, 290.00, 4, 'ocean');
insert into room values('21 Beachside Drive', 'Maximize Hotels', false, 340.00, 6, 'mountain');
insert into room values('21 Beachside Drive', 'Maximize Hotels', true, 390.00, 8, 'ocean');

-- Klaradon - 35 Lakeshore Drive
insert into room values('35 Lakeshore Drive', 'Klaradon', true, 210.00, 1, 'mountain');
insert into room values('35 Lakeshore Drive', 'Klaradon', false, 260.00, 2, 'ocean');
insert into room values('35 Lakeshore Drive', 'Klaradon', true, 310.00, 4, 'mountain');
insert into room values('35 Lakeshore Drive', 'Klaradon', false, 360.00, 5, 'ocean');
insert into room values('35 Lakeshore Drive', 'Klaradon', true, 410.00, 8, 'mountain');

-- Klaradon - 35 Humphrey Drive
insert into room values('35 Humphrey Drive', 'Klaradon', true, 190.00, 1, 'ocean');
insert into room values('35 Humphrey Drive', 'Klaradon', false, 240.00, 2, 'mountain');
insert into room values('35 Humphrey Drive', 'Klaradon', true, 290.00, 3, 'ocean');
insert into room values('35 Humphrey Drive', 'Klaradon', false, 340.00, 5, 'mountain');
insert into room values('35 Humphrey Drive', 'Klaradon', true, 390.00, 7, 'ocean');

-- Klaradon - 45 Queen Street
insert into room values('45 Queen Street', 'Klaradon', true, 220.00, 2, 'mountain');
insert into room values('45 Queen Street', 'Klaradon', false, 270.00, 3, 'ocean');
insert into room values('45 Queen Street', 'Klaradon', true, 320.00, 4, 'mountain');
insert into room values('45 Queen Street', 'Klaradon', false, 370.00, 6, 'ocean');
insert into room values('45 Queen Street', 'Klaradon', true, 420.00, 8, 'mountain');

-- Klaradon - 120 Pacific Blvd
insert into room values('120 Pacific Blvd', 'Klaradon', true, 250.00, 3, 'ocean');
insert into room values('120 Pacific Blvd', 'Klaradon', false, 300.00, 4, 'mountain');
insert into room values('120 Pacific Blvd', 'Klaradon', true, 350.00, 5, 'ocean');
insert into room values('120 Pacific Blvd', 'Klaradon', false, 400.00, 6, 'mountain');
insert into room values('120 Pacific Blvd', 'Klaradon', true, 450.00, 9, 'ocean');

-- Klaradon - 60 Elgin Street
insert into room values('60 Elgin Street', 'Klaradon', true, 230.00, 1, 'mountain');
insert into room values('60 Elgin Street', 'Klaradon', false, 280.00, 2, 'ocean');
insert into room values('60 Elgin Street', 'Klaradon', true, 330.00, 4, 'mountain');
insert into room values('60 Elgin Street', 'Klaradon', false, 380.00, 5, 'ocean');
insert into room values('60 Elgin Street', 'Klaradon', true, 430.00, 7, 'mountain');

-- Klaradon - 10 Calgary Road
insert into room values('10 Calgary Road', 'Klaradon', true, 240.00, 2, 'ocean');
insert into room values('10 Calgary Road', 'Klaradon', false, 290.00, 3, 'mountain');
insert into room values('10 Calgary Road', 'Klaradon', true, 340.00, 4, 'ocean');
insert into room values('10 Calgary Road', 'Klaradon', false, 390.00, 6, 'mountain');
insert into room values('10 Calgary Road', 'Klaradon', true, 440.00, 8, 'ocean');

-- Klaradon - 75 Saint Catherine Street
insert into room values('75 Saint Catherine Street', 'Klaradon', true, 260.00, 2, 'mountain');
insert into room values('75 Saint Catherine Street', 'Klaradon', false, 310.00, 3, 'ocean');
insert into room values('75 Saint Catherine Street', 'Klaradon', true, 360.00, 4, 'mountain');
insert into room values('75 Saint Catherine Street', 'Klaradon', false, 410.00, 6, 'ocean');
insert into room values('75 Saint Catherine Street', 'Klaradon', true, 460.00, 8, 'mountain');

-- Klaradon - 22 Old Port Road
insert into room values('22 Old Port Road', 'Klaradon', true, 280.00, 3, 'ocean');
insert into room values('22 Old Port Road', 'Klaradon', false, 330.00, 4, 'mountain');
insert into room values('22 Old Port Road', 'Klaradon', true, 380.00, 5, 'ocean');
insert into room values('22 Old Port Road', 'Klaradon', false, 430.00, 6, 'mountain');
insert into room values('22 Old Port Road', 'Klaradon', true, 480.00, 9, 'ocean');

-- Rosenblatt Hotels - 812 Stittsville Street
insert into room values('812 Stittsville Street', 'Rosenblatt Hotels', true, 200.00, 1, 'mountain');
insert into room values('812 Stittsville Street', 'Rosenblatt Hotels', false, 250.00, 2, 'ocean');
insert into room values('812 Stittsville Street', 'Rosenblatt Hotels', true, 300.00, 4, 'mountain');
insert into room values('812 Stittsville Street', 'Rosenblatt Hotels', false, 350.00, 6, 'ocean');
insert into room values('812 Stittsville Street', 'Rosenblatt Hotels', true, 400.00, 8, 'mountain');

-- Rosenblatt Hotels - 214 Granville Street
insert into room values('214 Granville Street', 'Rosenblatt Hotels', true, 220.00, 2, 'ocean');
insert into room values('214 Granville Street', 'Rosenblatt Hotels', false, 270.00, 3, 'mountain');
insert into room values('214 Granville Street', 'Rosenblatt Hotels', true, 320.00, 4, 'ocean');
insert into room values('214 Granville Street', 'Rosenblatt Hotels', false, 370.00, 5, 'mountain');
insert into room values('214 Granville Street', 'Rosenblatt Hotels', true, 420.00, 7, 'ocean');

-- Rosenblatt Hotels - 67 Crescent Street
insert into room values('67 Crescent Street', 'Rosenblatt Hotels', true, 230.00, 1, 'mountain');
insert into room values('67 Crescent Street', 'Rosenblatt Hotels', false, 280.00, 2, 'ocean');
insert into room values('67 Crescent Street', 'Rosenblatt Hotels', true, 330.00, 3, 'mountain');
insert into room values('67 Crescent Street', 'Rosenblatt Hotels', false, 380.00, 5, 'ocean');
insert into room values('67 Crescent Street', 'Rosenblatt Hotels', true, 430.00, 6, 'mountain');

-- Rosenblatt Hotels - 98 16th Avenue NW
insert into room values('98 16th Avenue NW', 'Rosenblatt Hotels', true, 240.00, 2, 'ocean');
insert into room values('98 16th Avenue NW', 'Rosenblatt Hotels', false, 290.00, 3, 'mountain');
insert into room values('98 16th Avenue NW', 'Rosenblatt Hotels', true, 340.00, 4, 'ocean');
insert into room values('98 16th Avenue NW', 'Rosenblatt Hotels', false, 390.00, 5, 'mountain');
insert into room values('98 16th Avenue NW', 'Rosenblatt Hotels', true, 440.00, 8, 'ocean');

-- Rosenblatt Hotels - 45 Wellington Street
insert into room values('45 Wellington Street', 'Rosenblatt Hotels', true, 250.00, 3, 'mountain');
insert into room values('45 Wellington Street', 'Rosenblatt Hotels', false, 300.00, 4, 'ocean');
insert into room values('45 Wellington Street', 'Rosenblatt Hotels', true, 350.00, 5, 'mountain');
insert into room values('45 Wellington Street', 'Rosenblatt Hotels', false, 400.00, 6, 'ocean');
insert into room values('45 Wellington Street', 'Rosenblatt Hotels', true, 450.00, 9, 'mountain');

-- Rosenblatt Hotels - 50 Rue Saint-Jean
insert into room values('50 Rue Saint-Jean', 'Rosenblatt Hotels', true, 270.00, 2, 'ocean');
insert into room values('50 Rue Saint-Jean', 'Rosenblatt Hotels', false, 320.00, 3, 'mountain');
insert into room values('50 Rue Saint-Jean', 'Rosenblatt Hotels', true, 370.00, 4, 'ocean');
insert into room values('50 Rue Saint-Jean', 'Rosenblatt Hotels', false, 420.00, 6, 'mountain');
insert into room values('50 Rue Saint-Jean', 'Rosenblatt Hotels', true, 470.00, 7, 'ocean');

-- Rosenblatt Hotels - 123 Jasper Avenue
insert into room values('123 Jasper Avenue', 'Rosenblatt Hotels', true, 290.00, 2, 'mountain');
insert into room values('123 Jasper Avenue', 'Rosenblatt Hotels', false, 340.00, 3, 'ocean');
insert into room values('123 Jasper Avenue', 'Rosenblatt Hotels', true, 390.00, 4, 'mountain');
insert into room values('123 Jasper Avenue', 'Rosenblatt Hotels', false, 440.00, 5, 'ocean');
insert into room values('123 Jasper Avenue', 'Rosenblatt Hotels', true, 490.00, 8, 'mountain');

-- Rosenblatt Hotels - 550 Main Street
insert into room values('550 Main Street', 'Rosenblatt Hotels', true, 310.00, 2, 'ocean');
insert into room values('550 Main Street', 'Rosenblatt Hotels', false, 360.00, 3, 'mountain');
insert into room values('550 Main Street', 'Rosenblatt Hotels', true, 410.00, 4, 'ocean');
insert into room values('550 Main Street', 'Rosenblatt Hotels', false, 460.00, 5, 'mountain');
insert into room values('550 Main Street', 'Rosenblatt Hotels', true, 510.00, 7, 'ocean');

''')

cur.execute('''create table amenities (
                    chain_name varchar(30),
                    hotel_address varchar(30),
                    room_id int,
                    amenity varchar(30),
                    constraint pk_amenities primary key (chain_name, hotel_address, room_id, amenity),
                    foreign key (chain_name, hotel_address, room_id) references room (chain_name, hotel_address, room_id)
                );
            ''')

cur.execute('''
-- Ottawa Hotels - 303 Sandy Street
insert into amenities values('Ottawa Hotels', '303 Sandy Street', 'Wi-Fi');
insert into amenities values('Ottawa Hotels', '303 Sandy Street', 'Gym');
insert into amenities values('Ottawa Hotels', '303 Sandy Street', 'Pool');
insert into amenities values('Ottawa Hotels', '303 Sandy Street', 'Breakfast');
insert into amenities values('Ottawa Hotels', '303 Sandy Street', 'Parking');

-- Ottawa Hotels - 402 Tremblent Way
insert into amenities values('Ottawa Hotels', '402 Tremblent Way', 'Wi-Fi');
insert into amenities values('Ottawa Hotels', '402 Tremblent Way', 'Gym');
insert into amenities values('Ottawa Hotels', '402 Tremblent Way', 'Pool');
insert into amenities values('Ottawa Hotels', '402 Tremblent Way', 'Breakfast');
insert into amenities values('Ottawa Hotels', '402 Tremblent Way', 'Parking');

-- Ottawa Hotels - 45 Elgin Street
insert into amenities values('Ottawa Hotels', '45 Elgin Street', 'Wi-Fi');
insert into amenities values('Ottawa Hotels', '45 Elgin Street', 'Gym');
insert into amenities values('Ottawa Hotels', '45 Elgin Street', 'Pool');
insert into amenities values('Ottawa Hotels', '45 Elgin Street', 'Breakfast');
insert into amenities values('Ottawa Hotels', '45 Elgin Street', 'Parking');

-- Ottawa Hotels - 201 Rideau Street
insert into amenities values('Ottawa Hotels', '201 Rideau Street', 'Wi-Fi');
insert into amenities values('Ottawa Hotels', '201 Rideau Street', 'Gym');
insert into amenities values('Ottawa Hotels', '201 Rideau Street', 'Pool');
insert into amenities values('Ottawa Hotels', '201 Rideau Street', 'Breakfast');
insert into amenities values('Ottawa Hotels', '201 Rideau Street', 'Parking');

-- Ottawa Hotels - 39 Snow Drive
insert into amenities values('Ottawa Hotels', '39 Snow Drive', 'Wi-Fi');
insert into amenities values('Ottawa Hotels', '39 Snow Drive', 'Gym');
insert into amenities values('Ottawa Hotels', '39 Snow Drive', 'Pool');
insert into amenities values('Ottawa Hotels', '39 Snow Drive', 'Breakfast');
insert into amenities values('Ottawa Hotels', '39 Snow Drive', 'Parking');

-- Ottawa Hotels - 17 Autumn Street
insert into amenities values('Ottawa Hotels', '17 Autumn Street', 'Wi-Fi');
insert into amenities values('Ottawa Hotels', '17 Autumn Street', 'Gym');
insert into amenities values('Ottawa Hotels', '17 Autumn Street', 'Pool');
insert into amenities values('Ottawa Hotels', '17 Autumn Street', 'Breakfast');
insert into amenities values('Ottawa Hotels', '17 Autumn Street', 'Parking');

-- Ottawa Hotels - 92 Pineview Crescent
insert into amenities values('Ottawa Hotels', '92 Pineview Crescent', 'Wi-Fi');
insert into amenities values('Ottawa Hotels', '92 Pineview Crescent', 'Gym');
insert into amenities values('Ottawa Hotels', '92 Pineview Crescent', 'Pool');
insert into amenities values('Ottawa Hotels', '92 Pineview Crescent', 'Breakfast');
insert into amenities values('Ottawa Hotels', '92 Pineview Crescent', 'Parking');

-- Ottawa Hotels - 14 Pleasant Park Road
insert into amenities values('Ottawa Hotels', '14 Pleasant Park Road', 'Wi-Fi');
insert into amenities values('Ottawa Hotels', '14 Pleasant Park Road', 'Gym');
insert into amenities values('Ottawa Hotels', '14 Pleasant Park Road', 'Pool');
insert into amenities values('Ottawa Hotels', '14 Pleasant Park Road', 'Breakfast');
insert into amenities values('Ottawa Hotels', '14 Pleasant Park Road', 'Parking');

-- Comfort Stay - 333 Bresserer Street
insert into amenities values('Comfort Stay', '333 Bresserer Street', 'Wi-Fi');
insert into amenities values('Comfort Stay', '333 Bresserer Street', 'Gym');
insert into amenities values('Comfort Stay', '333 Bresserer Street', 'Pool');
insert into amenities values('Comfort Stay', '333 Bresserer Street', 'Breakfast');
insert into amenities values('Comfort Stay', '333 Bresserer Street', 'Parking');

-- Comfort Stay - 154 Wrightville Way
insert into amenities values('Comfort Stay', '154 Wrightville Way', 'Wi-Fi');
insert into amenities values('Comfort Stay', '154 Wrightville Way', 'Gym');
insert into amenities values('Comfort Stay', '154 Wrightville Way', 'Pool');
insert into amenities values('Comfort Stay', '154 Wrightville Way', 'Breakfast');
insert into amenities values('Comfort Stay', '154 Wrightville Way', 'Parking');

-- Comfort Stay - 46 Elgin Street
insert into amenities values('Comfort Stay', '46 Elgin Street', 'Wi-Fi');
insert into amenities values('Comfort Stay', '46 Elgin Street', 'Gym');
insert into amenities values('Comfort Stay', '46 Elgin Street', 'Pool');
insert into amenities values('Comfort Stay', '46 Elgin Street', 'Breakfast');
insert into amenities values('Comfort Stay', '46 Elgin Street', 'Parking');

-- Comfort Stay - 30 Qualicum Street
insert into amenities values('Comfort Stay', '30 Qualicum Street', 'Wi-Fi');
insert into amenities values('Comfort Stay', '30 Qualicum Street', 'Gym');
insert into amenities values('Comfort Stay', '30 Qualicum Street', 'Pool');
insert into amenities values('Comfort Stay', '30 Qualicum Street', 'Breakfast');
insert into amenities values('Comfort Stay', '30 Qualicum Street', 'Parking');

-- Comfort Stay - 53 Ascot Avenue
insert into amenities values('Comfort Stay', '53 Ascot Avenue', 'Wi-Fi');
insert into amenities values('Comfort Stay', '53 Ascot Avenue', 'Gym');
insert into amenities values('Comfort Stay', '53 Ascot Avenue', 'Pool');
insert into amenities values('Comfort Stay', '53 Ascot Avenue', 'Breakfast');
insert into amenities values('Comfort Stay', '53 Ascot Avenue', 'Parking');

-- Comfort Stay - 62 Seyton Drive
insert into amenities values('Comfort Stay', '62 Seyton Drive', 'Wi-Fi');
insert into amenities values('Comfort Stay', '62 Seyton Drive', 'Gym');
insert into amenities values('Comfort Stay', '62 Seyton Drive', 'Pool');
insert into amenities values('Comfort Stay', '62 Seyton Drive', 'Breakfast');
insert into amenities values('Comfort Stay', '62 Seyton Drive', 'Parking');

-- Comfort Stay - 38 McClellan Road
insert into amenities values('Comfort Stay', '38 McClellan Road', 'Wi-Fi');
insert into amenities values('Comfort Stay', '38 McClellan Road', 'Gym');
insert into amenities values('Comfort Stay', '38 McClellan Road', 'Pool');
insert into amenities values('Comfort Stay', '38 McClellan Road', 'Breakfast');
insert into amenities values('Comfort Stay', '38 McClellan Road', 'Parking');

-- Comfort Stay - 48 Capital Drive
insert into amenities values('Comfort Stay', '48 Capital Drive', 'Wi-Fi');
insert into amenities values('Comfort Stay', '48 Capital Drive', 'Gym');
insert into amenities values('Comfort Stay', '48 Capital Drive', 'Pool');
insert into amenities values('Comfort Stay', '48 Capital Drive', 'Breakfast');
insert into amenities values('Comfort Stay', '48 Capital Drive', 'Parking');

-- Maximize Hotels - 59 Main Street
insert into amenities values('Maximize Hotels', '59 Main Street', 'Wi-Fi');
insert into amenities values('Maximize Hotels', '59 Main Street', 'Gym');
insert into amenities values('Maximize Hotels', '59 Main Street', 'Pool');
insert into amenities values('Maximize Hotels', '59 Main Street', 'Breakfast');
insert into amenities values('Maximize Hotels', '59 Main Street', 'Parking');

-- Maximize Hotels - 72 Broadway Ave
insert into amenities values('Maximize Hotels', '72 Broadway Ave', 'Wi-Fi');
insert into amenities values('Maximize Hotels', '72 Broadway Ave', 'Gym');
insert into amenities values('Maximize Hotels', '72 Broadway Ave', 'Pool');
insert into amenities values('Maximize Hotels', '72 Broadway Ave', 'Breakfast');
insert into amenities values('Maximize Hotels', '72 Broadway Ave', 'Parking');

-- Maximize Hotels - 15 Rue de la Paix
insert into amenities values('Maximize Hotels', '15 Rue de la Paix', 'Wi-Fi');
insert into amenities values('Maximize Hotels', '15 Rue de la Paix', 'Gym');
insert into amenities values('Maximize Hotels', '15 Rue de la Paix', 'Pool');
insert into amenities values('Maximize Hotels', '15 Rue de la Paix', 'Breakfast');
insert into amenities values('Maximize Hotels', '15 Rue de la Paix', 'Parking');

-- Maximize Hotels - 100 Sunset Blvd
insert into amenities values('Maximize Hotels', '100 Sunset Blvd', 'Wi-Fi');
insert into amenities values('Maximize Hotels', '100 Sunset Blvd', 'Gym');
insert into amenities values('Maximize Hotels', '100 Sunset Blvd', 'Pool');
insert into amenities values('Maximize Hotels', '100 Sunset Blvd', 'Breakfast');
insert into amenities values('Maximize Hotels', '100 Sunset Blvd', 'Parking');

-- Maximize Hotels - 47 Oxford Street
insert into amenities values('Maximize Hotels', '47 Oxford Street', 'Wi-Fi');
insert into amenities values('Maximize Hotels', '47 Oxford Street', 'Gym');
insert into amenities values('Maximize Hotels', '47 Oxford Street', 'Pool');
insert into amenities values('Maximize Hotels', '47 Oxford Street', 'Breakfast');
insert into amenities values('Maximize Hotels', '47 Oxford Street', 'Parking');

-- Maximize Hotels - 300 Shibuya Crossing
insert into amenities values('Maximize Hotels', '300 Shibuya Crossing', 'Wi-Fi');
insert into amenities values('Maximize Hotels', '300 Shibuya Crossing', 'Gym');
insert into amenities values('Maximize Hotels', '300 Shibuya Crossing', 'Pool');
insert into amenities values('Maximize Hotels', '300 Shibuya Crossing', 'Breakfast');
insert into amenities values('Maximize Hotels', '300 Shibuya Crossing', 'Parking');

-- Maximize Hotels - 100 Mountain View Road
insert into amenities values('Maximize Hotels', '100 Mountain View Road', 'Wi-Fi');
insert into amenities values('Maximize Hotels', '100 Mountain View Road', 'Gym');
insert into amenities values('Maximize Hotels', '100 Mountain View Road', 'Pool');
insert into amenities values('Maximize Hotels', '100 Mountain View Road', 'Breakfast');
insert into amenities values('Maximize Hotels', '100 Mountain View Road', 'Parking');

-- Maximize Hotels - 21 Beachside Drive
insert into amenities values('Maximize Hotels', '21 Beachside Drive', 'Wi-Fi');
insert into amenities values('Maximize Hotels', '21 Beachside Drive', 'Gym');
insert into amenities values('Maximize Hotels', '21 Beachside Drive', 'Pool');
insert into amenities values('Maximize Hotels', '21 Beachside Drive', 'Breakfast');
insert into amenities values('Maximize Hotels', '21 Beachside Drive', 'Parking');

-- Klaradon - 35 Lakeshore Drive
insert into amenities values('Klaradon', '35 Lakeshore Drive', 'Wi-Fi');
insert into amenities values('Klaradon', '35 Lakeshore Drive', 'Gym');
insert into amenities values('Klaradon', '35 Lakeshore Drive', 'Pool');
insert into amenities values('Klaradon', '35 Lakeshore Drive', 'Breakfast');
insert into amenities values('Klaradon', '35 Lakeshore Drive', 'Parking');

-- Klaradon - 35 Humphrey Drive
insert into amenities values('Klaradon', '35 Humphrey Drive', 'Wi-Fi');
insert into amenities values('Klaradon', '35 Humphrey Drive', 'Gym');
insert into amenities values('Klaradon', '35 Humphrey Drive', 'Pool');
insert into amenities values('Klaradon', '35 Humphrey Drive', 'Breakfast');
insert into amenities values('Klaradon', '35 Humphrey Drive', 'Parking');

-- Klaradon - 45 Queen Street
insert into amenities values('Klaradon', '45 Queen Street', 'Wi-Fi');
insert into amenities values('Klaradon', '45 Queen Street', 'Gym');
insert into amenities values('Klaradon', '45 Queen Street', 'Pool');
insert into amenities values('Klaradon', '45 Queen Street', 'Breakfast');
insert into amenities values('Klaradon', '45 Queen Street', 'Parking');

-- Klaradon - 120 Pacific Blvd
insert into amenities values('Klaradon', '120 Pacific Blvd', 'Wi-Fi');
insert into amenities values('Klaradon', '120 Pacific Blvd', 'Gym');
insert into amenities values('Klaradon', '120 Pacific Blvd', 'Pool');
insert into amenities values('Klaradon', '120 Pacific Blvd', 'Breakfast');
insert into amenities values('Klaradon', '120 Pacific Blvd', 'Parking');

-- Klaradon - 60 Elgin Street
insert into amenities values('Klaradon', '60 Elgin Street', 'Wi-Fi');
insert into amenities values('Klaradon', '60 Elgin Street', 'Gym');
insert into amenities values('Klaradon', '60 Elgin Street', 'Pool');
insert into amenities values('Klaradon', '60 Elgin Street', 'Breakfast');
insert into amenities values('Klaradon', '60 Elgin Street', 'Parking');

-- Klaradon - 10 Calgary Road
insert into amenities values('Klaradon', '10 Calgary Road', 'Wi-Fi');
insert into amenities values('Klaradon', '10 Calgary Road', 'Gym');
insert into amenities values('Klaradon', '10 Calgary Road', 'Pool');
insert into amenities values('Klaradon', '10 Calgary Road', 'Breakfast');
insert into amenities values('Klaradon', '10 Calgary Road', 'Parking');

-- Klaradon - 75 Saint Catherine Street
insert into amenities values('Klaradon', '75 Saint Catherine Street', 'Wi-Fi');
insert into amenities values('Klaradon', '75 Saint Catherine Street', 'Gym');
insert into amenities values('Klaradon', '75 Saint Catherine Street', 'Pool');
insert into amenities values('Klaradon', '75 Saint Catherine Street', 'Breakfast');
insert into amenities values('Klaradon', '75 Saint Catherine Street', 'Parking');

-- Klaradon - 22 Old Port Road
insert into amenities values('Klaradon', '22 Old Port Road', 'Wi-Fi');
insert into amenities values('Klaradon', '22 Old Port Road', 'Gym');
insert into amenities values('Klaradon', '22 Old Port Road', 'Pool');
insert into amenities values('Klaradon', '22 Old Port Road', 'Breakfast');
insert into amenities values('Klaradon', '22 Old Port Road', 'Parking');

-- Rosenblatt Hotels - 812 Stittsville Street
insert into amenities values('Rosenblatt Hotels', '812 Stittsville Street', 'Wi-Fi');
insert into amenities values('Rosenblatt Hotels', '812 Stittsville Street', 'Gym');
insert into amenities values('Rosenblatt Hotels', '812 Stittsville Street', 'Pool');
insert into amenities values('Rosenblatt Hotels', '812 Stittsville Street', 'Breakfast');
insert into amenities values('Rosenblatt Hotels', '812 Stittsville Street', 'Parking');

-- Rosenblatt Hotels - 214 Granville Street
insert into amenities values('Rosenblatt Hotels', '214 Granville Street', 'Wi-Fi');
insert into amenities values('Rosenblatt Hotels', '214 Granville Street', 'Gym');
insert into amenities values('Rosenblatt Hotels', '214 Granville Street', 'Pool');
insert into amenities values('Rosenblatt Hotels', '214 Granville Street', 'Breakfast');
insert into amenities values('Rosenblatt Hotels', '214 Granville Street', 'Parking');

-- Rosenblatt Hotels - 67 Crescent Street
insert into amenities values('Rosenblatt Hotels', '67 Crescent Street', 'Wi-Fi');
insert into amenities values('Rosenblatt Hotels', '67 Crescent Street', 'Gym');
insert into amenities values('Rosenblatt Hotels', '67 Crescent Street', 'Pool');
insert into amenities values('Rosenblatt Hotels', '67 Crescent Street', 'Breakfast');
insert into amenities values('Rosenblatt Hotels', '67 Crescent Street', 'Parking');

-- Rosenblatt Hotels - 98 16th Avenue NW
insert into amenities values('Rosenblatt Hotels', '98 16th Avenue NW', 'Wi-Fi');
insert into amenities values('Rosenblatt Hotels', '98 16th Avenue NW', 'Gym');
insert into amenities values('Rosenblatt Hotels', '98 16th Avenue NW', 'Pool');
insert into amenities values('Rosenblatt Hotels', '98 16th Avenue NW', 'Breakfast');
insert into amenities values('Rosenblatt Hotels', '98 16th Avenue NW', 'Parking');

-- Rosenblatt Hotels - 45 Wellington Street
insert into amenities values('Rosenblatt Hotels', '45 Wellington Street', 'Wi-Fi');
insert into amenities values('Rosenblatt Hotels', '45 Wellington Street', 'Gym');
insert into amenities values('Rosenblatt Hotels', '45 Wellington Street', 'Pool');
insert into amenities values('Rosenblatt Hotels', '45 Wellington Street', 'Breakfast');
insert into amenities values('Rosenblatt Hotels', '45 Wellington Street', 'Parking');

-- Rosenblatt Hotels - 50 Rue Saint-Jean
insert into amenities values('Rosenblatt Hotels', '50 Rue Saint-Jean', 'Wi-Fi');
insert into amenities values('Rosenblatt Hotels', '50 Rue Saint-Jean', 'Gym');
insert into amenities values('Rosenblatt Hotels', '50 Rue Saint-Jean', 'Pool');
insert into amenities values('Rosenblatt Hotels', '50 Rue Saint-Jean', 'Breakfast');
insert into amenities values('Rosenblatt Hotels', '50 Rue Saint-Jean', 'Parking');

-- Rosenblatt Hotels - 123 Jasper Avenue
insert into amenities values('Rosenblatt Hotels', '123 Jasper Avenue', 'Wi-Fi');
insert into amenities values('Rosenblatt Hotels', '123 Jasper Avenue', 'Gym');
insert into amenities values('Rosenblatt Hotels', '123 Jasper Avenue', 'Pool');
insert into amenities values('Rosenblatt Hotels', '123 Jasper Avenue', 'Breakfast');
insert into amenities values('Rosenblatt Hotels', '123 Jasper Avenue', 'Parking');

-- Rosenblatt Hotels - 550 Main Street
insert into amenities values('Rosenblatt Hotels', '550 Main Street', 'Wi-Fi');
insert into amenities values('Rosenblatt Hotels', '550 Main Street', 'Gym');
insert into amenities values('Rosenblatt Hotels', '550 Main Street', 'Pool');
insert into amenities values('Rosenblatt Hotels', '550 Main Street', 'Breakfast');
insert into amenities values('Rosenblatt Hotels', '550 Main Street', 'Parking');
''')

cur.execute("drop table if exists damage;")

cur.execute('''create table damage (
                    chain_name varchar(30),
                    hotel_address varchar(30),
                    room_id int,
                    damage varchar(30),
                    constraint pk_damage primary key (chain_name, hotel_address, room_id, damage),
                    foreign key (chain_name, hotel_address, room_id) references room (chain_name, hotel_address, room_id)
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
