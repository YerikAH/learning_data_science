import os
import json
from typing import List, Dict

# === Utility Functions ===
load_data = lambda file: json.load(open(file, "r")) if os.path.exists(file) else []
save_data = lambda data, file: json.dump(data, open(file, "w"), indent=4)

# === Menu Handling ===
def display_menu():
    """
    Displays the main menu options to the user.
    """
    print("\n=== CRUD de Empresas ===")
    print("1. Registrar Empresa")
    print("2. Mostrar Empresas")
    print("3. Actualizar Empresa")
    print("4. Eliminar Empresa")
    print("5. Guardar Datos en Archivo")
    print("6. Salir")

# === CRUD Operations ===
def register_company(companies: List[Dict[str, str]]):
    """
    Registers a new company by collecting its details from the user.
    
    Args:
        companies (List[Dict[str, str]]): List of existing companies.
    """
    company = {
        "nombre": input("Ingrese el nombre de la empresa: "),
        "direccion": input("Ingrese la dirección de la empresa: "),
        "telefono": input("Ingrese el teléfono de la empresa: "),
    }
    companies.append(company)
    print("Empresa registrada con éxito.")

def show_companies(companies: List[Dict[str, str]]):
    """
    Displays the list of registered companies.

    Args:
        companies (List[Dict[str, str]]): List of existing companies.
    """
    if not companies:
        print("No hay empresas registradas.")
        return
    print("\n=== Lista de Empresas ===")
    list(map(lambda c: print(f"{companies.index(c) + 1}. {c['nombre']} - {c['direccion']} - {c['telefono']}"), companies))

def update_company(companies: List[Dict[str, str]]):
    """
    Updates the details of a selected company.

    Args:
        companies (List[Dict[str, str]]): List of existing companies.
    """
    show_companies(companies)
    try:
        index = int(input("Ingrese el número de la empresa a actualizar: ")) - 1
        if index < 0 or index >= len(companies):
            raise IndexError("Índice fuera de rango.")
        
        company = companies[index]
        company["nombre"] = input(f"Nombre actual: {company['nombre']} (deje en blanco para mantener actual): ") or company["nombre"]
        company["direccion"] = input(f"Dirección actual: {company['direccion']} (deje en blanco para mantener actual): ") or company["direccion"]
        company["telefono"] = input(f"Teléfono actual: {company['telefono']} (deje en blanco para mantener actual): ") or company["telefono"]

        print("Empresa actualizada con éxito.")
    except (ValueError, IndexError) as e:
        print(f"Error: {e}")

def delete_company(companies: List[Dict[str, str]]):
    """
    Deletes a selected company from the list.

    Args:
        companies (List[Dict[str, str]]): List of existing companies.
    """
    show_companies(companies)
    try:
        index = int(input("Ingrese el número de la empresa a eliminar: ")) - 1
        if index < 0 or index >= len(companies):
            raise IndexError("Índice fuera de rango.")
        
        removed = companies.pop(index)
        print(f"Empresa '{removed['nombre']}' eliminada con éxito.")
    except (ValueError, IndexError) as e:
        print(f"Error: {e}")

# === Main Program ===
def main():
    """
    Main function to run the CRUD program.
    """
    FILE_NAME = "empresas.txt"
    companies = load_data(FILE_NAME)

    actions = {
        "1": lambda: register_company(companies),
        "2": lambda: show_companies(companies),
        "3": lambda: update_company(companies),
        "4": lambda: delete_company(companies),
        "5": lambda: save_data(companies, FILE_NAME) or print("Datos guardados con éxito."),
        "6": lambda: (save_data(companies, FILE_NAME), print("Saliendo del programa. Datos guardados.")) or exit(),
    }

    while True:
        display_menu()
        choice = input("Seleccione una opción: ")
        actions.get(choice, lambda: print("Opción inválida. Intente de nuevo."))()

if __name__ == "__main__":
    main()
