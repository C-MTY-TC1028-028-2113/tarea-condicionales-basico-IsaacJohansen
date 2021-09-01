def main():
    #escribe tu código abajo de esta línea
    peso = float(input("Peso en kg: "))
    altura = float(input("Altura en m: "))
    if peso > 0 and altura > 0:
     IMC = peso / altura**2
     if IMC < 20:
      print('PESO BAJO')
     elif 20 <= IMC and IMC <25:
      print('NORMAL')
     elif 25 <= IMC and IMC <30:
      print('SOBREPESO')
     elif 30 <= IMC and IMC <40:
      print('OBESIDAD')
     elif IMC > 40:
      print('OBESIDAD MORBIDA')
    else:
        print('Revisa tus datos, alguno de ellos es erróneo.')
    

if __name__=='__main__':
    main()