import tkinter as tk
from tkinter import messagebox


# Listas para armazenar o inventário de produtos e o histórico de vendas
inventario = []
historico_vendas = []






def adicionar_produto():
    """Adiciona um novo produto ao inventário."""
    nome = entrada_nome.get()
    preco = entrada_preco.get()
    quantidade = entrada_quantidade.get()


    if not nome or not preco or not quantidade:
        messagebox.showwarning("Campos Vazios", "Todos os campos são obrigatórios.")
        return

    try:
        preco = float(preco)
        quantidade = int(quantidade)
    except ValueError:
        messagebox.showerror("Erro de Tipo", "Preço deve ser um número decimal e quantidade um número inteiro.")
        return

    produto = {
        'nome': nome,
        'preco': preco,
        'quantidade': quantidade
    }
    inventario.append(produto)
    messagebox.showinfo("Sucesso", f"Produto {nome} adicionado com sucesso!")
    limpar_campos()


def limpar_campos():
    """Limpa os campos de entrada."""
    entrada_nome.delete(0, tk.END)
    entrada_preco.delete(0, tk.END)
    entrada_quantidade.delete(0, tk.END)


def listar_produtos():
    """Lista os produtos no inventário."""
    janela_listar = tk.Toplevel()
    janela_listar.title("Lista de Produtos")
    texto_listar = tk.Text(janela_listar, width=50, height=20)
    texto_listar.pack()

    if not inventario:
        texto_listar.insert(tk.END, "Inventário vazio.\n")
    else:
        for i, produto in enumerate(inventario, 1):
            texto_listar.insert(tk.END,
                                f"{i}. {produto['nome']} - Preço: R$ {produto['preco']:.2f} - Quantidade: {produto['quantidade']}\n")


def realizar_venda():
    """Realiza a venda de um produto."""
    janela_venda = tk.Toplevel()
    janela_venda.title("Realizar Venda")

    tk.Label(janela_venda, text="Número do Produto:").pack()
    entrada_num_produto = tk.Entry(janela_venda)
    entrada_num_produto.pack()

    tk.Label(janela_venda, text="Quantidade a Vender:").pack()
    entrada_quantidade_venda = tk.Entry(janela_venda)
    entrada_quantidade_venda.pack()

    def confirmar_venda():
        try:
            numero_produto = int(entrada_num_produto.get()) - 1
            quantidade_venda = int(entrada_quantidade_venda.get())
        except ValueError:
            messagebox.showerror("Erro de Tipo", "Informe números válidos.")
            return

        if numero_produto < 0 or numero_produto >= len(inventario):
            messagebox.showerror("Erro", "Produto inválido.")
            return

        produto = inventario[numero_produto]

        if quantidade_venda > produto['quantidade']:
            messagebox.showerror("Erro", "Quantidade em estoque insuficiente.")
            return

        produto['quantidade'] -= quantidade_venda
        valor_total = quantidade_venda * produto['preco']
        venda = {
            'nome': produto['nome'],
            'quantidade': quantidade_venda,
            'valor_total': valor_total
        }
        historico_vendas.append(venda)
        messagebox.showinfo("Venda Realizada",
                            f"Venda de {quantidade_venda} unidade(s) do produto {produto['nome']} realizada com sucesso!")
        janela_venda.destroy()

    tk.Button(janela_venda, text="Confirmar Venda", command=confirmar_venda).pack()


def mostrar_historico_vendas():
    """Mostra o histórico de vendas."""
    janela_historico = tk.Toplevel()
    janela_historico.title("Histórico de Vendas")
    texto_historico = tk.Text(janela_historico, width=50, height=20)
    texto_historico.pack()

    if not historico_vendas:
        texto_historico.insert(tk.END, "Nenhuma venda realizada até o momento.\n")
    else:
        for venda in historico_vendas:
            texto_historico.insert(tk.END,
                                   f"Produto: {venda['nome']} - Quantidade: {venda['quantidade']} - Valor Total: R$ {venda['valor_total']:.2f}\n")




# Configuração da janela principal
janela = tk.Tk()
janela.title("Sistema de Vendas")

janela.geometry("500x300")

# Campos para entrada de dados do produto
tk.Label(janela, text="Nome do Produto:").pack()
entrada_nome = tk.Entry(janela)
entrada_nome.pack()

tk.Label(janela, text="Preço do Produto:").pack()
entrada_preco = tk.Entry(janela)
entrada_preco.pack()

tk.Label(janela, text="Quantidade em Estoque:").pack()
entrada_quantidade = tk.Entry(janela)
entrada_quantidade.pack()

# Botões de ações
tk.Button(janela, text="Adicionar Produto", command=adicionar_produto).pack()
tk.Button(janela, text="Listar Produtos", command=listar_produtos).pack()
tk.Button(janela, text="Realizar Venda", command=realizar_venda).pack()
tk.Button(janela, text="Mostrar Histórico de Vendas", command=mostrar_historico_vendas).pack()

# Loop principal da aplicação
janela.mainloop()


