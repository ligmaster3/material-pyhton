import mysql.connector

def create_connection():
    #estsblece una conexxion
    config = {
        'host': 'localhost',
        'user': 'root',
        'password':'',
        'database':'proyecto'
    }
    
    try:
        connection = mysql.connector.connect(**config)
        print("Conexion a la base de dataos existosa")
        return connection
    except mysql.connector.Error as err:
        print("Error al conectar a mysql: ")
        return None
        
if __name__=="__main__":
        conn = create_connection()
        if conn:
           conn.close()
