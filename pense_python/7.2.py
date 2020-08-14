def eval_loop():
    while True:
        entrada = input('>>> ')
        print(eval(entrada))
        if entrada == 'done':
            break
        else:
            print(entrada)
      
eval_loop()
