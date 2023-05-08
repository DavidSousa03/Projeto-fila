lineOfOperation = []

def Start():
    print(' Bem-vindo ')
    Menu()

def Menu():
    print(' 1-Operações 2-Expressões 0-Sair')

    usr_inpt = (input('>>>  '))
    if usr_inpt == '0':
        end()
    elif usr_inpt == '1':
        Operations()
    elif usr_inpt == '2':
        Expressions()
    else:
        print(' Nenhuma operação disponível corresponde à entrada, tente novamente...')
        Menu()

    
def Expressions():
    print(' Digite a expressão matemática a ser validada:')
    user = input('>>> ')
    list = list(user)
    valueList = ['(',')','{','[',']','}']
    pairs = ['()','[]','{}']
    Compare = []
    Stack = []
    counter = len(list)
    while counter > 0:
        value = list.pop(0)
        if value in valueList:
            Compare.append(value)
        else:
            list.append(value)
        counter -= 1
    counterCompare = len(Compare)/2
    compareIndex = counterCompare
    while counterCompare > 0:
        transition = Compare.pop(0)
        Stack.append(transition)
        counterCompare -= 1
    validationFlag = 0
    invalidationFlag = 0
    Stack.reverse()
    validation = 0
    for value in Compare:
        stackTop = Stack.pop(0)
        if stackTop+value in pairs and validation == pairs.index(stackTop+value):
            validationFlag += 1
            compareIndex -= 1
        else:
            invalidationFlag += 1
            compareIndex -= 1
        validation += 1
    if invalidationFlag == 0:
        print(' A expressão é válida.')
        Menu()
    elif invalidationFlag >= 1:
        print(' A expressão não é válida.')
        Menu()

def fullOperation():
    counter = len(lineOfOperation)
    while counter > 0:
        singleOperation(1)
        counter -= 1
    Operations()

def singleOperation(x):
    if bool(lineOfOperation) == False:
        print('')
        print(' A lista de operações está vazia')
        print('')
        Operations()
    else:
        print('')
        banner = x
        op = lineOfOperation.pop(0)
        print('>>> ',op," <<<")
        operation = op.pop(0)
        result = 0
        if operation == '+':
            for x in op:
                result += x
        elif operation == '-':
            result = op.pop(0)
            for x in op:
                result -= x
        elif operation == '*':
            result = op.pop(0)
            for x in op:
                result = result*x
        elif operation == '/':
            result = op.pop(0)
            for x in op:
                result = result/x
        print(' Resultado da operação: ',result,' ')
        print('')
        if banner == 0:
            Operations()


def lineDictator(x,y):
    value = x
    banner = y
    if banner == 1:
        lineOfOperation.append(value)
    elif banner == 0:
        if value == 2:
            singleOperation(0)
        elif value == 3:
            fullOperation()

def adition():
    print(' Insira os valores a serem adicionados. Quando terminar, digite "Concluido" ')
    valueList = ["+"]
    banner = 0
    while banner == 0:
        usr_choice = input('>>>  ')
        if usr_choice == 'Concluido' or usr_choice == 'concluido':
            banner = 1
        else:
            valueList.append(int(usr_choice))
    lineDictator(valueList,1)
    Operations()

def subtration():
    print(' Insira os valores a serem subtraidos. Quando terminar, digite "Concluido" ')
    valueList = ["-"]
    banner = 0
    while banner == 0:
        usr_choice = input('>>>  ')
        if usr_choice == 'Concluido' or usr_choice == 'concluido':
            banner = 1
        else:
            valueList.append(int(usr_choice))
    lineDictator(valueList,1)
    Operations()

def multiplication():
    print(' Insira os valores a serem multiplicados. Quando terminar, digite "Concluido" ')
    valueList = ["*"]
    banner = 0
    while banner == 0:
        usr_choice = input('>>>  ')
        if usr_choice == 'Concluido' or usr_choice == 'concluido':
            banner = 1
        else:
            valueList.append(int(usr_choice))
    lineDictator(valueList,1)
    Operations()

def division():
    print(' Insira os valores a serem dividios. Quando terminar, digite "Concluido"')
    valueList = ["/"]
    banner = 0
    while banner == 0:
        usr_choice = input('>>>  ')
        if usr_choice == 'Concluido' or usr_choice == 'concluido':
            banner = 1
        else:
            if int(usr_choice) == 0:
                print(' Divisões por 0 não são permitidas.')
            else:
                valueList.append(int(usr_choice))
    lineDictator(valueList,1)
    Operations()
    
def AvailableOperation():
    print(' 1-Adição(+)')
    print(' 2-Subtração(-)')
    print(' 3-Multiplicação(*)')
    print(' 4-Divisão(/)')
   
    usr_inpt3 = (input('>>>  '))
    if usr_inpt3 == '1':
        adition()
    elif usr_inpt3 == '2':
        subtration()
    elif usr_inpt3 == '3':
        multiplication()
    elif usr_inpt3 == '4':
        division()
    else:
        print('Nenhuma operação disponível corresponde à entrada, tente novamente...')
        AvailableOperation()

def Operations():
    print(' 1- Adicionar operação à linha')
    print(' 2- Fazer a próxima operação na linha')
    print(' 3- Fazer todas as operações da linha')
    print(' 0- Voltar ao menu principal')
   
    usr_inpt2 = (input('>>>  '))
    if usr_inpt2 == '1':
        AvailableOperation()
    elif usr_inpt2 == '2':
        lineDictator(2,0)
    elif usr_inpt2 == '3':
        lineDictator(3,0)
    elif usr_inpt2 == '0':
        Start()
    else:
        print(' Nenhuma operação disponível corresponde à entrada, tente novamente...')
        Operations()

def end():
   
    print('Agradecemos sua preferência, volte sempre!')
   



Start()