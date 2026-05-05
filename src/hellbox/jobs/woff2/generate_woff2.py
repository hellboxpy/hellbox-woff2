from fontTools import ttLib

from hellbox import Chute, Hellbox


class GenerateWoff2(Chute):
    """GenerateWoff2 converts a TTF or OTF file to WOFF2."""

    def process(self, file):
        Hellbox.info(f"Generating WOFF2: {file.name}")
        copy = file.copy(name=file.stem + ".woff2")
        font = ttLib.TTFont(file.content_path)
        font.flavor = "woff2"
        font.save(copy.content_path)
        return copy
