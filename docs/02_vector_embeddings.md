# Vector Embeddings

## ¿Qué son los Vector Embeddings?

Los embeddings vectoriales son representaciones numéricas de texto en forma de vectores en un espacio multidimensional. Estos vectores capturan el significado semántico del texto.

## ¿Por qué son importantes?

Los embeddings permiten:
- Comparar la similitud entre textos
- Realizar búsquedas semánticas (por significado, no solo por palabras exactas)
- Agrupar documentos similares
- Reducir la dimensionalidad del texto para procesamiento eficiente

## Características de los embeddings

### Similitud semántica
Textos con significados similares tienen vectores cercanos en el espacio vectorial.

Ejemplo:
- "perro" y "cachorro" → vectores cercanos
- "perro" y "automóvil" → vectores distantes

### Dimensionalidad
Los embeddings típicamente tienen dimensiones entre 384 y 1536:
- OpenAI text-embedding-3-small: 1536 dimensiones
- sentence-transformers/all-MiniLM-L6-v2: 384 dimensiones

## ¿Cómo se generan los embeddings?

Los embeddings se generan mediante modelos de redes neuronales entrenados específicamente para esta tarea:

```python
# Ejemplo conceptual
texto = "El gato duerme en el sofá"
embedding = modelo_embedding.encode(texto)
# embedding = [0.123, -0.456, 0.789, ..., 0.234]  # Vector de 384+ dimensiones
```

## Medidas de similitud

### Similitud de Coseno
Mide el ángulo entre dos vectores:
- 1.0 = idénticos
- 0.0 = ortogonales (no relacionados)
- -1.0 = opuestos

### Distancia Euclidiana
Mide la distancia geométrica entre vectores:
- 0.0 = idénticos
- Mayor valor = más distantes

### Producto punto
Producto interno de dos vectores, útil para normalizar vectores.

## Modelos de embeddings populares

### Modelos open source
- **sentence-transformers**: Modelos ligeros y rápidos
- **BERT**: Modelo clásico de Google
- **MPNet**: Optimizado para similitud semántica

### Modelos comerciales
- **OpenAI Embeddings**: Alta calidad, requiere API key
- **Cohere Embeddings**: Especializado en búsqueda
- **Google PaLM Embeddings**: Integrado con servicios GCP

## Proceso de vectorización en RAG

1. **Chunking**: Dividir documentos en fragmentos manejables
2. **Embedding**: Convertir cada fragmento en vector
3. **Almacenamiento**: Guardar vectores en base de datos vectorial
4. **Indexación**: Crear índices para búsqueda rápida
5. **Recuperación**: Buscar vectores similares a la consulta

## Ejemplo práctico

```python
from sentence_transformers import SentenceTransformer

# Cargar modelo
model = SentenceTransformer('all-MiniLM-L6-v2')

# Generar embeddings
texts = [
    "Python es un lenguaje de programación",
    "Java es un lenguaje de programación",
    "Los gatos son animales domésticos"
]

embeddings = model.encode(texts)

# embeddings[0] y embeddings[1] serán más similares entre sí
# que cualquiera de ellos con embeddings[2]
```

## Consideraciones importantes

- **Calidad del modelo**: Mejores modelos = mejores embeddings
- **Tamaño del contexto**: Los modelos tienen límites de tokens
- **Idioma**: Usar modelos entrenados en el idioma objetivo
- **Dominio**: Algunos modelos están especializados en dominios específicos
