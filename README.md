# WebDump

**an fast, lightweight and free website dumper** 
Download complete websites for offline browsing with automatic asset fixing, beatifing, and instant static hosting.

[![Python](https://img.shields.io/badge/Python-3.12%2B-blue?logo=python&logoColor=white&style=for-the-badge)](https://www.python.org)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-green.svg?style=for-the-badge)](https://www.gnu.org/licenses/gpl-3.0)
[![Code size](https://img.shields.io/github/languages/code-size/Alangopro/WebDump?style=for-the-badge)](#)

[![GitHub stars](https://img.shields.io/github/stars/Alangopro/WebDump?style=for-the-badge)](https://github.com/Alangopro/WebDump/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Alangopro/WebDump?style=for-the-badge)](https://github.com/Alangopro/WebDump/network/members)
[![GitHub issues](https://img.shields.io/github/issues/Alangopro/WebDump?style=for-the-badge)](https://github.com/Alangopro/WebDump/issues)
[![Contributions](https://img.shields.io/badge/contributions-open-brightgreen.svg?style=for-the-badge)](https://github.com/Alangopro/WebDump/issues)


[![Discord](https://img.shields.io/badge/Discord-%235865F2.svg?style=for-the-badge&logo=discord&logoColor=white)](https://dc.queenmc.pl/)
[![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white)](https://feds.lol/Kamerzystanasyt)
[![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://feds.lol/Kamerzystanasyt)

## Features

| Feature                 | Description                                      |
|-------------------------|--------------------------------------------------|
| `Blazing-fast recursive downloading` | with concurrent requests            |
| `Automatic asset rewriting`          | fixes broken links for perfect offline experience  
| `Built-in static server`             | serve archived sites instantly with one flag  
| `HTML/CSS/JS beautification`         | (optional, powered by jsbeautifier & css-html-js-minify)  
| `Intelligent performance optimizations` | (minification, compression, image optimization)  
| `Single-file executable`             | no dependencies beyond standard Python  
| `Cross-platform`                     | works on Windows, macOS, and Linux  

## Preview

![WebDump in action](https://github.com/user-attachments/assets/39c31fb7-9880-4913-9c7f-83e80a2962e7)

## Usage

```bash
python WDumper.py <url> [options]
```

| Option                  | Description                                      |
|-------------------------|--------------------------------------------------|
| `-o, --output`          | Output directory (default: domain name)          |
| `--serve`               | Start local server after download                |
| `--port`                | Port for local server (default: 8000)            |
| `--beautify`            | Beautify HTML/CSS/JS files                       |
| `--minify`              | Minify assets for smaller size                   |
| `--threads`             | Number of concurrent threads (default: 20)       |
| `--delay`               | Delay between requests in seconds                |
| `--timeout`             | Request timeout                                  |
| `-q, --quiet`           | Suppress progress output                         |

Full help:
```bash
python WDumper.py --help
```

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.  
See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines (coming soon).


This project is licensed under the **GNU General Public License v3.0** see the [LICENSE](LICENSE) file for details.

---
