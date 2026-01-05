"""
Práctica 2: RAG Completo - Sistema de Preguntas y Respuestas

Este ejemplo demuestra un sistema RAG completo que:
1. Carga documentos sobre un tema específico
2. Los almacena en una base vectorial
3. Recupera información relevante según consultas
4. Simula la generación de respuestas (sin necesidad de API de LLM)

Autor: RAG Learning Project
"""

import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer


# Documentos de ejemplo sobre RAG y tecnologías relacionadas
KNOWLEDGE_BASE = {
    "rag_1": {
        "texto": "RAG (Retrieval-Augmented Generation) es una técnica que combina la recuperación de información con la generación de texto. Permite a los modelos de lenguaje acceder a información actualizada y específica sin necesidad de reentrenamiento.",
        "metadata": {"tema": "rag", "subtema": "definicion", "importancia": "alta"}
    },
    "rag_2": {
        "texto": "El proceso RAG tiene tres fases principales: primero recupera información relevante de una base de datos, luego aumenta el contexto con esta información, y finalmente genera una respuesta basada en el contexto enriquecido.",
        "metadata": {"tema": "rag", "subtema": "proceso", "importancia": "alta"}
    },
    "embeddings_1": {
        "texto": "Los embeddings vectoriales son representaciones numéricas de texto que capturan su significado semántico. Textos con significados similares tienen embeddings cercanos en el espacio vectorial.",
        "metadata": {"tema": "embeddings", "subtema": "definicion", "importancia": "alta"}
    },
    "embeddings_2": {
        "texto": "Los modelos de embeddings populares incluyen sentence-transformers, BERT y los embeddings de OpenAI. Cada uno tiene diferentes dimensiones y especialidades según el caso de uso.",
        "metadata": {"tema": "embeddings", "subtema": "modelos", "importancia": "media"}
    },
    "chromadb_1": {
        "texto": "ChromaDB es una base de datos vectorial open-source diseñada para aplicaciones de IA. Permite almacenar embeddings y realizar búsquedas semánticas de manera eficiente con una API simple.",
        "metadata": {"tema": "chromadb", "subtema": "definicion", "importancia": "alta"}
    },
    "chromadb_2": {
        "texto": "ChromaDB soporta múltiples funciones de distancia como similitud de coseno, distancia euclidiana y producto punto. También permite filtrar resultados usando metadatos para búsquedas más precisas.",
        "metadata": {"tema": "chromadb", "subtema": "funcionalidades", "importancia": "media"}
    },
    "vectordb_1": {
        "texto": "Las bases de datos vectoriales están optimizadas para almacenar y buscar vectores de alta dimensión. Utilizan algoritmos como HNSW y IVF para realizar búsquedas eficientes incluso con millones de vectores.",
        "metadata": {"tema": "bases_vectoriales", "subtema": "arquitectura", "importancia": "media"}
    },
    "aplicaciones_1": {
        "texto": "Las aplicaciones RAG son útiles para chatbots especializados, sistemas de preguntas y respuestas sobre documentación técnica, análisis de documentos legales y asistentes virtuales corporativos.",
        "metadata": {"tema": "aplicaciones", "subtema": "casos_uso", "importancia": "media"}
    }
}


