import datetime as dt
import smtplib
import random

my_email = "njambibennah@gmail.com"
password = "20172017"

current_day = dt.datetime.now()
day_of_week = current_day.weekday()
with open("quotes.txt") as quotes_file:
    quotes = quotes_file.readlines()
    a_quote = random.choice(quotes)
    if day_of_week == 6:
        print(a_quote)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="wambuibennahnjambi@yahoo.com",
                                msg=f"subject: Monday motivation \n\n{a_quote}")
