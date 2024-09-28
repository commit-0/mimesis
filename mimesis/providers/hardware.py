"""Provides data related to hardware."""
from mimesis.datasets import CPU, CPU_CODENAMES, GENERATION, GRAPHICS, HDD_SSD, MANUFACTURERS, PHONE_MODELS, RAM_SIZES, RAM_TYPES, RESOLUTIONS, SCREEN_SIZES
from mimesis.providers.base import BaseProvider
__all__ = ['Hardware']

class Hardware(BaseProvider):
    """Class for generate data related to hardware."""

    class Meta:
        """Class for metadata."""
        name = 'hardware'

    def resolution(self) -> str:
        """Generates a random screen resolution.

        :return: Resolution of screen.

        :Example:
            1280x720.
        """
        pass

    def screen_size(self) -> str:
        """Generates a random size of screen in inch.

        :return: Screen size.

        :Example:
            13″.
        """
        pass

    def cpu(self) -> str:
        """Generates a random CPU name.

        :return: CPU name.

        :Example:
            Intel® Core i7.
        """
        pass

    def cpu_frequency(self) -> str:
        """Generates a random frequency of CPU.

        :return: Frequency of CPU.

        :Example:
            4.0 GHz.
        """
        pass

    def generation(self) -> str:
        """Generates a random generation.

        :return: Generation of something.

        :Example:
             6th Generation.
        """
        pass

    def cpu_codename(self) -> str:
        """Generates a random CPU code name.

        :return: CPU code name.

        :Example:
            Cannonlake.
        """
        pass

    def ram_type(self) -> str:
        """Generates a random RAM type.

        :return: Type of RAM.

        :Example:
            DDR3.
        """
        pass

    def ram_size(self) -> str:
        """Generates a random size of RAM.

        :return: RAM size.

        :Example:
            16GB.
        """
        pass

    def ssd_or_hdd(self) -> str:
        """Generates a random type of disk.

        :return: HDD or SSD.

        :Example:
            512GB SSD.
        """
        pass

    def graphics(self) -> str:
        """Generates a random graphics card name.

        :return: Graphics.

        :Example:
            Intel® Iris™ Pro Graphics 6200.
        """
        pass

    def manufacturer(self) -> str:
        """Generates a random manufacturer of hardware.

        :return: Manufacturer.

        :Example:
            Dell.
        """
        pass

    def phone_model(self) -> str:
        """Generates a random phone model.

        :return: Phone model.

        :Example:
            Nokia Lumia 920.
        """
        pass