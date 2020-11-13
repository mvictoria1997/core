import sys #para la salida de error

#Numeros aleatorios
from random import randint
import random
#Calcula el hash del mensaje
import hashlib

from time import time

#Tablas para el calcular la multiplicacion en el cuerpo
exp = {
   0 : [0, 0, 0, 0, 0, 0, 1],
   1 : [0, 0, 0, 0, 0, 1, 0],
   2 : [0, 0, 0, 0, 1, 0, 0],
   3 : [0, 0, 0, 1, 0, 0, 0],
   4 : [0, 0, 1, 0, 0, 0, 0],
   5 : [0, 1, 0, 0, 0, 0, 0],
   6 : [1, 0, 0, 0, 0, 0, 0],
   7 : [0, 0, 0, 0, 0, 1, 1],
   8 : [0, 0, 0, 0, 1, 1, 0],
   9 : [0, 0, 0, 1, 1, 0, 0],
   10 : [0, 0, 1, 1, 0, 0, 0],
   11 : [0, 1, 1, 0, 0, 0, 0],
   12 : [1, 1, 0, 0, 0, 0, 0],
   13 : [1, 0, 0, 0, 0, 1, 1],
   14 : [0, 0, 0, 0, 1, 0, 1],
   15 : [0, 0, 0, 1, 0, 1, 0],
   16 : [0, 0, 1, 0, 1, 0, 0],
   17 : [0, 1, 0, 1, 0, 0, 0],
   18 : [1, 0, 1, 0, 0, 0, 0],
   19 : [0, 1, 0, 0, 0, 1, 1],
   20 : [1, 0, 0, 0, 1, 1, 0],
   21 : [0, 0, 0, 1, 1, 1, 1],
   22 : [0, 0, 1, 1, 1, 1, 0],
   23 : [0, 1, 1, 1, 1, 0, 0],
   24 : [1, 1, 1, 1, 0, 0, 0],
   25 : [1, 1, 1, 0, 0, 1, 1],
   26 : [1, 1, 0, 0, 1, 0, 1],
   27 : [1, 0, 0, 1, 0, 0, 1],
   28 : [0, 0, 1, 0, 0, 0, 1],
   29 : [0, 1, 0, 0, 0, 1, 0],
   30 : [1, 0, 0, 0, 1, 0, 0],
   31 : [0, 0, 0, 1, 0, 1, 1],
   32 : [0, 0, 1, 0, 1, 1, 0],
   33 : [0, 1, 0, 1, 1, 0, 0],
   34 : [1, 0, 1, 1, 0, 0, 0],
   35 : [0, 1, 1, 0, 0, 1, 1],
   36 : [1, 1, 0, 0, 1, 1, 0],
   37 : [1, 0, 0, 1, 1, 1, 1],
   38 : [0, 0, 1, 1, 1, 0, 1],
   39 : [0, 1, 1, 1, 0, 1, 0],
   40 : [1, 1, 1, 0, 1, 0, 0],
   41 : [1, 1, 0, 1, 0, 1, 1],
   42 : [1, 0, 1, 0, 1, 0, 1],
   43 : [0, 1, 0, 1, 0, 0, 1],
   44 : [1, 0, 1, 0, 0, 1, 0],
   45 : [0, 1, 0, 0, 1, 1, 1],
   46 : [1, 0, 0, 1, 1, 1, 0],
   47 : [0, 0, 1, 1, 1, 1, 1],
   48 : [0, 1, 1, 1, 1, 1, 0],
   49 : [1, 1, 1, 1, 1, 0, 0],
   50 : [1, 1, 1, 1, 0, 1, 1],
   51 : [1, 1, 1, 0, 1, 0, 1],
   52 : [1, 1, 0, 1, 0, 0, 1],
   53 : [1, 0, 1, 0, 0, 0, 1],
   54 : [0, 1, 0, 0, 0, 0, 1],
   55 : [1, 0, 0, 0, 0, 1, 0],
   56 : [0, 0, 0, 0, 1, 1, 1],
   57 : [0, 0, 0, 1, 1, 1, 0],
   58 : [0, 0, 1, 1, 1, 0, 0],
   59 : [0, 1, 1, 1, 0, 0, 0],
   60 : [1, 1, 1, 0, 0, 0, 0],
   61 : [1, 1, 0, 0, 0, 1, 1],
   62 : [1, 0, 0, 0, 1, 0, 1],
   63 : [0, 0, 0, 1, 0, 0, 1],
   64 : [0, 0, 1, 0, 0, 1, 0],
   65 : [0, 1, 0, 0, 1, 0, 0],
   66 : [1, 0, 0, 1, 0, 0, 0],
   67 : [0, 0, 1, 0, 0, 1, 1],
   68 : [0, 1, 0, 0, 1, 1, 0],
   69 : [1, 0, 0, 1, 1, 0, 0],
   70 : [0, 0, 1, 1, 0, 1, 1],
   71 : [0, 1, 1, 0, 1, 1, 0],
   72 : [1, 1, 0, 1, 1, 0, 0],
   73 : [1, 0, 1, 1, 0, 1, 1],
   74 : [0, 1, 1, 0, 1, 0, 1],
   75 : [1, 1, 0, 1, 0, 1, 0],
   76 : [1, 0, 1, 0, 1, 1, 1],
   77 : [0, 1, 0, 1, 1, 0, 1],
   78 : [1, 0, 1, 1, 0, 1, 0],
   79 : [0, 1, 1, 0, 1, 1, 1],
   80 : [1, 1, 0, 1, 1, 1, 0],
   81 : [1, 0, 1, 1, 1, 1, 1],
   82 : [0, 1, 1, 1, 1, 0, 1],
   83 : [1, 1, 1, 1, 0, 1, 0],
   84 : [1, 1, 1, 0, 1, 1, 1],
   85 : [1, 1, 0, 1, 1, 0, 1],
   86 : [1, 0, 1, 1, 0, 0, 1],
   87 : [0, 1, 1, 0, 0, 0, 1],
   88 : [1, 1, 0, 0, 0, 1, 0],
   89 : [1, 0, 0, 0, 1, 1, 1],
   90 : [0, 0, 0, 1, 1, 0, 1],
   91 : [0, 0, 1, 1, 0, 1, 0],
   92 : [0, 1, 1, 0, 1, 0, 0],
   93 : [1, 1, 0, 1, 0, 0, 0],
   94 : [1, 0, 1, 0, 0, 1, 1],
   95 : [0, 1, 0, 0, 1, 0, 1],
   96 : [1, 0, 0, 1, 0, 1, 0],
   97 : [0, 0, 1, 0, 1, 1, 1],
   98 : [0, 1, 0, 1, 1, 1, 0],
   99 : [1, 0, 1, 1, 1, 0, 0],
   100 : [0, 1, 1, 1, 0, 1, 1],
   101 : [1, 1, 1, 0, 1, 1, 0],
   102 : [1, 1, 0, 1, 1, 1, 1],
   103 : [1, 0, 1, 1, 1, 0, 1],
   104 : [0, 1, 1, 1, 0, 0, 1],
   105 : [1, 1, 1, 0, 0, 1, 0],
   106 : [1, 1, 0, 0, 1, 1, 1],
   107 : [1, 0, 0, 1, 1, 0, 1],
   108 : [0, 0, 1, 1, 0, 0, 1],
   109 : [0, 1, 1, 0, 0, 1, 0],
   110 : [1, 1, 0, 0, 1, 0, 0],
   111 : [1, 0, 0, 1, 0, 1, 1],
   112 : [0, 0, 1, 0, 1, 0, 1],
   113 : [0, 1, 0, 1, 0, 1, 0],
   114 : [1, 0, 1, 0, 1, 0, 0],
   115 : [0, 1, 0, 1, 0, 1, 1],
   116 : [1, 0, 1, 0, 1, 1, 0],
   117 : [0, 1, 0, 1, 1, 1, 1],
   118 : [1, 0, 1, 1, 1, 1, 0],
   119 : [0, 1, 1, 1, 1, 1, 1],
   120 : [1, 1, 1, 1, 1, 1, 0],
   121 : [1, 1, 1, 1, 1, 1, 1],
   122 : [1, 1, 1, 1, 1, 0, 1],
   123 : [1, 1, 1, 1, 0, 0, 1],
   124 : [1, 1, 1, 0, 0, 0, 1],
   125 : [1, 1, 0, 0, 0, 0, 1],
   126 : [1, 0, 0, 0, 0, 0, 1]
}

