# certifi-linux

[![PyPI - Version](https://img.shields.io/pypi/v/certifi-linux.svg)](https://pypi.org/project/certifi-linux)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/certifi-linux.svg)](https://pypi.org/project/certifi-linux)

-----

**Table of Contents**

- [About](#about)
- [Installation](#installation)
- [Usage](#usage)
- [Compatibility](#compatibility)
- [Implementation](#implementation)
- [Related Projects](#related-projects)
- [Credits](#credits)
- [License](#license)

## About

**WHAT:** `certifi-linux` wraps [certifi](https://pypi.org/project/certifi/), but instead of distributing a certificate like `certifi` does, it uses the Linux system trust store.

**WHY?** The [requests](https://pypi.org/project/requests/) module depends on `certifi` and uses it for TLS. `certifi` distributes the collection of root certificates provided by Mozilla for Python deployments. In some cases, especially in an enterprise setup it is necessary to use the certificates which are shipped with the OS.

## Installation

`certifi-linux` is purposed for **Linux**! For Windows take a look at [pip-system-certs](https://gitlab.com/alelec/pip-system-certs).

```console
pip install certifi-linux
```

## Usage

`certifi-linux` just needs to be installed. Afterwards `certifi.where()` or `$ python3 -m certifi` will return the path to the system store. Hence all dependent projects like `requests` will do as well.

## Compatibility

I am trying to keep tests up to date with [endoflife](https://endoflife.date/).

Tested distros are:

- alpine:3,
- ubuntu:focal, ubuntu:jammy, ubuntu:noble,
- debian:buster, debian:bullseye, debian:bookworm,
- fedora:33, fedora:>=34
- centos:stream9,
- (manually) rhel:37, rhel:38

Yet untested: Arch, Slackware, OpenWRT, FreeBSD, SUSE, gentoo, ...

## Implementation

`certifi-linux` monkey patches `certif.where` and `certifi.contents` by using [wrapt](https://pypi.org/project/wrapt/). When called, it searches in the defined set of possible certificate bundle paths for a match.

### Cert Path Candidates

Tested: yes✅, no❌

| Cert Bundle Path                     | Linux Distribution                                                               |
| ------------------------------------ | -------------------------------------------------------------------------------- |
| `/etc/ssl/cert.pem`                  | fedora >= 34✅, RHEL✅, alpine✅, centOS Stream✅, Arch❌, OpenWRT❌, FreeBSD❌ |
| `/etc/pki/tls/cert.pem`              | fedora <= 33✅                                                                  |
| `/etc/ssl/certs/ca-certificates.crt` | Debian✅, Ubuntu✅                                                               |
| `/etc/ssl/ca-bundle.pem`             | openSUSE❌                                                                       |

## Related Projects

The idea behind `certifi-linux` is the same as behind [certifi-system-store](https://github.com/tiran/certifi-system-store/). `certifi-system-store` replaces the dist-info of certifi with its own dist-info. This approach needs a specific order of installation for a succesful patch. When installed as a dependency among a whole set of dependencies this is hard to ensure and replacing dist-infos can mess up virtual environments.

[pip-system-certs](https://gitlab.com/alelec/pip-system-certs) solves the same problem with a different approach. It monkey patches the `requests.adapters.HTTPAdapter` and uses `ssl.create_default_context` to load the OS certs. This works fine on Windows but has shown limitations on Linux as it does not work in some cases.

Viewed from the outside, [certifi-debian](https://pypi.org/project/certifi-debian/) is doing the exact same thing like `certifi-linux` but just for debian. [certifi-system-store-wrapper](https://pypi.org/project/certifi-system-store-wrapper/) also does the same but with the necessity to set an environment variable.

## Credits

Credits go to the developers of `certifi-system-store` and `pip-system-certs` as `certifi-linux` is highly influenced by these two projects.

## License

`certifi-linux` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
