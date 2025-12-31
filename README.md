# POS Media Data Core Python Client

Lightweight helper package for authenticating against POS Media Data Core and calling its Campaigns API from Python. The library exposes two primary objects:

- `Credentials`: exchanges a username/password for a short-lived Bearer token.
- `Client`: wraps Data Core endpoints (e.g., list campaigns, fetch campaign photos) using an injected `Credentials` instance.

## Installation

```bash
pip install surquest-utils-poscore
```

## Quickstart

```python
from surquest.utils.poscore import Credentials, Client

# Create token provider
creds = Credentials(
	base_url="https://api.pos-media.example.com",
	username="your_username",
	password="your_password",
)

# Wire the authenticated client
client = Client(credentials=creds)

# 1) List campaigns
campaigns = client.list_campaigns(status="active", page=1, page_size=50)
for campaign in campaigns:
	print(campaign["id"], campaign["name"])

# 2) Get campaign photos
photos = client.get_campaign_photos(campaign_id="abc123")
for photo in photos:
	print(photo["url"], photo.get("caption"))
```

## Concepts

- Token handling: `Credentials` handles authentication and attaches the Bearer token to each request. Refresh logic is encapsulated so callers do not manually manage tokens.
- Thin HTTP wrapper: `Client` keeps endpoints small and explicit; it accepts request parameters and returns parsed JSON.

## Common Usage Patterns

- Pagination: supply `page` and `page_size` to `list_campaigns` to iterate through large result sets.
- Filtering: pass optional filters like `status`, date ranges, or brand identifiers if supported by your Data Core deployment.
- Media retrieval: `get_campaign_photos` returns metadata for campaign assets; download the file via the provided `url`.

## Error Handling

- Authentication errors: raised when credentials are invalid or tokens expire unexpectedly.
- HTTP errors: surfaced with status codes and response bodies to aid debugging; wrap calls in `try/except` as needed.

## Development

```bash
python -m venv .venv
./.venv/Scripts/activate
pip install -e .[dev]
pytest
```

## Support

Please open an issue or reach out to your POS Media administrator with endpoint-specific questions.
