# Práctica: Construcción de tu Primera Base Vectorial

Esta guía te llevará paso a paso a través de la construcción de tu primera base de datos vectorial usando ChromaDB.

## 📋 Requisitos previos

- Python 3.8 o superior
- Conocimientos básicos de Python
- Leer la documentación en la carpeta `docs/`

## 🎯 Objetivos de aprendizaje

Al completar esta práctica, serás capaz de:
- ✅ Crear una base de datos vectorial con ChromaDB
- ✅ Agregar documentos y metadatos
- ✅ Realizar búsquedas semánticas
- ✅ Filtrar resultados usando metadatos
- ✅ Interpretar métricas de similitud

## 🚀 Instalación

1. Clonar el repositorio (si aún no lo has hecho)
2. Instalar dependencias:

```bash
pip install -r requirements.txt
```

## 📚 Estructura de la práctica

La práctica está dividida en dos ejemplos progresivos:

### Ejemplo 1: Primera base vectorial
**Archivo:** `examples/01_primera_base_vectorial.py`

Este ejemplo te enseña los conceptos básicos:
- Crear cliente ChromaDB
- Crear colecciones
- Agregar documentos con metadatos
- Realizar búsquedas semánticas simples
- Filtrar por metadatos

**Ejecutar:**
```bash
python examples/01_primera_base_vectorial.py
```

### Ejemplo 2: Sistema RAG completo
**Archivo:** `examples/02_sistema_rag_completo.py`

Este ejemplo demuestra un sistema RAG funcional:
- Clase `SistemaRAG` reutilizable
- Base de conocimiento estructurada
- Proceso completo de recuperación
- Simulación de generación de respuestas

**Ejecutar:**
```bash
python examples/02_sistema_rag_completo.py
```

## 🧪 Ejercicios prácticos

### Ejercicio 1: Personalizar la base de conocimiento
Modifica `01_primera_base_vectorial.py` para agregar tus propios documentos:

```python
documentos = [
    "Tu primer documento aquí",
    "Tu segundo documento aquí",
    # ... más documentos
]

metadatos = [
    {"categoria": "tu_categoria", "tema": "tu_tema"},
    {"categoria": "otra_categoria", "tema": "otro_tema"},
    # ... más metadatos
]
```

### Ejercicio 2: Experimentar con consultas
Prueba diferentes consultas y observa los resultados:

```python
# Consultas de ejemplo
consultas = [
    "¿Cómo funciona Python?",
    "Bases de datos modernas",
    "Frameworks para desarrollo web"
]

for consulta in consultas:
    resultados = collection.query(
        query_texts=[consulta],
        n_results=3
    )
    # Procesar resultados
```

### Ejercicio 3: Filtrado avanzado
Implementa búsquedas con múltiples filtros:

```python
# Buscar solo documentos de nivel básico
resultados = collection.query(
    query_texts=["tu consulta"],
    n_results=5,
    where={"nivel": "basico"}
)

# Buscar en categorías específicas
resultados = collection.query(
    query_texts=["tu consulta"],
    n_results=5,
    where={"categoria": {"$in": ["lenguajes", "frameworks"]}}
)
```

## 🔍 Conceptos clave a observar

### 1. Similitud vs Distancia
- **Distancia más baja** = Mayor similitud
- **Similitud = 1 - distancia**
- Valores típicos:
  - Distancia < 0.3: Muy similar
  - Distancia 0.3-0.7: Moderadamente similar
  - Distancia > 0.7: Poco similar

### 2. Embeddings automáticos
ChromaDB genera embeddings automáticamente usando sentence-transformers. No necesitas crearlos manualmente.

### 3. Metadatos
Los metadatos permiten:
- Organizar documentos
- Filtrar búsquedas
- Agregar contexto adicional
- Rastrear fuentes

### 4. IDs únicos
Cada documento necesita un ID único para:
- Identificación
- Actualización
- Eliminación

## 📊 Interpretando resultados

Ejemplo de salida:

```
1. Documento: Python es un lenguaje de programación...
   Categoría: lenguajes | Tema: python | Nivel: basico
   Similitud: 0.8234 (distancia: 0.1766)
```

- **Similitud alta (>0.8)**: Muy relevante para la consulta
- **Similitud media (0.6-0.8)**: Moderadamente relevante
- **Similitud baja (<0.6)**: Poco relevante

## 🎓 Siguientes pasos

Después de completar esta práctica:

1. **Persistencia**: Aprende a guardar datos permanentemente
   ```python
   client = chromadb.PersistentClient(path="./mi_base_datos")
   ```

2. **Documentos grandes**: Implementa chunking para textos largos
   ```python
   # Dividir texto en fragmentos de 500 palabras
   chunks = [texto[i:i+500] for i in range(0, len(texto), 500)]
   ```

3. **Integración con LLMs**: Conecta con OpenAI, Anthropic u otros
   ```python
   # Usar contexto recuperado con un LLM
   respuesta = llm.generate(
       prompt=f"Contexto: {contexto}\n\nPregunta: {consulta}"
   )
   ```

4. **Carga de archivos**: Lee documentos desde PDFs, TXT, etc.
   ```python
   import PyPDF2
   # Cargar y procesar PDFs
   ```

## 🐛 Solución de problemas

### Error: "No module named 'chromadb'"
```bash
pip install chromadb
```

### Error: "No module named 'sentence_transformers'"
```bash
pip install sentence-transformers
```

### Advertencias de telemetría
Las advertencias sobre telemetría son normales y no afectan el funcionamiento.

### Errores de memoria
Si trabajas con muchos documentos, considera:
- Usar persistencia en disco
- Procesar en lotes
- Reducir `n_results` en consultas

## 📖 Recursos adicionales

- [Documentación ChromaDB](https://docs.trychroma.com/)
- [Sentence Transformers](https://www.sbert.net/)
- [Documentos del proyecto](../docs/)
  - `01_concepto_rag.md`: Fundamentos de RAG
  - `02_vector_embeddings.md`: Todo sobre embeddings
  - `03_chromadb.md`: Guía completa de ChromaDB

## 💬 Preguntas frecuentes

**P: ¿Puedo usar ChromaDB en producción?**  
R: Sí, ChromaDB es production-ready. Usa el modo cliente/servidor para producción.

**P: ¿Cuántos documentos puede manejar?**  
R: ChromaDB puede manejar millones de documentos eficientemente.

**P: ¿Necesito entrenar el modelo de embeddings?**  
R: No, ChromaDB usa modelos pre-entrenados listos para usar.

**P: ¿Funciona con otros idiomas además de inglés?**  
R: Sí, los modelos sentence-transformers soportan múltiples idiomas.

**P: ¿Es gratis?**  
R: Sí, ChromaDB es completamente open-source y gratuito.

## 🎉 ¡Éxito!

Si has llegado hasta aquí, ¡felicitaciones! Has dado tus primeros pasos en el mundo de RAG y bases de datos vectoriales.

Continúa practicando y experimentando con tus propios casos de uso.
