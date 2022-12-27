while True:
  try:
      condicao = input()
      if  condicao == 'esquerda':
          print('ingles')
    

      if condicao == 'direita':
          print('frances')
    

      if condicao == 'nenhuma':
          print('portugues')
    

      if condicao == 'ambas':
          print('caiu')
        
  except EOFError:
    break
