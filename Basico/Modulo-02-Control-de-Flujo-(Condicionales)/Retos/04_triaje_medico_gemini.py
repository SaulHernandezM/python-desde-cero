print("##### SISTEMA DE TRIAJE PROFESIONAL ####")

# 1. Entrada de Datos
nombre = input("Nombre: ")
edad = int(input("Edad: "))
oxigeno = int(input("Saturación O2 (0-100): "))
temp = float(input("Temperatura (°C): "))
respira_mal = input("¿Dificultad respiratoria? (S/N): ").strip().lower() in ["si", "s", "y"]

# 2. Validación de Integridad de Datos
if oxigeno < 0 or oxigeno > 100:
    print("ALERTA: Dato de oxígeno inválido. Reinicie el proceso.")
else:
    # 3. Definición de Banderas (Flags) - Esto es Lógica Pura
    es_critico = (oxigeno < 90) or respira_mal
    es_riesgo = (temp >= 39) or (edad > 65) or (edad < 5)

    # 4. Procesamiento de Prioridad (Jerarquía)
    print(f"\n--- RESUMEN PACIENTE: {nombre} ---")
    
    if es_critico:
        resultado = "PRIORIDAD 1: REANIMACIÓN INMEDIATA"
    elif es_riesgo:
        resultado = "PRIORIDAD 2: EVALUACIÓN URGENTE"
    else:
        resultado = "PRIORIDAD 3: SALA DE ESPERA GENERAL"
    
    print(f"Decisión Clínica: {resultado}")