class SistemaRAG:
    """
    Sistema RAG simplificado para demostración
    """
    
    def __init__(self, nombre_coleccion="conocimiento_rag"):
        """
        Inicializa el sistema RAG
        """
        print("🚀 Inicializando Sistema RAG...")
        print("📥 Cargando modelo de embeddings...")
        
        # Crear modelo de embeddings
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        
        # Crear cliente ChromaDB
        self.client = chromadb.Client(Settings(
            anonymized_telemetry=False
        ))
        
        # Crear función de embedding personalizada
        def embedding_function(texts):
            return self.model.encode(texts).tolist()
        
        # Crear colección con embedding function personalizada
        self.collection = self.client.create_collection(
            name=nombre_coleccion,
            metadata={"descripcion": "Base de conocimiento sobre RAG"},
            embedding_function=embedding_function
        )
        
        print("✅ Sistema RAG inicializado\n")
    
    def cargar_conocimiento(self):
        """
        Carga la base de conocimiento en ChromaDB
        """
        print("📚 Cargando base de conocimiento...")
        
        documentos = []
        metadatos = []
        ids = []
        
        for doc_id, contenido in KNOWLEDGE_BASE.items():
            documentos.append(contenido["texto"])
            metadatos.append(contenido["metadata"])
            ids.append(doc_id)
        
        self.collection.add(
            documents=documentos,
            metadatas=metadatos,
            ids=ids
        )
        
        print(f"✅ {len(documentos)} documentos cargados en la base vectorial\n")
    
    def recuperar_contexto(self, consulta, n_resultados=3):
        """
        Recupera los documentos más relevantes para una consulta
        """
        print(f"🔍 Buscando información relevante para: '{consulta}'")
        print("-" * 80)
        
        resultados = self.collection.query(
            query_texts=[consulta],
            n_results=n_resultados
        )
        
        documentos = resultados['documents'][0]
        metadatos = resultados['metadatas'][0]
        distancias = resultados['distances'][0]
        
        contexto = []
        
        print("\n📄 Documentos recuperados:\n")
        for i, (doc, meta, dist) in enumerate(zip(documentos, metadatos, distancias), 1):
            similitud = 1 - dist
            contexto.append(doc)
            print(f"{i}. [{meta['tema']}] Similitud: {similitud:.3f}")
            print(f"   {doc[:100]}...")
            print()
        
        return contexto
    
    def generar_respuesta(self, consulta, contexto):
        """
        Simula la generación de una respuesta basada en el contexto
        (En un sistema real, esto usaría un LLM como GPT, Claude, etc.)
        """
        print("🤖 Generando respuesta...\n")
        print("=" * 80)
        print("RESPUESTA GENERADA")
        print("=" * 80)
        
        # Simulación simple: concatenar contexto relevante
        respuesta = f"Basándome en la información recuperada:\n\n"
        
        for i, ctx in enumerate(contexto, 1):
            respuesta += f"{i}. {ctx}\n\n"
        
        respuesta += "En resumen, la información más relevante para tu consulta se encuentra en los documentos anteriores."
        
        print(respuesta)
        print("=" * 80 + "\n")
    
    def responder_consulta(self, consulta, n_resultados=3):
        """
        Proceso completo RAG: recuperar y generar respuesta
        """
        print("\n" + "=" * 80)
        print(f"❓ CONSULTA: {consulta}")
        print("=" * 80 + "\n")
        
        # Paso 1: Recuperar contexto relevante
        contexto = self.recuperar_contexto(consulta, n_resultados)
        
        # Paso 2: Generar respuesta (simulada)
        self.generar_respuesta(consulta, contexto)
    
    def estadisticas(self):
        """
        Muestra estadísticas del sistema
        """
        todos = self.collection.get()
        
        print("📊 Estadísticas del sistema:")
        print(f"   • Total documentos: {len(todos['ids'])}")
        
        # Contar por tema
        temas = {}
        for meta in todos['metadatas']:
            tema = meta['tema']
            temas[tema] = temas.get(tema, 0) + 1
        
        print(f"   • Temas en la base:")
        for tema, count in sorted(temas.items()):
            print(f"     - {tema}: {count} documentos")
        print()


def main():
    """
    Función principal que demuestra el sistema RAG
    """
    print("\n" + "=" * 80)
    print("🎓 PRÁCTICA: SISTEMA RAG COMPLETO")
    print("=" * 80 + "\n")
    
    # Crear sistema RAG
    sistema = SistemaRAG()
    
    # Cargar conocimiento
    sistema.cargar_conocimiento()
    
    # Mostrar estadísticas
    sistema.estadisticas()
    
    # Consultas de ejemplo
    consultas = [
        "¿Qué es RAG y cómo funciona?",
        "¿Qué son los embeddings vectoriales?",
        "¿Cuáles son las aplicaciones de RAG?",
        "Explícame ChromaDB"
    ]
    
    for consulta in consultas:
        sistema.responder_consulta(consulta, n_resultados=2)
        print("\n")
    
    print("=" * 80)
    print("🎉 ¡DEMOSTRACIÓN COMPLETADA!")
    print("=" * 80)
    print("\n💡 Este ejemplo demuestra:")
    print("   ✅ Carga de base de conocimiento")
    print("   ✅ Recuperación semántica de información")
    print("   ✅ Proceso completo de RAG")
    print("   ✅ Manejo de consultas múltiples")
    print("\n🚀 Siguiente nivel:")
    print("   • Integrar con OpenAI o Anthropic para respuestas reales")
    print("   • Cargar documentos desde archivos PDF o TXT")
    print("   • Implementar chunking para documentos largos")
    print("   • Agregar persistencia de la base vectorial")
    print()


if __name__ == "__main__":
    main()
