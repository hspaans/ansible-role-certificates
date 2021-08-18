"""Role testing files using testinfra."""

import pytest


@pytest.mark.parametrize("pkg", ["openssl"])
def test_pkg_installed(host, pkg):
    """Test if package installed."""
    package = host.package(pkg)

    assert package.is_installed


@pytest.mark.parametrize("directory",                         [
    "/etc/pki/tls/private",
    "/etc/pki/tls/private/www.example.org"
])
def test_directory_present(host, directory):
    """Test if directory is present."""
    item = host.file(directory)

    assert item.exists


@pytest.mark.parametrize("directory, file", [
    ("/etc/pki/tls/private/www.example.org", "cert.pem"),
    ("/etc/pki/tls/private/www.example.org", "chain.pem"),
    ("/etc/pki/tls/private/www.example.org", "fullchain.pem"),
    ("/etc/pki/tls/private/www.example.org", "privkey.pem")
])
def test_file_present(host, directory, file):
    """Test if directory is present."""
    item = host.file(directory+"/"+file)

    assert item.exists
