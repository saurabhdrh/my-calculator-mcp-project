# Contributing

Thanks for your interest in improving this project.

## How to contribute

1. Fork the repository.
2. Create a feature branch.
3. Make your changes and test them locally.
4. Open a pull request with a clear description.

## Local development

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -e .
```

Create a `.env` file with your Groq key:

```env
GROQ_API_KEY=your_key_here
GROQ_MODEL=llama-3.1-8b-instant
```

Then run:

```bash
python server.py
python client.py
```

## Code style

- Keep the code simple and readable.
- Prefer small, focused changes.
- Test the feature before opening a pull request.
