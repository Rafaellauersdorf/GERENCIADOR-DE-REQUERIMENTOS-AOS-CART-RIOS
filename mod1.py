import customtkinter
import os
from PIL import Image, ImageTk, ImageEnhance

def abrir_arquivo():
    opcao_selecionada = opcoes.get()
    pasta_destino = ""

    if opcao_selecionada == "1 - Arrazoado Leis IAP/IAT e REQ. Modelo":
        pasta_destino = "S:/GEAD-DAG-PATRIMONIO/REGISTRO DE IMOVEIS IAT - GERAL/LEIS E DECRETOS ATUAIS PARA REQUERIMENTO DE REGISTROS/ARRAZOADO DE LEIS CRIAÇÃO IAP ATE IAT - NÃO MUDA CNPJ" #PASTA ONDE CONTEM OS ARQUIVOS A SER EDITADOS.
    elif opcao_selecionada == "2 - Arrazoado Leis ITCG/IAT e REQ. Modelo":
        pasta_destino = "S:/GEAD-DAG-PATRIMONIO/REGISTRO DE IMOVEIS IAT - GERAL/LEIS E DECRETOS ATUAIS PARA REQUERIMENTO DE REGISTROS/ARRAZOADO DE LEIS CRIAÇÃO ITCG ATE IAT - MUDA CNPJ"
    elif opcao_selecionada == "3 - Arrazoado Leis ITC/IAT e REQ. Modelo":
        pasta_destino = "S:/GEAD-DAG-PATRIMONIO/REGISTRO DE IMOVEIS IAT - GERAL/LEIS E DECRETOS ATUAIS PARA REQUERIMENTO DE REGISTROS/ARRAZOADO DE LEIS CRIAÇÃO ITC ATE IAT - MUDA CNPJ"
    if pasta_destino:
        os.startfile(pasta_destino)

def criar_pasta():
    def confirmar_criacao():
        opcao_selecionada = opcoes.get()
        pasta_base = "S:/GEAD-DAG-PATRIMONIO/REGISTRO DE IMOVEIS IAT - GERAL"

        if opcao_selecionada == "1 - Arrazoado Leis IAP/IAT e REQ. Modelo":
            pasta_destino = "S:/GEAD-DAG-PATRIMONIO/REGISTRO DE IMOVEIS IAT - GERAL/LEIS E DECRETOS ATUAIS PARA REQUERIMENTO DE REGISTROS/ARRAZOADO DE LEIS CRIAÇÃO IAP ATE IAT - NÃO MUDA CNPJ"
        elif opcao_selecionada == "2 - Arrazoado Leis ITCG/IAT e REQ. Modelo":
            pasta_destino = "S:/GEAD-DAG-PATRIMONIO/REGISTRO DE IMOVEIS IAT - GERAL/LEIS E DECRETOS ATUAIS PARA REQUERIMENTO DE REGISTROS/ARRAZOADO DE LEIS CRIAÇÃO ITCG ATE IAT - MUDA CNPJ"
        elif opcao_selecionada == "3 - Arrazoado Leis ITC/IAT e REQ. Modelo":
            pasta_destino = "S:/GEAD-DAG-PATRIMONIO/REGISTRO DE IMOVEIS IAT - GERAL/LEIS E DECRETOS ATUAIS PARA REQUERIMENTO DE REGISTROS/ARRAZOADO DE LEIS CRIAÇÃO ITC ATE IAT - MUDA CNPJ"
        else:
            customtkinter.CTkLabel(frame_mensagens, text="Selecione uma opção válida!", text_color="red").pack(pady=5)
            return 

        if pasta_base:
            nome_subpasta = "PEDIDOS DE REGISTRO XXXXXXX - PROTOCOLAR SAEC - EPROC"
            caminho_subpasta = os.path.join(pasta_base, nome_subpasta)
            os.makedirs(caminho_subpasta, exist_ok=True)
            
            frame_confirmacao.pack_forget()

            # Abrir a subpasta criada
            os.startfile(caminho_subpasta)

            # Mensagem informativa (apenas após a confirmação)
            customtkinter.CTkLabel(frame_mensagens, text=f"A subpasta '{nome_subpasta}' foi criada e aberta em:\n{pasta_base}", text_color="red").pack(pady=5)

    # Limpar mensagens anteriores
    for widget in frame_mensagens.winfo_children():
        widget.destroy()

    frame_confirmacao = customtkinter.CTkFrame(frame_mensagens)
    label_confirmacao = customtkinter.CTkLabel(frame_confirmacao, text="Tem certeza que deseja criar a pasta agora?")
    botao_sim = customtkinter.CTkButton(frame_confirmacao, text="Sim", command=confirmar_criacao)
    botao_nao = customtkinter.CTkButton(frame_confirmacao, text="Não", command=lambda: frame_confirmacao.pack_forget())

    label_confirmacao.pack(pady=5)
    botao_sim.pack(side="left", padx=5)
    botao_nao.pack(side="left", padx=5)

    frame_confirmacao.pack(pady=5)

