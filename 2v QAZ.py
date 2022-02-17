cryptMode = input("[Ш]ифр|[Д]ешифр: ").upper()
if cryptMode not in ['Ш','Д']:
 print("Қате: Ш немесе Д Әріпін қолданыңыз!"); raise SystemExit

startMessage = input("АшыҚ мӘтін: ").upper()
try:rotKey = int(input("Қадамды еҢгізіҢіз: "))
except ValueError: print("Қате: тек сандар енгізілуі керек!"); raise SystemExit

def encryptDecrypt(mode, message, key, final = ""):
	for symbol in message:
		if mode == 'Ш':
			final += chr((ord(symbol) + key - 16)%32 + ord('А'))
		else:
			final += chr((ord(symbol) - key - 16)%32 + ord('А'))
	return final
	
print("Шифр мӘтін:",encryptDecrypt(cryptMode, startMessage, rotKey))