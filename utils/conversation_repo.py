

class ConversationRepo:
    def __init__(self, conn):
        self.conn = conn
        self.cur = self.conn.cursor()

    def get(self, user_id):
        self.cur.execute(
            "SELECT  messages FROM conversations WHERE user_id = %s",
            (user_id,)
        )
        row = self.cur.fetchone()
        return row if row else ([])
    
    def upsert(self,user_id, messages):
        if self.get(user_id) != [] :  
            self.update(user_id, messages)
        else:
            self.insert(user_id, messages)

    def insert(self, user_id: int, messages: list):
        self.cur.execute(
            """
            INSERT INTO conversations (user_id, messages)
            VALUES (%s, %s)
            ON CONFLICT (user_id) DO NOTHING
            """,
            ( user_id, messages)
        )
        self.conn.commit()

    def update(self,user_id, messages):
        self.cur.execute(
            """
            UPDATE conversations
            SET messages = %s
            WHERE user_id = %s
            """,
            (messages,user_id,)
        )
        self.conn.commit()

    def close(self):
        self.cur.close()
        self.conn.close()
