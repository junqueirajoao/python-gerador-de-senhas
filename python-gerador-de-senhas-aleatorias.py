import tkinter as tk
from tkinter import messagebox
import random
import string
import unicodedata
import re

# Função para remover acentos das palavras
def remover_acentos(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn'
    )

# Função para gerar a senha
def gerar_senha(tamanho=12, categoria="forte"):
    # Inserir condicional de tamanho mínimo para senha
    if tamanho < 6:
        raise ValueError("O tamanho da senha deve ser pelo menos 6.")
    
    # Definir os tipos de caracteres disponíveis para cada categoria
    categorias = {
        "fraca": string.ascii_lowercase,  # Apenas letras minúsculas
        "média": string.ascii_letters + string.digits,  # Letras (maiúsculas e minúsculas) e números
        "forte": string.ascii_letters + string.digits + string.punctuation  # Letras, números e símbolos
    }

    # Normalizar a entrada da categoria, removendo acentos
    categoria = remover_acentos(categoria.strip()).lower()

    # Normalizar também as chaves do dicionário para comparação sem acento
    categorias_normalizadas = {remover_acentos(key).lower(): value for key, value in categorias.items()}
    
    # Verificar se a categoria é válida
    if categoria not in categorias_normalizadas:
        raise ValueError("Categoria inválida! Escolha entre: fraca, média ou forte.")
    
    # Gerar senha aleatória conforme a categoria escolhida
    senha = ''.join(random.choices(categorias_normalizadas[categoria], k=tamanho))
    return senha

# Função que será chamada ao clicar no botão
def gerar():
    try:
        # Obter o tamanho e a categoria da senha
        tamanho = int(entry_tamanho.get())
        categoria = combo_categoria.get()

        # Gerar a senha
        senha = gerar_senha(tamanho, categoria)

        # Exibir a senha na caixa de texto
        text_senha.delete(1.0, tk.END)  # Limpar caixa de texto
        text_senha.insert(tk.END, senha)  # Inserir nova senha

    except ValueError as e:
        # Exibir erro se houver
        messagebox.showerror("Erro", str(e))

# Criar a janela principal
root = tk.Tk()
root.title("Gerador de Senha")

# Adicionar label para o tamanho da senha
label_tamanho = tk.Label(root, text="Digite o tamanho da senha:")
label_tamanho.grid(row=0, column=0, padx=10, pady=10)

# Adicionar campo de entrada para o tamanho
entry_tamanho = tk.Entry(root)
entry_tamanho.grid(row=0, column=1, padx=10, pady=10)

# Adicionar label para a categoria da senha
label_categoria = tk.Label(root, text="Escolha a categoria da senha:")
label_categoria.grid(row=1, column=0, padx=10, pady=10)

# Adicionar lista suspensa (combobox) para a categoria
combo_categoria = tk.StringVar()
categoria_lista = ["fraca", "média", "forte"]
combo_categoria.set(categoria_lista[2])  # Valor default é "forte"
combo_categoria_box = tk.OptionMenu(root, combo_categoria, *categoria_lista)
combo_categoria_box.grid(row=1, column=1, padx=10, pady=10)

# Adicionar botão para gerar a senha
botao_gerar = tk.Button(root, text="Gerar Senha", command=gerar)
botao_gerar.grid(row=2, column=0, columnspan=2, pady=10)

# Adicionar label para exibir a senha gerada
label_senha = tk.Label(root, text="Senha gerada:")
label_senha.grid(row=3, column=0, padx=10, pady=10)

# Adicionar caixa de texto para exibir a senha gerada
text_senha = tk.Text(root, height=3, width=30)
text_senha.grid(row=3, column=1, padx=10, pady=10)

# Iniciar o loop principal da interface
root.mainloop()