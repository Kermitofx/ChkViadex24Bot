from gerarnick import gerarNick
import telepot
import requests
import json
from bs4 import BeautifulSoup as bs
from random import randint
from random import choice
from pprint import pprint
import pyfiglet
import html
import subprocess
import os
import re
from yt import search_query_yt
from time import localtime
from time import sleep
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from time import time
from helps import *
import threading
from telepot.loop import MessageLoop

id_mensagem_enviada = ""
mensagem_enviada = ""
quantidade_cpf = 0
bot = telepot.Bot("1190846298:AAF9VoduZMYyZtUJXrQMZ2tofpz0bdXeFlU")
comandos_lista = ["/sky", "/paste", "/ml", "/link", "/nickgen", "/rt", "/ping", "/emails", "/report", "/cbgen@MaxCardersBot", "/youtube", "/hash", "/nome@MaxCardersBot", "/nome", "/ssh", "/cpf@MaxCardersBot", "/admins", "/anime", "/serie", "/regra", "/regras", "/regras@MaxCardersBot" "/clima","/fixar","/calc","/noticia", "/cep","/traduz","/criptocoins","/mp4","/chkcpf","/tablet","/cell","/mp3","/pc","/traduz","/figlet","/comandos@MaxCardersBot","/thumb","/fakedataus","/fakedatabr","/fakedataca","/comandos","/status","/start","/bin","/cpf","/nome","/chkg","/chkf","/cpfgen","/cbgen","/bingen","/chkcb","/meuip","/meumac","/ip","/speednet","/noticias","/wiki","/adfly","/cotacao","/btcreal","/realbtc","/reladolar","/dolareal","/dolarbtc","/btcdolar","/chkplaca","/fakedatabr","/fakedataus","/fakedataca"]
admins = []
super = ["TioFraviin"]
bot_interage = ["EAI","EAE", "IAE", "SALVE", "IAEW", "OI", "OLÁ", "OLA"]
silenciar = False
ativar = True
deram_start = []
mandou_mensagem = []
quem = ""
voto_sim = {}
voto_nao = {}
votos_sim = 0
votos_nao = 0
mensagens_count = 0
pergunta = ""
emojis = ["🌝", "🌚", "🌚☕️", "☕️🌚", "☕️🌝","🌝☕️", "🌜", "🌜☕️", "☕️🌜"]
second_serie = []
verify_members = subprocess.getstatusoutput("cat backup_members.txt")[1]
if(verify_members == ""):
	membros = {}
else:
	membros = eval(verify_members)
verify_sessao = subprocess.getstatusoutput("cat sessoes.txt")[1]
if(verify_sessao == ""):
	sessao = {}
else:
	sessao = eval(verify_sessao)

def pastebin(texto):
	url = "http://tabuadafree.000webhostapp.com/pastebin.php"
	data = {"texto":texto}
	return requests.post(url, data=data).text

help_paste = f"""<b>USE:</b>

<pre>/paste Texto/Anotação</pre>

<b>EXEMPLO:</b>

<pre>/paste O @Oteamo é aluno do @Fraviin</pre>

<b>Saida: {pastebin("O @oteamo é aluno do @Fraviin")}</b>"""

comandos_pagina1 = f"""<b>🔥LISTA DE COMANDOS🔥</b>

<pre>/status</pre>
<b>✅ [ON] EXIBE OS COMANDOS QUE ESTÃO ONLINE.</b>
<pre>/bin</pre>
<b>✅ [ON] CONSULTA BIN.</b>
<pre>/cpf</pre>
<b>✅ [ON] CONSULTA DADOS POR CPF. (BÁSICO)</b>
<pre>/nome</pre>
<b>❌ [OFF] CONSULTA DADOS POR NOME.</b>
<pre>/chkg</pre>
<b>✅ [ON] CHECKER DE CC GERADA.</b>
<pre>/chkf</pre>
<b>❌ [OFF] CHECKER DE CC FULL.</b>
<pre>/mp3</pre>
<b>❌ [OFF] CONVERTER VIDEO YT PARA MP3.</b>
<pre>/pc</pre>
<b>❌ [OFF] PRINTAR PÁGINA COM PC.</b>
<pre>/tablet</pre>
<b>❌ [OFF] PRINTAR PÁGINA COM TABLET.</b>
<pre>/cell</pre>
<b>❌ [OFF] PRINTAR PÁGINA COM CELULAR.</b>
<b>-&gt; Página [1/5]</b>"""

