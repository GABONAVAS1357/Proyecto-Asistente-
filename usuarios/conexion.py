# -*- coding: utf-8 -*-

import mysql.connector

def conectar():

    database = mysql.connector.connect(
        host ="localhost",
        user = "root",
        passwd = "",
        database = "asistente_virtual",
        port = 3306
    )

    cursor = database.cursor(buffered=True)

    return[database, cursor]