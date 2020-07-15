import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# ------------ Group email ----------------------------------------
msgRoot = MIMEMultipart('related')
me = 'erp-bi.service@transcombd.com'
to = ['ekbal.kanon@transcombd.com', 'rejaul.islam@transcombd.com']
cc = ['', '']
bcc = ['', '']

recipient = to + cc + bcc

subject = "Final Project"

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
                       <table style="width:100%">
  <tr>
    <th>Firstname</th>
    <th>Lastname</th>
    <th>Age</th>
  </tr>
  <tr>
    <td>Jill</td>
    <td>Smith</td>
    <td>50</td>
  </tr>
  <tr>
    <td>Eve</td>
    <td>Jackson</td>
    <td>94</td>
  </tr>
</table>
<img src="cid:img1">
<img src="cid:img2">
<img src="cid:img3">
<img src="cid:img4">
<img src="cid:img5">
<img src="cid:img6">
                    """, 'html')

msg.attach(msgText)

# --------- Set Credit image in mail   -----------------------
img = open('D:/Python/New training/Day2/day_2/T1.png', 'rb')
img1 = MIMEImage(img.read())
img.close()
img1.add_header('Content-ID', '<img1>')
msgRoot.attach(img1)

img = open('D:/Python/New training/Day2/day_2/T2.png', 'rb')
img2 = MIMEImage(img.read())
img.close()
img2.add_header('Content-ID', '<img2>')
msgRoot.attach(img2)

img = open('D:/Python/New training/Day2/day_2/T3(AminAtik).png', 'rb')
img3 = MIMEImage(img.read())
img.close()
img3.add_header('Content-ID', '<img3>')
msgRoot.attach(img3)

img = open('D:/Python/New training/Day2/day_2/T3(AnwarhossainKamrulahsan).png', 'rb')
img4 = MIMEImage(img.read())
img.close()
img4.add_header('Content-ID', '<img4>')
msgRoot.attach(img4)

img = open('D:/Python/New training/Day2/day_2/T3(HafizWhite).png', 'rb')
img5 = MIMEImage(img.read())
img.close()
img5.add_header('Content-ID', '<img5>')
msgRoot.attach(img5)

img = open('D:/Python/New training/Day2/day_2/T4.png', 'rb')
img6 = MIMEImage(img.read())
img.close()
img6.add_header('Content-ID', '<img6>')
msgRoot.attach(img6)




# # ----------- Finally send mail and close server connection ---
server = smtplib.SMTP(email_server_host, port)
server.ehlo()
server.sendmail(me, recipient, msgRoot.as_string())
server.close()
print('Mail Send')
