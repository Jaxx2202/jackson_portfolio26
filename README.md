# Marline A. Jackson — Portfolio Site

This folder is a ready-to-publish static site: your portfolio page plus three gated case studies.

## What's inside

```
index.html                          <- your portfolio (open this first)
case-studies/jump.html              <- Czarnowski, "The JUMP Campaign"     access code: cz11
case-studies/automationcon.html     <- B&R, "AutomationCON 2019"          access code: br19
case-studies/mastermind.html        <- automotiveMastermind, NADA Show    access code: am24
```

Every file is fully self-contained (all styling, fonts, and photos are baked into the HTML), so this folder is the entire site. Nothing else needs to be installed or built.

The portfolio's "Read the Full Case Study" links point to the case study files using relative paths, so as long as this folder structure stays intact, everything will keep working wherever you host it, GitHub Pages or otherwise.

## Put this on GitHub Pages

1. **Create a repository.** Go to [github.com/new](https://github.com/new), give it a name (for example `portfolio`), set it to Public (GitHub Pages on a free account requires a public repo), and create it. Don't add a README, .gitignore, or license when prompted, since you're uploading your own files.

2. **Upload the files.** On your new repo's page, click **Add file → Upload files**. Drag in `index.html`, `README.md`, and the whole `case-studies` folder (drag the folder itself; GitHub preserves the folder structure). Scroll down and click **Commit changes**.

3. **Turn on GitHub Pages.** In the repo, go to **Settings → Pages** (left sidebar, under "Code and automation"). Under **Build and deployment → Source**, choose **Deploy from a branch**. Under **Branch**, choose `main` and `/ (root)`, then click **Save**.

4. **Wait a minute, then find your link.** GitHub takes a minute or two to publish. Refresh the **Settings → Pages** screen and it will show your live URL, something like:
   `https://<your-username>.github.io/<repo-name>/`

   That URL loads `index.html`, your portfolio. The case studies live at:
   - `https://<your-username>.github.io/<repo-name>/case-studies/jump.html`
   - `https://<your-username>.github.io/<repo-name>/case-studies/automationcon.html`
   - `https://<your-username>.github.io/<repo-name>/case-studies/mastermind.html`

## Updating later

To change anything, edit the file locally and re-upload it through **Add file → Upload files** again (GitHub will ask to confirm you're replacing the existing file), or use `git` if you're comfortable with the command line. GitHub Pages redeploys automatically within a minute or two of any change on the branch you selected.

## Access codes

Each case study is gated behind a simple client-side password screen, meant to keep casual visitors out, not to secure sensitive data (anyone who views the page source can find the code). Share the relevant code only with the specific employer or client you want reviewing that case study:

- Czarnowski / JUMP Campaign: `cz11`
- B&R / AutomationCON: `br19`
- automotiveMastermind / NADA: `am24`
