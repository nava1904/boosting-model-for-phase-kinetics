import numpy as np
from collections import Counter
from typing import List, Dict


def normalize(d: Dict[str, float]) -> Dict[str, float]:
    total = sum(d.values())
    return {k: v / total for k, v in d.items()}


def weighted_sample(options: List[str], weights: List[float]) -> str:
    total = sum(weights)
    probs = [w / total for w in weights]
    return np.random.choice(options, p=probs)


def generate_site_config(
    composition: Dict[str, float],
    site_preference: Dict[str, Dict[str, float]],
    total_sites: int = 5,
    num_samples: int = 100
) -> List[List[str]]:
    element_pool = Counter()
    for el, frac in composition.items():
        element_pool[el] = int(round(frac * total_sites * num_samples))

    samples = []

    for _ in range(num_samples):
        config = []
        temp_pool = element_pool.copy()

        for site in ['A', 'B', 'C', 'D', 'E']:
            prefs = site_preference.get(site, {})
            available = {el: prefs[el] for el in prefs if temp_pool[el] > 0}

            if not available:
                # fallback to any available element
                fallback = {el: 1.0 for el in temp_pool if temp_pool[el] > 0}
                available = fallback

            norm_avail = normalize(available)
            chosen = weighted_sample(list(norm_avail.keys()), list(norm_avail.values()))
            config.append(chosen)
            temp_pool[chosen] -= 1

        samples.append(config)

    return samples


def compute_composition(samples: List[List[str]]) -> Dict[str, float]:
    flat = [el for config in samples for el in config]
    counts = Counter(flat)
    total = sum(counts.values())
    return {el: counts[el] / total for el in counts}