def atualizar_planilha():
    caminho_planilha = "S:/GEAD-DAG-PATRIMONIO/REGISTRO DE IMOVEIS IAT - GERAL/CONTROLE REQUERIMENTOS AOS CARTÓRIOS - GERAL.xlsx"
    os.startfile(caminho_planilha)

app = customtkinter.CTk()
app.geometry("650x350")
app.title("Programa Modelo de Pedidos aos Cartórios")

# Carregar e ajustar a imagem de fundo
imagem_fundo = Image.open(r"C:\Users\bol.rafaelsouza\Desktop\Docs-Rafael-Temporários\Programa-modelo-pedidos-cartorios\Logo animado azul neon futurista para tecnologia.png")  # Substitua pelo caminho da sua imagem
largura_imagem = 180  # Largura desejada para a imagem na lateral
altura_imagem = imagem_fundo.height * largura_imagem // imagem_fundo.width  # Ajusta a altura proporcionalmente
imagem_fundo = imagem_fundo.resize((largura_imagem, altura_imagem))  # Redimensiona a imagem

# Aumentar a saturação e o contraste
enhancer_cor = ImageEnhance.Color(imagem_fundo)
imagem_fundo = enhancer_cor.enhance(0.5)  # Ajuste o valor para controlar a saturação (1.0 = original)
enhancer_contraste = ImageEnhance.Contrast(imagem_fundo)
imagem_fundo = enhancer_contraste.enhance(0.7)  # Ajuste o valor para controlar o contraste (1.0 = original)

# Converter para PhotoImage (sem transparência)
imagem_fundo_tk = ImageTk.PhotoImage(imagem_fundo)

# Criar um rótulo para exibir a imagem de fundo
label_fundo = customtkinter.CTkLabel(app, image=imagem_fundo_tk, text="")
label_fundo.place(x=0, y=(app.winfo_height() - altura_imagem) // 2)  # Centraliza verticalmente

opcoes = customtkinter.CTkComboBox(app, 
                                  values=[
                                      "1 - Arrazoado Leis IAP/IAT e REQ. Modelo",
                                      "2 - Arrazoado Leis ITCG/IAT e REQ. Modelo",
                                      "3 - Arrazoado Leis ITC/IAT e REQ. Modelo"
                                  ],
                                  width=285)
opcoes.pack(pady=20)

botao_abrir = customtkinter.CTkButton(app, text="Abrir", command=abrir_arquivo)
botao_abrir.pack(pady=10)

botao_criar_pasta = customtkinter.CTkButton(app, text="Criar Nova Pasta", command=criar_pasta)
botao_criar_pasta.pack(pady=5)

botao_atualizar_planilha = customtkinter.CTkButton(app, text="Atualizar Planilha", command=atualizar_planilha)
botao_atualizar_planilha.pack(pady=5)

label_desenvolvedor = customtkinter.CTkLabel(app, 
                                            text="Desenvolvido por Rafael Souza - (41)99821-5865",
                                            text_color="green") #cor de fundo branca
label_desenvolvedor.place(relx=0.02, rely=0.95, anchor="sw")

frame_mensagens = customtkinter.CTkFrame(app, height=50)
frame_mensagens.pack()

app.update()
app.geometry(f"{app.winfo_width()}x{app.winfo_height()}")

app.mainloop()
