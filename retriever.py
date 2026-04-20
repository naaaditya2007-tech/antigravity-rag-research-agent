import math, re
from collections import Counter

class VectorRetriever:
    def __init__(self, docs):
        self.docs = docs
        self.vocab = sorted(list({w for d in docs for w in re.findall(r'\w+', d.lower())}))
        self.vecs = [self._vec(d) for d in docs]

    def _vec(self, text):
        c = Counter(re.findall(r'\w+', text.lower()))
        return [c.get(w, 0) for w in self.vocab]

    def query(self, q: str):
        qv = self._vec(q)
        best_score, best_doc = -1.0, ""
        for v, doc in zip(self.vecs, self.docs):
            dot = sum(a*b for a, b in zip(qv, v))
            mag = math.sqrt(sum(a*a for a in qv)) * math.sqrt(sum(b*b for b in v))
            score = dot / mag if mag else 0.0
            if score > best_score:
                best_score, best_doc = score, doc
        return {"score": round(best_score, 4), "document": best_doc}

if __name__ == "__main__":
    r = VectorRetriever(["Distributed consensus uses Raft and Paxos.", "Gradient descent optimizes neural weights."])
    print("Top Match:", r.query("How do distributed systems reach consensus?"))
