import ucimlrepo

class getData():
    dataset_name = ""
    def __init__(self, dataset_name) -> None:
        self.dataset_name = dataset_name

    def load_data(self):
        pass

    def pull_data(self):
        dataset_id_map = {
            'iris':53,
            'breast cancer wisconsin': 17,
            'heart disease': 45,
            'wine': 109,
            'census income': 20,
            'bank marketing': 222,
            'HAR using smartphones': '#',
            'wholesale customers': 292,
            'letter recognition': 59,
            'pen digits': 81,
            'yacht hydrodynamics': '#',
            'airfoil self-noise': 291,
            'energy efficiency': 242,
            'boston housing': 13,
            'concrete compressive strength': 165,
            'beijing pm2.5': 381
        }
        dataset = ucimlrepo.fetch_ucirepo(id = dataset_id_map[self.dataset_name])
        X = dataset.data.features
        y = dataset.data.targets
        return X, y