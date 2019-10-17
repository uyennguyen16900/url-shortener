# :link: TUrl
> A self-hosted URL shortening service built using Flask, Python and MongoDB.

Simply give the url you want to shorten and get the new shortened url based on base62 encoding.

## Project
Each url has a unique id in the database. We use this id and encode it using base62 encoding. This encoded string is stored as the short url for the original url.
