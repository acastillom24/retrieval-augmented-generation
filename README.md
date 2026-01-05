# 🚀 Retrieval-Augmented Generation (RAG) - Guía Completa de Aprendizaje

Repositorio educativo para aprender todo lo necesario sobre RAG (Retrieval-Augmented Generation), incluyendo conceptos fundamentales, vector embeddings, bases de datos vectoriales y prácticas hands-on.

## 📚 ¿Qué aprenderás?

Este repositorio cubre todo lo necesario para dominar RAG:

1. ✅ **Conceptos de RAG**: Fundamentos y arquitectura
2. ✅ **Vector Embeddings**: Representaciones semánticas de texto
3. ✅ **ChromaDB**: Base de datos vectorial para aplicaciones de IA
4. ✅ **Práctica**: Construcción de tu primera base vectorial

## 🎯 Para quién es este repositorio

- Desarrolladores que quieren aprender RAG desde cero
- Ingenieros de ML/IA que buscan implementar sistemas RAG
- Estudiantes interesados en procesamiento de lenguaje natural
- Cualquiera curioso sobre bases de datos vectoriales

## 🗂️ Estructura del repositorio

```
retrieval-augmented-generation/
├── docs/                          # Documentación teórica
│   ├── 01_concepto_rag.md        # Fundamentos de RAG
│   ├── 02_vector_embeddings.md   # Todo sobre embeddings vectoriales
│   ├── 03_chromadb.md            # Guía completa de ChromaDB
│   └── 04_practica_base_vectorial.md  # Guía de práctica
├── examples/                      # Ejemplos prácticos
│   ├── 01_primera_base_vectorial.py   # Ejemplo básico
│   └── 02_sistema_rag_completo.py     # Sistema RAG completo
├── requirements.txt              # Dependencias del proyecto
└── README.md                     # Este archivo
```

## 🚀 Inicio rápido

### 1. Clonar el repositorio

```bash
git clone https://github.com/acastillom24/retrieval-augmented-generation.git
cd retrieval-augmented-generation
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Explorar la documentación

Lee los documentos en orden:
1. `docs/01_concepto_rag.md` - Entiende qué es RAG
2. `docs/02_vector_embeddings.md` - Aprende sobre embeddings
3. `docs/03_chromadb.md` - Domina ChromaDB
4. `docs/04_practica_base_vectorial.md` - Guía de práctica

### 4. Ejecutar ejemplos prácticos

```bash
# Ejemplo 1: Primera base vectorial
python examples/01_primera_base_vectorial.py

