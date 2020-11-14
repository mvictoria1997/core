import { secp256k1 } from "bcrypto";
import { IKeyPair } from "../interfaces";
import {readFileSync } from 'fs';

export class Hash {
    public static signECDSA(hash: Buffer, keys: IKeyPair): string {
		 return Hash.signUOV(hash, keys);
		  return secp256k1.signatureExport(secp256k1.sign(hash, Buffer.from(keys.privateKey, "hex"))).toString("hex");
    }

    public static verifyECDSA(hash: Buffer, signature: Buffer | string, publicKey: Buffer | string): boolean {
		  return Hash.verifyUOV(hash, signature, publicKey);
		  return Hash.verifyECDSATransaction(hash, signature, publicKey);
		  /*const bufferSignature = signature instanceof Buffer ? signature : Buffer.from(signature, "hex");
        const signatureRS = secp256k1.signatureImport(bufferSignature);

        if (!secp256k1.isLowS(signatureRS)) {
            return false;
        }

        // check that global signature length matches R and S length, see DER format :
        // <header byte><signature length><integer marker><R length><R><integer marker><S length><S>
        const signatureLength = bufferSignature.readUInt8(1);
        const rLength = bufferSignature.readUInt8(3);
        const sLength = bufferSignature.readUInt8(4 + rLength + 1);
        if (bufferSignature.length !== 4 + rLength + 2 + sLength || signatureLength !== 2 + rLength + 2 + sLength) {
            return false;
        }

        // check that first byte is positive, if it is then the whole R / S will be positive as required
        const rFirstByte = bufferSignature.readInt8(4);
        const sFirstByte = bufferSignature.readInt8(4 + rLength + 2);
        if (rFirstByte < 0 || sFirstByte < 0) {
            return false;
        }

        // if first byte is zero it is to make R/S positive, so second byte should be negative
        if (
            (rFirstByte === 0 && bufferSignature.readInt8(4 + 1) >= 0) ||
            (sFirstByte === 0 && bufferSignature.readInt8(4 + rLength + 2 + 1) >= 0)
        ) {
            return false;
        }

        return secp256k1.verify(
            hash,
            signatureRS,
            publicKey instanceof Buffer ? publicKey : Buffer.from(publicKey, "hex"),
        );*/
    }
	 public static verifyECDSATransaction(hash: Buffer, signature: Buffer | string, publicKey: Buffer | string): boolean {
			  const bufferSignature = signature instanceof Buffer ? signature : Buffer.from(signature, "hex");
			  const signatureRS = secp256k1.signatureImport(bufferSignature);

			  if (!secp256k1.isLowS(signatureRS)) {
					return false;
			  }

			  // check that global signature length matches R and S length, see DER format :
			  // <header byte><signature length><integer marker><R length><R><integer marker><S length><S>
			  const signatureLength = bufferSignature.readUInt8(1);
			  const rLength = bufferSignature.readUInt8(3);
			  const sLength = bufferSignature.readUInt8(4 + rLength + 1);
			  if (bufferSignature.length !== 4 + rLength + 2 + sLength || signatureLength !== 2 + rLength + 2 + sLength) {
					return false;
			  }

			  // check that first byte is positive, if it is then the whole R / S will be positive as required
			  const rFirstByte = bufferSignature.readInt8(4);
			  const sFirstByte = bufferSignature.readInt8(4 + rLength + 2);
			  if (rFirstByte < 0 || sFirstByte < 0) {
					return false;
			  }

			  // if first byte is zero it is to make R/S positive, so second byte should be negative
			  if (
					(rFirstByte === 0 && bufferSignature.readInt8(4 + 1) >= 0) ||
					(sFirstByte === 0 && bufferSignature.readInt8(4 + rLength + 2 + 1) >= 0)
			  ) {
					return false;
			  }

			  return secp256k1.verify(
					hash,
					signatureRS,
					publicKey instanceof Buffer ? publicKey : Buffer.from(publicKey, "hex"),
			  );
	 }

    public static signSchnorr(hash: Buffer, keys: IKeyPair): string {
        return secp256k1.schnorrSign(hash, Buffer.from(keys.privateKey, "hex")).toString("hex");
    }

    public static verifySchnorr(hash: Buffer, signature: Buffer | string, publicKey: Buffer | string): boolean {
        return secp256k1.schnorrVerify(
            hash,
            signature instanceof Buffer ? signature : Buffer.from(signature, "hex"),
            publicKey instanceof Buffer ? publicKey : Buffer.from(publicKey, "hex"),
        );
    }

