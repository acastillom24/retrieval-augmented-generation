"""
Práctica 1: Construcción de tu primera base de datos vectorial con ChromaDB

Este script demuestra cómo:
1. Crear una base de datos vectorial
2. Agregar documentos
3. Realizar búsquedas semánticas
4. Recuperar información relevante

Autor: RAG Learning Project
"""

import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer


def crear_base_vectorial():
    """
    Crea una base de datos vectorial en memoria con ChromaDB
    """
    print("🚀 Iniciando ChromaDB...")
    
    # Crear cliente de ChromaDB (en memoria para esta práctica)
    client = chromadb.Client(Settings(
        anonymized_telemetry=False
    ))
    
    print("✅ Cliente ChromaDB creado exitosamente\n")
    return client


def crear_coleccion(client, nombre="mi_primera_coleccion"):
    """
    Crea una colección (similar a una tabla) en ChromaDB
    """
    print(f"📚 Creando colección '{nombre}'...")
    print("📥 Cargando modelo de embeddings (esto puede tardar un momento)...")
    
    # Crear modelo de embeddings con sentence-transformers
    model = SentenceTransformer('all-MiniLM-L6-v2')
    
    # Crear función de embedding personalizada
    def embedding_function(texts):
        return model.encode(texts).tolist()
    
    # Crear colección con embedding function personalizada
    collection = client.create_collection(
        name=nombre,
        metadata={"descripcion": "Mi primera colección de documentos"},
        embedding_function=embedding_function
    )
    
    print(f"✅ Colección '{nombre}' creada exitosamente\n")
    return collection


def agregar_documentos(collection):
    """
    Agrega documentos a la colección con sus metadatos
    """
    print("📝 Agregando documentos a la colección...\n")
    
    # Documentos sobre tecnología y programación
    documentos = [
        "Python es un lenguaje de programación de alto nivel, interpretado y de propósito general.",
        "JavaScript es el lenguaje de programación más utilizado para desarrollo web frontend.",
        "Las bases de datos vectoriales almacenan embeddings para búsqueda semántica eficiente.",
        "Machine Learning es una rama de la inteligencia artificial que permite a las computadoras aprender.",
        "React es una biblioteca de JavaScript para construir interfaces de usuario.",
        "ChromaDB es una base de datos vectorial open-source ideal para aplicaciones de IA.",
        "Los transformers revolucionaron el procesamiento del lenguaje natural en 2017.",
        "Docker permite empaquetar aplicaciones con todas sus dependencias en contenedores.",
        "Git es un sistema de control de versiones distribuido para rastrear cambios en código.",
        "SQL es un lenguaje para gestionar y consultar bases de datos relacionales."
    ]
    
    # Metadatos para cada documento
    metadatos = [
        {"categoria": "lenguajes", "tema": "python", "nivel": "basico"},
        {"categoria": "lenguajes", "tema": "javascript", "nivel": "basico"},
        {"categoria": "bases_datos", "tema": "vectorial", "nivel": "intermedio"},
        {"categoria": "ia", "tema": "machine_learning", "nivel": "basico"},
        {"categoria": "frameworks", "tema": "react", "nivel": "intermedio"},
        {"categoria": "bases_datos", "tema": "chromadb", "nivel": "intermedio"},
        {"categoria": "ia", "tema": "nlp", "nivel": "avanzado"},
        {"categoria": "devops", "tema": "docker", "nivel": "intermedio"},
        {"categoria": "herramientas", "tema": "git", "nivel": "basico"},
        {"categoria": "bases_datos", "tema": "sql", "nivel": "basico"}
    ]
    
    # IDs únicos para cada documento
    ids = [f"doc_{i+1}" for i in range(len(documentos))]
    
    # Agregar documentos a la colección
    collection.add(
        documents=documentos,
        metadatas=metadatos,
        ids=ids
    )
    
    print(f"✅ {len(documentos)} documentos agregados exitosamente\n")
    
    # Mostrar algunos documentos agregados
    print("📄 Ejemplos de documentos agregados:")
    for i in range(min(3, len(documentos))):
        print(f"   {i+1}. {documentos[i][:70]}...")
    print()


