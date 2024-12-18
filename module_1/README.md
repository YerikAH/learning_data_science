# CRUD de Empresas - Documentación

Este programa implementa un CRUD (Crear, Leer, Actualizar y Eliminar) para la gestión de empresas. Está diseñado utilizando las mejores prácticas de programación en Python, priorizando la modularidad, la reutilización de código y la claridad.

## Propósito

El propósito de este programa es proporcionar una solución eficiente para la gestión de información sobre empresas. Los datos se almacenan en un archivo de texto en formato JSON, permitiendo su persistencia entre sesiones.

---

## Funciones

### **Funciones utilitarias**

#### `load_data`

```python
load_data = lambda file: json.load(open(file, "r")) if os.path.exists(file) else []
```

Carga los datos desde un archivo JSON.

- Si el archivo existe, lo abre y carga los datos.
- Si no existe, devuelve una lista vacía.

**Ventaja:** Uso de `lambda` para simplificar el código y manejar excepciones implícitamente.

#### `save_data`

```python
save_data = lambda data, file: json.dump(data, open(file, "w"), indent=4)
```

Guarda los datos en un archivo JSON con formato legible.

- Acepta una lista de datos y un nombre de archivo.

**Ventaja:** Solución compacta y directa para persistir datos.

---

### **Funciones principales del CRUD**

#### `display_menu`

```python
def display_menu():
```

Muestra el menú principal con las opciones disponibles para el usuario.

**Propósito:** Facilitar la navegación por las opciones del programa.

#### `register_company`

```python
def register_company(companies: List[Dict[str, str]]):
```

Registra una nueva empresa recopilando los datos del usuario.

- Recibe una lista de empresas como argumento.
- Solicita al usuario el nombre, dirección y teléfono de la empresa.
- Agrega la nueva empresa a la lista.

**Ventaja:** Simplificación del flujo de creación y validación de datos.

#### `show_companies`

```python
def show_companies(companies: List[Dict[str, str]]):
```

Muestra la lista de empresas registradas en un formato claro.

- Itera sobre la lista de empresas e imprime los detalles de cada una.

**Ventaja:** Uso de `map` para iterar sobre la lista y mejorar la legibilidad del código.

#### `update_company`

```python
def update_company(companies: List[Dict[str, str]]):
```

Actualiza los datos de una empresa seleccionada por el usuario.

- Muestra las empresas y solicita un índice para seleccionar cuál actualizar.
- Permite mantener los datos actuales si no se ingresan valores nuevos.
- Valida entradas incorrectas.

**Ventaja:** Combina flexibilidad y robustez en la edición de datos.

#### `delete_company`

```python
def delete_company(companies: List[Dict[str, str]]):
```

Elimina una empresa seleccionada por el usuario.

- Muestra las empresas y solicita un índice para seleccionar cuál eliminar.
- Valida entradas incorrectas y elimina el elemento de la lista.

**Ventaja:** Simplifica la gestión de errores y proporciona retroalimentación clara.

---

### **Función principal**

#### `main`

```python
def main():
```

Controla el flujo principal del programa.

- Carga datos desde el archivo al iniciar.
- Muestra el menú principal y ejecuta la opción seleccionada por el usuario.
- Guarda los datos antes de salir.

**Ventaja:** Uso de un diccionario (`actions`) para mapear las opciones a funciones, reduciendo código redundante y mejorando la escalabilidad.

---

## Ventajas de la solución

1. **Modularidad:** Cada función tiene una responsabilidad clara, facilitando el mantenimiento y la ampliación del código.
2. **Reutilización de código:** Uso de funciones lambda y mapeos para simplificar tareas repetitivas como carga y guardado de datos.
3. **Robustez:** Manejo de errores y validaciones en las interacciones con el usuario, garantizando estabilidad.
4. **Persistencia:** Los datos se guardan en un archivo JSON, asegurando que persistan entre sesiones.
5. **Legibilidad:** Uso de tipado estático y `docstrings` para hacer el código más fácil de entender y documentar.
6. **Escalabilidad:** El uso de un diccionario para manejar las opciones del menú facilita la adición de nuevas funcionalidades.

---

## Ejecución

Para ejecutar el programa, simplemente ejecuta el archivo principal. Se creará automáticamente un archivo `empresas.txt` si no existe, donde se almacenarán los datos en formato JSON. Cada operación del CRUD se reflejará en este archivo para asegurar la persistencia de los datos.
