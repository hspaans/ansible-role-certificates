"""Role testing files using testinfra."""

import pytest


@pytest.mark.parametrize("pkg", ["openssl"])
def test_pkg_installed(host, pkg):
    """Test if package installed."""
    package = host.package(pkg)

    assert package.is_installed


@pytest.mark.parametrize("directory", ["/etc/ssl/private"])
def test_directory_present(host, directory):
    """Test if directory is present."""
    dir = host.file(directory)

    assert dir.exists
