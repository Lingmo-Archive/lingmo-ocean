#!/usr/bin/env python3

import logging
from multiprocessing import cpu_count
from multiprocessing.pool import Pool
from pathlib import Path
from itertools import chain
from typing import Final

try:
	import PIL
	from PIL import Image
except ImportError:
	logging.critical("Please install the python PIL library.")
	logging.critical("e.g.: python3 -m pip install PIL")
	exit()

sizes = {
	'horizontal': (
		(8000, 4500), (4096, 3070)
		)
	}

templates = {
	'horizontal': ('base_size.png', 'base_size.jpg'),
	}

PIL_VERSION: Final = tuple(map(int, PIL.__version__.split(".")))


def resize_and_save_image(file: Path, image: Image, width: int, height: int) -> None:
	"""
	Image.LANCZOS is deprecated since 9.1.0 https://pillow.readthedocs.io/en/stable/deprecations.html#constants
	"""
	logging.info(f'Generating {width}x{height}')

	base_dir, extension = file.parent, file.suffix
	base_width, base_height = image.size

	if width / height > base_width / base_height:
		crop = int(base_height - height / (width / base_width)) // 2
		box = (0, crop, base_width, base_height - crop)
	elif width / height < base_width / base_height:
		crop = int(base_width - width / (height / base_height)) // 2
		box = (crop, 0, base_width - crop, base_height)
	else:
		box = None

	if PIL_VERSION >= (9, 1):
		resized_image = image.resize((width, height), Image.Resampling.LANCZOS, box)
	else:
		resized_image = image.resize((width, height), Image.LANCZOS, box)

	resized_image.save(base_dir / f'{width}x{height}{extension}',
					  quality=90, optimize=True, subsampling=1)


argument_list: list[tuple] = []

for orientation in ('horizontal'):
	for file in chain(*map(Path().rglob, templates[orientation])):
		image = Image.open(file)
		image.load()
		for width, height in sizes[orientation]:
			argument_list.append((file, image, width, height))

with Pool(processes=cpu_count()) as pool:
	pool.starmap(resize_and_save_image, argument_list)
