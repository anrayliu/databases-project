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


conn.commit()

cur.close()
conn.close()


print("db init successful")
