import sys
from uov import *
import os
import json
from ast import literal_eval

def main():
	m, v = 3, 3
	hash_schnorr = sys.argv[1]
	signature = literal_eval(sys.argv[2])
	pub_schnorr = sys.argv[3]
	alpha, beta = [], []
	hash, hashed_message = [], []
	number = ''

	for i in range(len(hash_schnorr)):
		if hash_schnorr[i] != ',':
			number +=hash_schnorr[i]
		else:
			aux = int (number, 16)%128
			hash += [aux]
			number = ''
	aux = int (number, 16)%128
	hash += [aux]


	with open("/home/deployer/core-bridgechain/packages/crypto/src/crypto/data.json", "r") as jsonread:
		data = json.load(jsonread)
		for i in range(len(data)):
			if data[i]['pub_schnorr'] == pub_schnorr:
				alpha = data[i]['pub_alpha_UOV']
				beta = data[i]['pub_beta_UOV']
				break

	hash = hash[0:m]
	for j in range(len(hash)):
		hashed_message += [bin(hash[j])[2:]] #Pasa a binario el hash

	for i in range (len(hashed_message)):
		aux = [int(d) for d in (hashed_message[i])]
		for k in range(7-len(aux)):
			aux.insert(0, 0)
		hashed_message [i] = aux

	print (verificacion (hashed_message, signature, alpha, beta, m))
	sys.stdout.flush()

if __name__=="__main__":
	main()
