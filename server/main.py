from datetime import datetime
import sqlite3
from flask import Flask, request, make_response
from svm_model import model as svm_model
import sms

app = Flask(__name__)

db = sqlite3.connect("sql.db", check_same_thread=False)
cursor = db.cursor()

cursor.execute(
    "CREATE TABLE IF NOT EXISTS FARMER (phone_number INT PRIMARY KEY, crop_name TEXT, month INT)"
)


def monthToPredict(currentMonth):
    """returns the predictable month relative to current month"""

    months = {
        "[11, 12, 1, 2]": "spring",
        "[3, 4]": "summer",
        "[5, 6, 7, 8]": "monsoon",
        "[9, 10]": "winter",
    }

    for keys, values in months.items():
        if currentMonth in eval(keys):
            return values


def sms_query(number):
    curr_month = datetime.now().month
    saved_month = f"select month from FARMER where phone_number = {number}"
    cursor.execute(saved_month)

    saved_month = cursor.fetchall()[0][0]

    try:
        if curr_month == saved_month:
            sms.message_daily(monthToPredict(saved_month), number)
        elif curr_month != saved_month:
            sms.message_month(number)
            cursor.execute(
                f"update FARMER set month = {curr_month} where phone_number = {number}")
            db.commit()
        return {"message": "sms sent successfully"}
    except Exception:
        return {"message": "error in sms_query function"}


@app.route("/")
def hello_world():
    """8700877045,WATERMELON,22-10-2020"""
    query = "select sqlite_version()"
    cursor.execute(query)
    result = cursor.fetchone()
    return {
        "sqlite_version": result[0],
        "message": "server is working!",
    }


@app.route("/predict")
def predict():
    number = request.args.get("number")
    month = datetime.now().month
    month_prediction = svm_model.predict(monthToPredict(month))
    if number and len(number) == 10:
        send_sms = sms_query(int(number))
        print(send_sms)
        # try:
        #     cursor.execute(
        #         f"INSERT INTO FARMER (phone_number, crop_name, month) values ({number}, '{month_prediction}' ,{month})"
        #     )
        #     db.commit()

        return {"message": "data updated successfully"}
        # except Exception as e:
        #     print(e)
        #     return make_response({"message": "parameters not fullfilled"}, 400)
    else:
        return make_response({"message": "parameters not fullfilled"}, 400)


@app.route("/numbers")
def num():
    cursor.execute("SELECT * from FARMER")
    return {"data": cursor.fetchall()}


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
    cursor.close()
    db.close()