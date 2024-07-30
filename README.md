# GERENCIADOR DE REQUERIMENTOS AOS CARTÓRIOS

Este código cria uma interface gráfica do usuário (GUI) visando a necessidade de encontrar os diversos arquivos necessários para pedidos de averbação e registro de imóveis aos cartórios, bem como facilitar esse processo a outras pessoas que nunca trabalharam com essa demanda, e precisam eventualmente fazê-lo.

## Bibliotecas/dependências utilizadas:
   - customtkinter
        > CTKImage
   - Os
   - PIL
        > Image, ImageEnhance
   - sys

<strong>O usuário/dev deverá instalar o Python e as bibliotecas necessárias em todos os computadores que for executar o programa. Optei por não incluir funções de localização de pastas no programa, exatamente para poder instalar manualmente toda vez que for necessário!</strong>
  
    
Resumo:
O Programa apresenta na janela principal uma caixa de seleção no qual o usuário pode escolher 3 opções de averbação:
   - Arrazoado Leis AUTARQUIA-4/AUTARQUIA-1 e REQ. Modelo (Conjunto de leis atualizadas e necessárias mais o requerimento modelo para editar e iniciar o pedido de averbação/registro de imóveis)
   - Arrazoado Leis AUTARQUIA-3/AUTARQUIA-1 e REQ. Modelo
   - Arrazoado Leis AUTARQUIA-2/AUTARQUIA-1 e REQ. Modelo
logo abaixo, 3 botões:
   - Abrir: Abre a pasta onde contém o arquivo pdf das leis e requerimento modelo conforme opção selecionada na caixa acima;
   - Criar Nova Pasta: Abre uma nova pasta no local selecionado para iniciar um novo pedido com nome padrão a ser usado no setor de Patrimônio.
     -> Ao clicar nesse botão, aparecerá a mensagem "Tem certeza que deseja criar a pasta agora?" e dois botões com a opção: "Sim" ou "Não".
     -> Ao Clicar em <strong>Sim</strong> o programa abre a nova pasta e apresenta uma mensagem do local exato que foi criada. Se o usuário selecionar <strong>Não</strong>, as opções se encerram.
     
   - Atualizar Planilha: Abre a planilha no qual é feito o controle do pedido, contendo informações gerais e histórico completo.

Desenvolvido por Rafael Souza. ©
