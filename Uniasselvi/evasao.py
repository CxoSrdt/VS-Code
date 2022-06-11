p = print
p ("1 - Taxa de evasão por série e evasão total: ATIVIDADE 1 ")
p ("2 - Caminhao: ATIVIDADE 2")
p ('3 - Clube de karting: ATIVIDADE 3')


inicio = int(input("Escolha uma das opções: "))


if inicio == 1:
    atv1 = int(input('1 = Taxa de evaão por série\n2 = Evasao total\n'))
    if atv1 == 1:
        p('ATIVIDADE: A\n(MI - MF) / MI para cada uma das séries')
        p('-'*50)
        p(f'{45} - {66} = {45-66} \ {45} = {(45-66)/45:.4} ou seja {((45-66)/45)*100:.4}%')
        p(f'{39} - {37} =   {39-37}  \ {39} = {(39-37)/39:.4} ou seja {((39-37)/39)*100:.3}%')
        p(f'{32} - {27} =   {32-27}  \ {32} = {(32-27)/32:.4} ou seja {((32-27)/32)*100:.4}%')
        p(f'{18} - {16} =   {18-16}  \ {18} = {(18-16)/18:.4} ou seja {((18-16)/18)*100:.4}%')
        p('-'*50)

    else:
        p('ATIVIDADE: B\n Evasao total')
        p('-'*50)
        p(f'(134 - 146) / 134 = {(134-146)/134:.5} ou seja {((134-146)/134)*100:.3}%')
        p('-'*50)


if inicio == 2:
    p('ATIVIDADE: 2')
    p('-'*50)
    p(f'25 Caminhao carregando cada um 14T ou seja {25*14}T')
    p(f'Na cidade B foram descarregador 65% dos caminhoes, ou seja {(65*350)/100}')
    p(f'7 homens, sendo que 4 deles trabalharam por 7 horas ou seja, {4*7} horas de trabalho')
    p(f'os outros 3 homens trabalharam 9 horas cada um, e assim temos {3*9} horas de trabalho')
    p(f'Conclui-se que, na cidade B, os 7 homens levaram {(4*7)+(3*9)} horas para descarregar as {(65*350)/100}T')
    p(f'{227.5/55:.3} Toneladas por hora')
    p('-'*50)
    p(f'Chegando na cidade A, os caminhões tiveram os 35% das 350 toneladas {350-227.5}T restante descarregadas por 5 homens trabalhando 7 horas cada um')
    p(f'ou seja foram {5*7} horas para descarregar {350-227.5}T ')
    p(f'Sua produtividade foi de {122.5/35} toneladas por hora')
    p('Fazendo a comparação entre as produtividades das equipes percebe-se que a equipe B foi mais produtiva, pois descarregou maior quantidade no mesmo tempo em horas.')
    p('-'*50)


if inicio == 3:
    atv3 = int(input('1 = População e a amostra\n2 = Indique qual a variável estatística\n'))
    if atv3 == 1:
        p('A população estudada envolve os 60 elementos de um clube de karting, de ondo foi tirada uma amostra de 16 elementos')
    else:
        p('Essa variável é classificada como uma variável quantitativa contínua')
