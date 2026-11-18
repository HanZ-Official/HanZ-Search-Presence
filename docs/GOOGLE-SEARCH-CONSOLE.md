# Google Search Console setup

This repository does not replace the existing Google Search Console property.

1. Keep the verified Domain property for `hanzfinance.name.ng` if it already exists.
2. Open [Google Search Console](https://search.google.com/search-console/).
3. Select the existing `hanzfinance.name.ng` property.
4. Submit `https://hanzfinance.name.ng/sitemap.xml` under Sitemaps.
5. Use URL Inspection for `https://hanzfinance.name.ng/` and request indexing after the production files are deployed.
6. Recheck sitemap status and Page indexing reports after Google has had time to crawl.

Do not create duplicate properties or remove existing verification records as part of this project.

## Important
The repository's sitemap and robots files are reference artifacts until they are deployed at the website root. A file in GitHub does not automatically become available at the HanZ domain.
