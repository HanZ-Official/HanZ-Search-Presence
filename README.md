# HanZ Search Presence

Official source of truth for HanZ public brand identity and search-discovery assets.

**Public brand:** HanZ  
**Positioning:** A technology ecosystem covering finance, AI, education, business and everyday life.  
**Brand promise:** Your Money in Your Hands.  
**Growth philosophy:** Dream Bigger. Build Daily with HanZ.  
**Official website:** https://hanzfinance.name.ng/

## What this repository contains

- `brand/` — approved public identity and product facts.
- `seo/` — homepage metadata reference snippet.
- `sitemaps/` — canonical XML sitemap source.
- `crawler/` — public crawler policy source.
- `structured-data/` — Organization and WebSite JSON-LD.
- `docs/` — Search Console, deployment and factual-publishing guidance.
- `scripts/` — offline asset validation.

## Validate

Run:

```bash
python3 scripts/validate-search-assets.py
```

A GitHub Actions workflow runs this validation on pushes and pull requests.

## Important deployment boundary

This repository is the source of truth for search assets; it is not the production HanZ application and is not currently connected to the Cloudflare Worker or custom domain. Merging these files into this repository does **not** publish them at `https://hanzfinance.name.ng/`.

The sitemap and robots file must be published at the root of the existing website, and the metadata/JSON-LD must be integrated into its existing HTML document head. Follow [the deployment guide](docs/DEPLOYMENT.md). Do not change production DNS, Cloudflare security or the existing Worker as part of this repository-only change.

## Accuracy rules

Use only verified public facts. Do not invent a registered legal name, founder details, contact information, social profiles, awards, customers or regulatory status. Clearly distinguish live products from planned and in-development initiatives. See [the brand facts policy](docs/BRAND-FACTS-POLICY.md).
