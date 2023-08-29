class GlobalResultsSQLAlchemy:
    """
    This is a mock. Here we should make a query
    """

    def get(self):
        return {
            "data": {
                "1": {
                    "name": "Rachel Green",
                    "tournaments": {
                        "may": {"points": "900"},
                        "june": {"points": "500"},
                    },
                    "total_points": "1400",
                },
                "2": {
                    "name": "Ross Geller",
                    "tournaments": {
                        "may": {"points": "800"},
                        "june": {"points": "400"},
                    },
                    "total_points": "1200",
                },
                "3": {
                    "name": "Chandler Bing",
                    "tournaments": {
                        "may": {"points": "600"},
                        "june": {"points": "400"},
                    },
                    "total_points": "1000",
                },
                "4": {
                    "name": "Monica Geller",
                    "tournaments": {
                        "may": {"points": "500"},
                        "june": {"points": "100"},
                    },
                    "total_points": "600",
                },
                "5": {
                    "name": "Joey Tribbiani",
                    "tournaments": {
                        "may": {"points": "300"},
                        "june": {"points": "100"},
                    },
                    "total_points": "400",
                },
                "6": {
                    "name": "Phoebe Buffay",
                    "tournaments": {"may": {"points": "30"}, "june": {"points": "10"}},
                    "total_points": "40",
                },
            }
        }
