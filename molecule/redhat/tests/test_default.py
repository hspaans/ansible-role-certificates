"""Role testing files using testinfra."""

import pytest


@pytest.mark.parametrize("pkg", ["openssl"])
def test_pkg_installed(host, pkg):
    """Test if package installed."""
    package = host.package(pkg)

    assert package.is_installed


@pytest.mark.parametrize("directory", ["/etc/pki/tls/private", "/etc/pki/tls/private/www.example.org"])
def test_directory_present(host, directory):
    """Test if directory is present."""
    item = host.file(directory)

    assert item.exists


@pytest.mark.parametrize("directory", ["/etc/pki/tls/private/www.example.org"])
def test_file_present(host, directory):
    """Test if directory is present."""
    item_certs = host.file(file+"/certs.pem")
    item_chain = host.file(file+"/chain.pem")

    assert item_certs.exists
    assert item_chain.exists