log = {
   tuple( [0, 0, 0, 0, 0, 0, 1] ) : ' 0 ',
   tuple( [0, 0, 0, 0, 0, 1, 0] ) : ' 1 ',
   tuple( [0, 0, 0, 0, 1, 0, 0] ) : ' 2 ',
   tuple( [0, 0, 0, 1, 0, 0, 0] ) : ' 3 ',
   tuple( [0, 0, 1, 0, 0, 0, 0] ) : ' 4 ',
   tuple( [0, 1, 0, 0, 0, 0, 0] ) : ' 5 ',
   tuple( [1, 0, 0, 0, 0, 0, 0] ) : ' 6 ',
   tuple( [0, 0, 0, 0, 0, 1, 1] ) : ' 7 ',
   tuple( [0, 0, 0, 0, 1, 1, 0] ) : ' 8 ',
   tuple( [0, 0, 0, 1, 1, 0, 0] ) : ' 9 ',
   tuple( [0, 0, 1, 1, 0, 0, 0] ) : ' 10 ',
   tuple( [0, 1, 1, 0, 0, 0, 0] ) : ' 11 ',
   tuple( [1, 1, 0, 0, 0, 0, 0] ) : ' 12 ',
   tuple( [1, 0, 0, 0, 0, 1, 1] ) : ' 13 ',
   tuple( [0, 0, 0, 0, 1, 0, 1] ) : ' 14 ',
   tuple( [0, 0, 0, 1, 0, 1, 0] ) : ' 15 ',
   tuple( [0, 0, 1, 0, 1, 0, 0] ) : ' 16 ',
   tuple( [0, 1, 0, 1, 0, 0, 0] ) : ' 17 ',
   tuple( [1, 0, 1, 0, 0, 0, 0] ) : ' 18 ',
   tuple( [0, 1, 0, 0, 0, 1, 1] ) : ' 19 ',
   tuple( [1, 0, 0, 0, 1, 1, 0] ) : ' 20 ',
   tuple( [0, 0, 0, 1, 1, 1, 1] ) : ' 21 ',
   tuple( [0, 0, 1, 1, 1, 1, 0] ) : ' 22 ',
   tuple( [0, 1, 1, 1, 1, 0, 0] ) : ' 23 ',
   tuple( [1, 1, 1, 1, 0, 0, 0] ) : ' 24 ',
   tuple( [1, 1, 1, 0, 0, 1, 1] ) : ' 25 ',
   tuple( [1, 1, 0, 0, 1, 0, 1] ) : ' 26 ',
   tuple( [1, 0, 0, 1, 0, 0, 1] ) : ' 27 ',
   tuple( [0, 0, 1, 0, 0, 0, 1] ) : ' 28 ',
   tuple( [0, 1, 0, 0, 0, 1, 0] ) : ' 29 ',
   tuple( [1, 0, 0, 0, 1, 0, 0] ) : ' 30 ',
   tuple( [0, 0, 0, 1, 0, 1, 1] ) : ' 31 ',
   tuple( [0, 0, 1, 0, 1, 1, 0] ) : ' 32 ',
   tuple( [0, 1, 0, 1, 1, 0, 0] ) : ' 33 ',
   tuple( [1, 0, 1, 1, 0, 0, 0] ) : ' 34 ',
   tuple( [0, 1, 1, 0, 0, 1, 1] ) : ' 35 ',
   tuple( [1, 1, 0, 0, 1, 1, 0] ) : ' 36 ',
   tuple( [1, 0, 0, 1, 1, 1, 1] ) : ' 37 ',
   tuple( [0, 0, 1, 1, 1, 0, 1] ) : ' 38 ',
   tuple( [0, 1, 1, 1, 0, 1, 0] ) : ' 39 ',
   tuple( [1, 1, 1, 0, 1, 0, 0] ) : ' 40 ',
   tuple( [1, 1, 0, 1, 0, 1, 1] ) : ' 41 ',
   tuple( [1, 0, 1, 0, 1, 0, 1] ) : ' 42 ',
   tuple( [0, 1, 0, 1, 0, 0, 1] ) : ' 43 ',
   tuple( [1, 0, 1, 0, 0, 1, 0] ) : ' 44 ',
   tuple( [0, 1, 0, 0, 1, 1, 1] ) : ' 45 ',
   tuple( [1, 0, 0, 1, 1, 1, 0] ) : ' 46 ',
   tuple( [0, 0, 1, 1, 1, 1, 1] ) : ' 47 ',
   tuple( [0, 1, 1, 1, 1, 1, 0] ) : ' 48 ',
   tuple( [1, 1, 1, 1, 1, 0, 0] ) : ' 49 ',
   tuple( [1, 1, 1, 1, 0, 1, 1] ) : ' 50 ',
   tuple( [1, 1, 1, 0, 1, 0, 1] ) : ' 51 ',
   tuple( [1, 1, 0, 1, 0, 0, 1] ) : ' 52 ',
   tuple( [1, 0, 1, 0, 0, 0, 1] ) : ' 53 ',
   tuple( [0, 1, 0, 0, 0, 0, 1] ) : ' 54 ',
   tuple( [1, 0, 0, 0, 0, 1, 0] ) : ' 55 ',
   tuple( [0, 0, 0, 0, 1, 1, 1] ) : ' 56 ',
   tuple( [0, 0, 0, 1, 1, 1, 0] ) : ' 57 ',
   tuple( [0, 0, 1, 1, 1, 0, 0] ) : ' 58 ',
   tuple( [0, 1, 1, 1, 0, 0, 0] ) : ' 59 ',
   tuple( [1, 1, 1, 0, 0, 0, 0] ) : ' 60 ',
   tuple( [1, 1, 0, 0, 0, 1, 1] ) : ' 61 ',
   tuple( [1, 0, 0, 0, 1, 0, 1] ) : ' 62 ',
   tuple( [0, 0, 0, 1, 0, 0, 1] ) : ' 63 ',
   tuple( [0, 0, 1, 0, 0, 1, 0] ) : ' 64 ',
   tuple( [0, 1, 0, 0, 1, 0, 0] ) : ' 65 ',
   tuple( [1, 0, 0, 1, 0, 0, 0] ) : ' 66 ',
   tuple( [0, 0, 1, 0, 0, 1, 1] ) : ' 67 ',
   tuple( [0, 1, 0, 0, 1, 1, 0] ) : ' 68 ',
   tuple( [1, 0, 0, 1, 1, 0, 0] ) : ' 69 ',
   tuple( [0, 0, 1, 1, 0, 1, 1] ) : ' 70 ',
   tuple( [0, 1, 1, 0, 1, 1, 0] ) : ' 71 ',
   tuple( [1, 1, 0, 1, 1, 0, 0] ) : ' 72 ',
   tuple( [1, 0, 1, 1, 0, 1, 1] ) : ' 73 ',
   tuple( [0, 1, 1, 0, 1, 0, 1] ) : ' 74 ',
   tuple( [1, 1, 0, 1, 0, 1, 0] ) : ' 75 ',
   tuple( [1, 0, 1, 0, 1, 1, 1] ) : ' 76 ',
   tuple( [0, 1, 0, 1, 1, 0, 1] ) : ' 77 ',
   tuple( [1, 0, 1, 1, 0, 1, 0] ) : ' 78 ',
   tuple( [0, 1, 1, 0, 1, 1, 1] ) : ' 79 ',
   tuple( [1, 1, 0, 1, 1, 1, 0] ) : ' 80 ',
   tuple( [1, 0, 1, 1, 1, 1, 1] ) : ' 81 ',
   tuple( [0, 1, 1, 1, 1, 0, 1] ) : ' 82 ',
   tuple( [1, 1, 1, 1, 0, 1, 0] ) : ' 83 ',
   tuple( [1, 1, 1, 0, 1, 1, 1] ) : ' 84 ',
   tuple( [1, 1, 0, 1, 1, 0, 1] ) : ' 85 ',
   tuple( [1, 0, 1, 1, 0, 0, 1] ) : ' 86 ',
   tuple( [0, 1, 1, 0, 0, 0, 1] ) : ' 87 ',
   tuple( [1, 1, 0, 0, 0, 1, 0] ) : ' 88 ',
   tuple( [1, 0, 0, 0, 1, 1, 1] ) : ' 89 ',
   tuple( [0, 0, 0, 1, 1, 0, 1] ) : ' 90 ',
   tuple( [0, 0, 1, 1, 0, 1, 0] ) : ' 91 ',
   tuple( [0, 1, 1, 0, 1, 0, 0] ) : ' 92 ',
   tuple( [1, 1, 0, 1, 0, 0, 0] ) : ' 93 ',
   tuple( [1, 0, 1, 0, 0, 1, 1] ) : ' 94 ',
   tuple( [0, 1, 0, 0, 1, 0, 1] ) : ' 95 ',
   tuple( [1, 0, 0, 1, 0, 1, 0] ) : ' 96 ',
   tuple( [0, 0, 1, 0, 1, 1, 1] ) : ' 97 ',
   tuple( [0, 1, 0, 1, 1, 1, 0] ) : ' 98 ',
   tuple( [1, 0, 1, 1, 1, 0, 0] ) : ' 99 ',
   tuple( [0, 1, 1, 1, 0, 1, 1] ) : ' 100 ',
   tuple( [1, 1, 1, 0, 1, 1, 0] ) : ' 101 ',
   tuple( [1, 1, 0, 1, 1, 1, 1] ) : ' 102 ',
   tuple( [1, 0, 1, 1, 1, 0, 1] ) : ' 103 ',
   tuple( [0, 1, 1, 1, 0, 0, 1] ) : ' 104 ',
   tuple( [1, 1, 1, 0, 0, 1, 0] ) : ' 105 ',
   tuple( [1, 1, 0, 0, 1, 1, 1] ) : ' 106 ',
   tuple( [1, 0, 0, 1, 1, 0, 1] ) : ' 107 ',
   tuple( [0, 0, 1, 1, 0, 0, 1] ) : ' 108 ',
   tuple( [0, 1, 1, 0, 0, 1, 0] ) : ' 109 ',
   tuple( [1, 1, 0, 0, 1, 0, 0] ) : ' 110 ',
   tuple( [1, 0, 0, 1, 0, 1, 1] ) : ' 111 ',
   tuple( [0, 0, 1, 0, 1, 0, 1] ) : ' 112 ',
   tuple( [0, 1, 0, 1, 0, 1, 0] ) : ' 113 ',
   tuple( [1, 0, 1, 0, 1, 0, 0] ) : ' 114 ',
   tuple( [0, 1, 0, 1, 0, 1, 1] ) : ' 115 ',
   tuple( [1, 0, 1, 0, 1, 1, 0] ) : ' 116 ',
   tuple( [0, 1, 0, 1, 1, 1, 1] ) : ' 117 ',
   tuple( [1, 0, 1, 1, 1, 1, 0] ) : ' 118 ',
   tuple( [0, 1, 1, 1, 1, 1, 1] ) : ' 119 ',
   tuple( [1, 1, 1, 1, 1, 1, 0] ) : ' 120 ',
   tuple( [1, 1, 1, 1, 1, 1, 1] ) : ' 121 ',
   tuple( [1, 1, 1, 1, 1, 0, 1] ) : ' 122 ',
   tuple( [1, 1, 1, 1, 0, 0, 1] ) : ' 123 ',
   tuple( [1, 1, 1, 0, 0, 0, 1] ) : ' 124 ',
   tuple( [1, 1, 0, 0, 0, 0, 1] ) : ' 125 ',
   tuple( [1, 0, 0, 0, 0, 0, 1] ) : ' 126 ',
}

