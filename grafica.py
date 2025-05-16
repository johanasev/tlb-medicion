import matplotlib.pyplot as plt

# Leer los datos
pages = []
times = []

with open("resultados.txt", "r") as f:
    for line in f:
        parts = line.strip().split()
        pages.append(int(parts[0]))
        times.append(float(parts[1]))

# Crear la gráfica
plt.plot(pages, times, marker='o')
plt.xlabel('Número de páginas')
plt.ylabel('Tiempo promedio por acceso (ns)')
plt.title('Medición del tamaño de la TLB')
plt.grid(True)
plt.savefig("grafica_tlb.png")
plt.show()
