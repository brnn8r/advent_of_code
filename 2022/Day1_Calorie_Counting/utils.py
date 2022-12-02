from typing import List


def chunk_list(seq: List, partition):
    chunk = []
    for item in seq:
        if item == partition:
            yield chunk
            chunk = []
        else:
            chunk.append(item)
