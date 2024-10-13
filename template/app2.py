import tkinter as tk
from PIL import Image, ImageTk

# Configuração da janela principal
janela = tk.Tk()
janela.title("Sistema de Vendas com Background")
janela.geometry("500x320")

# Carregar a imagem de fundo
imagem_fundo = Image.open("Imagens/perfil.jpg")  # Substitua pelo caminho da sua imagem
imagem_fundo = imagem_fundo.resize((500, 320), Image.LANCZOS)  # Ajusta o tamanho da imagem
imagem_fundo_tk = ImageTk.PhotoImage(imagem_fundo)

# Criar um Canvas para adicionar a imagem de fundo
canvas = tk.Canvas(janela, width=500, height=320)
canvas.pack(fill="both", expand=True)

# Adicionar a imagem ao Canvas
canvas.create_image(0, 0, image=imagem_fundo_tk, anchor="nw")

# Adicionar widgets sobre o Canvas
label_item = tk.Label(janela, text="Item:", bg="white")
label_item_window = canvas.create_window(50, 50, anchor="nw", window=label_item)

entry_item = tk.Entry(janela)
entry_item_window = canvas.create_window(150, 50, anchor="nw", window=entry_item)

label_quantidade = tk.Label(janela, text="Quantidade:", bg="white")
label_quantidade_window = canvas.create_window(50, 100, anchor="nw", window=label_quantidade)

entry_quantidade = tk.Entry(janela)
entry_quantidade_window = canvas.create_window(150, 100, anchor="nw", window=entry_quantidade)

label_preco = tk.Label(janela, text="Preço (R$):", bg="white")
label_preco_window = canvas.create_window(50, 150, anchor="nw", window=label_preco)

entry_preco = tk.Entry(janela)
entry_preco_window = canvas.create_window(150, 150, anchor="nw", window=entry_preco)

botao_vender = tk.Button(janela, text="Realizar Venda")
botao_vender_window = canvas.create_window(150, 200, anchor="nw", window=botao_vender)

# Loop principal da aplicação
janela.mainloop()
