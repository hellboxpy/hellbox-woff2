# hellbox-woff2

A [hellbox](https://github.com/hellboxpy/hellbox) plugin that generates WOFF2 files from TTF or OTF sources using [fonttools](https://github.com/fonttools/fonttools).

## Usage

```python
from hellbox import Hellbox
from hellbox.jobs.woff2 import GenerateWoff2

with Hellbox("webfonts") as task:
    task.read("build/*.ttf") >> GenerateWoff2() >> task.write("webfonts")
```

## Installation

```sh
hell add hellbox-woff2
```

## Development

```sh
uv sync
uv run pytest
```
