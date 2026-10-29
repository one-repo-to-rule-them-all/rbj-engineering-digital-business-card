# RBJ Engineering Services — Digital Business Card

Static, single-page digital business card for Rodolfo Baez Jr.

**Live:** https://card.rbjengineeringservices.com/

## Files

| File | Purpose |
|---|---|
| `index.html` | The card: inline CSS, no JavaScript, no build step. Includes link-preview (Open Graph) tags. |
| `rodolfo-baez-jr.vcf` | vCard 3.0 behind the **Save Contact** button. Keep it in sync with `index.html`. |
| `profile.jpg` | 512px card image, also used as the link-preview image. |
| `favicon.png`, `apple-touch-icon.png` | Browser tab and iOS home-screen icons. |
| `RBJ_Business_profile_image.png` | 1024px source image. Not served by the page. Regenerate the files above from it. |
| `CNAME` | Custom domain for GitHub Pages. |

## Deployment

GitHub Pages, deployed from the `main` branch root (classic branch deploy, no workflow). A push to `main` is live in about a minute.

- DNS: `card.rbjengineeringservices.com` has a CNAME record pointing to `one-repo-to-rule-them-all.github.io`.
- HTTPS: Let's Encrypt certificate managed and auto-renewed by GitHub; "Enforce HTTPS" is on.
- The old `one-repo-to-rule-them-all.github.io/rbj-engineering-digital-business-card/` URL 301-redirects to the custom domain.

The card (and its certificate renewal) depends on the domain staying registered and that CNAME record staying in place.

## Local preview

```sh
python -m http.server 8000
```

Then open http://localhost:8000.