def realizar_busquedas(collection):
    """
    Realiza búsquedas semánticas en la colección
    """
    print("=" * 80)
    print("🔍 REALIZANDO BÚSQUEDAS SEMÁNTICAS")
    print("=" * 80 + "\n")
    
    # Consulta 1: Búsqueda general
    print("📌 Consulta 1: '¿Qué es una base de datos para IA?'")
    print("-" * 80)
    resultados = collection.query(
        query_texts=["¿Qué es una base de datos para IA?"],
        n_results=3
    )
    mostrar_resultados(resultados)
    
    # Consulta 2: Búsqueda sobre lenguajes
    print("📌 Consulta 2: 'lenguaje de programación para web'")
    print("-" * 80)
    resultados = collection.query(
        query_texts=["lenguaje de programación para web"],
        n_results=3
    )
    mostrar_resultados(resultados)
    
    # Consulta 3: Búsqueda sobre inteligencia artificial
    print("📌 Consulta 3: 'aprendizaje automático'")
    print("-" * 80)
    resultados = collection.query(
        query_texts=["aprendizaje automático"],
        n_results=3
    )
    mostrar_resultados(resultados)


def busqueda_con_filtros(collection):
    """
    Realiza búsquedas con filtros de metadatos
    """
    print("\n" + "=" * 80)
    print("🎯 BÚSQUEDAS CON FILTROS DE METADATOS")
    print("=" * 80 + "\n")
    
    # Búsqueda filtrada por categoría
    print("📌 Búsqueda: Solo documentos de categoría 'bases_datos'")
    print("-" * 80)
    resultados = collection.query(
        query_texts=["bases de datos"],
        n_results=5,
        where={"categoria": "bases_datos"}
    )
    mostrar_resultados(resultados)


def mostrar_resultados(resultados):
    """
    Muestra los resultados de una búsqueda de forma legible
    """
    documentos = resultados['documents'][0]
    metadatos = resultados['metadatas'][0]
    distancias = resultados['distances'][0]
    
    for i, (doc, meta, dist) in enumerate(zip(documentos, metadatos, distancias), 1):
        print(f"\n{i}. Documento: {doc}")
        print(f"   Categoría: {meta['categoria']} | Tema: {meta['tema']} | Nivel: {meta['nivel']}")
        print(f"   Similitud: {1 - dist:.4f} (distancia: {dist:.4f})")
    print()


def estadisticas_coleccion(collection):
    """
    Muestra estadísticas de la colección
    """
    print("=" * 80)
    print("📊 ESTADÍSTICAS DE LA COLECCIÓN")
    print("=" * 80 + "\n")
    
    # Obtener todos los documentos
    todos = collection.get()
    
    print(f"📈 Total de documentos: {len(todos['ids'])}")
    print(f"📝 Primer ID: {todos['ids'][0]}")
    print(f"📝 Último ID: {todos['ids'][-1]}")
    
    # Contar categorías
    categorias = {}
    for meta in todos['metadatas']:
        cat = meta['categoria']
        categorias[cat] = categorias.get(cat, 0) + 1
    
    print(f"\n📊 Documentos por categoría:")
    for cat, count in sorted(categorias.items()):
        print(f"   • {cat}: {count} documentos")
    print()


def main():
    """
    Función principal que ejecuta todo el flujo
    """
    print("\n" + "=" * 80)
    print("🎓 PRÁCTICA: CONSTRUCCIÓN DE TU PRIMERA BASE DE DATOS VECTORIAL")
    print("=" * 80 + "\n")
    
    # Paso 1: Crear base vectorial
    client = crear_base_vectorial()
    
    # Paso 2: Crear colección
    collection = crear_coleccion(client)
    
    # Paso 3: Agregar documentos
    agregar_documentos(collection)
    
    # Paso 4: Mostrar estadísticas
    estadisticas_coleccion(collection)
    
    # Paso 5: Realizar búsquedas semánticas
    realizar_busquedas(collection)
    
    # Paso 6: Búsquedas con filtros
    busqueda_con_filtros(collection)
    
    print("=" * 80)
    print("🎉 ¡PRÁCTICA COMPLETADA EXITOSAMENTE!")
    print("=" * 80)
    print("\n💡 Has aprendido a:")
    print("   ✅ Crear una base de datos vectorial con ChromaDB")
    print("   ✅ Agregar documentos con metadatos")
    print("   ✅ Realizar búsquedas semánticas")
    print("   ✅ Filtrar resultados por metadatos")
    print("   ✅ Interpretar resultados de similitud")
    print("\n📚 Próximos pasos:")
    print("   • Experimenta con tus propios documentos")
    print("   • Prueba diferentes consultas")
    print("   • Explora bases de datos persistentes")
    print("   • Integra con modelos de lenguaje (LLMs)")
    print()


if __name__ == "__main__":
    main()