#------------------------------------------------------------------
#---------------FUNCIONES DE LUOV---------------
#------------------------------------------------------------------

#---------------------Clave privada------------------------
def clavePrivada (m, v, hash_schnorr):

   """
   Random alpha and beta calculation

   Parameters:
   m (int): Number of oil
   v (int): Number of vinager

   Returns:
   alpha  (tridimensional matrix): Part of a private key
   beta (matrix): Part of a private key

   """
   alpha, beta = [], []
   n = m+v
   random.seed(hash_schnorr)

   for k in range(m):
      #alpha matriz triangular superior
      aux = []
      for i in range (v):
         row = []
         for j in range (n):
            if i > j:
               row += [0]
            else:
               if randint(0,1) == 0:
                  row += [0]
               else:
                  row += [1]
         aux += [row]
      alpha += [aux]



      #beta
      row = []
      for i in range(n):
         if randint(0,1) == 0:
            row += [0]
         else:
            row += [1]
      beta += [row]
   return alpha, beta


#-----------------Clave publica------------------------
def clavePublica(m, v, alpha, beta, T):
   """
   Public keys calculation using private keys

   Parameters:
   m (int): Number of oil
   v (int): Number of vinager
   alpha (tridimensional matrix): Part of private key
   beta (matrix): Part of a private key
   T (matrix): it use for calculate alpha

   Returns:
   alpha_pub (tridimensional matrix): Part of a public key
   beta_pub (matrix): Part of a public key

   """
   alpha_pub = []
   beta_pub = []
   T_trans = matrix_transpose(T[0:v])

   tiempo_ini = time()
   for k in range(len(alpha)):
      aux = matrix_product_F2(T_trans , alpha [k])
      alpha_pub += [matrix_product_F2(aux, T)]


      beta_pub += [matrix_product_F2([beta[k]], T)]
      #print (time() - tiempo_ini)

   return alpha_pub, beta_pub


