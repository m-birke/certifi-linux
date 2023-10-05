from pathlib import Path

_POSSIBLE_CERT_PATHS = [
    "/etc/ssl/cert.pem",  # Alpine, Fedora
    "/etc/ssl/certs/ca-certificates.crt",  # Debian
    "/etc/pki/tls/cert.pem",  # Fedora
    "/etc/ssl/ca-bundle.pem",  # SUSE
]
_FOUND_CERT_PATH: str = ""


def where() -> str:
    global _FOUND_CERT_PATH  # noqa: PLW0603

    if _FOUND_CERT_PATH:
        return _FOUND_CERT_PATH

    for possible_cert_path in _POSSIBLE_CERT_PATHS:
        if Path(possible_cert_path).is_file():
            _FOUND_CERT_PATH = possible_cert_path
            return _FOUND_CERT_PATH

    error_msg = f"None of the following cert paths could be found: {', '.join(_POSSIBLE_CERT_PATHS)}"
    raise FileNotFoundError(error_msg)


def contents() -> str:
    cert_path = Path(where())

    with cert_path.open(encoding="utf-8") as file:
        content = file.read()

    return content
