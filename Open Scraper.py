#!/usr/bin/env python
# coding: utf-8

# In[10]:


from bs4 import BeautifulSoup
from datetime import date
import requests, smtplib, email, ssl

from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


# In[11]:


def puncClean(soup):
    soup = soup.replace("âs", "\'s")
    soup = soup.replace("â", "\"")
    soup = soup.replace("â", "\"")
    soup = soup.replace("â", "\'")
    soup = soup.replace("â", "\'")
    soup = soup.replace("â", "—")
    soup = soup.replace("\t", "")
    soup = soup.replace("\xa0", "")
    return soup


# In[12]:


# scrap and clean the text from url
url = 'https://www.djcustomnews.com/tntcaviso/mb.html'
req = requests.get(url)
page = req.text
soup = BeautifulSoup(page, 'html.parser')
marketwrap_soup = soup.find('td', attrs = {'align': 'left','class': 'padding-copy', 'style': 'font-size:14px;line-height:16px;font-family:\'Helvetica Neue\', Helvetica, Arial, \'Roboto\', sans-serif;color:#000000;padding-top:5px;padding-bottom:5px;padding-right:0;padding-left:0;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;mso-table-lspace:0pt;mso-table-rspace:0pt;text-align:auto;'})
headlines_soup = soup.find('td', attrs = {'align': 'left', 'class': 'padding-copy', 'style': 'font-size:14px;line-height:20px;font-family:\'Helvetica Neue\', Helvetica, Arial, \'Roboto\', sans-serif;color:#000000;padding-top:5px;padding-bottom:5px;padding-right:0;padding-left:0;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;mso-table-lspace:0pt;mso-table-rspace:0pt;text-align:auto;'})
text = "Headlines:\n" + puncClean(headlines_soup.get_text()) + puncClean(marketwrap_soup.get_text())
print(text)


# In[14]:


today = date.today()
date1 = today.strftime("%B %d, %Y")
my_address = '16sr8@queensu.ca'
test_address = 'stefanrobb@icloud.com'
real_address = '16sr8@queensu.ca,isaac.benjamin@queensu.ca,,jordan.abramsky@queensu.ca,matt.bourque@queensu.ca'
password = input("Type your password and press enter:")
port = 587
smtp_server = "smtp-mail.outlook.com"

# set up the SMTP server
s = smtplib.SMTP(host=smtp_server, port=port)
s.starttls()
s.login(my_address, password)

msg = MIMEMultipart()   # create a message
message = text
print(message)

# setup the parameters of the message
msg['From'] = my_address
msg['To'] = real_address
msg['Subject'] = date1 + ": Morning Briefing"
        
# add in the message body
msg.attach(MIMEText(message, 'plain'))
        
# send the message via the server set up earlier.
s.send_message(msg)
del msg
        
# Terminate the SMTP session and close the connection
s.quit()

