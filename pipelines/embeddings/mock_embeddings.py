from typing import List

def embed_texts(texts: List[str]) -> List[List[float]]:
    """Return deterministic mock embeddings (placeholder)."""
    return [[float(len(t)) for _ in range(8)] for t in texts]
