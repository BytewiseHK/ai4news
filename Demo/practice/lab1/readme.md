# NewsAPI Services Overview

This document summarizes the available news services provided by NewsAPI (https://newsapi.org/docs/endpoints/everything).

## Everything Endpoint (`/v2/everything`)

Search through millions of articles from over 150,000 news sources and blogs. This endpoint is suitable for article discovery and analysis.

### Key Features
- Search by keywords or phrases in article title and body
- Advanced search: exact match, required/excluded words, AND/OR/NOT logic
- Restrict search to specific fields: title, description, content
- Filter by sources or domains
- Exclude specific domains
- Date range filtering (`from`, `to`)
- Language selection (ISO-639-1 codes)
- Sort by relevancy, popularity, or published date
- Pagination support (`pageSize`, `page`)

### Response Structure
- `status`: success or error
- `totalResults`: number of results available
- `articles`: array of articles, each with:
  - `source`: id and name
  - `author`, `title`, `description`, `url`, `urlToImage`, `publishedAt`, `content`

### Authentication
- Requires API key (provided in `key.md`)

### Example Usage
To access the API, use your key and make requests to the endpoint with desired parameters. See the official documentation for details.

---
This README was generated based on the documentation in `doc.md` and the API key in `key.md`.