# Ejemplo 2: Sistema RAG completo
python examples/02_sistema_rag_completo.py
```

## 📖 Documentación

### 1. Concepto de RAG
**Archivo:** `docs/01_concepto_rag.md`

Aprende:
- ¿Qué es RAG?
- ¿Cómo funciona?
- Ventajas de RAG
- Arquitectura básica
- Casos de uso comunes
- Componentes clave

### 2. Vector Embeddings
**Archivo:** `docs/02_vector_embeddings.md`

Cubre:
- Qué son los embeddings vectoriales
- Por qué son importantes
- Características y dimensionalidad
- Cómo se generan
- Medidas de similitud
- Modelos populares
- Proceso de vectorización en RAG

### 3. ChromaDB
**Archivo:** `docs/03_chromadb.md`

Explica:
- Qué es ChromaDB
- Características principales
- Instalación y configuración
- Conceptos clave (colecciones, metadatos)
- Uso básico y operaciones CRUD
- Modos de operación
- Funciones de embedding
- Filtrado con metadatos
- Comparación con otras bases vectoriales

### 4. Práctica - Base Vectorial
**Archivo:** `docs/04_practica_base_vectorial.md`

Guía práctica que incluye:
- Requisitos previos
- Objetivos de aprendizaje
- Ejercicios prácticos
- Conceptos clave a observar
- Interpretación de resultados
- Siguientes pasos
- Solución de problemas

## 💻 Ejemplos prácticos

### Ejemplo 1: Primera base vectorial
**Archivo:** `examples/01_primera_base_vectorial.py`

Este script demuestra:
- ✅ Crear cliente ChromaDB
- ✅ Crear colecciones
- ✅ Agregar documentos con metadatos
- ✅ Realizar búsquedas semánticas
- ✅ Filtrar por metadatos
- ✅ Visualizar estadísticas

**Ejecutar:**
```bash
python examples/01_primera_base_vectorial.py
```

**Salida esperada:**
- Creación de base de datos vectorial
- Inserción de 10 documentos sobre tecnología
- Búsquedas semánticas con resultados
- Filtrado por categorías
- Estadísticas de la colección

### Ejemplo 2: Sistema RAG completo
**Archivo:** `examples/02_sistema_rag_completo.py`

Un sistema RAG funcional que incluye:
- ✅ Clase `SistemaRAG` reutilizable
- ✅ Base de conocimiento sobre RAG
- ✅ Recuperación semántica
- ✅ Proceso completo RAG
- ✅ Múltiples consultas de ejemplo

**Ejecutar:**
```bash
python examples/02_sistema_rag_completo.py
```

**Características:**
- Sistema orientado a objetos
- Base de conocimiento estructurada
- Recuperación de contexto relevante
- Simulación de generación de respuestas
- Estadísticas del sistema

## 🛠️ Tecnologías utilizadas

- **ChromaDB** (v0.4.22): Base de datos vectorial
- **sentence-transformers** (v2.3.1): Modelos de embeddings
- **OpenAI** (v1.12.0): API para embeddings/LLMs (opcional)
- **Python** (3.8+): Lenguaje de programación

## 📊 ¿Qué es RAG?

RAG (Retrieval-Augmented Generation) combina:

1. **Recuperación**: Busca información relevante en documentos
2. **Aumento**: Añade contexto a la consulta
3. **Generación**: LLM genera respuesta basada en contexto

```
Consulta → Búsqueda Vectorial → Documentos → LLM → Respuesta
```

## 🎓 Ruta de aprendizaje recomendada

### Nivel 1: Fundamentos (1-2 horas)
1. ✅ Lee `01_concepto_rag.md`
2. ✅ Lee `02_vector_embeddings.md`
3. ✅ Lee `03_chromadb.md`

### Nivel 2: Práctica básica (1-2 horas)
1. ✅ Instala dependencias
2. ✅ Ejecuta `01_primera_base_vectorial.py`
3. ✅ Modifica el código con tus propios documentos
4. ✅ Experimenta con diferentes consultas

### Nivel 3: Sistema completo (2-3 horas)
1. ✅ Lee `04_practica_base_vectorial.md`
2. ✅ Ejecuta `02_sistema_rag_completo.py`
3. ✅ Completa los ejercicios prácticos
4. ✅ Crea tu propio sistema RAG

### Nivel 4: Avanzado (opcional)
1. ✅ Implementa persistencia de datos
2. ✅ Integra con OpenAI o Anthropic
3. ✅ Carga documentos desde PDFs
4. ✅ Implementa chunking inteligente
5. ✅ Despliega en producción

## 🔧 Requisitos del sistema

- **Python**: 3.8 o superior
- **RAM**: Mínimo 4GB (8GB recomendado)
- **Espacio en disco**: 500MB para dependencias
- **Sistema operativo**: Windows, macOS, Linux

## 📦 Instalación detallada

### Opción 1: pip (recomendado)
```bash
pip install -r requirements.txt
```

### Opción 2: Instalación manual
```bash
pip install chromadb==0.4.22
pip install sentence-transformers==2.3.1
pip install openai==1.12.0
pip install python-dotenv==1.0.1
```

### Opción 3: Ambiente virtual
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## 🚀 Casos de uso prácticos

### 1. Chatbot especializado
Crea un chatbot con conocimiento específico de tu empresa o dominio.

### 2. Sistema de Q&A sobre documentación
Responde preguntas sobre manuales, documentación técnica o políticas.

### 3. Asistente de análisis de documentos
Analiza contratos, reportes o documentos legales.

### 4. Búsqueda semántica
Implementa búsqueda inteligente en tu base de conocimiento.

### 5. Sistema de recomendaciones
Recomienda contenido similar basado en intereses.

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si quieres mejorar este repositorio:

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Agrega nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## 📝 Notas importantes

- Los ejemplos están diseñados para ser educativos, no para producción directa
- ChromaDB en modo memoria no persiste datos al cerrar el programa
- Para producción, usa `PersistentClient` o modo cliente/servidor
- Los embeddings automáticos usan modelos open-source (no requieren API key)

## 🐛 Solución de problemas

### Error de instalación de ChromaDB
```bash
pip install --upgrade pip
pip install chromadb
```

### Error de memoria con sentence-transformers
Usa un modelo más ligero:
```python
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')  # Solo 80MB
```

### Advertencias de telemetría
Son normales y no afectan el funcionamiento. Para deshabilitarlas:
```python
client = chromadb.Client(Settings(anonymized_telemetry=False))
```

## 📚 Recursos adicionales

- [Documentación oficial de ChromaDB](https://docs.trychroma.com/)
- [Sentence Transformers](https://www.sbert.net/)
- [OpenAI Embeddings](https://platform.openai.com/docs/guides/embeddings)
- [Pinecone Learning Center](https://www.pinecone.io/learn/)

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Ver el archivo `LICENSE` para más detalles.

## ✨ Autor

Desarrollado con ❤️ para la comunidad de aprendizaje de IA.

## 🎉 ¡Comienza ahora!

```bash
# 1. Clona el repositorio
git clone https://github.com/acastillom24/retrieval-augmented-generation.git

# 2. Instala dependencias
cd retrieval-augmented-generation
pip install -r requirements.txt

# 3. Ejecuta tu primer ejemplo
python examples/01_primera_base_vectorial.py
```

---

**¿Preguntas o sugerencias?** Abre un issue en GitHub.

**¿Te gustó este proyecto?** ¡Dale una ⭐ en GitHub!