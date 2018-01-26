#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

mail_host = "mail.ops.buble.org"
mail_user = "donotreply@ops.buble.org"
mail_pass = "123456"
#mailto_list = ["Wang_Yu.vb0586@buble.org","mao_junyi@buble.org"]
mailto_list = ["chen_qun@buble.org"]

msg = MIMEMultipart()

#ticks = time.strftime("%Y%m%d",time.localtime(time.time() - 24*60*60))
ticks = time.strftime("%Y%m%d")
bubili_path = "/opt/Daily_program/bubili/"+"program_daily_"+ticks+".xls"
program_dat_path = "/opt/Daily_program/program_dat/"+"program_daily_"+ticks+".dat"
content_file = open(program_dat_path)
content = content_file.read()

att2 = MIMEText(open(bubili_path, 'rb').read(), 'base64', 'utf-8')
att2["Content-Type"] = 'application/octet-stream'
att2["Content-Disposition"] = 'attachment; filename="Reclaim_Daily_program.xls"'
msg.attach(att2)
msg.attach(MIMEText('      Reclaim Daily program  Please refer to the attachment!  ', 'plain', 'utf-8'))
msg.attach(MIMEText(content, 'plain', 'utf-8'))

msg['to'] = ','.join(mailto_list)
msg['from'] = 'Reclaim_donotreply@ops.buble.org'
msg['subject'] = "Reclaim Daily program"+"_"+ticks

try:
    server = smtplib.SMTP()
    server.connect(mail_host)
    server.ehlo()
    server.starttls()
    server.login(mail_user, mail_pass)
    server.sendmail(msg['from'], mailto_list,msg.as_string())
    server.close()
    print 'Success'
except Exception, e:
   print str(e)