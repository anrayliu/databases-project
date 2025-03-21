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


conn.commit()

cur.close()
conn.close()


print("db init successful")