	 public static signUOV(hash:Buffer, keys:IKeyPair): string {
			 console.log("signature UOV");
			 //return secp256k1.signatureExport(secp256k1.sign(hash, Buffer.from(keys.privateKey, "hex"))).toString("hex");
			 //console.log(hash);
			 var hash_string = new Array();
			 for (let i=0; i < hash.length; i++){
				 hash_string.push(hash[i].toString());
			 }
			 //console.log(hash_string);
			 const { execSync } = require('child_process');
			 var cmd = 'python ' + __dirname + '/../../src/crypto/signature.py ' + hash_string + ' ' + keys.publicKey + ' ' + keys.privateKey;
			 console.log(cmd);

			 var signature  = execSync(cmd);
			 //var hash_signature = HashAlgorithms.sha256(signature).toString("hex");
			 console.log(signature.toString());
			 onsole.log(signature.toString("hex"));
			 console.log(signature.toString("hex").slice(0,10));
			 //console.log(secp256k1.signatureExport(secp256k1.sign(hash, Buffer.from(keys.privateKey, "hex"))).toString("hex"));
			 const data = readFileSync(__dirname + '/../../src/crypto/signature.json');
			 var data_json = JSON.parse(data.toString());
			 let new_sign = {
				 hex: signature.toString("hex").slice(0, -2),
				 vector: signature.toString().trim()
			 };
			 data_json.push(new_sign);
			 var fs = require('fs');
			 //console.log(data_json);
			 fs.writeFileSync(__dirname + '/../../src/crypto/signature.json', JSON.stringify(data_json));

			 console.log(secp256k1.signatureExport(secp256k1.sign(hash, Buffer.from(keys.privateKey, "hex"))).toString("hex"));
			 return signature.toString("hex").slice(0,10);
			 return secp256k1.signatureExport(secp256k1.sign(hash, Buffer.from(keys.privateKey, "hex"))).toString("hex");
			 //return hash_signature;
	 }

	 public static verifyUOV(hash: Buffer, signature: Buffer | string, publicKey: Buffer | string): boolean {
		 console.log("verifica UOv");
		 //console.log(__dirname);

		 //console.log(hash);
		 var hash_string = new Array();
		 for (let i=0; i < hash.length; i++){
			 hash_string.push(hash[i].toString());
		 }
		 //console.log(hash_string);
		 /*const data_json = readFileSync(__dirname + '/../../src/crypto/verify.txt');
		 var signature_string = JSON.parse(data_json['string']);

		 var child = require("child_process").spawn('python', [__dirname + '/../../src/crypto/verify.py', hash_string, signature_string, publicKey.toString()]);
		 child.on('data', function(data){
			 console.log("VERIFY " + data);
			 var fs = require('fs');
			 fs.writeFile(__dirname + '/../../src/crypto/verify.txt', data, function(err){
				 if(err) throw err;
				 console.log('veri');
			 });
		 });

		 if (readFileSync(__dirname + '/../../src/crypto/verify.txt').toString() == "true"){
			 return true;
		 }*/
	   //console.log(signature)
	   //var hex_signature = signature.toString("hex");
	   let data = readFileSync(__dirname + '/../../src/crypto/signature.json');
	   let data_json = JSON.parse(data.toString());
	   //let encontrado : boolean = false;
	   var i=data_json.length-1;
	   var signature_string;
	   //var regular_expression = new RegExp(hex_signature + '[^]*', 'i');
	   //console.log(regular_expression);
		if (i == 0)
			return Hash.verifyECDSATransaction(hash, signature, publicKey);
	   /*while (i >= 0  && !encontrado){
			 if (regular_expression.test(data_json[i]['hex'])){
				  signature_string = data_json[i]['vector'];
				 encontrado = true;
			 }
			 --i;
	   }*/
		signature_string = data_json[i]['vector'];
	   //console.log(encontrado);
		//return true;
	   /*const convert = (from, to) => str => Buffer.from(str, from).toString(to)
	   const hexToUtf8 = convert('hex', 'utf8')
	   var signature_string = hexToUtf8(signature);*/
	   //Quitar espacios sino toma hasta cada espacio como param
		//console.log(signature_string);
	   while (signature_string.search('\ ') != -1){
			 signature_string = signature_string.replace('\ ', '');
	   }
	   signature_string.replace('\n', '');
	   console.log(signature_string);
	   //signature_string += '[0,0,0,0,0,0,0],[1,0,1,0,1,0,1]]'
	   const { execSync } = require('child_process');
	   var cmd =  'python ' + __dirname + '/../../src/crypto/verify.py ' + hash_string + ' ' + signature_string + ' ' + publicKey.toString();
	   console.log(cmd);
	   var verify  = execSync(cmd);
	   console.log(verify.toString().trim());
	   if (verify.toString().trim() == 'True')
			 return true;
	   else
			 return false;
  }
}