#--------------------------GeneracionT-----------------------------
def generacionT (v, m):
   """
   Signature of a message with hash, hashed. Here we have to use the private key.

   Parameters:
   m (int): Number of oil
   v (int): Number of vinager

   Returns:
   T (matrix): Matrix with dimension nxn

   """
   #Matriz de distorsion
   T = []
   n = v + m
   for i in range(n):
      row = []
      if i < v:
         for k in range(n):
            if k < v: #Matriz indentidad dimension v
               if i == k:
                  row += [1]
               else:
                  row += [0]

            else: #Matriz aleatoria vxm
               if randint(0,2) == 1:
                  row += [1]
               else:
                  row += [0]

      else:
         for k in range(n):
            if k < v: #Matriz nula dimension v
               row += [0]

            else: #Matriz identidad dimension m
               if i == k:
                  row += [1]
               else:
                  row += [0]
      T += [row]
   return T

#--------------------------Firma-----------------------------
def signature(hashed, alpha_F2, beta_F2, m, v, T):
   """
   Signature of a message with hash, hashed. Here we have to use the private key.

   Parameters:
   hashed: Hash of a message
   alpha (tridimensional matrix): Part of private key
   beta (matrix): Part of a private key
   m (int): Number of oil
   r (int): Extended field dimension
   v (int): Number of vinager
   T (matrix):

   Returns:
   signature (vector): Vector with dimension n

   """
   alpha = matrix3d_F2to128(alpha_F2)
   beta = matrix_F2to128(beta_F2)

   vinagre = []
   for k in range(v):
      aux = randint(0, 127)
      vinagre += [F128(aux)]
   coef = []
   term = []

   n= m + v
   for k in range(m):
      A = matrix_product([vinagre], alpha[k])
      coef += matrix_sum([A[0][v:n]], [beta[k][v:n]])
      v_suma = suma (matrix_product([A[0][0:v]], matrix_transpose([vinagre]))[0][0], matrix_product([beta[k][0:v]], matrix_transpose([vinagre]))[0][0])
      term += [suma(hashed[k], v_suma)]


   oil = matrix_rref(coef, matrix_transpose([term]))

   aux = []
   aux += vinagre + matrix_transpose(oil)[0]
   firma = matrix_product([aux], matrix_transpose(matrix_F2to128(T))) #T = T.inverse()
   return firma[0]



