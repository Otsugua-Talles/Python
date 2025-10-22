import matplotlib.pyplot as plt

# Dados do gráfico
categorias = ['Python 🐍', 'Java ☕', 'C++ 💻', 'JavaScript 🌐', 'Go 🚀']
valores = [40, 20, 15, 15, 10]
cores = ['#00FFAA', '#FFAA00', '#FF5555', '#55AAFF', '#AA55FF']

# "Explode" (destaca) o primeiro pedaço (Python)
explode = [0.1, 0, 0, 0, 0]

# Cria o gráfico de pizza
fig, ax = plt.subplots(figsize=(7, 7))
wedges, texts, autotexts = ax.pie(
    valores,
    labels=categorias,
    autopct='%1.1f%%',
    startangle=90,
    shadow=True,
    colors=cores,
    explode=explode,
    wedgeprops={'edgecolor': 'black'}
)

# Deixa o texto mais bonito
for t in texts:
    t.set_fontsize(12)
for at in autotexts:
    at.set_color('white')
    at.set_fontsize(11)

# Adiciona título
plt.title("Popularidade das Linguagens de Programação 💻", fontsize=16, pad=20)

# Deixa o gráfico redondo
plt.axis('equal')

# Ativa interatividade — ao clicar, mostra o valor no console
def onclick(event):
    for i, w in enumerate(wedges):
        if w.contains_point([event.x, event.y]):
            print(f"👉 Você clicou em: {categorias[i]} ({valores[i]}%)")

fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()
