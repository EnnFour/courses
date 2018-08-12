import pymysql.cursors, re, config
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/listpeople', methods=['GET'])
def listpeople():
    course = request.args.get('course')
    if validate_course(course):
        sql = 'SELECT `username` FROM `courses` WHERE `course` = "{}"'.format(str(course))
        return jsonify(run_sql(sql)) 
    return 'Invalid Course', 400

@app.route('/listcourses', methods=['GET'])
def listcourses():
    uname = request.args.get('uname')
    if validate_username(uname):
        sql = 'select course from courses where username = "{}"'.format(str(uname))
        return jsonify(run_sql(sql))
    return 'Invalid Username', 400

@app.route('/addcourse', methods=['POST'])
def addcourse():
    uname, course = request.args.get('uname'), request.args.get('course')
    if validate_username(uname) and validate_course(course):
        sql = 'INSERT INTO `courses` (`username`, `course`) VALUES ("{}", "{}")'.format(str(uname), str(course))
        run_sql(sql, insert=True)
        return 'OK'
    return 'Invalid username or course', 400

@app.route('/removecourse', methods=['POST'])
def removecourse():
    uname, course = request.args.get('uname'), request.args.get('course')
    if validate_username(uname) and validate_course(course):
        sql = 'DELETE FROM `courses` WHERE `username` = "{}" AND `course` = "{}"'.format(str(uname), str(course))
        run_sql(sql, insert=True)
        return 'OK'
    return 'Invalid username or course', 400

def run_sql(sql, insert=False):
    connection, tbr = config.get_connection(), None
    
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            if not insert:
                tbr = cursor.fetchall()
            else:
                connection.commit()
    except Exception as e:
        print(e)
    finally:
        connection.close()

    return tbr

def validate_username(uname):
    if uname is None or  not uname.isalnum() or len(uname) > 32:
        return False
    return True


def validate_course(c):
    if c is None or not c.isalnum():
        return False
    
    c = c.upper().replace(" ", "")
    parts = re.split('(\d+)', c)

    if len(parts) != 3:
        return False

    dept, num, let = parts

    if len(dept) > 7:
        return False
    if len(num) > 3:
        return Fasle
    if len(let) > 2:
        return False
    return True


