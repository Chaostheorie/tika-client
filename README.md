# Tika Rest Client

[![PyPI - Version](https://img.shields.io/pypi/v/tika-client.svg)](https://pypi.org/project/tika-client)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/tika-client.svg)](https://pypi.org/project/tika-client)

---

**Table of Contents**

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Features

- Simplified: No need to worry about XML or JSON responses, downloading a Tika jar file or Python 2 leftovers
- Support for Tika 2+ only
- Based on the modern httpx library for support of all modern features
- Full support for type hinting
- Full test coverage run against an actual Tika server for multiple Python and PyPy versions

## Installation

```console
pip3 install tika-client
```

## Usage

```python3
from pathlib import Path
from tika_client import TikaClient

test_file = Path("sample.docx")


with TikaClient("http://localhost:9998) as client

    # Extract a document's metadata
    metadata = client.metadata.from_file(test_file)

    # Get the content of a document as HTML
    data = client.tika.html.parse(test_file)

    # Or as plain text
    text = client.tika.text.parse(test_file)

    # Content and metadata combined
    data = client.rmeta.text.parse(test_file)

    # The mime type can also be given
    # This allows Content-Type to be set most accurately
    text = client.tika.text.parse(test_file,
                                  "application/vnd.openxmlformats-officedocument.wordprocessingml.document")

```

## Why

Only one other library for interfacing with Tika exists that I know of. I find it too complicated, trying to handle
a lot of differing uses.

The biggest issue I have with the library is its downloading and running of a jar file if needed. To me, an
API client should only interface to the API and not try to provide functionality to start
the API as well. The user is responsible for providing the server with the Tika version they desire.

The library also provides a lot of knobs to turn, but I argue most developers will not want to configure XML as
the response type, they just want the data, already parsed.

This library attempts to provide a simpler interface, minimal lines of code and typing of the parsed response.

## License

`tika-client` is distributed under the terms of the [GPL-3.0-only](https://spdx.org/licenses/GPL-3.0-only.html) license.
