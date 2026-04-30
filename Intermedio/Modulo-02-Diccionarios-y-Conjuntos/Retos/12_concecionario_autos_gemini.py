autos = {
    "Toyota": {"Corolla": 2022, "Hilux": 2021}, 
    "Ford": {"Mustang": 2023}
}

marca = input("Marca: ").strip()
if marca in autos:
    print(f"Modelos de {marca}: {list(autos[marca].keys())}")
    modelo = input("Elige el modelo: ").strip()
    if modelo in autos[marca]:
        print(f"Año del {modelo}: {autos[marca][modelo]}")