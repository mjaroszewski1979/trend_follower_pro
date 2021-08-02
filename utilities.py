import datetime
import pandas_datareader.data as pdr
import smtplib
from email.message import EmailMessage
from os import environ

user_name = environ.get('USER_NAME')
user_password = environ.get('USER_PASSWORD')
email_name = environ.get('EMAIL_NAME')
email_password = environ.get('EMAIL_PASSWORD')

data = {user_name: {'password': user_password}}

markets_data = [{'name':'S&P 500'}, {'name':'GOLD'}, {'name':'BITCOIN'}]

marketspro_data = [{'name':'S&P 500'}, {'name':'NASDAQ'}, {'name':'DOW JONES'}, {'name':'NIKKEI'}, {'name':'GOLD'}, {'name':'SILVER'}, {'name':'BITCOIN'}, {'name':'LITECOIN'}, {'name':'ETHEREUM'}, {'name':'US DOLLAR'}, {'name':'JP YEN'}, {'name':'CH FRANC'}, {'name':'CA DOLLAR'}]

markets = {
    'S&P 500' : 'SP500',
    'DOW JONES' : 'DJIA',
    'NASDAQ' : 'NASDAQ100',
    'NIKKEI' : 'NIKKEI225',
    'GOLD' : 'GOLDAMGBD228NLBM',
    'SILVER' : 'SLVPRUSD',
    'US DOLLAR' : 'DTWEXBGS',
    'JP YEN' : 'DEXJPUS',
    'CH FRANC' : 'DEXSZUS',
    'CA DOLLAR' : 'DEXCAUS',
    'BITCOIN' : 'CBBTCUSD',
    'LITECOIN' : 'CBLTCUSD',
    'ETHEREUM' : 'CBETHUSD'
    }  


def get_trend(symbol, start = datetime.datetime(2020, 1, 1), end = datetime.datetime.now()):
    df = pdr.DataReader(symbol, 'fred', start, end)
    if df[symbol][-1] > df[symbol][-252]:
        return 'BULLISH'
    else:
        return 'BEARISH'

def send_mail(name, email):
    message = "Thank you" + " " + name.capitalize() + " " + "for registration. You can now login with the Trend Follower - name:" + " " + user_name + "and password:" + " " + user_password + "."
    msg = EmailMessage()
    msg['Subject'] = 'Registration'
    msg['From'] = 'Trend Follower'
    msg['To'] = email
    msg.set_content(message)   



    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_name, email_password)
        smtp.send_message(msg)