#-----------------Verificacion------------------------
def verificacion(hashed, firma, alpha_pub_F2, beta_pub_F2, m):
   """
   Verification of a signature message with hash, hashed. Here we have to use the public key.

   Parameters:
   hashed: Hash of a message
   firma: Signature of a message
   alpha_pub (tridimensional matrix): Part of public key
   beta_pub (matrix): Part of a public key
   m (int): Number of oil

   Returns:
   verif (bool): If is True the message hasn't have some modification, else the signature isn't valid

   """
   verif = True
   alpha_pub = matrix3d_F2to128(alpha_pub_F2)
   beta_pub = matrix3d_F2to128(beta_pub_F2)
   #print(beta_pub)
   for k in range(m):
      aux_alpha = matrix_product(matrix_product ([firma], alpha_pub[k]), matrix_transpose([firma]))
      aux_beta = matrix_product (beta_pub[k], matrix_transpose([firma]))
      verif = verif and (hashed[k] == matrix_sum(aux_alpha,  aux_beta)[0][0])

   return verif

#------------------------------------------------------------------
#-----------FIN FUNCIONES DE LUOV------------
#------------------------------------------------------------------


#------------------------------------------------------------------
#----------FUNCIONES DEL CUERPO-------------
#------------------------------------------------------------------
#--------------------------Suma-------------------------------
def suma(n1=[], n2=[]):
   """
   Sum of two field elements. In this case we have implemented the xor gate by the structure field.

   Parameters:
   n1(vector): field element
   n2(vector): field element

   Returns:
   suma (vector): Sum vector
   """

   suma = []
   for i in range(len(n1)):
      if n1[i] == n2[i]:
         suma += [0]
      else:
         suma += [1]
   return suma



