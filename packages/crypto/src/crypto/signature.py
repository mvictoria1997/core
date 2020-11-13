import sys
from uov import *
import json

def main():
	m, v = 3, 3
	hash_schnorr = sys.argv[1]
	pub_schnorr = sys.argv[2]
	priv_schnorr = sys.argv[3]

	alpha, beta = [], []

	hash, hashed_message = [], []
	number = ''

	for i in range(len(hash_schnorr)):
		if hash_schnorr[i] != ',':
			number += hash_schnorr[i]
		else:
			aux = int (number, 16)%128
			hash +=[aux]
			number = ''
	aux = int (number, 16)%128
	hash += [aux]

	T = generacionT (m, v)

	encontrado = False
	with open("/home/deployer/core-bridgechain/packages/crypto/src/crypto/data.json", "r") as jsonread:
		data = json.load(jsonread)
		for i in range(len(data)):
			if data[i]['pub_schnorr'] == pub_schnorr:
				alpha = data[i]['priv_alpha_UOV']
				beta = data[i]['priv_beta_UOV']
				encontrado = True
				break

	if not encontrado:
		alpha, beta = clavePrivada(m, v, priv_schnorr)
		alpha_pub, beta_pub = clavePublica(m, v, alpha, beta, T)
		with open("/home/deployer/core-bridgechain/packages/crypto/src/crypto/data.json", "w") as jsonwrite:
			nuevo = {"id":len(data),
				"pub_schnorr": pub_schnorr,
				"priv_schnorr": priv_schnorr,
				"priv_alpha_UOV": alpha,
				"priv_beta_UOV": beta,
				"pub_alpha_UOV": alpha_pub,
				"pub_beta_UOV": beta_pub}
			data.append(nuevo)
			jsonwrite.seek(0)
			json.dump(data, jsonwrite)

	hash = hash[0:m]
	for i in range(len(hash)):
		hashed_message += [bin(hash[i])[2:]] #Pasa a binario el hash

	for i in range (len(hashed_message)):
		aux = [int(d) for d in (hashed_message[i])]
		for k in range(7-len(aux)):
			aux.insert(0, 0)
		hashed_message [i] = aux

	firma = signature (hashed_message, alpha, beta, m, v, T)
	print (firma)
	sys.stdout.flush()

	#print (alpha)
	#verif = verificacion (hashed_message, firma, alpha_pub, beta_pub, m)

if __name__=="__main__":
	main()
