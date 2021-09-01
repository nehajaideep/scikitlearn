import os
import random

__version__ = "1.0.dev0"


def setup_module(module):
    import numpy as np

    _random_seed = os.environ.get("SKLEARN_SEED", None)
    if _random_seed is None:
        _random_seed = np.random.uniform() * np.iinfo(np.int32).max
    _random_seed = int(_random_seed)
    print("Seeding %r" % _random_seed)
    np.random.seed(_random_seed)
    random.seed(_random_seed)