#---------------------Producto--------------------------
def product(n1=[], n2=[]):
   """
   Product of two field elements. We have used the dict log and exp

   Parameters:
   n1(vector): field element
   n2(vector): field element

   Returns:
   product (vector): Product vector
   """
   product = []
   if (n1 == [0,0,0,0,0,0,0]) or (n2 == [0,0,0,0,0,0,0]):
      product = [0,0,0,0,0,0,0]
   else:
      suma = (int(log.get(tuple(n1))) + int(log.get(tuple(n2))))%127
      product = exp.get(suma)
   return product


#---------------------Mayor que--------------------------
def mayor (n1=[],n2=[]):
   """
   Implementation of a greater than with two field elements.

   Parameters:
   n1(vector): field element
   n2(vector): field element

   Returns:
   (bool): If is True n1 is greater than n2, else n2 is greater than n1
   """

   if n1 == [0,0,0,0,0,0,0]:
      return False
   else:
      log1, log2 = log.get(tuple(n1)), log.get(tuple(n2))
      return int(log1) > int(log2)


#---------------------------Inverso---------------------------
   """
   Calculate the inverse in the finite field with 128 element.

   Parameters:
   n(vector): field element

   Returns:
   (vector): Inverse of n
   """
def inverse(n=[]):
   i = 0
   while product(n, F128(i)) != [0,0,0,0,0,0,1]:
      i += 1
   return F128(i)


