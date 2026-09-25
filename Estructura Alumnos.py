import random
import time

MATERIAS = ["Matemáticas", "Español", "Historia", "Geografía", "Biología", "Física"]

def generar_matriz(total_alumnos, total_materias):
    """Crea la matriz de 100,000 alumnos x 6 materias con notas del 1 al 10."""
    print("\nGenerando datos para 100,000 alumnos en memoria... Por favor espera un momento.")
    inicio_gen = time.perf_counter()
    matriz = []
    for _ in range(total_alumnos):
        fila = [random.randint(1, 10) for _ in range(total_materias)]
        matriz.append(fila)
    fin_gen = time.perf_counter()
    tiempo_gen = (fin_gen - inicio_gen) * 1000
    print(f"¡Matriz creada exitosamente! Tiempo de generación: {tiempo_gen:.2f} ms")
    return matriz

def mostrar_tabla_completa(matriz):
    """Imprime el registro completo de los 100,000 alumnos en pantalla."""
    ancho = 85
    print("\n" + "=" * ancho)
    print("           REGISTRO COMPLETO DE CALIFICACIONES (100,000 ALUMNOS)")
    print("=" * ancho)
    
    encabezado = f"{'Alumno':<12} | " + " | ".join([f"{m[:8]:^9}" for m in MATERIAS])
    print(encabezado)
    print("-" * ancho)

    inicio = time.perf_counter()
    for idx, fila in enumerate(matriz, start=1):
        calificaciones = " | ".join([f"{nota:^9}" for nota in fila])
        print(f"Alumno {idx:<7} | {calificaciones}")
    fin = time.perf_counter()

    tiempo = (fin - inicio) * 1000
    print("=" * ancho)
    print(f"⏱️ TIEMPO TOTAL DE IMPRESIÓN (100,000 ALUMNOS): {tiempo:.2f} ms")
    print("=" * ancho)

def buscar_por_alumno(matriz, num_alumno):
    """Muestra todas las materias de un alumno específico y el tiempo de acceso."""
    idx = num_alumno - 1  # Ajuste de base 0
    
    inicio = time.perf_counter()
    notas = matriz[idx]
    fin = time.perf_counter()
    tiempo = (fin - inicio) * 1000

    print(f"\n" + "=" * 50)
    print(f" CALIFICACIONES DEL ALUMNO {num_alumno:,}")
    print("=" * 50)
    for m in range(len(MATERIAS)):
        print(f" • {MATERIAS[m]:<15} : {notas[m]}")
    print("─" * 50)
    print(f"⏱️ TIEMPO DE BÚSQUEDA: {tiempo:.6f} ms")
    print("=" * 50)

def buscar_por_materia(matriz, num_materia):
    """Muestra la calificación de los 100,000 alumnos en una materia y el tiempo."""
    idx_materia = num_materia - 1 
    nombre_materia = MATERIAS[idx_materia]

    inicio = time.perf_counter()
    notas_alumnos = [matriz[a][idx_materia] for a in range(len(matriz))]
    fin = time.perf_counter()
    tiempo = (fin - inicio) * 1000

    print(f"\n" + "=" * 50)
    print(f" CALIFICACIONES DE LA MATERIA: {nombre_materia.upper()}")
    print("=" * 50)
    for a in range(len(notas_alumnos)):
        print(f" • Alumno {a+1:<7} : {notas_alumnos[a]}")
    print("─" * 50)
    print(f"⏱️ TIEMPO DE BÚSQUEDA (100,000 ALUMNOS): {tiempo:.6f} ms")
    print("=" * 50)
    
if __name__ == "__main__":
    TOTAL_ALUMNOS = 100000
    TOTAL_MATERIAS = 6
    
    matriz = generar_matriz(TOTAL_ALUMNOS, TOTAL_MATERIAS)
    ejecutando = True
    while ejecutando:
        print("\n" + "═" * 55)
        print("                 MENÚ DE OPCIONES (100,000 ALUMNOS)")
        print("═" * 55)
        print("1. Ver la TABLA COMPLETA (Imprime los 100,000 Alumnos)")
        print("2. Buscar por ALUMNO (Muestra sus 6 materias + Tiempo)")
        print("3. Buscar por MATERIA (Imprime a los 100,000 alumnos + Tiempo)")
        print("4. Buscar Alumno 321 y Materia 5 (Punto específico del ADA)")
        print("Escribe 'fin' en cualquier momento para salir del programa.")
        print("═" * 55)

        opcion = input("\nSelecciona una opción o escribe 'fin': ").strip().lower()

        if opcion == "fin":
            print("\n>> Ejecución finalizada correctamente. ¡Hasta luego!\n")
            ejecutando = False

        elif opcion == "1":
            mostrar_tabla_completa(matriz)

        elif opcion == "2":
            entrada = input(f"Ingresa el número de alumno (1 a {TOTAL_ALUMNOS:,}) o 'fin': ").strip().lower()
            if entrada == "fin":
                print("\n>> Ejecución finalizada correctamente. ¡Hasta luego!\n")
                ejecutando = False
            elif entrada.isdigit():
                num = int(entrada)
                if 1 <= num <= TOTAL_ALUMNOS:
                    buscar_por_alumno(matriz, num)
                else:
                    print(f"Error: El alumno debe estar entre 1 y {TOTAL_ALUMNOS:,}.")
            else:
                print("Entrada no válida.")

        elif opcion == "3":
            print("\nMaterias disponibles:")
            for i, mat in enumerate(MATERIAS, start=1):
                print(f"  {i}. {mat}")
            
            entrada = input(f"Ingresa el número de materia (1 a {TOTAL_MATERIAS}) o 'fin': ").strip().lower()
            if entrada == "fin":
                print("\n>> Ejecución finalizada correctamente. ¡Hasta luego!\n")
                ejecutando = False
            elif entrada.isdigit():
                num = int(entrada)
                if 1 <= num <= TOTAL_MATERIAS:
                    buscar_por_materia(matriz, num)
                else:
                    print(f"Error: La materia debe estar entre 1 y {TOTAL_MATERIAS}.")
            else:
                print("Entrada no válida.")

        elif opcion == "4":
            inicio = time.perf_counter()
            nota = matriz[320][4]
            fin = time.perf_counter()
            tiempo = (fin - inicio) * 1000

            print(f"\n" + "=" * 50)
            print(f" BÚSQUEDA PUNTUAL: ALUMNO 321 | MATERIA 5 ({MATERIAS[4]})")
            print("=" * 50)
            print(f" • Calificación obtenida : {nota}")
            print(f" TIEMPO DE ACCESO       : {tiempo:.6f} ms")
            print("=" * 50)

        else:
            print("Opción no reconocida. Intenta de nuevo.")
