# https://docs.python.org/3/library/multiprocessing.html
from argparse import ArgumentParser, Namespace
from functools import partial
from multiprocessing import Pool
from pathlib import Path
from typing import Optional

import requests
from tqdm import tqdm


def get_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument(
        "-n",
        "--num-processes",  # num_processes
        required=False,
        default=10,
        help="Number of processes",
    )
    parser.add_argument(
        "-r",
        "--root",
        required=False,
        type=str,
        default="images_multi",
        help="Root directory of the dataset",
    )
    return parser.parse_args()


def download_and_save(url: Optional[str], path: Path) -> None:
    response = requests.get(url)
    response.raise_for_status()
    with open(path, "wb") as f:
        f.write(response.content)


def process(root: Path, url_idx: int) -> None:
    url = f"https://pokeapi.co/api/v2/pokemon/{url_idx}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        pokemon_response = response.json()
    except requests.HTTPError:
        print(f"cannot download {url}")
        return
    try:
        pokemon_name = pokemon_response["name"]
        image_path = pokemon_response["sprites"]["other"]["official-artwork"][
            "front_default"
        ]
        download_and_save(image_path, root / f"{pokemon_name}.png")
    except requests.exceptions.MissingSchema:
        print(f"image path is None for {pokemon_name}")
    except requests.HTTPError:
        print(f"cannot download image for {pokemon_name}")
    except KeyError:
        print(f"dict is invalid for {pokemon_name}")


def main():
    args = get_args()
    root = Path(args.root)
    root.mkdir(exist_ok=True)

    # total_number = 897
    total_number = 100
    func = partial(process, root)

    with tqdm(total=total_number, desc="Downloading pokemons") as pbar:
        with Pool(args.num_processes) as p:
            # https://stackoverflow.com/questions/26520781/multiprocessing-pool-whats-the-difference-between-map-async-and-imap
            for _ in p.imap_unordered(func, iterable=range(1, total_number)):
                pbar.update()


if __name__ == "__main__":
    main()
