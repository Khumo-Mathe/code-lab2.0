from math import radians, sin, cos, sqrt, atan2


class DeliveryRouter:
    """
    Delivery route optimization system.

    Finds the nearest driver to a delivery request
    using geographical coordinates.
    """

    def __init__(self):
        self.drivers = []

    def add_driver(
        self,
        driver_id,
        latitude,
        longitude,
        available=True
    ):
        """
        Register a driver.
        """

        self.drivers.append({
            "driver_id": driver_id,
            "latitude": latitude,
            "longitude": longitude,
            "available": available
        })

    def calculate_distance(
        self,
        lat1,
        lon1,
        lat2,
        lon2
    ):
        """
        Calculate distance using Haversine Formula.
        """

        earth_radius_km = 6371

        dlat = radians(lat2 - lat1)
        dlon = radians(lon2 - lon1)

        a = (
            sin(dlat / 2) ** 2
            + cos(radians(lat1))
            * cos(radians(lat2))
            * sin(dlon / 2) ** 2
        )

        c = 2 * atan2(
            sqrt(a),
            sqrt(1 - a)
        )

        return earth_radius_km * c

    def find_nearest_driver(
        self,
        customer_latitude,
        customer_longitude
    ):
        """
        Find closest available driver.
        """

        nearest_driver = None
        shortest_distance = float("inf")

        for driver in self.drivers:

            if not driver["available"]:
                continue

            distance = self.calculate_distance(
                customer_latitude,
                customer_longitude,
                driver["latitude"],
                driver["longitude"]
            )

            if distance < shortest_distance:
                shortest_distance = distance
                nearest_driver = driver

        if not nearest_driver:
            return {
                "success": False,
                "message": "No available drivers"
            }

        return {
            "success": True,
            "driver_id": (
                nearest_driver["driver_id"]
            ),
            "distance_km": round(
                shortest_distance,
                2
            )
        }


# Example usage
router = DeliveryRouter()

router.add_driver(
    driver_id="DRV100",
    latitude=-26.2041,
    longitude=28.0473
)

router.add_driver(
    driver_id="DRV101",
    latitude=-26.1076,
    longitude=28.0567
)

router.add_driver(
    driver_id="DRV102",
    latitude=-25.7479,
    longitude=28.2293,
    available=False
)

nearest_driver = router.find_nearest_driver(
    customer_latitude=-26.1952,
    customer_longitude=28.0341
)