comandos_pagina2 = """<b>🔥LISTA DE COMANDOS🔥</b>

<pre>/chkcpf</pre>
<b>✅ [ON] CHECKER DE CPF.</b>
<pre>/ccgen</pre>
<b>✅ [ON] GERADOR DE CC's.</b>
<pre>/cpfgen</pre>
<b>✅ [ON] GERADOR DE CPF's.</b>
<pre>/cbgen</pre>
<b>✅ [ON] GERADOR DE CONTAS BANCÁRIAS (CAIXA ECONÔMICA FEDERAL).</b>
<pre>/bingen</pre>
<b>✅ [ON] GERADOR DE BIN.</b>
<pre>/youtube</pre>
<b>✅ [ON] FAZ UMA PESQUISA NO YOUTUBE.</b>
<pre>/ip</pre>
<b>✅ [ON] RASTREAR IP.</b>
<pre>/noticias</pre>
<b>✅ [ON] EXIBIR NOTICIAS.</b>
<pre>/wiki</pre>
<b>✅ [ON] PESQUISA WIKIPEDIA.</b>
<pre>/report</pre>
<b>✅ [ON] REPORTA USUÁRIO.</b>

<b>-&gt; Página [2/5]</b>"""

comandos_pagina3 = """<b>🔥LISTA DE COMANDOS🔥</b>

<pre>/cotacao</pre>
<b>✅ [ON] EXIBIR COTAÇÕES.</b>
<pre>/extrap</pre>
<b>✅ [ON] GERA EXTRAPOLAÇÕES.</b>
<pre>/ssh</pre>
<b>✅ [ON] CRIA CONTAS SSH.</b>
<pre>/hash</pre>
<b>✅ [ON] IDÊNTIFICA POSSÍVEIS HASH's.</b>
<pre>/emails</pre>
<b>✅ [ON] CAPTURA EMAILS APARTIR DO LINK DE UM SITE.</b>
<pre>/dolarbtc</pre>
<b>❌ [OFF] CONVERTER DOLAR PRA BTC.</b>
<pre>/btcdolar</pre>
<b>❌ [OFF] CONVERTER BTC PRA DOLAR.</b>
<pre>/chkplaca</pre>
<b>❌ [OFF] CONSULTA PLACA DE VEÍCULO.</b>
<pre>/fakedatabr</pre>
<b>✅ [ON] GERADOR DE PESSOAS BR.</b>
<pre>/fakedataus</pre>
<b>❌ [OFF] GERADOR DE PESSOAS US.</b>

<b>-&gt; Página [3/5]</b>"""

comandos_pagina4 = """<b>🔥LISTA DE COMANDOS🔥</b>

<pre>/thumb</pre>
<b>✅ [ON] CAPTURAR CAPA DE VIDEO YT.</b>
<pre>/criptocoins</pre>
<b>✅ [ON] VER POSIÇÕES DE CRIPTOMOEDAS.</b>
<pre>/traduz</pre>
<b>✅ [ON] TRADUZ QUALQUER MENSAGEM PRA PORTUGUÊS.</b>
<pre>/cep</pre>
<b>✅ [ON] CONSULTA CEP.</b>
<pre>/calc</pre>
<b>✅ [ON] REALIZA CÁLCULOS.</b>
<pre>/wiki</pre>
<b>✅ [ON] FAZ PESQUISAS NO WIKIPEDIA.</b>
<pre>/fixar</pre>
<b>✅ [ON] FIXA MENSAGENS NO TOPO DO GRUPO.</b>
<pre>/regras</pre>
<b>✅ [ON] EXIBE AS REGRAS DO GRUPO.</b>
<pre>/serie</pre>
<b>❌ [OFF] EXIBE INFORMAÇÕES DE UMA SÉRIE.</b>
<pre>/anime</pre>
<b>✅ [ON] EXIBE INFORMAÇÕES DE UM ANIME.</b>

<b>-&gt; Página [4/5]</b>"""