#-----------Pasar un elemento al cuerpo--------------
def F128(n1):
   """
   Calculate the vector in the finite field with 128 element.

   Parameters:
   n(int): Integer in {0,..,127}

   Returns:
   (vector): Field element
   """
   if n1 == 127:
      return [0,0,0,0,0,0,0]
   else:
      return exp.get(n1)

#-----------Pasar un elemento al cuerpo--------------
def matrix_F2to128(n1=[]):
   """
   Calculate the vector in the finite field with 128 element.

   Parameters:
   n(int): Integer in {0, 1}

   Returns:
   (vector): Field element
   """
   n =[]
   for i in range(len(n1)):
      row =[]
      for j in range(len(n1[0])):
         if n1[i][j] == 0:
            row += [[0,0,0,0,0,0,0]]
         else:
            row += [[0,0,0,0,0,0,1]]
      n += [row]
   return n

#-----------Pasar un elemento al cuerpo--------------
def matrix3d_F2to128(n1=[]):
   """
   Calculate the vector in the finite field with 128 element.

   Parameters:
   n(int): Integer in {0, 1}

   Returns:
   (vector): Field element
   """

   matrix =[]
   for i in range(len(n1)):
      n = []
      for j in range(len(n1[0])):
         row = []
         for k in range(len(n1[0][0])):
            if n1[i][j][k] == 0:
               row += [[0,0,0,0,0,0,0]]
            else:
               row += [[0,0,0,0,0,0,1]]
         n += [row]
      matrix += [n]
   return matrix



#------------------------------------------------------------------
#-------FIN FUNCIONES DEL CUERPO---------
#------------------------------------------------------------------


#------------------------------------------------------------------
#----------MATRICES EN EL CUERPO-------------
#------------------------------------------------------------------
#---------------Producto de matrices------------------
def matrix_product_F2 (n1=[], n2=[]):
   """
   Calculate the product matrix in the finite field F2. This matrix is the product of n1 and n2

   Parameters:
   n1(list): First matrix
   n2(list): Second matrix

   Returns:
   prod(list): Product of n1 and n2
   """

   prod=[]

   if len(n1[0]) == len(n2):
      for row1 in range(len(n1)):
         aux = []
         for col in range(len(n2[0])):
            p_suma = 0
            for row2 in range(len(n2)):
               p_suma = (n1[row1][row2] * n2[row2][col]) ^ p_suma
            aux += [p_suma]
         prod += [aux]
   return prod


#---------------Producto de matrices------------------
def matrix_product (n1=[], n2=[]):
   """
   Calculate the product matrix in the finite field. This matrix is the product of n1 and n2

   Parameters:
   n1(list): First matrix
   n2(list): Second matrix

   Returns:
   prod(list): Product of n1 and n2
   """

   prod=[]
   if len(n1[0]) == len(n2):
      for row1 in range(len(n1)):
         aux = []
         for col in range(len(n2[0])):
            p_suma = [0,0,0,0,0,0,0]
            for row2 in range(len(n2)):
               p_suma = suma (product(n1[row1][row2], n2[row2][col]), p_suma)
            aux += [p_suma]
         prod += [aux]
   return prod

