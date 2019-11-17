import psycopg2

def establish_connection():
    conexion = psycopg2.connect("dbname=apirest user=postgres password=12345")
    return conexion

def insertar_estudiante(nombre,carne,carrera):
    try:
        conexion = establish_connection()
    except:
         return 'No se logro la conección con la base de datos'
    try:
        conexion.autocommit = True
        cur = conexion.cursor()
        name = "'"+nombre+"'"
        carr = "'"+carrera+"'"
        cur.execute('INSERT into estudiantes(nombre,carne, carrera) VALUES ('+name+','+str(carne)+','+carr+')')
        cur.close()
        conexion.close()
        return "Usuario insertado"
    except:
        conexion.close()
        return 'No se ha podido realizar la insercion'

def get_estudiante(carne):
    try:
        conexion = establish_connection()
    except:
         return 'No se logro la conexión con la base de datos'
    try:
        conexion.autocommit = True
        cur = conexion.cursor()
        cur.execute('SELECT * FROM estudiantes WHERE carne = '+str(carne)+'')
        json_resp = {}
        for resp in cur.fetchall():
            print("hola")
            json_resp = {
                "Id": resp[0],
                "Nombre": resp[1],
                "Carne": resp[2],
                "Carrera": resp[3]
            }
        cur.close()
        conexion.close()
        return json_resp
    except:
        conexion.close()
        return 'No se ha podido encontrar al usuario'

def update_nombre_estudiante(id_est,nombre):
    try:
        conexion = establish_connection()
    except:
         return 'No se logro la conexión con la base de datos'
    try:
        conexion.autocommit = True
        name = "'"+nombre+"'"
        cur = conexion.cursor()
        cur.execute('update estudiantes set nombre = '+name+' where id_estudiante = '+str(id_est)+'')
        cur.close()
        conexion.close()
        return "actualizado"
    except:
        conexion.close()
        return 'No se ha podido actualizar al usuario'

def delete_estudiante(id_est):
    try:
        conexion = establish_connection()
    except:
         return 'No se logro la conexión con la base de datos'
    try:
        conexion.autocommit = True
        cur = conexion.cursor()
        cur.execute('DELETE from estudiantes where id_estudiante = '+str(id_est)+'')
        cur.close()
        conexion.close()
        return "Eliminado"
    except:
        conexion.close()
        return 'No se ha podido encontrar al usuario'