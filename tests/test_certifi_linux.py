from pathlib import Path

from certifi_linux.certifi_linux import _POSSIBLE_CERT_PATHS, contents, where


def test_where():
    cert_path = where()
    assert Path(cert_path).is_file()
    assert cert_path in _POSSIBLE_CERT_PATHS


def test_contents():
    content = contents()
    assert "BEGIN CERTIFICATE" in content
    assert "END CERTIFICATE" in content
