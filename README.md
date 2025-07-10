# Forlinx Embedded Documentation

This repository contains multiple Sphinx documentation projects for different platforms.

## Platforms supported:

- Rockchip: rk3568, rk3576, rk3588
- NXP: imx8mp, imx9352

## Features

- Each platform subfolder contains an independent Sphinx project
- Supports both reStructuredText (.rst) and Markdown (.md) files (via myst-parser)
- Uses Read the Docs theme (`sphinx_rtd_theme`)
- Automatically built and deployed to GitHub Pages with GitHub Actions

## Deployment URL pattern

The documentation will be available under:

```
https://yourname.github.io/forlinx-docs/rockchip/rk3568/
https://yourname.github.io/forlinx-docs/nxp/imx8mp/
```

## How to build locally

```bash
cd platform/rockchip/rk3568
make html
```

## How to contribute

Add or update docs under respective platform folders, commit and push to the main branch. The GitHub Actions will auto-build and deploy the docs.