comandos_pagina5 = """<b>🔥LISTA DE COMANDOS🔥</b>

<pre>/rt</pre>
<b>✅ [ON] CONCORDA/RETWEETA MENSAGEM QUE ALGUM USUÁRIO ENVIOU.</b>
<pre>/ping</pre>
<b>✅ [ON] EXIBE TEMPO DE RESPOSTA DO BOT.</b>
<pre>/nickgen</pre>
<b>✅ [ON] GERA NICKS CHEIOS DE CARACTERES.</b>
<pre>/link</pre>
<b>✅ [ON] EXIBE USER E LINK DO GRUPO.</b>
<pre>/ml</pre>
<b>❌ [OFF] CHECKER MERCADO LIVRE.</b>
<pre>/paste</pre>
<b>✅ [ON] RETORNA UM LINK CONTENDO O TEXTO ENVIADO.</b>
<pre>/sky</pre>
<b>❌ [OFF] CHECKER SKY.</b>

<pre>VAZIO</pre>
<b>VAZIO</b>

<pre>VAZIO</pre>
<b>VAZIO</b>

<pre>VAZIO</pre>
<b>VAZIO</b>

<b>-&gt; Página [5/5]</b>"""

comandos_online = f"""<b>COMANDOS ONLINES:</b>
	
✅  <pre>/ip</pre>
✅  <pre>/chkg</pre>
✅  <pre>/bin</pre>
✅  <pre>/cpf</pre>
✅  <pre>/comandos@MaxCardersBot</pre>
✅️  <pre>/cpfgen</pre>
✅  <pre>/status</pre>
✅  <pre>/fakedatabr</pre>
✅  <pre>/cbgen</pre>
✅  <pre>/thumb</pre>
✅  <pre>/figlet</pre>
✅  <pre>/chkcpf</pre>
✅  <pre>/cotacao</pre>
✅  <pre>/criptocoins</pre>
✅  <pre>/traduz</pre>
✅  <pre>/cep</pre>
✅  <pre>/noticias</pre>
✅  <pre>/calc</pre>
✅  <pre>/wiki</pre>
✅  <pre>/fixar</pre>
✅  <pre>/regras</pre>
✅  <pre>/anime</pre>
✅  <pre>/admins</pre>
✅  <pre>/extrap</pre>
✅  <pre>/ssh</pre>
✅  <pre>/bingen</pre>
✅  <pre>/hash</pre>
✅  <pre>/youtube</pre>
✅  <pre>/report</pre>
✅  <pre>/emails</pre>
✅  <pre>/ping</pre>
✅  <pre>/rt</pre>
✅  <pre>/nickgen</pre>
✅  <pre>/link</pre>

<b>Dê um</b> /comandos <b>para ver as descrições dos comandos e os que brevemente serão lançados.</b>\n<b>Ou envie o comando para exibir os modos de uso.</b>"""

print("\n"*9999)

def megadadosCpf(cpf):
	url = "https://braske-decode-com.umbler.net/api.php?cpf="+str(cpf);
	api = requests.get(url).json()
	return api

def cc2(cc):
	ccapi = 'http://chknet-id.com/api.php'
	r = requests.post(ccapi, {"data":cc}).text
	r = bs(r, "html.parser")
	api = r.find_all()[0].text.replace("[GATE:01]","").replace("|", " ").replace("@/ChkNET-ID", "#MaxCardersBot").replace("Unknown", "<b>✖️ REPROVADA:</b>").replace("Die", "<b>✖️ REPROVADA:</b>").replace("Live", "<b>✅️ APROVADA:</b>").replace("@/ATCHK", "#MaxCardersBot").replace("[BIN:  -  -  - ]", "<b>💵 DEBITOU:</b> 2,00 R$").replace("@ATCHK", "#MaxCardersBot")
	return api

def ccgen(quantidade, bin):
	ccs = ""
	bin = bin[0:6]
	if(len(bin) == 6):
		prefix = [bin]
		for x in range(0, quantidade):
			valid = prefix[randint(0, len(prefix)-1)]
			newcard = list(map(int, str(valid)))
			for i in range(9):
				newcard.append(randint(0, 9))
			gen = list(newcard)
			gen.reverse()
			for i, x in zip(range(len(gen)), gen):
				if i % 2 == 0:
					dub = x * 2
					dub = dub / 10 + dub % 10
					gen[i] = int(dub)
			check = sum(gen) * 9 % 10
			newcard.append(check)
			output = map(str, newcard)
			ccs += f"{''.join(output)}|{str(randint(1,12)).zfill(2)}|{str(randint(2017, 2027))}|{str(randint(1, 999)).zfill(3)}\n"
		return ccs[0:-1]
	else:
		return False
