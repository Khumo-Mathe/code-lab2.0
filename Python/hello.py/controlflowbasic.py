from collections import Counter
import re


def search_documents(documents, query, top_n=3):
    """
    Simple search engine ranking algorithm.

    Scores documents based on how often
    query words appear.
    """

    # Clean and tokenize query
    query_words = re.findall(r"\w+", query.lower())

    document_scores = []

    for document in documents:
        text = document["content"].lower()

        # Tokenize words
        words = re.findall(r"\w+", text)

        # Count word frequencies
        word_counts = Counter(words)

        score = 0

        # Add score for matching query words
        for word in query_words:
            score += word_counts[word]

        document_scores.append({
            "title": document["title"],
            "score": score
        })

    # Sort by highest score
    ranked_results = sorted(
        document_scores,
        key=lambda item: item["score"],
        reverse=True
    )

    return ranked_results[:top_n]


# Example documents
documents = [
    {
        "title": "Python Backend Development",
        "content": """
        Python is commonly used in backend systems,
        APIs, automation, and cloud engineering.
        """
    },
    {
        "title": "Network Security Basics",
        "content": """
        Cybersecurity includes firewalls,
        authentication, and intrusion detection.
        """
    },
    {
        "title": "Cloud Computing",
        "content": """
        Cloud platforms like Azure and AWS
        provide scalable infrastructure.
        """
    }
]

results = search_documents(
    documents,
    query="python cloud backend"
)