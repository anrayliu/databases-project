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
insert into hotel_chain values('Ottawa Hotels', 8);
insert into hotel_chain values('Comfort Stay', 8);
insert into hotel_chain values('Maximize Hotels', 8);
insert into hotel_chain values('Klaradon', 8);
insert into hotel_chain values('Rosenblatt Hotels', 8);
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
                    email varchar(60),
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
insert into hotel values('otthotel.sandyhill@gmail.com', 4, 5, '303 Sandy Street', 'Ottawa Hotels', 'John Dosely');
insert into hotel values('otthotel.gatineau@gmail.com', 3, 5, '402 Tremblent Way', 'Ottawa Hotels', 'Jane Dosely');
insert into hotel values('otthotel.elgin@gmail.com', 2, 5, '45 Elgin Street', 'Ottawa Hotels', 'Luke Peters');
insert into hotel values('otthotel.rideau@gmail.com', 3, 5, '201 Rideau Street', 'Ottawa Hotels', 'Victor Matthews');
insert into hotel values('otthotel.kanata@gmail.com', 3, 5, '39 Snow Drive', 'Ottawa Hotels', 'Joshua Kayley');
insert into hotel values('otthotel.stittsville@gmail.com', 2, 5, '17 Autumn Street', 'Ottawa Hotels', 'Anray Liu');
insert into hotel values('otthotel.westOtt@gmail.com', 4, 5, '92 Pineview Crescent', 'Ottawa Hotels', 'Willard Hickling');
insert into hotel values('otthotel.urbandale@gmail.com', 2, 5, '14 Pleasant Park Road', 'Ottawa Hotels', 'Roberto Haisty');


insert into hotel values('comfstayOttawa@hotmail.com', 2, 5, '333 Bresserer Street', 'Comfort Stay', 'Sammy Ross');
insert into hotel values('comfstayGatineau@hotmail.com', 5, 5, '154 Wrightville Way', 'Comfort Stay', 'Charlie E. Hook');
insert into hotel values('comfstayElgin@hotmail.com', 2, 5, '46 Elgin Street', 'Comfort Stay', 'Frederick Spurgin');
insert into hotel values('comfstayKanata@hotmail.com', 3, 5, '30 Qualicum Street', 'Comfort Stay', 'Milton Shwift');
insert into hotel values('comfstayLynwood@hotmail.com', 4, 5, '53 Ascot Avenue', 'Comfort Stay', 'Johnathan Rico');
insert into hotel values('comfstayWestcliffe@hotmail.com', 2, 5, '62 Seyton Drive', 'Comfort Stay', 'Frank Browser');
insert into hotel values('comfstayArlington@hotmail.com', 4, 5, '38 McClellan Road', 'Comfort Stay', 'Bertha Leamy');
insert into hotel values('comfstayMerivale@hotmail.com', 1, 5, '48 Capital Drive', 'Comfort Stay', 'Jamie Thomas');

insert into hotel values('maximizeOttawa@gmail.com', 5, 5, '59 Main Street', 'Maximize Hotels', 'Elisha Travers');
insert into hotel values('maximizeNewYork@gmail.com', 4, 5, '72 Broadway Ave', 'Maximize Hotels', 'Sarah Johnson');
insert into hotel values('maximizeParis@gmail.com', 3, 5, '15 Rue de la Paix', 'Maximize Hotels', 'Lucie Dupont');
insert into hotel values('maximizeCalifornia@gmail.com', 5, 5, '100 Sunset Blvd', 'Maximize Hotels', 'Mark Thompson');
insert into hotel values('maximizeLondon@gmail.com', 4, 5, '47 Oxford Street', 'Maximize Hotels', 'Emma Parker');
insert into hotel values('maximizeTokyo@gmail.com', 3, 5, '300 Shibuya Crossing', 'Maximize Hotels', 'Hiroshi Tanaka');
insert into hotel values('maximizeMountainLodge@gmail.com', 5, 5, '100 Mountain View Road', 'Maximize Hotels', 'James Mitchell');
insert into hotel values('maximizeCoastalEscape@gmail.com', 4, 5, '21 Beachside Drive', 'Maximize Hotels', 'Nina Williams');

insert into hotel values('klaradonBurlington@gmail.com', 4, 5, '35 Lakeshore Drive', 'Klaradon', 'Manny Stevens');
insert into hotel values('klaradonWaterdown@gmail.com', 3, 5, '35 Humphrey Drive', 'Klaradon', 'Matthew Boyle');
insert into hotel values('klaradonToronto@gmail.com', 3, 5, '45 Queen Street', 'Klaradon', 'Lisa Green');
insert into hotel values('klaradonVancouver@gmail.com', 5, 150, '120 Pacific Blvd', 'Klaradon', 'John Harris');
insert into hotel values('klaradonOttawa@gmail.com', 4, 5, '60 Elgin Street', 'Klaradon', 'Rachel Adams');
insert into hotel values('klaradonCalgary@gmail.com', 3, 5, '10 Calgary Road', 'Klaradon', 'David Brown');
insert into hotel values('klaradonMontreal@gmail.com', 5, 5, '75 Saint Catherine Street', 'Klaradon', 'Jessica Lee');
insert into hotel values('klaradonQuebecCity@gmail.com', 4, 5, '22 Old Port Road', 'Klaradon', 'Michael Roberts');

