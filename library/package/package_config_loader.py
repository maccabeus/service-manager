
import json
from pathlib import Path


class PackageConfigLoader():
    """Package configurations loader
    """
    @staticmethod
    def load_package_info(package_name: str, package_version: str = None, package_file_name: str = "packman.json") -> dict:
        """load package list

        Args:
            package_name (str): The name of the package to install
            package_version (str, optional): _description_. Defaults to None.
            package_file_name (str, optional): _description_. Defaults to "packman.json".
        """
        PackageConfigLoader.__package_name = package_name
        PackageConfigLoader.__version = package_version
        PackageConfigLoader.__home_path = "./"+package_file_name
        with open(PackageConfigLoader.__home_path) as installed_packages:
            package_list= json.loads(installed_packages.read())
            return package_list.get(PackageConfigLoader.__package_name)
            