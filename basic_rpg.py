choice1 = input("Comandante: Vamos, acorde, já é hora de trocar a patrulha! Se atrasarmos pro jantar a culpa será sua! (responda, levantar ou ignorar? \n").lower()
if choice1 == "levantar":
        print("Comandante: Vamos depressa! Estou morrendo de fome!")
if choice1 == "ignorar":
        print("Parabéns você acaba de receber um tapão na cara\nComandante: Acelera o passo seu bostinha!")
choice2 = input("Ainda com os olhos marejados você vê um agente do governo, que carregava uma maleta, entrar no prédio principal da base.\nvocê pergunta para o comandante o que tem na maleta? (responda, sim ou não)")
if choice2 == "sim":
        print("Parabéns você acaba de receber um tapão na cara\nComandante: Se for da sua conta você vai ficar sabendo.")
if choice2 == "nao":
        print("Comandante: Parabéns recruta, parece que você tá aprendendo quando fazer suas perguntas idiotas, agora vamos ou comeremos restos no jantar.")
choice3 = input("O refeitório da base áerea se encontrava meio vazio, faltava vida no lugar.\n- Eu deveria cantar uma música para meus companheiros?(sim ou não)")
if choice3 =="sim":
        print("Comandante: O que você acha que ta fazendo recruta? - O som de 3 tiros de uma pistola foi a última coisa que você ouviu antes de morre... GAME OVER")
if choice3 =="não":
        print("Comandante: É recruta, parece que os tempos estão mudando, me lembro do James cantando as músicas da Adele, totalmente desafinando, mas cantando com alegria,\ncomo se fosse no almoço de hoje.")
choice4 = input("Comandante: Ao terminar de jantar você vai ir pra academia ou irá direto pra cama? (responda, academia ou cama) ")
if choice4 == "academia":
        print("Comandante: Ótima decisão recruta, mas vê se não se sobrecarregue, precisamos de nossas energias para o dia de amanhã")
if choice4 == "cama":
        print("Comandante: Tá certo, só não durma demais, precisa estar acordado ás 0400")
choice5 = input("No caminho pro seu quarto você vê mais uma vez aquele agente do governo saindo dos aposentos do Comandante.\n-O que será que ele estava fazendo nos aposentos do Comandante sem a presença dele? (deseja seguir o agente? sim ou não) ")                                 
if choice5 == "não":
        choice5_2 = input("Não vou me meter com um agente do governo, mas será que eu deveria ao menos checar o aposento do Comandante? (sim ou não)") 
        if choice5_2 == "sim":
            choice5_2_1= input("Você encontra o aposento do Comandante limpo e organizado,\nvocê percebe que a maleta do agente do governo se encontra no criado mudo do comandante. Deseja abrir a maleta? (sim ou não")
            if choice5_2_1 == "sim":
                choice5_2_2= input("-Estes são documentos com nossas táticas de guerra, mas por que ele está em mandarin?\n O Comandante não seria um espião, ou seria?\nEu deveria entregar esses documentos ao General? (entregar, esconder, deixar onde estava)")
                if choice5_2_2 == "deixar onde estava":
                        print("??????:Parece que você achou algo que não era pra você achar.\n-sangue começa escorrer por suas costas, você foi esfaqueado onde não é um bom lugar pra ser esfaqueado. GAME OVER")
                if choice5_2_2 == "esconder":
                        print("Vou esconder isso no meu quarto.\nNo dia seguinte seu exécito perde o dia D da guerra.\nParabéns você fodeu com o batalhão.")
                if choice5_2_2 == "entregar":
                        choice5_2_3 = input("Estou indo agora mesmo nos aposentos do General, preciso esclarecer este assunto antes que seja tarde demais.\nVocê chega nos aposentos do General. General: O que houve garoto? parece que você viu um fantasma hahaha (senhor...)")
                        if choice5_2_3 == "senhor":
                            print("General: O que você encontrou garoto?\nSão documentos com nossas estratégias de guerra senhor, estavam no aposento do Comandante, parece que o Agente do governo que veio aqui mais cedo deixou essa papelada lá!\nGeneral:Porra garoto, deveria ter começado com isso!")
                            print("Parabéns você nos salvou de termos uma derrota certeira no dia de amanhã")
if choice5 == "sim":
    print("Você segue o Agente longe o suficiente para ele não te notar, mas isso não adianta muito, ele armou uma emboscada pra você, você foi inocente demais otário.")
