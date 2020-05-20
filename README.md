# Anki Data

Generic project for my Anki flashcards.

Store data in various formats, apply templates, render markdown, use images, sounds and video clips.

All files use `utf-8` encoding.

## Setup

```powershell
python -m venv .venv
.venv\Scripts\activate.ps1

python -m pip install --upgrade pip

pip install -r requirements.txt

deactivate
```

## Generating identifiers

To generate Anki ID:

```python
import random
random.randrange(1 << 30, 1 << 31)
```

To generate GUID:

```python
import uuid
str(uuid.uuid4())
```
