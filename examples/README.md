# Ejemplos Prácticos de RAG

Este directorio contiene ejemplos prácticos para aprender RAG (Retrieval-Augmented Generation) y bases de datos vectoriales.

## 📋 Ejemplos disponibles

### 1. Primera Base Vectorial (Versión Simple) ⭐ RECOMENDADO
**Archivo:** `01_primera_base_vectorial_simple.py`

✅ **Funciona sin internet**  
✅ **No requiere descargar modelos**  
✅ **Ideal para comenzar**

Este ejemplo usa embeddings personalizados simples para demostrar los conceptos sin necesidad de descargar modelos pre-entrenados. Perfecto para:
- Aprender los conceptos básicos
- Probar sin conexión a internet
- Entender cómo funcionan las bases vectoriales

**Ejecutar:**
```bash
python examples/01_primera_base_vectorial_simple.py
```

**Qué aprenderás:**
- Crear una base de datos vectorial
- Agregar documentos con metadatos
- Realizar búsquedas semánticas
- Filtrar por metadatos
- Interpretar resultados de similitud

---

### 2. Primera Base Vectorial (Versión Completa)
**Archivo:** `01_primera_base_vectorial.py`

⚠️ **Requiere internet para descargar modelos**  
⚠️ **Primera ejecución puede tardar varios minutos**

Este ejemplo usa sentence-transformers con el modelo `all-MiniLM-L6-v2` para generar embeddings de alta calidad. Proporciona:
- Embeddings más precisos y semánticos
- Resultados de búsqueda más relevantes
- Experiencia más cercana a producción

**Ejecutar:**
```bash
python examples/01_primera_base_vectorial.py
```

**Requisitos:**
- Conexión a internet (solo primera vez)
- ~200MB de espacio para el modelo

---

### 3. Sistema RAG Completo
**Archivo:** `02_sistema_rag_completo.py`

⚠️ **Requiere internet para descargar modelos**

Implementación completa de un sistema RAG que incluye:
- Clase `SistemaRAG` reutilizable
- Base de conocimiento estructurada
- Proceso completo de recuperación
- Simulación de generación de respuestas
- Múltiples consultas de ejemplo

**Ejecutar:**
```bash
python examples/02_sistema_rag_completo.py
```

**Características:**
- Arquitectura orientada a objetos
- Fácil de extender y personalizar
- Listo para integrar con LLMs reales (GPT, Claude, etc.)

---

## 🚀 Comenzar rápidamente

### Opción 1: Sin internet (Recomendado para comenzar)
```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar ejemplo simple
python examples/01_primera_base_vectorial_simple.py
```

### Opción 2: Con modelos pre-entrenados
```bash
# Instalar dependencias
pip install -r requirements.txt

# Primera ejecución (descarga modelos)
python examples/01_primera_base_vectorial.py

# Ejecuciones posteriores serán más rápidas
```

---

## 📚 Orden de aprendizaje recomendado

1. **Leer documentación** (30-45 minutos)
   - `docs/01_concepto_rag.md`
   - `docs/02_vector_embeddings.md`
   - `docs/03_chromadb.md`

2. **Ejecutar ejemplo simple** (15-20 minutos)
   - `examples/01_primera_base_vectorial_simple.py`
   - Experimentar con diferentes consultas
   - Modificar documentos y metadatos

3. **Ejecutar ejemplo completo** (30-45 minutos)
   - `examples/01_primera_base_vectorial.py`
   - Comparar resultados con el ejemplo simple
   - Observar la diferencia en calidad

4. **Explorar sistema RAG** (45-60 minutos)
   - `examples/02_sistema_rag_completo.py`
   - Entender la arquitectura
   - Considerar cómo integrarlo con un LLM

---

## 🔧 Personalización

### Agregar tus propios documentos

Edita la lista `documentos` en cualquier ejemplo:

```python
documentos = [
    "Tu primer documento aquí",
    "Tu segundo documento aquí",
    "Tu tercer documento aquí",
]

metadatos = [
    {"categoria": "tu_categoria", "tema": "tema1"},
    {"categoria": "tu_categoria", "tema": "tema2"},
    {"categoria": "otra_categoria", "tema": "tema3"},
]
```

### Cambiar el modelo de embeddings

En los ejemplos completos, cambia el modelo:

```python
# Modelo más pequeño y rápido
model = SentenceTransformer('all-MiniLM-L6-v2')  # 384 dimensiones

# Modelo más grande y preciso
model = SentenceTransformer('all-mpnet-base-v2')  # 768 dimensiones

# Modelo multilingüe
model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')
```

### Persistir datos en disco

Cambia de cliente en memoria a persistente:

```python
# En lugar de:
client = chromadb.Client()

# Usa:
client = chromadb.PersistentClient(path="./mi_base_datos")
```

---

## 💡 Consejos

1. **Comienza simple**: Usa `01_primera_base_vectorial_simple.py` primero
2. **Experimenta**: Modifica documentos y consultas para entender mejor
3. **Observa las distancias**: Valores más bajos = mayor similitud
4. **Usa metadatos**: Permiten filtrar y organizar mejor los resultados
5. **Escala gradualmente**: Empieza con pocos documentos, luego aumenta

---

## 🐛 Solución de problemas

### Error: "No module named 'chromadb'"
```bash
pip install chromadb
```

### Error: "numpy.float_ was removed"
```bash
pip install "numpy<2.0" --force-reinstall
```

### Error de conexión al descargar modelos
- Verifica tu conexión a internet
- O usa el ejemplo simple: `01_primera_base_vectorial_simple.py`

### Los resultados no son relevantes
- El ejemplo simple usa embeddings básicos para demostración
- Usa `01_primera_base_vectorial.py` para mejores resultados
- Considera agregar más documentos relacionados

---

## 📖 Referencias

- [ChromaDB Documentation](https://docs.trychroma.com/)
- [Sentence Transformers](https://www.sbert.net/)
- [Documentación del proyecto](../docs/)

---

## 🎉 ¡Próximos pasos!

Después de completar estos ejemplos:

1. **Integra con un LLM real** (OpenAI, Anthropic, etc.)
2. **Carga documentos desde archivos** (PDF, TXT, DOCX)
3. **Implementa chunking inteligente** para documentos largos
4. **Despliega en producción** con ChromaDB en modo servidor
5. **Agrega una interfaz web** con Streamlit o Gradio

¡Buena suerte en tu viaje de aprendizaje de RAG! 🚀