#---------------Suma de matrices------------------
def matrix_sum (m1, m2):
   """
   Calculate the sum matrix in the finite field. This matrix is the sum of n1 and n2

   Parameters:
   n1(list): First matrix
   n2(list): Second matrix

   Returns:
   m_suma(list): Sum of n1 and n2
   """
   m_suma = []

   if (len(m1) == len(m2)) and (len(m1[0]) == len(m2[0])):
      for row in range(len(m1)):
         aux = []
         for col in range(len(m1[0])):
            aux += [suma (m1[row][col], m2[row][col])]
         m_suma += [aux]
   return m_suma

#---------------Matriz transpuesta------------------
def matrix_transpose(m):
   """
   Calculate the transpose matrix, in the finite field,m

   Parameters:
   m(list): Matrix

   Returns:
   trans(list): Transpose of m
   """

   trans = []
   for col in range(len(m[0])):
      aux = []
      for row in range(len(m)):
         aux += [m[row][col]]
      trans += [aux]
   return trans



#---------------Metodo de Gauss-Jordan------------------
def matrix_rref(A, b):
   """
   Calculate the solution of a equations system in the finite field. This system has the form Ax=b

   Parameters:
   A(list): Coefficient matrix
   b(list): Terms matrix

   Returns:
   x(list): Solution of a system
   """

   r = 0
   row = []
   n = len(A)

   #Anadir b como una columna
   M = A
   for i in range(len(M)):
      M[i] += b[i]


   for k in range(n):
      #Intercambio de filas para que quede arriba la de menor valor
      for i in range(k, n):
         if mayor(M[i][k], M[k][k]):
            row = M[k]
            M[k] = M[i]
            M[i] = row


      #Hacer ceros
      for j in range(k+1, n):
         q = product(M[j][k], inverse(M[k][k]))
         for m in range(k, n+1):
            M[j][m] = suma(M[j][m], product(q, M[k][m]))


   #Calcular la solucion x de abajo arriba
   x = [[[0,0,0,0,0,0,0]] for i in range(n)]

   x[n-1] = [product(M[n-1][n], inverse(M[n-1][n-1]))]
   for i in range(n-1, -1, -1):
      z = [0,0,0,0,0,0,0]
      for j in range(i+1, n):
         z = suma(z, product(M[i][j], x[j][0]))
      x[i] = [product(suma(M[i][n], z), inverse(M[i][i]))]

   return x

#---------------Matriz identidad------------------
def matrix_identity(dim):
   """
   Calculate the identity matrix with dimension dim in the finite field.

   Parameters:
   dim(int): Dimension of identity matrix

   Returns:
   matrix(list): Identity matrix with dimension dim
   """
   matrix = []

   for i in range(dim):
      aux = []
      for j in range(dim):
         if i == j:
            aux += [[0,0,0,0,0,0,1]]
         else:
            aux += [[0,0,0,0,0,0,0]]
      matrix += [aux]
   return matrix
#------------------------------------------------------------------
#-------FIN MATRICES EN EL CUERPO---------
#------------------------------------------------------------------


def main():

   #Number of vinegar and oil
   #r, m, v = 7, 83, 283
   #r, m, v =7, 57, 197
   r, m, v= 7, 44, 151
   #r, m, v = 7, 35, 121
   #r, m, v = 7, 19, 65
   #r, m, v = 7, 10, 30 #con este tamano funciona
   m, v = 3, 3
   n = m + v

   #Private key
   alpha, beta = clavePrivada(m, v, "c2f1")

   #generacion matriz T
   T = []
   T = generacionT (m, v)


   #Publics keys
   alpha_pub, beta_pub = clavePublica(m, v, alpha, beta, T)


   #Signature
   mensaje = "Este mensaje es un mensaje de prueba. Quiero se sea un poco largo para que se aprecie el efecto de la funcion hash"
   hashed = hashlib.sha256(mensaje.encode('utf-8')).hexdigest()[0:m]

   hashed_message = []

   for i in range(len(hashed)):
      hashed_message += [bin(int(hashed[i], 16))[2:]] #Pasa a binario el hash

   for i in range (len(hashed_message)):
      aux = [int(d) for d in (hashed_message[i])]
      for k in range(7-len(aux)):
         aux.insert(0, 0)
      hashed_message [i] = aux

   firma = signature (hashed_message, alpha, beta, m, r, v, T)


   #Verification
   verif = verificacion (hashed_message, firma, alpha_pub, beta_pub, m)
   print(verif)


if __name__ == "__main__":
   main()