insert into hotel values('rosenblatToronto@gmail.com', 5, 5, '812 Stittsville Street', 'Rosenblatt Hotels', 'Atom Rosenblatt');
insert into hotel values('rosenblattVancouver@gmail.com', 4, 5, '214 Granville Street', 'Rosenblatt Hotels', 'Sophie Cohen');
insert into hotel values('rosenblattMontreal@gmail.com', 3, 5, '67 Crescent Street', 'Rosenblatt Hotels', 'Daniel Kim');
insert into hotel values('rosenblattCalgary@gmail.com', 5, 5, '98 16th Avenue NW', 'Rosenblatt Hotels', 'Lena Patel');
insert into hotel values('rosenblattOttawa@gmail.com', 4, 5, '45 Wellington Street', 'Rosenblatt Hotels', 'Matthew Davis');
insert into hotel values('rosenblattQuebecCity@gmail.com', 3, 5, '50 Rue Saint-Jean', 'Rosenblatt Hotels', 'Chloe Lee');
insert into hotel values('rosenblattEdmonton@gmail.com', 5, 5, '123 Jasper Avenue', 'Rosenblatt Hotels', 'Ethan Smith');
insert into hotel values('rosenblattWinnipeg@gmail.com', 4, 5, '550 Main Street', 'Rosenblatt Hotels', 'Olivia Martinez');
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
                    password varchar(30),
                    PRIMARY KEY(id)
                );
            ''')
cur.execute('''
insert into customer values('000000', 'Valentino Vinod', '720 Rideau Street', '28/03/20', 'password1');
insert into customer values('000001', 'Anray Liu', '100 Rideau Street', '13/02/23', '123456789');
insert into customer values('000002', 'Adam Rosenblatt', '382 Markhamm Way', '05/10/24', 'qwerty');
insert into customer values('000003', 'Manny Matthews', '48 Blue Sky Way', '20/01/25', 'password');
insert into customer values('000004', 'Maradin Leo', '34 Wacky Street', '14/08/25', 'strongPassword');
''')


cur.execute("drop table if exists employee cascade;")

cur.execute('''create table employee (
                    employee_name varchar(30),
                    employee_address varchar(30),
                    password varchar(30),
                    ssn int,
                    PRIMARY KEY(ssn)
                );
            ''')

cur.execute('''
insert into employee values('John Doe', '123 Elm St', 'password1', 100001234);
insert into employee values('Jane Smith', '456 Oak St', '123456789', 100002345);
insert into employee values('Alice Johnson', '789 Pine St', 'qwerty', 100003456);
insert into employee values('Bob Brown', '101 Maple St', 'strongPassword', 100004567);
insert into employee values('Charlie Davis', '202 Birch St', 'password', 100005678);
insert into employee values('Deborah Wilson', '303 Cedar St', 'qwerty', 100006789);
insert into employee values('Edward Moore', '404 Walnut St', '9876543210', 100007890);
insert into employee values('Fiona White', '505 Chestnut St', '123456789', 100008901);
insert into employee values('George Harris', '606 Ash St', '!@#$%^&*()', 100009012);
insert into employee values('Hannah Clark', '707 Willow St', 'q1w2e3r4t5y6', 100010123);
insert into employee values('Isaac Lewis', '808 Redwood St', 'abcdefg', 100011234);
insert into employee values('Jackie Scott', '909 Pinecrest St', 'hijkl', 100012345);
insert into employee values('Kevin Martin', '101 Birchwood St', 'mnopqr', 100013456);
insert into employee values('Laura Young', '202 Oakdale St', 'stuvwxyz', 100014567);
insert into employee values('Michael King', '303 Maplewood St', '12345', 100015678);
insert into employee values('Nina Adams', '404 Elmwood St', '67890', 100016789);
insert into employee values('Oscar Nelson', '505 Oakview St', 'zxcvbnm', 100017890);
insert into employee values('Patricia Carter', '606 Ashwood St', 'asdfghjkl', 100018901);
insert into employee values('Quinn Mitchell', '707 Cedarwood St', 'qwertyuiop', 100019012);
insert into employee values('Rachel Robinson', '808 Chestnutwood St', 'qazxswedcvfr', 100020123);
insert into employee values('Samuel Clark', '909 Redwoodview St', 'bgtnhymjukilop', 100021234);
insert into employee values('Tina Perez', '101 Mapleview St', '1234567890', 100022345);
insert into employee values('Ursula Lee', '202 Birchview St', '0987654321', 100023456);
insert into employee values('Victor Hall', '303 Willowview St', 'valentinoPassword', 100024567);
insert into employee values('Wendy Allen', '404 Pineview St', 'adamPassoword', 100025678);
insert into employee values('Xander Scott', '505 Cedarview St', 'anrayPassword', 100026789);
insert into employee values('Yvonne Gonzalez', '606 Oakview St', '123456789', 100027890);
insert into employee values('Zane Martinez', '707 Redwoodview St', '1qaz2wsx3edc4rfv', 100028901);
insert into employee values('Amelia Carter', '808 Pineview St', '5tgb6yhn7ujm', 100029012);
insert into employee values('Brandon Clark', '909 Ashview St', 'password', 100030123);
insert into employee values('Carmen Thompson', '101 Willowview St', 'password1', 100031234);
insert into employee values('Diana Lewis', '202 Chestnutview St', 'password2', 100032345);
insert into employee values('Elliot Harris', '303 Mapleview St', 'password3', 100033456);
insert into employee values('Felicia Evans', '404 Oakwood St', 'password4', 100034567);
insert into employee values('Graham Walker', '505 Ashwood St', 'password5', 100035678);
insert into employee values('Helen Green', '606 Cedarwood St', 'password6', 100036789);
insert into employee values('Ian White', '707 Redwood St', 'password7', 100037890);
insert into employee values('Julia Young', '808 Pinecrest St', 'password8', 100038901);
insert into employee values('Kyle Mitchell', '909 Birch St', 'password9', 100039012);
insert into employee values('Lana Moore', '101 Elmwood St', 'password10', 100040123);
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
insert into works_at values('Ottawa Hotels', '92 Pineview Crescent', 100040123, 'Porter');
''')

cur.execute("drop table if exists room cascade;")

cur.execute('''create table room (
                    room_id int,
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
insert into room values('100001', '303 Sandy Street', 'Ottawa Hotels', true, 120.00, 1, 'mountain');
insert into room values('100002', '303 Sandy Street', 'Ottawa Hotels', false, 160.00, 2, 'ocean');
insert into room values('100003', '303 Sandy Street', 'Ottawa Hotels', true, 210.00, 3, 'mountain');
insert into room values('100004', '303 Sandy Street', 'Ottawa Hotels', false, 260.00, 4, 'ocean');
insert into room values('100005', '303 Sandy Street', 'Ottawa Hotels', true, 310.00, 5, 'mountain');

-- Ottawa Hotels - 402 Tremblent Way
insert into room values('100006', '402 Tremblent Way', 'Ottawa Hotels', true, 150.00, 1, 'mountain');
insert into room values('100007', '402 Tremblent Way', 'Ottawa Hotels', false, 200.00, 2, 'ocean');
insert into room values('100008', '402 Tremblent Way', 'Ottawa Hotels', true, 250.00, 3, 'mountain');
insert into room values('100009', '402 Tremblent Way', 'Ottawa Hotels', false, 300.00, 5, 'ocean');
insert into room values('100010', '402 Tremblent Way', 'Ottawa Hotels', true, 350.00, 7, 'mountain');

-- Ottawa Hotels - 45 Elgin Street
insert into room values('100011', '45 Elgin Street', 'Ottawa Hotels', true, 180.00, 1, 'ocean');
insert into room values('100012', '45 Elgin Street', 'Ottawa Hotels', false, 230.00, 2, 'mountain');
insert into room values('100013', '45 Elgin Street', 'Ottawa Hotels', true, 280.00, 3, 'ocean');
insert into room values('100014', '45 Elgin Street', 'Ottawa Hotels', false, 330.00, 4, 'mountain');
insert into room values('100015', '45 Elgin Street', 'Ottawa Hotels', true, 380.00, 6, 'ocean');

-- Ottawa Hotels - 201 Rideau Street
insert into room values('100016', '201 Rideau Street', 'Ottawa Hotels', true, 220.00, 2, 'mountain');
insert into room values('100017', '201 Rideau Street', 'Ottawa Hotels', false, 270.00, 3, 'ocean');
insert into room values('100018', '201 Rideau Street', 'Ottawa Hotels', true, 320.00, 4, 'mountain');
insert into room values('100019', '201 Rideau Street', 'Ottawa Hotels', false, 370.00, 5, 'ocean');
insert into room values('100020', '201 Rideau Street', 'Ottawa Hotels', true, 420.00, 7, 'mountain');

-- Ottawa Hotels - 39 Snow Drive
insert into room values('100021', '39 Snow Drive', 'Ottawa Hotels', true, 210.00, 1, 'ocean');
insert into room values('100022', '39 Snow Drive', 'Ottawa Hotels', false, 260.00, 2, 'mountain');
insert into room values('100023', '39 Snow Drive', 'Ottawa Hotels', true, 310.00, 3, 'ocean');
insert into room values('100024', '39 Snow Drive', 'Ottawa Hotels', false, 360.00, 5, 'mountain');
insert into room values('100025', '39 Snow Drive', 'Ottawa Hotels', true, 410.00, 8, 'ocean');

-- Ottawa Hotels - 17 Autumn Street
insert into room values('100026', '17 Autumn Street', 'Ottawa Hotels', true, 180.00, 1, 'mountain');
insert into room values('100027', '17 Autumn Street', 'Ottawa Hotels', false, 230.00, 2, 'ocean');
insert into room values('100028', '17 Autumn Street', 'Ottawa Hotels', true, 280.00, 3, 'mountain');
insert into room values('100029', '17 Autumn Street', 'Ottawa Hotels', false, 330.00, 5, 'ocean');
insert into room values('100030', '17 Autumn Street', 'Ottawa Hotels', true, 380.00, 6, 'mountain');

-- Ottawa Hotels - 92 Pineview Crescent
insert into room values('100031', '92 Pineview Crescent', 'Ottawa Hotels', true, 190.00, 2, 'ocean');
insert into room values('100032', '92 Pineview Crescent', 'Ottawa Hotels', false, 240.00, 3, 'mountain');
insert into room values('100033', '92 Pineview Crescent', 'Ottawa Hotels', true, 290.00, 4, 'ocean');
insert into room values('100034', '92 Pineview Crescent', 'Ottawa Hotels', false, 340.00, 5, 'mountain');
insert into room values('100035', '92 Pineview Crescent', 'Ottawa Hotels', true, 390.00, 7, 'ocean');

-- Ottawa Hotels - 14 Pleasant Park Road
insert into room values('100036', '14 Pleasant Park Road', 'Ottawa Hotels', true, 200.00, 1, 'mountain');
insert into room values('100037', '14 Pleasant Park Road', 'Ottawa Hotels', false, 250.00, 2, 'ocean');
insert into room values('100038', '14 Pleasant Park Road', 'Ottawa Hotels', true, 300.00, 3, 'mountain');
insert into room values('100039', '14 Pleasant Park Road', 'Ottawa Hotels', false, 350.00, 5, 'ocean');
insert into room values('100040', '14 Pleasant Park Road', 'Ottawa Hotels', true, 400.00, 7, 'mountain');

-- Comfort Stay - 333 Bresserer Street
insert into room values('100041', '333 Bresserer Street', 'Comfort Stay', true, 120.00, 1, 'mountain');
insert into room values('100042', '333 Bresserer Street', 'Comfort Stay', false, 170.00, 2, 'ocean');
insert into room values('100043', '333 Bresserer Street', 'Comfort Stay', true, 220.00, 3, 'mountain');
insert into room values('100044', '333 Bresserer Street', 'Comfort Stay', false, 270.00, 4, 'ocean');
insert into room values('100045', '333 Bresserer Street', 'Comfort Stay', true, 320.00, 6, 'mountain');

-- Comfort Stay - 154 Wrightville Way
insert into room values('100046', '154 Wrightville Way', 'Comfort Stay', true, 130.00, 2, 'ocean');
insert into room values('100047', '154 Wrightville Way', 'Comfort Stay', false, 180.00, 3, 'mountain');
insert into room values('100048', '154 Wrightville Way', 'Comfort Stay', true, 230.00, 4, 'ocean');
insert into room values('100049', '154 Wrightville Way', 'Comfort Stay', false, 280.00, 5, 'mountain');
insert into room values('100050', '154 Wrightville Way', 'Comfort Stay', true, 330.00, 7, 'ocean');

-- Comfort Stay - 46 Elgin Street
insert into room values('100051', '46 Elgin Street', 'Comfort Stay', true, 140.00, 1, 'mountain');
insert into room values('100052', '46 Elgin Street', 'Comfort Stay', false, 190.00, 2, 'ocean');
insert into room values('100053', '46 Elgin Street', 'Comfort Stay', true, 240.00, 3, 'mountain');
insert into room values('100054', '46 Elgin Street', 'Comfort Stay', false, 290.00, 4, 'ocean');
insert into room values('100055', '46 Elgin Street', 'Comfort Stay', true, 340.00, 6, 'mountain');

-- Comfort Stay - 30 Qualicum Street
insert into room values('100056', '30 Qualicum Street', 'Comfort Stay', true, 150.00, 2, 'ocean');
insert into room values('100057', '30 Qualicum Street', 'Comfort Stay', false, 200.00, 3, 'mountain');
insert into room values('100058', '30 Qualicum Street', 'Comfort Stay', true, 250.00, 4, 'ocean');
insert into room values('100059', '30 Qualicum Street', 'Comfort Stay', false, 300.00, 5, 'mountain');
insert into room values('100060', '30 Qualicum Street', 'Comfort Stay', true, 350.00, 7, 'ocean');

-- Comfort Stay - 53 Ascot Avenue
insert into room values('100061', '53 Ascot Avenue', 'Comfort Stay', true, 160.00, 1, 'mountain');
insert into room values('100062', '53 Ascot Avenue', 'Comfort Stay', false, 210.00, 2, 'ocean');
insert into room values('100063', '53 Ascot Avenue', 'Comfort Stay', true, 260.00, 3, 'mountain');
insert into room values('100064', '53 Ascot Avenue', 'Comfort Stay', false, 310.00, 4, 'ocean');
insert into room values('100065', '53 Ascot Avenue', 'Comfort Stay', true, 360.00, 6, 'mountain');

-- Comfort Stay - 62 Seyton Drive
insert into room values('100066', '62 Seyton Drive', 'Comfort Stay', true, 170.00, 2, 'ocean');
insert into room values('100067', '62 Seyton Drive', 'Comfort Stay', false, 220.00, 3, 'mountain');
insert into room values('100068', '62 Seyton Drive', 'Comfort Stay', true, 270.00, 4, 'ocean');
insert into room values('100069', '62 Seyton Drive', 'Comfort Stay', false, 320.00, 5, 'mountain');
insert into room values('100070', '62 Seyton Drive', 'Comfort Stay', true, 370.00, 7, 'ocean');

-- Comfort Stay - 38 McClellan Road
insert into room values('100071', '38 McClellan Road', 'Comfort Stay', true, 180.00, 1, 'mountain');
insert into room values('100072', '38 McClellan Road', 'Comfort Stay', false, 230.00, 2, 'ocean');
insert into room values('100073', '38 McClellan Road', 'Comfort Stay', true, 280.00, 3, 'mountain');
insert into room values('100074', '38 McClellan Road', 'Comfort Stay', false, 330.00, 5, 'ocean');
insert into room values('100075', '38 McClellan Road', 'Comfort Stay', true, 380.00, 6, 'mountain');

-- Comfort Stay - 48 Capital Drive
insert into room values('100076', '48 Capital Drive', 'Comfort Stay', true, 190.00, 1, 'ocean');
insert into room values('100077', '48 Capital Drive', 'Comfort Stay', false, 240.00, 2, 'mountain');
insert into room values('100078', '48 Capital Drive', 'Comfort Stay', true, 290.00, 3, 'ocean');
insert into room values('100079', '48 Capital Drive', 'Comfort Stay', false, 340.00, 4, 'mountain');
insert into room values('100080', '48 Capital Drive', 'Comfort Stay', true, 390.00, 6, 'ocean');

-- Maximize Hotels - 59 Main Street
insert into room values('100081', '59 Main Street', 'Maximize Hotels', true, 150.50, 1, 'mountain');
insert into room values('100082', '59 Main Street', 'Maximize Hotels', false, 200.00, 2, 'ocean');
insert into room values('100083', '59 Main Street', 'Maximize Hotels', true, 250.00, 4, 'mountain');
insert into room values('100084', '59 Main Street', 'Maximize Hotels', false, 300.00, 6, 'ocean');
insert into room values('100085', '59 Main Street', 'Maximize Hotels', true, 350.00, 8, 'mountain');

-- Maximize Hotels - 72 Broadway Ave
insert into room values('100086', '72 Broadway Ave', 'Maximize Hotels', true, 180.00, 1, 'ocean');
insert into room values('100087', '72 Broadway Ave', 'Maximize Hotels', false, 220.00, 2, 'mountain');
insert into room values('100088', '72 Broadway Ave', 'Maximize Hotels', true, 270.00, 3, 'ocean');
insert into room values('100089', '72 Broadway Ave', 'Maximize Hotels', false, 330.00, 5, 'mountain');
insert into room values('100090', '72 Broadway Ave', 'Maximize Hotels', true, 380.00, 7, 'ocean');

-- Maximize Hotels - 15 Rue de la Paix
insert into room values('100091', '15 Rue de la Paix', 'Maximize Hotels', true, 210.00, 2, 'mountain');
insert into room values('100092', '15 Rue de la Paix', 'Maximize Hotels', false, 260.00, 3, 'ocean');
insert into room values('100093', '15 Rue de la Paix', 'Maximize Hotels', true, 310.00, 4, 'mountain');
insert into room values('100094', '15 Rue de la Paix', 'Maximize Hotels', false, 370.00, 6, 'ocean');
insert into room values('100095', '15 Rue de la Paix', 'Maximize Hotels', true, 420.00, 8, 'mountain');

-- Maximize Hotels - 100 Sunset Blvd
insert into room values('100096', '100 Sunset Blvd', 'Maximize Hotels', true, 230.00, 3, 'ocean');
insert into room values('100097', '100 Sunset Blvd', 'Maximize Hotels', false, 280.00, 4, 'mountain');
insert into room values('100098', '100 Sunset Blvd', 'Maximize Hotels', true, 330.00, 5, 'ocean');
insert into room values('100099', '100 Sunset Blvd', 'Maximize Hotels', false, 380.00, 6, 'mountain');
insert into room values('100100', '100 Sunset Blvd', 'Maximize Hotels', true, 430.00, 9, 'ocean');

-- Maximize Hotels - 47 Oxford Street
insert into room values('100101', '47 Oxford Street', 'Maximize Hotels', true, 160.00, 1, 'mountain');
insert into room values('100102', '47 Oxford Street', 'Maximize Hotels', false, 210.00, 2, 'ocean');
insert into room values('100103', '47 Oxford Street', 'Maximize Hotels', true, 260.00, 3, 'mountain');
insert into room values('100104', '47 Oxford Street', 'Maximize Hotels', false, 320.00, 5, 'ocean');
insert into room values('100105', '47 Oxford Street', 'Maximize Hotels', true, 370.00, 7, 'mountain');

-- Maximize Hotels - 300 Shibuya Crossing
insert into room values('100106', '300 Shibuya Crossing', 'Maximize Hotels', true, 270.00, 2, 'ocean');
insert into room values('100107', '300 Shibuya Crossing', 'Maximize Hotels', false, 320.00, 3, 'mountain');
insert into room values('100108', '300 Shibuya Crossing', 'Maximize Hotels', true, 370.00, 4, 'ocean');
insert into room values('100109', '300 Shibuya Crossing', 'Maximize Hotels', false, 420.00, 6, 'mountain');
insert into room values('100110', '300 Shibuya Crossing', 'Maximize Hotels', true, 470.00, 8, 'ocean');

-- Maximize Hotels - 100 Mountain View Road
insert into room values('100111', '100 Mountain View Road', 'Maximize Hotels', true, 280.00, 2, 'mountain');
insert into room values('100112', '100 Mountain View Road', 'Maximize Hotels', false, 330.00, 3, 'ocean');
insert into room values('100113', '100 Mountain View Road', 'Maximize Hotels', true, 380.00, 5, 'mountain');
insert into room values('100114', '100 Mountain View Road', 'Maximize Hotels', false, 430.00, 6, 'ocean');
insert into room values('100115', '100 Mountain View Road', 'Maximize Hotels', true, 480.00, 9, 'mountain');

-- Maximize Hotels - 21 Beachside Drive
insert into room values('100116', '21 Beachside Drive', 'Maximize Hotels', true, 190.00, 1, 'ocean');
insert into room values('100117', '21 Beachside Drive', 'Maximize Hotels', false, 240.00, 2, 'mountain');
insert into room values('100118', '21 Beachside Drive', 'Maximize Hotels', true, 290.00, 4, 'ocean');
insert into room values('100119', '21 Beachside Drive', 'Maximize Hotels', false, 340.00, 6, 'mountain');
insert into room values('100120', '21 Beachside Drive', 'Maximize Hotels', true, 390.00, 8, 'ocean');


-- Klaradon - 35 Lakeshore Drive
insert into room values('100121', '35 Lakeshore Drive', 'Klaradon', true, 210.00, 1, 'mountain');
insert into room values('100122', '35 Lakeshore Drive', 'Klaradon', false, 260.00, 2, 'ocean');
insert into room values('100123', '35 Lakeshore Drive', 'Klaradon', true, 310.00, 4, 'mountain');
insert into room values('100124', '35 Lakeshore Drive', 'Klaradon', false, 360.00, 5, 'ocean');
insert into room values('100125', '35 Lakeshore Drive', 'Klaradon', true, 410.00, 8, 'mountain');

-- Klaradon - 35 Humphrey Drive
insert into room values('100126', '35 Humphrey Drive', 'Klaradon', true, 190.00, 1, 'ocean');
insert into room values('100127', '35 Humphrey Drive', 'Klaradon', false, 240.00, 2, 'mountain');
insert into room values('100128', '35 Humphrey Drive', 'Klaradon', true, 290.00, 3, 'ocean');
insert into room values('100129', '35 Humphrey Drive', 'Klaradon', false, 340.00, 5, 'mountain');
insert into room values('100130', '35 Humphrey Drive', 'Klaradon', true, 390.00, 7, 'ocean');

-- Klaradon - 45 Queen Street
insert into room values('100131', '45 Queen Street', 'Klaradon', true, 220.00, 2, 'mountain');
insert into room values('100132', '45 Queen Street', 'Klaradon', false, 270.00, 3, 'ocean');
insert into room values('100133', '45 Queen Street', 'Klaradon', true, 320.00, 4, 'mountain');
insert into room values('100134', '45 Queen Street', 'Klaradon', false, 370.00, 6, 'ocean');
insert into room values('100135', '45 Queen Street', 'Klaradon', true, 420.00, 8, 'mountain');

-- Klaradon - 120 Pacific Blvd
insert into room values('100136', '120 Pacific Blvd', 'Klaradon', true, 250.00, 3, 'ocean');
insert into room values('100137', '120 Pacific Blvd', 'Klaradon', false, 300.00, 4, 'mountain');
insert into room values('100138', '120 Pacific Blvd', 'Klaradon', true, 350.00, 5, 'ocean');
insert into room values('100139', '120 Pacific Blvd', 'Klaradon', false, 400.00, 6, 'mountain');
insert into room values('100140', '120 Pacific Blvd', 'Klaradon', true, 450.00, 9, 'ocean');

-- Klaradon - 60 Elgin Street
insert into room values('100141', '60 Elgin Street', 'Klaradon', true, 230.00, 1, 'mountain');
insert into room values('100142', '60 Elgin Street', 'Klaradon', false, 280.00, 2, 'ocean');
insert into room values('100143', '60 Elgin Street', 'Klaradon', true, 330.00, 4, 'mountain');
insert into room values('100144', '60 Elgin Street', 'Klaradon', false, 380.00, 5, 'ocean');
insert into room values('100145', '60 Elgin Street', 'Klaradon', true, 430.00, 7, 'mountain');

-- Klaradon - 10 Calgary Road
insert into room values('100146', '10 Calgary Road', 'Klaradon', true, 240.00, 2, 'ocean');
insert into room values('100147', '10 Calgary Road', 'Klaradon', false, 290.00, 3, 'mountain');
insert into room values('100148', '10 Calgary Road', 'Klaradon', true, 340.00, 4, 'ocean');
insert into room values('100149', '10 Calgary Road', 'Klaradon', false, 390.00, 6, 'mountain');
insert into room values('100150', '10 Calgary Road', 'Klaradon', true, 440.00, 8, 'ocean');

-- Klaradon - 75 Saint Catherine Street
insert into room values('100151', '75 Saint Catherine Street', 'Klaradon', true, 260.00, 2, 'mountain');
insert into room values('100152', '75 Saint Catherine Street', 'Klaradon', false, 310.00, 3, 'ocean');
insert into room values('100153', '75 Saint Catherine Street', 'Klaradon', true, 360.00, 4, 'mountain');
insert into room values('100154', '75 Saint Catherine Street', 'Klaradon', false, 410.00, 6, 'ocean');
insert into room values('100155', '75 Saint Catherine Street', 'Klaradon', true, 460.00, 8, 'mountain');

-- Klaradon - 22 Old Port Road
insert into room values('100156', '22 Old Port Road', 'Klaradon', true, 280.00, 3, 'ocean');
insert into room values('100157', '22 Old Port Road', 'Klaradon', false, 330.00, 4, 'mountain');
insert into room values('100158', '22 Old Port Road', 'Klaradon', true, 380.00, 5, 'ocean');
insert into room values('100159', '22 Old Port Road', 'Klaradon', false, 430.00, 6, 'mountain');
insert into room values('100160', '22 Old Port Road', 'Klaradon', true, 480.00, 9, 'ocean');


-- Rosenblatt Hotels - 812 Stittsville Street
insert into room values('100161', '812 Stittsville Street', 'Rosenblatt Hotels', true, 200.00, 1, 'mountain');
insert into room values('100162', '812 Stittsville Street', 'Rosenblatt Hotels', false, 250.00, 2, 'ocean');
insert into room values('100163', '812 Stittsville Street', 'Rosenblatt Hotels', true, 300.00, 4, 'mountain');
insert into room values('100164', '812 Stittsville Street', 'Rosenblatt Hotels', false, 350.00, 6, 'ocean');
insert into room values('100165', '812 Stittsville Street', 'Rosenblatt Hotels', true, 400.00, 8, 'mountain');

-- Rosenblatt Hotels - 214 Granville Street
insert into room values('100166', '214 Granville Street', 'Rosenblatt Hotels', true, 220.00, 2, 'ocean');
insert into room values('100167', '214 Granville Street', 'Rosenblatt Hotels', false, 270.00, 3, 'mountain');
insert into room values('100168', '214 Granville Street', 'Rosenblatt Hotels', true, 320.00, 4, 'ocean');
insert into room values('100169', '214 Granville Street', 'Rosenblatt Hotels', false, 370.00, 5, 'mountain');
insert into room values('100170', '214 Granville Street', 'Rosenblatt Hotels', true, 420.00, 7, 'ocean');

-- Rosenblatt Hotels - 67 Crescent Street
insert into room values('100171', '67 Crescent Street', 'Rosenblatt Hotels', true, 230.00, 1, 'mountain');
insert into room values('100172', '67 Crescent Street', 'Rosenblatt Hotels', false, 280.00, 2, 'ocean');
insert into room values('100173', '67 Crescent Street', 'Rosenblatt Hotels', true, 330.00, 3, 'mountain');
insert into room values('100174', '67 Crescent Street', 'Rosenblatt Hotels', false, 380.00, 5, 'ocean');
insert into room values('100175', '67 Crescent Street', 'Rosenblatt Hotels', true, 430.00, 6, 'mountain');

-- Rosenblatt Hotels - 98 16th Avenue NW
insert into room values('100176', '98 16th Avenue NW', 'Rosenblatt Hotels', true, 240.00, 2, 'ocean');
insert into room values('100177', '98 16th Avenue NW', 'Rosenblatt Hotels', false, 290.00, 3, 'mountain');
insert into room values('100178', '98 16th Avenue NW', 'Rosenblatt Hotels', true, 340.00, 4, 'ocean');
insert into room values('100179', '98 16th Avenue NW', 'Rosenblatt Hotels', false, 390.00, 5, 'mountain');
insert into room values('100180', '98 16th Avenue NW', 'Rosenblatt Hotels', true, 440.00, 8, 'ocean');

-- Rosenblatt Hotels - 45 Wellington Street
insert into room values('100181', '45 Wellington Street', 'Rosenblatt Hotels', true, 250.00, 3, 'mountain');
insert into room values('100182', '45 Wellington Street', 'Rosenblatt Hotels', false, 300.00, 4, 'ocean');
insert into room values('100183', '45 Wellington Street', 'Rosenblatt Hotels', true, 350.00, 5, 'mountain');
insert into room values('100184', '45 Wellington Street', 'Rosenblatt Hotels', false, 400.00, 6, 'ocean');
insert into room values('100185', '45 Wellington Street', 'Rosenblatt Hotels', true, 450.00, 9, 'mountain');

-- Rosenblatt Hotels - 50 Rue Saint-Jean
insert into room values('100186', '50 Rue Saint-Jean', 'Rosenblatt Hotels', true, 270.00, 2, 'ocean');
insert into room values('100187', '50 Rue Saint-Jean', 'Rosenblatt Hotels', false, 320.00, 3, 'mountain');
insert into room values('100188', '50 Rue Saint-Jean', 'Rosenblatt Hotels', true, 370.00, 4, 'ocean');
insert into room values('100189', '50 Rue Saint-Jean', 'Rosenblatt Hotels', false, 420.00, 6, 'mountain');
insert into room values('100190', '50 Rue Saint-Jean', 'Rosenblatt Hotels', true, 470.00, 7, 'ocean');

-- Rosenblatt Hotels - 123 Jasper Avenue
insert into room values('100191', '123 Jasper Avenue', 'Rosenblatt Hotels', true, 290.00, 2, 'mountain');
insert into room values('100192', '123 Jasper Avenue', 'Rosenblatt Hotels', false, 340.00, 3, 'ocean');
insert into room values('100193', '123 Jasper Avenue', 'Rosenblatt Hotels', true, 390.00, 4, 'mountain');
insert into room values('100194', '123 Jasper Avenue', 'Rosenblatt Hotels', false, 440.00, 5, 'ocean');
insert into room values('100195', '123 Jasper Avenue', 'Rosenblatt Hotels', true, 490.00, 8, 'mountain');

-- Rosenblatt Hotels - 550 Main Street
insert into room values('100196', '550 Main Street', 'Rosenblatt Hotels', true, 310.00, 2, 'ocean');
insert into room values('100197', '550 Main Street', 'Rosenblatt Hotels', false, 360.00, 3, 'mountain');
insert into room values('100198', '550 Main Street', 'Rosenblatt Hotels', true, 410.00, 4, 'ocean');
insert into room values('100199', '550 Main Street', 'Rosenblatt Hotels', false, 460.00, 5, 'mountain');
insert into room values('100200', '550 Main Street', 'Rosenblatt Hotels', true, 510.00, 7, 'ocean');


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
insert into amenities values('Ottawa Hotels', '303 Sandy Street', 100001, 'TV');
insert into amenities values('Ottawa Hotels', '303 Sandy Street', 100002, 'air conditioning');
insert into amenities values('Ottawa Hotels', '303 Sandy Street', 100003, 'snack bar');
insert into amenities values('Ottawa Hotels', '303 Sandy Street', 100004, 'TV');
insert into amenities values('Ottawa Hotels', '303 Sandy Street', 100005, 'air conditioning');

-- Ottawa Hotels - 402 Tremblent Way
insert into amenities values('Ottawa Hotels', '402 Tremblent Way', 100006, 'snack bar');
insert into amenities values('Ottawa Hotels', '402 Tremblent Way', 100007, 'TV');
insert into amenities values('Ottawa Hotels', '402 Tremblent Way', 100008, 'air conditioning');
insert into amenities values('Ottawa Hotels', '402 Tremblent Way', 100009, 'snack bar');
insert into amenities values('Ottawa Hotels', '402 Tremblent Way', 100010, 'TV');

-- Ottawa Hotels - 45 Elgin Street
insert into amenities values('Ottawa Hotels', '45 Elgin Street', 100011, 'air conditioning');
insert into amenities values('Ottawa Hotels', '45 Elgin Street', 100012, 'snack bar');
insert into amenities values('Ottawa Hotels', '45 Elgin Street', 100013, 'TV');
insert into amenities values('Ottawa Hotels', '45 Elgin Street', 100014, 'air conditioning');
insert into amenities values('Ottawa Hotels', '45 Elgin Street', 100015, 'snack bar');

-- Ottawa Hotels - 201 Rideau Street
insert into amenities values('Ottawa Hotels', '201 Rideau Street', 100016, 'TV');
insert into amenities values('Ottawa Hotels', '201 Rideau Street', 100017, 'snack bar');
insert into amenities values('Ottawa Hotels', '201 Rideau Street', 100018, 'air conditioning');
insert into amenities values('Ottawa Hotels', '201 Rideau Street', 100019, 'TV');
insert into amenities values('Ottawa Hotels', '201 Rideau Street', 100020, 'snack bar');

-- Ottawa Hotels - 39 Snow Drive
insert into amenities values('Ottawa Hotels', '39 Snow Drive', 100021, 'snack bar');
insert into amenities values('Ottawa Hotels', '39 Snow Drive', 100022, 'air conditioning');
insert into amenities values('Ottawa Hotels', '39 Snow Drive', 100023, 'TV');
insert into amenities values('Ottawa Hotels', '39 Snow Drive', 100024, 'snack bar');
insert into amenities values('Ottawa Hotels', '39 Snow Drive', 100025, 'air conditioning');

-- Ottawa Hotels - 17 Autumn Street
insert into amenities values('Ottawa Hotels', '17 Autumn Street', 100026, 'TV');
insert into amenities values('Ottawa Hotels', '17 Autumn Street', 100027, 'snack bar');
insert into amenities values('Ottawa Hotels', '17 Autumn Street', 100028, 'air conditioning');
insert into amenities values('Ottawa Hotels', '17 Autumn Street', 100029, 'TV');
insert into amenities values('Ottawa Hotels', '17 Autumn Street', 100030, 'snack bar');

-- Ottawa Hotels - 92 Pineview Crescent
insert into amenities values('Ottawa Hotels', '92 Pineview Crescent', 100031, 'air conditioning');
insert into amenities values('Ottawa Hotels', '92 Pineview Crescent', 100032, 'snack bar');
insert into amenities values('Ottawa Hotels', '92 Pineview Crescent', 100033, 'TV');
insert into amenities values('Ottawa Hotels', '92 Pineview Crescent', 100034, 'air conditioning');
insert into amenities values('Ottawa Hotels', '92 Pineview Crescent', 100035, 'snack bar');

-- Ottawa Hotels - 14 Pleasant Park Road
insert into amenities values('Ottawa Hotels', '14 Pleasant Park Road', 100036, 'snack bar');
insert into amenities values('Ottawa Hotels', '14 Pleasant Park Road', 100037, 'TV');
insert into amenities values('Ottawa Hotels', '14 Pleasant Park Road', 100038, 'air conditioning');
insert into amenities values('Ottawa Hotels', '14 Pleasant Park Road', 100039, 'snack bar');
insert into amenities values('Ottawa Hotels', '14 Pleasant Park Road', 100040, 'TV');


-- Comfort Stay - 333 Bresserer Street
insert into amenities values('Comfort Stay', '333 Bresserer Street', 100041, 'air conditioning');
insert into amenities values('Comfort Stay', '333 Bresserer Street', 100042, 'snack bar');
insert into amenities values('Comfort Stay', '333 Bresserer Street', 100043, 'TV');
insert into amenities values('Comfort Stay', '333 Bresserer Street', 100044, 'air conditioning');
insert into amenities values('Comfort Stay', '333 Bresserer Street', 100045, 'snack bar');

-- Comfort Stay - 154 Wrightville Way
insert into amenities values('Comfort Stay', '154 Wrightville Way', 100046, 'TV');
insert into amenities values('Comfort Stay', '154 Wrightville Way', 100047, 'air conditioning');
insert into amenities values('Comfort Stay', '154 Wrightville Way', 100048, 'snack bar');
insert into amenities values('Comfort Stay', '154 Wrightville Way', 100049, 'TV');
insert into amenities values('Comfort Stay', '154 Wrightville Way', 100050, 'air conditioning');

-- Comfort Stay - 46 Elgin Street
insert into amenities values('Comfort Stay', '46 Elgin Street', 100051, 'snack bar');
insert into amenities values('Comfort Stay', '46 Elgin Street', 100052, 'TV');
insert into amenities values('Comfort Stay', '46 Elgin Street', 100053, 'air conditioning');
insert into amenities values('Comfort Stay', '46 Elgin Street', 100054, 'snack bar');
insert into amenities values('Comfort Stay', '46 Elgin Street', 100055, 'TV');

-- Comfort Stay - 30 Qualicum Street
insert into amenities values('Comfort Stay', '30 Qualicum Street', 100056, 'air conditioning');
insert into amenities values('Comfort Stay', '30 Qualicum Street', 100057, 'snack bar');
insert into amenities values('Comfort Stay', '30 Qualicum Street', 100058, 'TV');
insert into amenities values('Comfort Stay', '30 Qualicum Street', 100059, 'air conditioning');
insert into amenities values('Comfort Stay', '30 Qualicum Street', 100060, 'snack bar');

-- Comfort Stay - 53 Ascot Avenue
insert into amenities values('Comfort Stay', '53 Ascot Avenue', 100061, 'TV');
insert into amenities values('Comfort Stay', '53 Ascot Avenue', 100062, 'air conditioning');
insert into amenities values('Comfort Stay', '53 Ascot Avenue', 100063, 'snack bar');
insert into amenities values('Comfort Stay', '53 Ascot Avenue', 100064, 'TV');
insert into amenities values('Comfort Stay', '53 Ascot Avenue', 100065, 'air conditioning');

-- Comfort Stay - 62 Seyton Drive
insert into amenities values('Comfort Stay', '62 Seyton Drive', 100066, 'snack bar');
insert into amenities values('Comfort Stay', '62 Seyton Drive', 100067, 'TV');
insert into amenities values('Comfort Stay', '62 Seyton Drive', 100068, 'air conditioning');
insert into amenities values('Comfort Stay', '62 Seyton Drive', 100069, 'snack bar');
insert into amenities values('Comfort Stay', '62 Seyton Drive', 100070, 'TV');

-- Comfort Stay - 38 McClellan Road
insert into amenities values('Comfort Stay', '38 McClellan Road', 100071, 'air conditioning');
insert into amenities values('Comfort Stay', '38 McClellan Road', 100072, 'snack bar');
insert into amenities values('Comfort Stay', '38 McClellan Road', 100073, 'TV');
insert into amenities values('Comfort Stay', '38 McClellan Road', 100074, 'air conditioning');
insert into amenities values('Comfort Stay', '38 McClellan Road', 100075, 'snack bar');

-- Comfort Stay - 48 Capital Drive
insert into amenities values('Comfort Stay', '48 Capital Drive', 100076, 'TV');
insert into amenities values('Comfort Stay', '48 Capital Drive', 100077, 'air conditioning');
insert into amenities values('Comfort Stay', '48 Capital Drive', 100078, 'snack bar');
insert into amenities values('Comfort Stay', '48 Capital Drive', 100079, 'TV');
insert into amenities values('Comfort Stay', '48 Capital Drive', 100080, 'air conditioning');

-- Maximize Hotels - 59 Main Street
insert into amenities values('Maximize Hotels', '59 Main Street', 100081, 'air conditioning');
insert into amenities values('Maximize Hotels', '59 Main Street', 100082, 'snack bar');
insert into amenities values('Maximize Hotels', '59 Main Street', 100083, 'TV');
insert into amenities values('Maximize Hotels', '59 Main Street', 100084, 'air conditioning');
insert into amenities values('Maximize Hotels', '59 Main Street', 100085, 'snack bar');

-- Maximize Hotels - 72 Broadway Ave
insert into amenities values('Maximize Hotels', '72 Broadway Ave', 100086, 'TV');
insert into amenities values('Maximize Hotels', '72 Broadway Ave', 100087, 'air conditioning');
insert into amenities values('Maximize Hotels', '72 Broadway Ave', 100088, 'snack bar');
insert into amenities values('Maximize Hotels', '72 Broadway Ave', 100089, 'TV');
insert into amenities values('Maximize Hotels', '72 Broadway Ave', 100090, 'air conditioning');

-- Maximize Hotels - 15 Rue de la Paix
insert into amenities values('Maximize Hotels', '15 Rue de la Paix', 100091, 'snack bar');
insert into amenities values('Maximize Hotels', '15 Rue de la Paix', 100092, 'TV');
insert into amenities values('Maximize Hotels', '15 Rue de la Paix', 100093, 'air conditioning');
insert into amenities values('Maximize Hotels', '15 Rue de la Paix', 100094, 'snack bar');
insert into amenities values('Maximize Hotels', '15 Rue de la Paix', 100095, 'TV');

-- Maximize Hotels - 100 Sunset Blvd
insert into amenities values('Maximize Hotels', '100 Sunset Blvd', 100096, 'air conditioning');
insert into amenities values('Maximize Hotels', '100 Sunset Blvd', 100097, 'snack bar');
insert into amenities values('Maximize Hotels', '100 Sunset Blvd', 100098, 'TV');
insert into amenities values('Maximize Hotels', '100 Sunset Blvd', 100099, 'air conditioning');
insert into amenities values('Maximize Hotels', '100 Sunset Blvd', 100100, 'snack bar');

-- Maximize Hotels - 47 Oxford Street
insert into amenities values('Maximize Hotels', '47 Oxford Street', 100101, 'TV');
insert into amenities values('Maximize Hotels', '47 Oxford Street', 100102, 'air conditioning');
insert into amenities values('Maximize Hotels', '47 Oxford Street', 100103, 'snack bar');
insert into amenities values('Maximize Hotels', '47 Oxford Street', 100104, 'TV');
insert into amenities values('Maximize Hotels', '47 Oxford Street', 100105, 'air conditioning');

-- Maximize Hotels - 300 Shibuya Crossing
insert into amenities values('Maximize Hotels', '300 Shibuya Crossing', 100106, 'snack bar');
insert into amenities values('Maximize Hotels', '300 Shibuya Crossing', 100107, 'TV');
insert into amenities values('Maximize Hotels', '300 Shibuya Crossing', 100108, 'air conditioning');
insert into amenities values('Maximize Hotels', '300 Shibuya Crossing', 100109, 'snack bar');
insert into amenities values('Maximize Hotels', '300 Shibuya Crossing', 100110, 'TV');

-- Maximize Hotels - 100 Mountain View Road
insert into amenities values('Maximize Hotels', '100 Mountain View Road', 100111, 'air conditioning');
insert into amenities values('Maximize Hotels', '100 Mountain View Road', 100112, 'snack bar');
insert into amenities values('Maximize Hotels', '100 Mountain View Road', 100113, 'TV');
insert into amenities values('Maximize Hotels', '100 Mountain View Road', 100114, 'air conditioning');
insert into amenities values('Maximize Hotels', '100 Mountain View Road', 100115, 'snack bar');

-- Maximize Hotels - 21 Beachside Drive
insert into amenities values('Maximize Hotels', '21 Beachside Drive', 100116, 'TV');
insert into amenities values('Maximize Hotels', '21 Beachside Drive', 100117, 'air conditioning');
insert into amenities values('Maximize Hotels', '21 Beachside Drive', 100118, 'snack bar');
insert into amenities values('Maximize Hotels', '21 Beachside Drive', 100119, 'TV');
insert into amenities values('Maximize Hotels', '21 Beachside Drive', 100120, 'air conditioning');

-- Klaradon - 35 Lakeshore Drive
insert into amenities values('Klaradon', '35 Lakeshore Drive', 100121, 'TV');
insert into amenities values('Klaradon', '35 Lakeshore Drive', 100122, 'air conditioning');
insert into amenities values('Klaradon', '35 Lakeshore Drive', 100123, 'snack bar');
insert into amenities values('Klaradon', '35 Lakeshore Drive', 100124, 'TV');
insert into amenities values('Klaradon', '35 Lakeshore Drive', 100125, 'air conditioning');

-- Klaradon - 35 Humphrey Drive
insert into amenities values('Klaradon', '35 Humphrey Drive', 100126, 'snack bar');
insert into amenities values('Klaradon', '35 Humphrey Drive', 100127, 'TV');
insert into amenities values('Klaradon', '35 Humphrey Drive', 100128, 'air conditioning');
insert into amenities values('Klaradon', '35 Humphrey Drive', 100129, 'snack bar');
insert into amenities values('Klaradon', '35 Humphrey Drive', 100130, 'TV');

-- Klaradon - 45 Queen Street
insert into amenities values('Klaradon', '45 Queen Street', 100131, 'air conditioning');
insert into amenities values('Klaradon', '45 Queen Street', 100132, 'snack bar');
insert into amenities values('Klaradon', '45 Queen Street', 100133, 'TV');
insert into amenities values('Klaradon', '45 Queen Street', 100134, 'air conditioning');
insert into amenities values('Klaradon', '45 Queen Street', 100135, 'snack bar');

-- Klaradon - 120 Pacific Blvd
insert into amenities values('Klaradon', '120 Pacific Blvd', 100136, 'TV');
insert into amenities values('Klaradon', '120 Pacific Blvd', 100137, 'air conditioning');
insert into amenities values('Klaradon', '120 Pacific Blvd', 100138, 'snack bar');
insert into amenities values('Klaradon', '120 Pacific Blvd', 100139, 'TV');
insert into amenities values('Klaradon', '120 Pacific Blvd', 100140, 'air conditioning');

-- Klaradon - 60 Elgin Street
insert into amenities values('Klaradon', '60 Elgin Street', 100141, 'snack bar');
insert into amenities values('Klaradon', '60 Elgin Street', 100142, 'TV');
insert into amenities values('Klaradon', '60 Elgin Street', 100143, 'air conditioning');
insert into amenities values('Klaradon', '60 Elgin Street', 100144, 'snack bar');
insert into amenities values('Klaradon', '60 Elgin Street', 100145, 'TV');

-- Klaradon - 10 Calgary Road
insert into amenities values('Klaradon', '10 Calgary Road', 100146, 'air conditioning');
insert into amenities values('Klaradon', '10 Calgary Road', 100147, 'snack bar');
insert into amenities values('Klaradon', '10 Calgary Road', 100148, 'TV');
insert into amenities values('Klaradon', '10 Calgary Road', 100149, 'air conditioning');
insert into amenities values('Klaradon', '10 Calgary Road', 100150, 'snack bar');

-- Klaradon - 75 Saint Catherine Street
insert into amenities values('Klaradon', '75 Saint Catherine Street', 100151, 'TV');
insert into amenities values('Klaradon', '75 Saint Catherine Street', 100152, 'air conditioning');
insert into amenities values('Klaradon', '75 Saint Catherine Street', 100153, 'snack bar');
insert into amenities values('Klaradon', '75 Saint Catherine Street', 100154, 'TV');
insert into amenities values('Klaradon', '75 Saint Catherine Street', 100155, 'air conditioning');

-- Klaradon - 22 Old Port Road
insert into amenities values('Klaradon', '22 Old Port Road', 100156, 'snack bar');
insert into amenities values('Klaradon', '22 Old Port Road', 100157, 'TV');
insert into amenities values('Klaradon', '22 Old Port Road', 100158, 'air conditioning');
insert into amenities values('Klaradon', '22 Old Port Road', 100159, 'snack bar');
insert into amenities values('Klaradon', '22 Old Port Road', 100160, 'TV');

-- Rosenblatt Hotels - 812 Stittsville Street
insert into amenities values('Rosenblatt Hotels', '812 Stittsville Street', 100161, 'air conditioning');
insert into amenities values('Rosenblatt Hotels', '812 Stittsville Street', 100162, 'TV');
insert into amenities values('Rosenblatt Hotels', '812 Stittsville Street', 100163, 'snack bar');
insert into amenities values('Rosenblatt Hotels', '812 Stittsville Street', 100164, 'air conditioning');
insert into amenities values('Rosenblatt Hotels', '812 Stittsville Street', 100165, 'TV');

-- Rosenblatt Hotels - 214 Granville Street
insert into amenities values('Rosenblatt Hotels', '214 Granville Street', 100166, 'snack bar');
insert into amenities values('Rosenblatt Hotels', '214 Granville Street', 100167, 'air conditioning');
insert into amenities values('Rosenblatt Hotels', '214 Granville Street', 100168, 'TV');
insert into amenities values('Rosenblatt Hotels', '214 Granville Street', 100169, 'snack bar');
insert into amenities values('Rosenblatt Hotels', '214 Granville Street', 100170, 'air conditioning');

-- Rosenblatt Hotels - 67 Crescent Street
insert into amenities values('Rosenblatt Hotels', '67 Crescent Street', 100171, 'TV');
insert into amenities values('Rosenblatt Hotels', '67 Crescent Street', 100172, 'snack bar');
insert into amenities values('Rosenblatt Hotels', '67 Crescent Street', 100173, 'air conditioning');
insert into amenities values('Rosenblatt Hotels', '67 Crescent Street', 100174, 'TV');
insert into amenities values('Rosenblatt Hotels', '67 Crescent Street', 100175, 'snack bar');

-- Rosenblatt Hotels - 98 16th Avenue NW
insert into amenities values('Rosenblatt Hotels', '98 16th Avenue NW', 100176, 'air conditioning');
insert into amenities values('Rosenblatt Hotels', '98 16th Avenue NW', 100177, 'TV');
insert into amenities values('Rosenblatt Hotels', '98 16th Avenue NW', 100178, 'snack bar');
insert into amenities values('Rosenblatt Hotels', '98 16th Avenue NW', 100179, 'air conditioning');
insert into amenities values('Rosenblatt Hotels', '98 16th Avenue NW', 100180, 'TV');

-- Rosenblatt Hotels - 45 Wellington Street
insert into amenities values('Rosenblatt Hotels', '45 Wellington Street', 100181, 'snack bar');
insert into amenities values('Rosenblatt Hotels', '45 Wellington Street', 100182, 'air conditioning');
insert into amenities values('Rosenblatt Hotels', '45 Wellington Street', 100183, 'TV');
insert into amenities values('Rosenblatt Hotels', '45 Wellington Street', 100184, 'snack bar');
insert into amenities values('Rosenblatt Hotels', '45 Wellington Street', 100185, 'air conditioning');

-- Rosenblatt Hotels - 50 Rue Saint-Jean
insert into amenities values('Rosenblatt Hotels', '50 Rue Saint-Jean', 100186, 'TV');
insert into amenities values('Rosenblatt Hotels', '50 Rue Saint-Jean', 100187, 'snack bar');
insert into amenities values('Rosenblatt Hotels', '50 Rue Saint-Jean', 100188, 'air conditioning');
insert into amenities values('Rosenblatt Hotels', '50 Rue Saint-Jean', 100189, 'TV');
insert into amenities values('Rosenblatt Hotels', '50 Rue Saint-Jean', 100190, 'snack bar');

-- Rosenblatt Hotels - 123 Jasper Avenue
insert into amenities values('Rosenblatt Hotels', '123 Jasper Avenue', 100191, 'air conditioning');
insert into amenities values('Rosenblatt Hotels', '123 Jasper Avenue', 100192, 'TV');
insert into amenities values('Rosenblatt Hotels', '123 Jasper Avenue', 100193, 'snack bar');
insert into amenities values('Rosenblatt Hotels', '123 Jasper Avenue', 100194, 'air conditioning');
insert into amenities values('Rosenblatt Hotels', '123 Jasper Avenue', 100195, 'TV');

-- Rosenblatt Hotels - 550 Main Street
insert into amenities values('Rosenblatt Hotels', '550 Main Street', 100196, 'snack bar');
insert into amenities values('Rosenblatt Hotels', '550 Main Street', 100197, 'air conditioning');
insert into amenities values('Rosenblatt Hotels', '550 Main Street', 100198, 'TV');
insert into amenities values('Rosenblatt Hotels', '550 Main Street', 100199, 'snack bar');
insert into amenities values('Rosenblatt Hotels', '550 Main Street', 100200, 'air conditioning');
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

cur.execute('''
-- Ottawa Hotels - 303 Sandy Street
insert into damage values('Ottawa Hotels', '303 Sandy Street', 100001, 'heating');
insert into damage values('Ottawa Hotels', '303 Sandy Street', 100004, 'bedbugs');

-- Ottawa Hotels - 402 Tremblent Way
insert into damage values('Ottawa Hotels', '402 Tremblent Way', 100006, 'showerhead');
insert into damage values('Ottawa Hotels', '402 Tremblent Way', 100009, 'bedbugs');

-- Ottawa Hotels - 45 Elgin Street
insert into damage values('Ottawa Hotels', '45 Elgin Street', 100011, 'bedbugs');
insert into damage values('Ottawa Hotels', '45 Elgin Street', 100012, 'heating');

-- Ottawa Hotels - 201 Rideau Street
insert into damage values('Ottawa Hotels', '201 Rideau Street', 100016, 'heating');
insert into damage values('Ottawa Hotels', '201 Rideau Street', 100020, 'heating');

-- Ottawa Hotels - 39 Snow Drive
insert into damage values('Ottawa Hotels', '39 Snow Drive', 100021, 'showerhead');
insert into damage values('Ottawa Hotels', '39 Snow Drive', 100023, 'bedbugs');

-- Ottawa Hotels - 17 Autumn Street
insert into damage values('Ottawa Hotels', '17 Autumn Street', 100026, 'heating');
insert into damage values('Ottawa Hotels', '17 Autumn Street', 100028, 'bedbugs');

-- Ottawa Hotels - 92 Pineview Crescent
insert into damage values('Ottawa Hotels', '92 Pineview Crescent', 100031, 'heating');
insert into damage values('Ottawa Hotels', '92 Pineview Crescent', 100033, 'bedbugs');

-- Ottawa Hotels - 14 Pleasant Park Road
insert into damage values('Ottawa Hotels', '14 Pleasant Park Road', 100036, 'showerhead');
insert into damage values('Ottawa Hotels', '14 Pleasant Park Road', 100037, 'heating');

-- Comfort Stay - 333 Bresserer Street
insert into damage values('Comfort Stay', '333 Bresserer Street', 100042, 'ceiling_leakage');

-- Comfort Stay - 154 Wrightville Way
insert into damage values('Comfort Stay', '154 Wrightville Way', 100046, 'bedbugs');

-- Comfort Stay - 46 Elgin Street
insert into damage values('Comfort Stay', '46 Elgin Street', 100053, 'showerhead');

-- Comfort Stay - 30 Qualicum Street
insert into damage values('Comfort Stay', '30 Qualicum Street', 100056, 'heating');

-- Comfort Stay - 53 Ascot Avenue
insert into damage values('Comfort Stay', '53 Ascot Avenue', 100061, 'heating');

-- Comfort Stay - 62 Seyton Drive
insert into damage values('Comfort Stay', '62 Seyton Drive', 100066, 'bedbugs');

-- Comfort Stay - 38 McClellan Road
insert into damage values('Comfort Stay', '38 McClellan Road', 100073, 'ceiling_leakage');

-- Comfort Stay - 48 Capital Drive
insert into damage values('Comfort Stay', '48 Capital Drive', 100077, 'heating');

-- Maximize Hotels - 59 Main Street
insert into damage values('Maximize Hotels', '59 Main Street', 100083, 'ceiling_leakage');

-- Maximize Hotels - 72 Broadway Ave
insert into damage values('Maximize Hotels', '72 Broadway Ave', 100086, 'showerhead');

-- Maximize Hotels - 15 Rue de la Paix
insert into damage values('Maximize Hotels', '15 Rue de la Paix', 100091, 'bedbugs');

-- Maximize Hotels - 100 Sunset Blvd
insert into damage values('Maximize Hotels', '100 Sunset Blvd', 100096, 'heating');

-- Maximize Hotels - 47 Oxford Street
insert into damage values('Maximize Hotels', '47 Oxford Street', 100101, 'heating');

-- Maximize Hotels - 300 Shibuya Crossing
insert into damage values('Maximize Hotels', '300 Shibuya Crossing', 100108, 'ceiling_leakage');

-- Maximize Hotels - 100 Mountain View Road
insert into damage values('Maximize Hotels', '100 Mountain View Road', 100113, 'showerhead');

-- Maximize Hotels - 21 Beachside Drive
insert into damage values('Maximize Hotels', '21 Beachside Drive', 100116, 'bedbugs');

-- Klaradon - 35 Lakeshore Drive
insert into damage values('Klaradon', '35 Lakeshore Drive', 100121, 'showerhead');

-- Klaradon - 35 Humphrey Drive
insert into damage values('Klaradon', '35 Humphrey Drive', 100130, 'heating');

-- Klaradon - 45 Queen Street
insert into damage values('Klaradon', '45 Queen Street', 100134, 'ceiling_leakage');

-- Klaradon - 120 Pacific Blvd
insert into damage values('Klaradon', '120 Pacific Blvd', 100137, 'showerhead');

-- Klaradon - 60 Elgin Street
insert into damage values('Klaradon', '60 Elgin Street', 100144, 'bedbugs');

-- Klaradon - 10 Calgary Road
insert into damage values('Klaradon', '10 Calgary Road', 100149, 'heating');

-- Klaradon - 75 Saint Catherine Street
insert into damage values('Klaradon', '75 Saint Catherine Street', 100152, 'showerhead');

-- Klaradon - 22 Old Port Road
insert into damage values('Klaradon', '22 Old Port Road', 100159, 'heating');

-- Rosenblatt Hotels - 812 Stittsville Street
insert into damage values('Rosenblatt Hotels', '812 Stittsville Street', 100163, 'heating');

-- Rosenblatt Hotels - 214 Granville Street
insert into damage values('Rosenblatt Hotels', '214 Granville Street', 100170, 'showerhead');

-- Rosenblatt Hotels - 67 Crescent Street
insert into damage values('Rosenblatt Hotels', '67 Crescent Street', 100172, 'ceiling_leakage');

-- Rosenblatt Hotels - 98 16th Avenue NW
insert into damage values('Rosenblatt Hotels', '98 16th Avenue NW', 100179, 'heating');

-- Rosenblatt Hotels - 45 Wellington Street
insert into damage values('Rosenblatt Hotels', '45 Wellington Street', 100184, 'bedbugs');

-- Rosenblatt Hotels - 50 Rue Saint-Jean
insert into damage values('Rosenblatt Hotels', '50 Rue Saint-Jean', 100189, 'showerhead');

-- Rosenblatt Hotels - 123 Jasper Avenue
insert into damage values('Rosenblatt Hotels', '123 Jasper Avenue', 100193, 'heating');

-- Rosenblatt Hotels - 550 Main Street
insert into damage values('Rosenblatt Hotels', '550 Main Street', 100199, 'ceiling_leakage');
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
