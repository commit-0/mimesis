# -*- coding: utf-8 -*-

"""Binary data provider."""

from pathlib import Path
from typing import Any, Union

from mimesis.enums import (
    AudioFile,
    CompressedFile,
    DocumentFile,
    ImageFile,
    VideoFile,
)
from mimesis.providers.base import BaseProvider

__all__ = ["BinaryFile"]


class BinaryFile(BaseProvider):
    """Class for generating binary data"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize attributes.

        :param locale: Current locale.
        :param seed: Seed.
        """
        super().__init__(*args, **kwargs)
        self._data_dir = Path(__file__).parent.parent.joinpath("data", "bin")
        self._sample_name = "sample"

    class Meta:
        """Class for metadata."""

        name = "binaryfile"

    def _read_file(
        self,
        *,
        file_type: Union[
            AudioFile,
            CompressedFile,
            DocumentFile,
            ImageFile,
            VideoFile,
        ],
    ) -> bytes:
        file_type = self.validate_enum(file_type, file_type.__class__)
        file_path = self._data_dir.joinpath(f"{self._sample_name}.{file_type}")

        with open(file_path, "rb") as file:
            return file.read()

    def video(self, *, file_type: VideoFile = VideoFile.MP4) -> bytes:
        """Generates video file of given format and returns it as bytes.

        .. note:: This method accepts keyword-only arguments.

        :param file_type: File extension.
        :return: File as a sequence of bytes.
        """
        return self._read_file(file_type=file_type)

    def audio(self, *, file_type: AudioFile = AudioFile.MP3) -> bytes:
        """Generates audio file of given format and returns it as bytes.

        .. note:: This method accepts keyword-only arguments.

        :param file_type: File extension.
        :return: File as a sequence of bytes.
        """
        return self._read_file(file_type=file_type)

    def document(self, *, file_type: DocumentFile = DocumentFile.PDF) -> bytes:
        """Generates document of given format and returns it as bytes.

        .. note:: This method accepts keyword-only arguments.

        :param file_type: File extension.
        :return: File as a sequence of bytes.
        """
        return self._read_file(file_type=file_type)

    def image(self, *, file_type: ImageFile = ImageFile.PNG) -> bytes:
        """Generates image of given format and returns it as bytes.

        .. note:: This method accepts keyword-only arguments.

        :param file_type: File extension.
        :return: File as a sequence of bytes.
        """
        return self._read_file(file_type=file_type)

    def compressed(self, *, file_type: CompressedFile = CompressedFile.ZIP) -> bytes:
        """Generates compressed file of given format and returns it as bytes.

        .. note:: This method accepts keyword-only arguments.

        :param file_type: File extension.
        :return: File as a sequence of bytes.
        """
        return self._read_file(file_type=file_type)
