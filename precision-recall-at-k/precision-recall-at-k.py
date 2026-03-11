def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    hits = 0
    top_k = recommended[:k]
    for i in top_k:
        for j in relevant:
            if i == j:
                hits+=1
    precision = hits/k
    recall = hits/len(relevant)
    return [precision, recall]