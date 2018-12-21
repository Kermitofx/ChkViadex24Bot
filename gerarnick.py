import random
import html

def gerarNick(palavra):
	palavra = html.escape(palavra.strip())
	
	#LETRAS
	a = list("Aﾑ4ĀᴀΛᐂ⍲Ă∆ĄÄ")
	b = list("B乃β")
	c = list("CĆČ")
	d = list("DĎĐ")
	e = list("EË€乇3ĒᙍƐҽĔĚĘĖ")
	f = list("ғFｷ₣ﾓ")
	g = list("GĢǤĞ")
	h = list("HんĦΉʜｻ")
	i = list("IÎÏΞɪĮĪﾉ")
	j = list("ᒘJ")
	k = list("KҟĶ")
	l = list("LĹĻĽŁﾚ")
	m = list("MᘻⱮ")
	n = list("ŃŅ刀иɴПƝŇN")
	o = list("O◊のᴏØӨටŐ")
	p = list("Pｱ")
	q = list("Q")
	r = list("RɾŔ尺Ř")
	s = list("SŠㄎ$Ş")
	t = list("TŤȚͲƬᴛƬŢ")
	u = list("UÜŪЦŮŰŲ")
	v = list("V")
	w = list("WЩ₩")
	x = list("ﾒX")
	y = list("¥ЏYÝ")
	z = list("ZŹ乙ŻŽ")

	risco = "̸"
	tracado = "̶"
	capa = "̲̅"
	
	resultado = ""
	for letra in palavra:
		if(random.randint(1, 2) == 1):
			if(letra.upper() == "A"):
				if(letra.isupper()):
					letra = random.choice(a)
				else:
					letra = random.choice(a).lower()
		
		if(random.randint(1, 2) == 1):
			if(letra.upper() == "B"):
				if(letra.isupper()):
					letra = random.choice(b)
				else:
					letra = random.choice(b).lower()
		
		
		if(random.randint(1, 2) == 1):
			if(letra.upper() == "C"):
				if(letra.isupper()):
					letra = random.choice(c)
				else:
					letra = random.choice(c).lower()
		
		
		if(random.randint(1, 2) == 1):
			if(letra.upper() == "D"):
				if(letra.isupper()):
					letra = random.choice(d)
				else:
					letra = random.choice(d).lower()
		
		if(random.randint(1, 2) == 1):
			if(letra.upper() == "E"):
				if(letra.isupper()):
					letra = random.choice(e)
				else:
					letra = random.choice(e).lower()
		
		if(random.randint(1, 2) == 1):
			if(letra.upper() == "F"):
				if(letra.isupper()):
					letra = random.choice(f)
				else:
					letra = random.choice(f).lower()
		
		if(random.randint(1, 2) == 1):
			if(letra.upper() == "G"):
				if(letra.isupper()):
					letra = random.choice(g)
				else:
					letra = random.choice(g).lower()
		
		if(random.randint(1, 2) == 1):
			if(letra.upper() == "H"):
				if(letra.isupper()):
					letra = random.choice(h)
				else:
					letra = random.choice(h).lower()
		
		if(random.randint(1, 2) == 1):
			if(letra.upper() == "I"):
				if(letra.isupper()):
					letra = random.choice(i)
				else:
					letra = random.choice(i).lower()
					
		if(random.randint(1, 2) == 1):
			if(letra.upper() == "J"):
				if(letra.isupper()):
					letra = random.choice(j)
				else:
					letra = random.choice(j).lower()
		
		if(random.randint(1, 2) == 1):
			if(letra.upper() == "K"):
				if(letra.isupper()):
					letra = random.choice(k)
				else:
					letra = random.choice(k).lower()
		
		if(random.randint(1, 2) == 1):
			if(letra.upper() == "L"):
				if(letra.isupper()):
					letra = random.choice(l)
				else:
					letra = random.choice(l).lower()
		
		if(random.randint(1, 2) == 1):
			if(letra.upper() == "M"):
				if(letra.isupper()):
					letra = random.choice(m)
				else:
					letra = random.choice(m).lower()
		
		if(random.randint(1, 2) == 1):
			if(letra.upper() == "N"):
				if(letra.isupper()):
					letra = random.choice(n)
				else:
					letra = random.choice(n).lower()
		
		if(random.randint(1, 2) == 1):
			if(letra.upper() == "O"):
				if(letra.isupper()):
					letra = random.choice(o)
				else:
					letra = random.choice(o).lower()
		
		if(random.randint(1, 2) == 1):
			if(letra.upper() == "P"):
				if(letra.isupper()):
					letra = random.choice(p)
				else:
					letra = random.choice(p).lower()
		
		if(random.randint(1, 2) == 1):
			if(letra.upper() == "Q"):
				if(letra.isupper()):
					letra = random.choice(q)
				else:
					letra = random.choice(q).lower()
		
		if(random.randint(1, 2) == 1):
			if(letra.upper() == "R"):
				if(letra.isupper()):
					letra = random.choice(r)
				else:
					letra = random.choice(r).lower()
		
		if(random.randint(1, 2) == 1):
			if(letra.upper() == "S"):
				if(letra.isupper()):
					letra = random.choice(s)
				else:
					letra = random.choice(s).lower()
		
		if(random.randint(1, 2) == 1):
			if(letra.upper() == "T"):
				if(letra.isupper()):
					letra = random.choice(t)
				else:
					letra = random.choice(t).lower()
		
		if(random.randint(1, 2) == 1):
			if(letra.upper() == "U"):
				if(letra.isupper()):
					letra = random.choice(u)
				else:
					letra = random.choice(u).lower()
		
		if(random.randint(1, 2) == 1):
			if(letra.upper() == "V"):
				if(letra.isupper()):
					letra = random.choice(v)
				else:
					letra = random.choice(v).lower()
		
		if(random.randint(1, 2) == 1):
			if(letra.upper() == "W"):
				if(letra.isupper()):
					letra = random.choice(w)
				else:
					letra = random.choice(w).lower()
		
		if(random.randint(1, 2) == 1):
			if(letra.upper() == "X"):
				if(letra.isupper()):
					letra = random.choice(x)
				else:
					letra = random.choice(x).lower()
		
		if(random.randint(1, 2) == 1):
			if(letra.upper() == "Y"):
				if(letra.isupper()):
					letra = random.choice(y)
				else:
					letra = random.choice(y).lower()
		
		if(random.randint(1, 2) == 1):
			if(letra.upper() == "Z"):
				if(letra.isupper()):
					letra = random.choice(z)
				else:
					letra = random.choice(z).lower()
		
		
		if(letra != " "):
			if(random.randint(1, 2) == 1):
				letra += risco
		
		if(letra != " "):
			if(random.randint(1, 2) == 1):
				letra += tracado
			
		if(letra != " "):
			if(random.randint(1, 5) == 3):
				letra += capa
			
		resultado += letra
		
	if(random.randint(1, 2) == 1):
		resultado = resultado+"ツ"
	
	if(random.randint(1, 2) == 1):
		if(resultado[-1] != "ツ"):
			items = random.choice(list("ヾヴガギグゲゴザジஇズゼゾダヂヅデドバパビピブプベペボポヷヸヹヺ"))
			resultado = items+resultado+items

	return resultado