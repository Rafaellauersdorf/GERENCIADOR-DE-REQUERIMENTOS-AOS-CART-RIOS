# GERENCIADOR DE REQUERIMENTOS AOS CARTÓRIOS

Este código cria uma interface gráfica do usuário (GUI) visando a necessidade de encontrar os diversos arquivos necessários para pedidos de averbação e registro de imóveis aos cartórios, bem como facilitar esse processo a outras pessoas que nunca trabalharam com essa demanda, e precisam eventualmente fazê-lo.

## Bibliotecas/dependências utilizadas:
   - customtkinter
        > CTKImage, CTkInputDialog, CTkLabel, CTkButton, CTkToplevel        
   - Os
   - PIL
        > Image, ImageEnhance
   - sys
   - socket
   - hashlib
   - uuid
   - json
   - datetime
        > timedelta
   - subprocess

<strong>O usuário não precisará instalar o Python e as bibliotecas necessárias nos computadores que for executar o programa. Somente copiar o executável e utilizar, a menos que seja um Desenvolvedor.</strong>
  
    
Resumo:
O Programa apresenta na janela principal uma caixa de seleção no qual o usuário pode escolher 4 opções de averbação:
   - Arrazoado Leis AUTARQUIA-5/AUTARQUIA-1 e REQ. Modelo (Conjunto de leis atualizadas e necessárias mais o requerimento modelo para editar e iniciar o pedido de averbação/registro de imóveis)
   - Arrazoado Leis AUTARQUIA-4/AUTARQUIA-1 e REQ. Modelo
   - Arrazoado Leis AUTARQUIA-3/AUTARQUIA-1 e REQ. Modelo
   - Arrazoado Leis AUTARQUIA-2/AUTARQUIA-1 e REQ. Modelo
logo abaixo, 4 botões:
   - Abrir: Abre a pasta onde contém o arquivo pdf das leis e requerimento modelo conforme opção selecionada na caixa acima;
   - Atualizar Planilha: Abre a planilha no qual é feito o controle do pedido, contendo informações gerais e histórico completo.
   - Telas Orientativas XXXX: Abre um arquivo .docx contendo toda orientação para a pessoa iniciar o pedido de averbação/registro de imóvel.
   - Criar Nova Pasta: Abre uma nova pasta no local selecionado para iniciar um novo pedido com nome padrão a ser usado no setor de Patrimônio.
     - Ao clicar nesse botão, aparecerá a mensagem "Tem certeza que deseja criar a pasta agora?" e dois botões com a opção: "Sim" ou "Não".
     - Ao Clicar em <strong>Sim</strong> o programa abre a nova pasta e apresenta uma mensagem do local exato que foi criada. Se o usuário selecionar <strong>Não</strong>, as opções se encerram.
     
   
     
<strong>ATUALIZAÇÃO:</strong>
- Incluido o botão "4 - Telas Orientativas SAEC" que retorna o arquivo docx das telas orientativas para se iniciar o requerimento.
- Incluido números antes da descrição nos botões para identificar a ordem de importância do processo.
- Incluido outros orgãos para iniciar os pedidos.
- incluido verificação de segurança por IP/palavra passe/endereço MAC

[![Status do Projeto](https://img.shields.io/badge/Status-Ready%20To%20Use!-brightgreen)](https://github.com/Rafaellauersdorf/GERENCIADOR-DE-REQUERIMENTOS-AOS-CART-RIOS/tree/main)
[![Número de Downloads](https://img.shields.io/github/downloads/Rafaellauersdorf/GERENCIADOR-DE-REQUERIMENTOS-AOS-CART-RIOS/total?cacheSeconds=0)](https://github.com/Rafaellauersdorf/GERENCIADOR-DE-REQUERIMENTOS-AOS-CART-RIOS/releases)


  
Desenvolvido por Rafael Souza. ©
