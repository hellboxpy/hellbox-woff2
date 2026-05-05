from unittest.mock import MagicMock, patch

from hellbox.jobs.woff2 import GenerateWoff2


class TestGenerateWoff2:
    def test_init(self):
        assert GenerateWoff2()

    def test_process(self):
        file = MagicMock()
        copy = MagicMock()
        file.stem = "MyFont"
        file.copy.return_value = copy

        with patch("hellbox.jobs.woff2.generate_woff2.ttLib") as mock_ttlib:
            mock_font = MagicMock()
            mock_ttlib.TTFont.return_value = mock_font
            result = GenerateWoff2().process(file)

        file.copy.assert_called_once_with(name="MyFont.woff2")
        mock_ttlib.TTFont.assert_called_once_with(file.content_path)
        assert mock_font.flavor == "woff2"
        mock_font.save.assert_called_once_with(copy.content_path)
        assert result is copy
