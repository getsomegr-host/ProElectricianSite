# ProElectricianSite

A small demo/resume website for electrician services built as a portfolio project.

Demo: https://proelectriciannow.com/RepoTest/

## Quick start

- Open `index.html` in a web browser for the static demo.
- To enable the PHP contact form (contact.php), run a local PHP server from the project root:

  php -S localhost:8000

  Then visit: http://localhost:8000/

- Alternatively for a static-only preview (no PHP):

  python -m http.server 8000

  and visit: http://localhost:8000/

## Command snippets

URL

```txt
http://localhost:8000/
```

Start local PHP server (from project root)

```powershell
php -S localhost:8000 -t .
```

If `php` is not in PATH yet, use full executable path:

```powershell
& "C:\Users\tmill\AppData\Local\Microsoft\WinGet\Packages\PHP.PHP.8.4_Microsoft.Winget.Source_8wekyb3d8bbwe\php.exe" -S localhost:8000 -t "C:\Users\tmill\OneDrive\Documents\ProElectric\ProElectricianSite"
```

Stop local server

```txt
In the terminal running the server: Ctrl + C
```

Agent/background terminal stop (Copilot tool)

```txt
kill_terminal id=7da9c555-fa73-425d-a449-fb2f46c26e04
```

## Usage

Edit `index.html`, files under `js/`, `scripts/`, and `images/` to customize the site content and assets.

## Notes

- Contact form (contact.php) requires a working PHP environment and server-side mail configuration; do not expose credentials in the repo.

## License / Reuse

Not licensed for reuse — For resume/demo only. All rights reserved by @getsomegr-host.

## Contact

Owner: @getsomegr-host
