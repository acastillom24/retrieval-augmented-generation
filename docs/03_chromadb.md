# ChromaDB - Base de Datos Vectorial

## ¿Qué es ChromaDB?

ChromaDB es una base de datos vectorial open-source diseñada específicamente para almacenar y consultar embeddings. Es ideal para aplicaciones de IA y RAG.

## Características principales

### 1. Simplicidad
- API intuitiva y fácil de usar
- Sin configuración compleja
- Funciona inmediatamente "out of the box"

### 2. Embeddings automáticos
- Puede generar embeddings automáticamente
- Soporta múltiples modelos de embedding
- Permite usar embeddings personalizados

### 3. Búsqueda semántica
- Búsqueda por similitud vectorial
- Filtrado de metadatos
- Consultas híbridas (vectorial + metadatos)

### 4. Persistencia
- Almacenamiento en disco
- Modo en memoria para pruebas rápidas
- Cliente/servidor para producción

## Instalación

```bash
pip install chromadb
```

## Conceptos clave

### Collections (Colecciones)
Una colección es un conjunto de documentos con sus embeddings:
- Similar a una tabla en SQL
- Puede tener múltiples documentos
- Cada documento tiene ID, embedding, metadata y contenido

### Metadatos
Información adicional sobre documentos:
```python
metadata = {
    "source": "manual_usuario.pdf",
    "page": 5,
    "author": "Juan Pérez",
    "date": "2024-01-15"
}
```

### Distance Functions
ChromaDB soporta múltiples funciones de distancia:
- **Cosine similarity** (por defecto): Basada en ángulos
- **Euclidean distance (L2)**: Distancia geométrica
- **Inner product**: Producto punto

## Uso básico

### 1. Crear cliente y colección

```python
import chromadb

# Crear cliente (en memoria)
client = chromadb.Client()

# Crear colección
collection = client.create_collection(name="mi_coleccion")
```

### 2. Agregar documentos

```python
collection.add(
    documents=["Este es un documento", "Este es otro documento"],
    metadatas=[{"source": "doc1"}, {"source": "doc2"}],
    ids=["id1", "id2"]
)
```

### 3. Realizar consultas

```python
results = collection.query(
    query_texts=["buscar documentos sobre este tema"],
    n_results=2
)
```

## Modos de operación

### Modo Ephemeral (en memoria)
```python
client = chromadb.Client()  # No persiste datos
```

### Modo Persistent (persistente)
```python
client = chromadb.PersistentClient(path="/ruta/a/datos")
```

### Modo Client/Server
```python
client = chromadb.HttpClient(host="localhost", port=8000)
```

## Funciones de embedding

### Embedding por defecto
ChromaDB usa sentence-transformers por defecto:
```python
collection = client.create_collection(
    name="mi_coleccion",
    embedding_function=None  # Usa default
)
```

### Embedding personalizado
```python
from chromadb.utils import embedding_functions

openai_ef = embedding_functions.OpenAIEmbeddingFunction(
    api_key="tu-api-key",
    model_name="text-embedding-3-small"
)

collection = client.create_collection(
    name="mi_coleccion",
    embedding_function=openai_ef
)
```

## Operaciones CRUD

### Create (Crear)
```python
collection.add(
    documents=["documento"],
    ids=["id1"]
)
```

### Read (Leer)
```python
# Obtener por ID
result = collection.get(ids=["id1"])

# Consulta semántica
results = collection.query(
    query_texts=["consulta"],
    n_results=5
)
```

### Update (Actualizar)
```python
collection.update(
    ids=["id1"],
    documents=["documento actualizado"]
)
```

### Delete (Eliminar)
```python
collection.delete(ids=["id1"])
```

## Filtrado con metadatos

```python
# Búsqueda con filtros
results = collection.query(
    query_texts=["consulta"],
    n_results=5,
    where={"source": "manual.pdf"},
    where_document={"$contains": "importante"}
)
```

## Ventajas de ChromaDB

✅ **Fácil de usar**: API simple e intuitiva  
✅ **Ligero**: No requiere infraestructura pesada  
✅ **Rápido**: Búsquedas eficientes incluso con millones de vectores  
✅ **Flexible**: Múltiples modos de operación  
✅ **Open Source**: Código abierto y gratuito  

## Comparación con otras bases vectoriales

| Característica | ChromaDB | Pinecone | Weaviate | Qdrant |
|----------------|----------|----------|----------|--------|
| Open Source | ✅ | ❌ | ✅ | ✅ |
| Auto-embeddings | ✅ | ❌ | ✅ | ❌ |
| Modo local | ✅ | ❌ | ✅ | ✅ |
| Simplicidad | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| Escalabilidad | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |

## Casos de uso

- 📚 Sistemas de preguntas y respuestas
- 🔍 Búsqueda semántica en documentos
- 💬 Chatbots con memoria
- 📊 Análisis de similitud de textos
- 🏷️ Sistemas de recomendación
