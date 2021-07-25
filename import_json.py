import psycopg2

class DataBase:
    def __init__(self,name,password):
        self.name=name
        self.password=password
        self.con = psycopg2.connect(
            host='localhost',
            database=self.name,
            user='postgres',
            password=self.password,)

     

    def Excute_upd(self,new,name_send):
        self.cur= self.con.cursor()
        self.cur.execute("UPDATE enc_words SET words = %s WHERE id = %s",(new,name_send))
        self.con.commit()
        self.cur.close()
        self.con.close()


       


