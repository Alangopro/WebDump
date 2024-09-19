import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import signal
import time
import threading
import pathlib
import shutil
import argparse
import http.server
import socketserver
import pyfiglet
import colorama
os.system("title WEB DUMP - 1.0 & mode con cols=150 lines=26 & cls")

print(f"""
[38;2;255;5;0m



                               ▄█     █▄     ▄████████ ▀█████████▄       ████████▄  ███    █▄    ▄▄▄▄███▄▄▄▄      ▄███████▄
                              ███     ███   ███    ███   ███    ███      ███   ▀███ ███    ███ ▄██▀▀▀███▀▀▀██▄   ███    ███
                              ███     ███   ███    █▀    ███    ███      ███    ███ ███    ███ ███   ███   ███   ███    ███
                              ███     ███  ▄███▄▄▄      ▄███▄▄▄██▀       ███    ███ ███    ███ ███   ███   ███   ███    ███
                              ███     ███ ▀▀███▀▀▀     ▀▀███▀▀▀██▄       ███    ███ ███    ███ ███   ███   ███ ▀█████████▀ 
                              ███     ███   ███    █▄    ███    ██▄      ███    ███ ███    ███ ███   ███   ███   ███       
                              ███ ▄█▄ ███   ███    ███   ███    ███      ███   ▄███ ███    ███ ███   ███   ███   ███       
                               ▀███▀███▀    ██████████ ▄█████████▀       ████████▀  ████████▀   ▀█   ███   █▀   ▄████▀      

                                                                    By: Kamerzystanasyt
                                                                    
                                                                    
                                                                    
                                                                 Press any key to Continue
[0m
""")
os.system("pause > nul")


def signal_handler(sig, frame):
    print("\nInterrupted by user. Exiting...")
    exit(0)

signal.signal(signal.SIGINT, signal_handler)

def delete_folder(folder_path):
    try:
        shutil.rmtree(folder_path)
    except Exception as e:
        print(f"Error deleting folder: {e}")

def scrape_website(url, castify=False, antifont=False, bf=False, nosocal=False, noshit=False):
    folder_name = urlparse(url).netloc
    folder_path = os.path.join(os.getcwd(), folder_name)

    if os.path.exists(folder_path):
        print("Folder already exists. Deleting...")
        threading.Thread(target=delete_folder, args=(folder_path,)).start()
        time.sleep(2)

    os.makedirs(folder_path, exist_ok=True)

    try:
        response = requests.get(url, timeout=30)
    except requests.exceptions.RequestException as e:
        print(f"Error accessing website: {e}")
        return

    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    html_filename = 'index.html'
    html_filepath = os.path.join(folder_path, html_filename)
    with open(html_filepath, 'w', encoding='utf-8') as f:
        if castify:
            for tag in soup.find_all(['link', 'script', 'img']):
                if tag.get('href') or tag.get('src'):
                    link = tag.get('href') or tag.get('src')
                    if link.startswith(url):
                        link = link.replace(url, '/')
                    tag['href'] = link
                    tag['src'] = link
        if bf:
            html_content = soup.prettify()
        f.write(html_content)
    print(f"DUMPING | 0/1 | File: {html_filename}")

    links = []
    for tag in soup.find_all(['link', 'script', 'img']):
        if tag.get('href') or tag.get('src'):
            link = tag.get('href') or tag.get('src')
            if link.startswith('/'):
                link = urljoin(url, link)
            links.append(link)

    for i, link in enumerate(links):
        print(f"Link: {link}")
        filename = os.path.basename(urlparse(link).path)
        print(f"Filename: {filename}")
        if not filename:
            filename = 'index.html'
        dir_path = os.path.dirname(urlparse(link).path)
        if dir_path:
            dir_path = dir_path.strip('/')
            folder_path_rel = pathlib.Path(folder_path) / pathlib.Path(*dir_path.split('/'))
            print(f"Dir path: {dir_path}")
            folder_path_rel.mkdir(parents=True, exist_ok=True)
        else:
            folder_path_rel = pathlib.Path(folder_path)

        filepath = os.path.join(str(folder_path_rel), filename)

        print(f"DUMPING | {i+1}/{len(links)} | File: {filename}")

        try:
            response = requests.get(link, stream=True, timeout=30)
            with open(filepath, 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
        except requests.exceptions.RequestException as e:
            print(f"Error downloading {filename}: {e}")

    if nosocal:
        for tag in soup.find_all('a'):
            if tag.get('href') and not tag.get('href').startswith('/'):
                tag.decompose()
        with open(html_filepath, 'w', encoding='utf-8') as f:
            f.write(str(soup))

    if antifont:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith(('.woff', '.woff2', '.ttf', '.otf')):
                    os.remove(os.path.join(root, file))

    print(f"Dumped website to folder {folder_name}")

def autohost(folder_path, port=8000):
    os.chdir(folder_path)
    with socketserver.TCPServer(("", port), http.server.SimpleHTTPRequestHandler) as httpd:
        print(f"Serving at port {port}")
        print(f"Open http://localhost:{port} in your browser to view the website.")
        httpd.serve_forever()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Web scraper and autohost")
    parser.add_argument("url", help="The URL of the website to scrape")
    parser.add_argument("--castify", action="store_true", help="Replace official links to assets with localhost links")
    parser.add_argument("--autohost", action="store_true", help="Automatically host the website after scraping")
    parser.add_argument("--timeout", type=int, default=30, help="Timeout in seconds for requests")
    parser.add_argument("--antifont", action="store_true", help="Remove all font files")
    parser.add_argument("--bf", action="store_true", help="Beautify the HTML, CSS, and JS files")
    parser.add_argument("--nosocal", action="store_true", help="Remove all other page links from the index.html")
    parser.add_argument("--noshit", action="store_true", help="Run on full CPU threads and other resources")
    parser.add_argument("--port", type=int, default=8000, help="Port number for autohost")
    args = parser.parse_args()

    scrape_website(args.url, castify=args.castify, antifont=args.antifont, bf=args.bf, nosocal=args.nosocal, noshit=args.noshit)

    if args.autohost:
        folder_name = urlparse(args.url).netloc
        folder_path = os.path.join(os.getcwd(), folder_name)
        autohost(folder_path, port=args.port)
