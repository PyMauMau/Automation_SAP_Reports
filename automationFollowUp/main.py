from ReportFromSap import TakeReportFromSap
from conectionEmail import SendEmail

site_inicial = 'pagina inicial do site'
site_target = 'pagina a ser preenchida'

# COLETANDO RELATÓRIO DO SAP
sap = TakeReportFromSap()
sap.goToSap(site_inicial,site_target,0)

# SETANDO EMAIL
email_sender = SendEmail('seu email', 'sua senha')
email_sender.sendEmail('Destinatário', 'Assunto', 'Corpo do Email')