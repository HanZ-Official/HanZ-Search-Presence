#!/usr/bin/env python3
"""Basic offline validation for HanZ search-presence assets."""
from pathlib import Path
import json
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
errors = []

def load_json(path):
    try:
        return json.loads((ROOT / path).read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"{path}: {exc}")
        return None

identity = load_json("brand/identity.json")
organization = load_json("brand/organization.json")
products = load_json("brand/products.json")
load_json("structured-data/organization.jsonld")
load_json("structured-data/website.jsonld")

if identity and identity.get("brandName") != "HanZ":
    errors.append("brand/identity.json: brandName must be HanZ")

if organization and organization.get("name") != "HanZ":
    errors.append("brand/organization.json: name must be HanZ")

if products:
    for product in products.get("products", []):
        if product.get("status") in {"Planned", "In development"} and product.get("publicUrl"):
            errors.append(f"{product.get('name')}: planned/in-development product must not have a public URL")

try:
    sitemap = ET.parse(ROOT / "sitemaps/sitemap.xml")
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    locs = [node.text for node in sitemap.findall(".//sm:loc", ns)]
    if not locs:
        errors.append("sitemaps/sitemap.xml: no URLs found")
    if any(not url or not url.startswith("https://hanzfinance.name.ng/") for url in locs):
        errors.append("sitemaps/sitemap.xml: URLs must use the canonical HanZ HTTPS domain")
except Exception as exc:
    errors.append(f"sitemaps/sitemap.xml: {exc}")

robots = (ROOT / "crawler/robots.txt").read_text(encoding="utf-8")
if "Sitemap: https://hanzfinance.name.ng/sitemap.xml" not in robots:
    errors.append("crawler/robots.txt: canonical sitemap declaration missing")

if errors:
    print("VALIDATION FAILED")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("HanZ search assets: validation passed.")
