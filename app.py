from flask import Flask, render_template , request , flash, redirect
import sqlite3
import os
from datetime import datetime 
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user

currentdirectory = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/")
def main_page():
    return render_template("index.html")

@app.route("/student", methods=['GET', 'POST'])
def student_page():
    if request.method == 'POST':
        #Getting data from HTML page
        std_id = request.form['stdid']
        std_password = request.form['stdpass']
        std_name = request.form['stdname']

        #Making database connection
        connection = sqlite3.connect(currentdirectory + "/AMS.db")
        cursor = connection.cursor()

        #fetching student id from student table and storing it in data1
        cursor.execute("SELECT std_id FROM student")
        data1 = cursor.fetchall()

        #converting the list of tuples into list
        data1_list = []

        for d in data1:
            for x in d:
                data1_list.append(x)

        #fetching student id from student_validation table and storing it in data2
        cursor.execute("SELECT id FROM studentvalidation")
        data2 = cursor.fetchall()

        #converting the list of tuples into list
        data2_id_list = []

        for dd in data2:
            for y in dd:
                data2_id_list.append(y)

        #fetching student password from student_validation table and storing it in data3
        cursor.execute("SELECT password FROM studentvalidation WHERE id = {}".format(std_id))
        data3 = cursor.fetchall()
        print("data = ", data3)

        #converting the list of tuples into list
        data3_pass_list = []
        for ddd in data3:
            for z in ddd:
                data3_pass_list.append(z)

        if str(std_id) in str(data2_id_list):
            if str(std_password) in str(data3_pass_list):
                if str(std_id) in str(data1_list):
                    flash("Your Attendace has Already bean Marked For the Day")
                    return redirect(request.url)
                else:
                    cursor.execute("INSERT INTO student VALUES(?, ?, ?, ?)", (std_id, std_name, std_password, datetime.now().strftime("%H:%M")))
                    connection.commit()
                    connection.close()
                    flash("Your Attendace Is Successfully Marked For The Day")
                    return redirect(request.url)
            else:
                flash("Invalid password")
                return redirect(request.url)
        else:
            flash("Invalid Id")
            return redirect(request.url)

    return render_template("student.html")

@app.route("/staff", methods=['GET', 'POST'])
def staff_page():
    if request.method == 'POST':

        #Getting data from HTML page
        staff_id = request.form['staffid']
        staff_password = request.form['staffpass']
        staff_name = request.form['staffname']

        #Making database connection
        connection = sqlite3.connect(currentdirectory + "/AMS.db")
        cursor = connection.cursor()

        #fetching staff id from student table and storing it in data1
        cursor.execute("SELECT staff_id FROM staff")
        data1 = cursor.fetchall()

        #converting the list of tuples into list
        data1_list = []

        for d in data1:
            for x in d:
                data1_list.append(x)

        #fetching student id from student_validation table and storing it in data2
        cursor.execute("SELECT id FROM staffvalidation")
        data2 = cursor.fetchall()

        #converting the list of tuples into list
        data2_id_list = []

        for dd in data2:
            for y in dd:
                data2_id_list.append(y)

        #fetching student password from student_validation table and storing it in data3
        cursor.execute("SELECT password FROM staffvalidation WHERE id = {}".format(staff_id))
        data3 = cursor.fetchall()
        print("data = ", data3)

        #converting the list of tuples into list
        data3_pass_list = []
        for ddd in data3:
            for z in ddd:
                data3_pass_list.append(z)

        if str(staff_id) in str(data2_id_list):
            if str(staff_password) in str(data3_pass_list):
                if str(staff_id) in str(data1_list):
                    flash("Your Attendace has Already bean Marked For the Day")
                    return redirect(request.url)
                else:
                    cursor.execute("INSERT INTO staff VALUES(?, ?, ?, ?)", (staff_id, staff_name, staff_password, datetime.now().strftime("%H:%M")))
                    connection.commit()
                    connection.close()
                    flash("Your Attendace Is Successfully Marked For The Day")
                    return redirect(request.url)
            else:
                flash("Invalid password")
                return redirect(request.url)
        else:
            flash("Invalid Id")
            return redirect(request.url)
   
    return render_template("staff.html")

'''login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'admin'

@login_manager.user_loader
def load_user():'''

@app.route("/admin" , methods=['GET', 'POST'])
def admin():
    return render_template("admin.html")

@app.route("/admin_login", methods=['GET', 'POST'])
def admin_login():
        
    return render_template("admin_login.html")

@app.route("/admin/change_password", methods=['GET', 'POST'])
def admin_change_password():
    return render_template("changePassword.html")

if __name__ == '__main__':
    app.run(debug=True)