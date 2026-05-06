def generar_boletas(dicc_escuela):
    escuela_promedio = {}
    
    for alumno, lista_materias in dicc_escuela.items():
        suma_notas = 0
        # lista_materias es: [{"materia": "Mate", "nota": 90}, ...]
        for item in lista_materias:
            suma_notas += item["nota"] # Accedemos a la llave nota de cada dict
        
        promedio = suma_notas / len(lista_materias)
        escuela_promedio[alumno] = promedio
            
    return escuela_promedio

escuela =  {"Ana": [{"materia": "Mate", "nota": 90}, {"materia": "Prog", "nota": 100}],
            "Saul": [{"materia": "Mate", "nota": 80}, {"materia": "Prog", "nota": 100}],
            "Pedro": [{"materia": "Mate", "nota": 80}, {"materia": "Prog", "nota": 90}],
            "Maria": [{"materia": "Mate", "nota": 70}, {"materia": "Prog", "nota": 70}]}


print(generar_boletas(escuela))