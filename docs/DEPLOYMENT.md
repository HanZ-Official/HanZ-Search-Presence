# Deployment plan

## Current production architecture
The public website is `https://hanzfinance.name.ng/`. Its application is already hosted separately from this repository.

## Safe deployment sequence
1. Review the files in this repository.
2. Integrate the approved homepage metadata and JSON-LD into the existing HanZ website's document head.
3. Publish the sitemap as `/sitemap.xml` and crawler instructions as `/robots.txt` at the domain root using the existing hosting/deployment pipeline.
4. Verify both URLs return HTTP 200 with the correct content type and no unexpected challenge, redirect loop or HTML error page.
5. Validate structured data and canonical URL.
6. Submit the sitemap in the existing Google Search Console property and Bing Webmaster Tools.

## Deployment boundary
This repository is not currently configured with Cloudflare Pages, a Pages project, or a deployment credential. Do not claim the live domain has been deployed from this repository. Do not change DNS, Cloudflare security, the existing Worker, or production application settings without an explicit deployment plan and verified access.

## Rollback
Keep the previous production files and deployment revision available. If a new metadata or crawler file causes problems, restore the previous version through the existing application deployment pipeline.
