# 🧠 Medición del Tamaño de la TLB (Translation Lookaside Buffer)

Este proyecto implementa un experimento en C para estimar el tamaño de la TLB (Translation Lookaside Buffer) de un sistema operativo, siguiendo el enfoque del capítulo 19 del libro *Operating Systems: Three Easy Pieces*.

## 📌 ¿Qué es la TLB?

La TLB es una caché de traducciones de direcciones virtuales a físicas. Almacena un número limitado de entradas de la tabla de páginas para acelerar el acceso a memoria. Si el conjunto de páginas accedidas excede su tamaño, se producen fallos de TLB, lo que incrementa el tiempo de acceso a memoria.

---

## 🧪 Objetivo del experimento

Medir el tiempo promedio de acceso a memoria al recorrer un arreglo distribuido en diferentes páginas, para identificar el punto en que comienzan los fallos de TLB.

---

## 🧰 Archivos del repositorio

- `tlb.c`: código fuente en C del experimento.
- `script.sh`: script bash que automatiza la ejecución de pruebas de 1 a 64 páginas.
- `grafica.py`: script Python que genera una gráfica a partir de los resultados.
- `grafica_tlb.png`: gráfica generada (puede regenerarse).
- `resultados.txt`: archivo con los datos crudos generados por el experimento.
- `README.md`: este archivo.

---

## ⚙️ Compilación

Compilar el programa desactivando optimizaciones:

```bash
gcc -O0 -o tlb tlb.c
```
## 🚀 Ejecución del experimento

Ejecutar el script para realizar 64 pruebas (con 100 repeticiones cada una):

```bash
chmod +x script.sh
./script.sh
```
Esto genera el archivo resultados.txt.

## 📊 Generar la gráfica

1. Crear un entorno virtual (opcional pero recomendado):
```bash
python3 -m venv venv
source venv/bin/activate
```
2. Instalar matplotlib
```bash
python grafica.py
```
Se generará grafica_tlb.png con la curva de tiempo promedio por acceso según el número de páginas.

## 📈 Interpretación

Mientras el número de páginas sea menor o igual al tamaño de la TLB, el tiempo de acceso será bajo y constante.

Cuando el número de páginas supera la capacidad de la TLB, el tiempo promedio aumenta significativamente.

El punto de cambio en la gráfica indica el tamaño aproximado de la TLB del sistema.

## By

@johanasev - Proyecto realizado para la materia Sistemas Operativos — Universidad de Antioquia.


> "La mejor forma de entender cómo funciona la memoria virtual es ver cómo se comporta al fallar."




