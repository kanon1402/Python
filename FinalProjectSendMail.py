import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# ------------ Group email ----------------------------------------
msgRoot = MIMEMultipart('related')
me = 'erp-bi.service@transcombd.com'
# to = ['rejaul.islam@transcombd.com', '']
# cc = ['biswas@transcombd.com', 'yakub@transcombd.com']
# bcc = ['ekbal.kanon@transcombd.com', '']
to = ['roseline@transcombd.com', '']
cc = ['ekbal.kanon@transcombd.com', '']
bcc = ['', '']


recipient = to + cc + bcc

subject = "Submit My project related to AHD-Chemist Analysis"

email_server_host = 'mail.transcombd.com'
port = 25

msgRoot['From'] = me

msgRoot['To'] = ', '.join(to)
msgRoot['Cc'] = ', '.join(cc)
msgRoot['Bcc'] = ', '.join(bcc)
msgRoot['Subject'] = subject

msg = MIMEMultipart()
msgRoot.attach(msg)
#
# msgText = MIMEText('This is the alternative plain text message.')
# msgAlternative.attach(msgText)

msgText = MIMEText("""
<b>Dear Apu,</b> <br>
<p>My task(AHD-Chemist Analysis) for email automation project by python has been completed.</p>
                       
<img src="cid:img1">
<img src="cid:img2">
<img src="cid:img3">
<img src="cid:img4">


<b>Thanks, </b> <br>
Md. Alhama Ekbal Kanon <br>
                    """, 'html')

msg.attach(msgText)

# --------- Set Credit image in mail -----------------------
img = open('D:/Python/New training/Day2/day_2/TT&CC.png', 'rb')
img1 = MIMEImage(img.read())
img.close()
img1.add_header('Content-ID', '<img1>')
msgRoot.attach(img1)

img = open('D:/Python/New training/Day2/day_2/CC&INV.png', 'rb')
img2 = MIMEImage(img.read())
img.close()
img2.add_header('Content-ID', '<img2>')
msgRoot.attach(img2)

img = open('D:/Python/New training/Day2/day_2/RTN&White.png', 'rb')
img3 = MIMEImage(img.read())
img.close()
img3.add_header('Content-ID', '<img3>')
msgRoot.attach(img3)

img = open('D:/Python/New training/Day2/day_2/rsm_mtd_sales.png', 'rb')
img4 = MIMEImage(img.read())
img.close()
img4.add_header('Content-ID', '<img4>')
msgRoot.attach(img4)
#
# img = open('D:/Python/New training/Day2/day_2/T3(HafizWhite).png', 'rb')
# img5 = MIMEImage(img.read())
# img.close()
# img5.add_header('Content-ID', '<img5>')
# msgRoot.attach(img5)
#
# img = open('D:/Python/New training/Day2/day_2/T4.png', 'rb')
# img6 = MIMEImage(img.read())
# img.close()
# img6.add_header('Content-ID', '<img6>')
# msgRoot.attach(img6)




# # ----------- Finally send mail and close server connection ---
server = smtplib.SMTP(email_server_host, port)
server.ehlo()
server.sendmail(me, recipient, msgRoot.as_string())
server.close()
print('Mail Send')
