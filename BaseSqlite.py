# -*- coding: utf-8 -*-
import sqlite3


class BaseSqlite(object):
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.conn.execute('pragma foreign_keys = on')
        self.conn.commit()
        self.cur = self.conn.cursor()

    def ejecutar(self, sql, parametro=None):

        if parametro:
            print(("Ejecutar", sql, parametro))
            with self.conn.cursor() as cursor:
                cursor.execute(sql, parametro)
        else:
            self.cur.execute(sql)
        self.conn.commit()
        return self.cur

    def desconectar(self):
        self.conn.close()