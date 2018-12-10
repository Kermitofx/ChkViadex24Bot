#Bibliotecas Necessárias
import re
import telepot
import requests
import html
from bs4 import BeautifulSoup as bs

bot = telepot.Bot("621597516:AAFjtiRTP1vqyCLvlq_4C4mutIv2wVOO9HE")

def cc2(cc):
	ccapi = 'http://chknet-id.com/api.php'
	r = requests.post(ccapi, {"data":cc}).text
	r = bs(r, "html.parser")
	api = r.find_all()[0].text.replace("[GATE:01]", "").replace("|", " ").replace("@/ChkNET-ID", "#ChkViadex24").replace("Unknown", "<b>✖️ INVÁLIDA:</b>").replace("Die", "<b>✖️ REPROVADA:</b>").replace("Live", "<b>✅️ APROVADA:</b>").replace("@/ATCHK", "#ChkViadex24").replace("[BIN:  -  -  - ]", "").replace("@ATCHK", "#ChkViadex24")
	return api
#Cérebro do Bot
def main(msg):

#msg na 
	def enviaMsg(texto):
		m = bot.sendMessage(msg["chat"]["id"], texto, parse_mode="html", reply_to_message_id = msg["message_id"])
		return m
#[1] enviaMsg faz o bot mandar uma mensagem.

	chatid = msg["chat"]["id"]
	marcaMsg = msg["message_id"]
	
#Inicia o bot
	if(msg["text"].upper() == "/START"):
		enviaMsg(f"""☺️ <b>Olá {msg['from']['first_name']}</b> clique em /comandos para visualizar meus comandos""")
#Lista de comandos
	elif(msg["text"].upper() == "/COMANDOS" or msg["text"].upper() == "/COMANDOS@CHKVIADEXBOT"):
		enviaMsg(f"""<b>✅ COMANDOS ONLINE:</b>

✅️ /chk - Checa um cartão

✅ /bin - Consulta dados de uma bin""")
#Consultor de Bin
	elif(msg["text"].upper() == "/BIN" or msg["text"].upper() == "/BIN@CHKVIADEXBOT"):
		enviaMsg(f"""<b>⚠️ PARA CONSULTAR UMA BIN DIGITE SEUS 6 PRIMEIROS DIGITOS EXEMPLO:</b>

<pre>/bin 541187</pre>""")
	elif(msg["text"].upper().split()[0] == "/BIN" and msg["text"].split()[1]):
		bin = msg["text"].split()[1].replace(".","").replace("/","").replace("-","")
		bin_con = enviaMsg("<b>✔️ CONSULTANDO A BIN...</b>")
		api_bin = requests.get("https://api.freebinchecker.com/bin/"+bin).json()
		coud = api_bin["card"]["type"]
		if(coud == "credit"):
			coud = "CRÉDITO"
		if(coud == "debit"):
			coud = "DÉBITO"
			
		if(api_bin["valid"] == "false"):
			enviaMsg("<b>✖️ BIN INVÁLIDA...</b>")
		else:
			bot.editMessageText((chatid, bin_con["message_id"]), f"""<b>BIN:</b> {bin}
<b>BANDEIRA:</b> {api_bin["card"]["scheme"]}
<b>TIPO:</b> {coud}
<b>NÍVEL:</b> {api_bin["card"]["category"]}
<b>BANCO:</b> {api_bin["issuer"]["name"]}
<b>SITE:</b> {api_bin["issuer"]["url"]}
<b>TELEFONE:</b> {api_bin["issuer"]["tel"]}
<b>PAÍS:</b> {api_bin["country"]["name"]}
<b>SIGLA:</b> {api_bin["country"]["alpha 2 code"]}
<b>MOEDA:</b> {api_bin["country"]["currency"]}""", parse_mode="html")
	elif(msg["text"].upper() == "/CHK" or msg["text"].upper() == "/CHK@CHKVIADEXBOT"):
		enviaMsg(f"""<b>✅ USE DESTA MANEIRA:</b>

<pre>/chk 4500043679173127|08|2020|789</pre>""")
	elif(msg["text"].upper().split()[0] == "/CHK" and msg["text"]): 
		msg_bot = enviaMsg("<b>✅ CHECANDO OS CARTÕES...</b>")
		msgb = msg["text"]
		regex = r"\d{16}\|\d{2}\|\d{4}\|\d{3}"
		cc = re.compile(regex).findall(msgb)   
		dados = ""
		for x in cc:
			dados += f"""\n \n{cc2(x)}"""
	#   enviaMsg(dados)   
#		bot.editMessage
		bot.editMessageText((msg["chat"]["id"], msg_bot["message_id"]), dados, parse_mode="html")			
			
#Para bot não parar de receber comandos
bot.message_loop(main)

while True:
   pass
  
#PROGAMADO POR: @MRHAROLD         NÃO TIRA MEUS CRÉDITOS AMIGO :3