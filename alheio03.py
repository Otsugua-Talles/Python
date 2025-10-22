import matplotlib.pyplot as plt

# Pergunta quantas categorias o usuário quer
qtd = int(input("Quantas categorias você quer no gráfico? "))

categorias = []
valores = []

# Coleta os dados do usuário
for i in range(qtd):
    nome = input(f"Digite o nome da categoria {i+1}: ")
    valor = float(input(f"Digite o valor de {nome}: "))
    categorias.append(nome)
    valores.append(valor)

# Cores automáticas (paleta colorida)
cores = plt.cm.Set3.colors

# Cria o gráfico de pizza
plt.figure(figsize=(7, 7))
plt.pie(
    valores,
    labels=categorias,
    autopct='%1.1f%%',
    startangle=90,
    colors=cores[:qtd],
    shadow=True
)

plt.title("Gráfico de Pizza Personalizado 🍕", fontsize=16, pad=20)
plt.axis('equal')  # Mantém o gráfico circular

# Mostra o gráfico
plt.show()

# Salva o gráfico em arquivo
plt.savefig("grafico_pizza.png", dpi=300, bbox_inches='tight')

print("\n✅ Gráfico gerado e salvo como 'grafico_pizza.png' com sucesso!")
