"""
Ejemplo simplificado de base de datos vectorial con ChromaDB

Este script demuestra los conceptos de bases de datos vectoriales usando
embeddings generados localmente (sin necesidad de descargar modelos).

NOTA: Este ejemplo usa embeddings simples para demostración. En producción,
      usarías modelos pre-entrenados como sentence-transformers.

Autor: RAG Learning Project
"""

import chromadb
from chromadb.config import Settings
import numpy as np


def generar_embedding_simple(texto):
    """
    Genera un embedding simple basado en características del texto.
    NOTA: Esto es solo para demostración. En producción usa modelos reales.
    """
    # Características básicas del texto
    longitud = len(texto)
    num_palabras = len(texto.split())
    num_a = texto.lower().count('a')
    num_e = texto.lower().count('e')
    num_i = texto.lower().count('i')
    num_o = texto.lower().count('o')
    num_u = texto.lower().count('u')
    
    # Crear vector normalizado de 10 dimensiones
    embedding = np.array([
        longitud / 100,
        num_palabras / 20,
        num_a / 10,
        num_e / 10,
        num_i / 10,
        num_o / 10,
        num_u / 10,
        hash(texto) % 100 / 100,
        len(set(texto.split())) / num_palabras if num_palabras > 0 else 0,
        texto.count('.') + texto.count(',')
    ])
    
    # Normalizar el vector
    norm = np.linalg.norm(embedding)
    if norm > 0:
        embedding = embedding / norm
    
    return embedding.tolist()


def crear_base_vectorial():
    """
    Crea una base de datos vectorial en memoria con ChromaDB
    """
    print("🚀 Iniciando ChromaDB...")
    
    client = chromadb.Client(Settings(
        anonymized_telemetry=False
    ))
    
    print("✅ Cliente ChromaDB creado exitosamente\n")
    return client


def crear_coleccion(client, nombre="mi_primera_coleccion"):
    """
    Crea una colección con función de embedding personalizada
    """
    print(f"📚 Creando colección '{nombre}'...")
    
    # Clase de embedding personalizada
    class EmbeddingFunction:
        def __call__(self, input):
            return [generar_embedding_simple(t) for t in input]
    
    # Crear colección con embedding function personalizada
    collection = client.create_collection(
        name=nombre,
        metadata={"descripcion": "Mi primera colección de documentos"},
        embedding_function=EmbeddingFunction()
    )
    
    print(f"✅ Colección '{nombre}' creada exitosamente\n")
    return collection


def agregar_documentos(collection):
    """
    Agrega documentos a la colección con sus metadatos
    """
    print("📝 Agregando documentos a la colección...\n")
    
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
    
    ids = [f"doc_{i+1}" for i in range(len(documentos))]
    
    collection.add(
        documents=documentos,
        metadatas=metadatos,
        ids=ids
    )
    
    print(f"✅ {len(documentos)} documentos agregados exitosamente\n")
    
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
    
    print("📌 Consulta 1: '¿Qué es una base de datos para IA?'")
    print("-" * 80)
    resultados = collection.query(
        query_texts=["¿Qué es una base de datos para IA?"],
        n_results=3
    )
    mostrar_resultados(resultados)
    
    print("📌 Consulta 2: 'lenguaje de programación para web'")
    print("-" * 80)
    resultados = collection.query(
        query_texts=["lenguaje de programación para web"],
        n_results=3
    )
    mostrar_resultados(resultados)
    
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
    
    todos = collection.get()
    
    print(f"📈 Total de documentos: {len(todos['ids'])}")
    print(f"📝 Primer ID: {todos['ids'][0]}")
    print(f"📝 Último ID: {todos['ids'][-1]}")
    
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
    
    print("💡 NOTA: Este ejemplo usa embeddings simples para demostración.")
    print("   En producción, usarías modelos como sentence-transformers.\n")
    
    client = crear_base_vectorial()
    collection = crear_coleccion(client)
    agregar_documentos(collection)
    estadisticas_coleccion(collection)
    realizar_busquedas(collection)
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
    print("   • Usa modelos pre-entrenados (sentence-transformers)")
    print("   • Explora bases de datos persistentes")
    print("   • Integra con modelos de lenguaje (LLMs)")
    print()


if __name__ == "__main__":
    main()
