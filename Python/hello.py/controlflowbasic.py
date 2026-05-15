from collections import defaultdict
from datetime import datetime


class RecommendationEngine:
    """
    Basic recommendation system using
    user interaction history.
    """

    def __init__(self):
        self.user_activity = defaultdict(list)
        self.product_popularity = defaultdict(int)

    def track_interaction(
        self,
        user_id,
        product_id,
        interaction_type
    ):
        """
        Track user activity.
        """

        interaction = {
            "product_id": product_id,
            "interaction_type": interaction_type,
            "timestamp": datetime.now()
        }

        self.user_activity[user_id].append(
            interaction
        )

        # Increase popularity score
        self.product_popularity[product_id] += 1

    def recommend_products(
        self,
        user_id,
        limit=5
    ):
        """
        Recommend products based on
        user interaction history.
        """

        interacted_products = {
            activity["product_id"]
            for activity in self.user_activity[user_id]
        }

        recommendations = []

        # Recommend popular products
        for product_id, score in sorted(
            self.product_popularity.items(),
            key=lambda item: item[1],
            reverse=True
        ):

            if product_id not in interacted_products:
                recommendations.append({
                    "product_id": product_id,
                    "popularity_score": score
                })

            if len(recommendations) >= limit:
                break

        return recommendations

    def user_summary(self, user_id):
        """
        Return user activity statistics.
        """

        interactions = self.user_activity[user_id]

        interaction_counts = defaultdict(int)

        for activity in interactions:
            interaction_counts[
                activity["interaction_type"]
            ] += 1

        return {
            "total_interactions": len(interactions),
            "interaction_breakdown": dict(
                interaction_counts
            )
        }


# Example usage
engine = RecommendationEngine()

engine.track_interaction(
    user_id="khumo",
    product_id="P100",
    interaction_type="VIEW"
)

engine.track_interaction(
    user_id="khumo",
    product_id="P200",
    interaction_type="PURCHASE"
)

engine.track_interaction(
    user_id="user_2",
    product_id="P300",
    interaction_type="VIEW"
)

engine.track_interaction(
    user_id="user_3",
    product_id="P300",
    interaction_type="PURCHASE"
)

engine.track_interaction(
    user_id="user_4",
    product_id="P400",
    interaction_type="VIEW"
)

recommendations = engine.recommend_products(
    user_id="khumo"
)

summary = engine.user_summary(
    user_id="khumo"
)