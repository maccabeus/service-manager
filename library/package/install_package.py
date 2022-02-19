from library.package.package_interface import PackageInterface
from library.package.package_config_loader import PackageConfigLoader


class InstallPackage(PackageInterface):
    """The package Instance
    """

    def set_name(self, package_name: str) -> None:
        """Set the name of the package to work on
        """
        self.__package_name = package_name

    def run_action(self) -> None:
        """The action runnable on a package instance. 
        """
        installed_package = PackageConfigLoader.load_package_info(
            self.__package_name)
        print(installed_package)
        if not installed_package or installed_package == None:
            # Install package  as new
            # install all dependencies first
            deps= installed_package.get("deps")
            if(deps)
            pass
        else:
            print("package already installed")

        return True
