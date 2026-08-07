import os
import sys
import json
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, IntPrompt
from rich.table import Table
from rich import print as rprint
from rich.align import Align
from rich.text import Text

from core.port_scanner import PortScanner
from core.password_analyzer import PasswordAnalyzer
from core.file_crypto import FileCrypto
from core.hash_toolkit import HashToolkit
from core.log_analyzer import LogAnalyzer
from core.ssl_checker import SSLChecker
from core.dns_recon import DNSRecon

# Phase 1 modules
from core.data_encoder import DataEncoder
from core.pwd_validator import PasswordValidator
from core.ssh_keygen import SSHKeyGenerator
from core.jwt_inspector import JWTInspector

console = Console()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_banner():
    banner_text = """
  ____      _                 ____               _____           _ _    _ _   
 / ___|   _| |__   ___ _ __  / ___|  ___  ___   |_   _|__   ___ | | | _(_) |_ 
| |  | | | | '_ \ / _ \ '__| \___ \ / _ \/ __|    | |/ _ \ / _ \| | |/ / | __|
| |__| |_| | |_) |  __/ |     ___) |  __/ (__     | | (_) | (_) | |   <| | |_ 
 \____\__,_|_.__/ \___|_|    |____/ \___|\___|    |_|\___/ \___/|_|_|\_\_|\__|
    """
    
    panel = Panel(
        Align.center(
            Text(banner_text, style="bold cyan") + 
            Text("\n\nAn Advanced Defensive Security Toolkit", style="bold white") +
            Text("\nDeveloped by: Roshab Bhandari", style="bold green")
        ),
        border_style="cyan",
        title="[bold yellow]v2.0[/bold yellow]",
        padding=(1, 2)
    )
    console.print(panel)
    console.print()

def main_menu():
    table = Table(show_header=False, box=None, padding=(0, 2))
    table.add_column(style="bold cyan")
    table.add_column(style="white")
    
    table.add_row("[1]", "Network & Reconnaissance")
    table.add_row("[2]", "Cryptography & Identity Management")
    table.add_row("[3]", "Endpoint Security & Forensics (Coming Soon)")
    table.add_row("[4]", "Log Analysis & Incident Response (Coming Soon)")
    table.add_row("[5]", "Compliance, Cloud & Configuration (Coming Soon)")
    table.add_row("[0]", "Exit")
    
    console.print(Panel(table, title="[bold green]Main Categories[/bold green]", border_style="green", expand=False))

def menu_network():
    while True:
        clear_screen()
        show_banner()
        table = Table(show_header=False, box=None, padding=(0, 2))
        table.add_column(style="bold cyan")
        table.add_column(style="white")
        table.add_row("[1]", "Port Scanner (Threaded + Banner Grabbing)")
        table.add_row("[2]", "DNS / Subdomain Recon (Passive)")
        table.add_row("[3]", "SSL/TLS Certificate Checker")
        table.add_row("[0]", "Back to Main Menu")
        
        console.print(Panel(table, title="[bold green]Network & Reconnaissance[/bold green]", border_style="green", expand=False))
        choice = Prompt.ask("\n[bold yellow]Select a tool[/bold yellow]", choices=["1", "2", "3", "0"])
        
        if choice == "0":
            break
        elif choice == "1":
            target = Prompt.ask("[bold cyan]Enter target IP or Domain[/bold cyan]")
            port_range = IntPrompt.ask("[bold cyan]Enter max port to scan (e.g. 1024)[/bold cyan]", default=1024)
            console.print(f"\n[bold yellow]Scanning {target}...[/bold yellow]")
            scanner = PortScanner(target, range(1, port_range + 1))
            results = scanner.run()
            if results:
                t = Table(title="Open Ports")
                t.add_column("Port", style="cyan")
                t.add_column("Banner", style="magenta")
                for p, b in results: t.add_row(str(p), b)
                console.print(t)
            else:
                console.print("[bold red]No open ports found.[/bold red]")
        elif choice == "2":
            domain = Prompt.ask("[bold cyan]Enter domain[/bold cyan]")
            res = DNSRecon(domain).run()
            for rtype, records in res.items():
                if records:
                    console.print(f"\n[bold yellow]{rtype} Records:[/bold yellow]")
                    for rec in records: console.print(f" - {rec}")
                else:
                    console.print(f"\n[bold yellow]{rtype} Records:[/bold yellow] [dim]None found[/dim]")
        elif choice == "3":
            host = Prompt.ask("[bold cyan]Enter hostname[/bold cyan]")
            res = SSLChecker(host).check()
            if "error" in res:
                console.print(f"[bold red]Error: {res['error']}[/bold red]")
            else:
                t = Table(title=f"SSL/TLS Info for {host}")
                t.add_column("Property", style="cyan")
                t.add_column("Value", style="green")
                for k, v in res.items(): t.add_row(k.capitalize().replace("_", " "), str(v))
                console.print(t)
        Prompt.ask("\n[dim]Press Enter to continue...[/dim]")

def menu_crypto():
    while True:
        clear_screen()
        show_banner()
        table = Table(show_header=False, box=None, padding=(0, 2))
        table.add_column(style="bold cyan")
        table.add_column(style="white")
        table.add_row("[1]", "Password Strength Analyzer (Entropy + Heuristics)")
        table.add_row("[2]", "File Encryptor / Decryptor (AES-256)")
        table.add_row("[3]", "Hash Toolkit (Generate / Identify)")
        table.add_row("[4]", "Data Encoder / Decoder (Base64, Hex, Binary, URL)")
        table.add_row("[5]", "Password Complexity Policy Validator")
        table.add_row("[6]", "SSH Key Pair Generator (RSA / Ed25519)")
        table.add_row("[7]", "JWT Token Inspector")
        table.add_row("[0]", "Back to Main Menu")
        
        console.print(Panel(table, title="[bold green]Cryptography & Identity Management[/bold green]", border_style="green", expand=False))
        choice = Prompt.ask("\n[bold yellow]Select a tool[/bold yellow]", choices=["1", "2", "3", "4", "5", "6", "7", "0"])
        
        if choice == "0":
            break
        elif choice == "1":
            pwd = Prompt.ask("[bold cyan]Enter password to analyze[/bold cyan]", password=True)
            res = PasswordAnalyzer(pwd).analyze()
            console.print(f"\n[bold white]Entropy:[/bold white] [cyan]{res['entropy']} bits[/cyan]")
            console.print(f"[bold white]Strength:[/bold white] [green]{res['strength']}[/green]")
            if res['warnings']:
                console.print("\n[bold red]Warnings:[/bold red]")
                for w in res['warnings']: console.print(f" - {w}")
        elif choice == "2":
            sub_choice = Prompt.ask("[bold cyan]Do you want to (E)ncrypt or (D)ecrypt?[/bold cyan]", choices=["E", "e", "D", "d"])
            file_path = Prompt.ask("[bold cyan]Enter file path[/bold cyan]")
            pwd = Prompt.ask("[bold cyan]Enter password[/bold cyan]", password=True)
            try:
                if sub_choice.upper() == 'E':
                    out = FileCrypto(pwd).encrypt_file(file_path)
                    console.print(f"[bold green]Encrypted to {out}[/bold green]")
                else:
                    out = FileCrypto(pwd).decrypt_file(file_path)
                    console.print(f"[bold green]Decrypted to {out}[/bold green]")
            except Exception as e: console.print(f"[bold red]Error: {e}[/bold red]")
        elif choice == "3":
            sub_choice = Prompt.ask("[bold cyan]Do you want to (G)enerate or (I)dentify a hash?[/bold cyan]", choices=["G", "g", "I", "i"])
            if sub_choice.upper() == 'G':
                text = Prompt.ask("[bold cyan]Enter string to hash[/bold cyan]")
                algo = Prompt.ask("[bold cyan]Algorithm[/bold cyan]", default="sha256")
                console.print(f"[bold green]Hash:[/bold green] {HashToolkit.hash_string(text, algo)}")
            else:
                h = Prompt.ask("[bold cyan]Enter hash to identify[/bold cyan]")
                console.print(f"[bold green]Identification:[/bold green] {HashToolkit.identify_hash(h)}")
        elif choice == "4":
            mode = Prompt.ask("[bold cyan](E)ncode or (D)ecode?[/bold cyan]", choices=["E", "e", "D", "d"])
            fmt = Prompt.ask("[bold cyan]Format[/bold cyan]", choices=["base64", "hex", "binary", "url", "rot13"])
            data = Prompt.ask("[bold cyan]Enter data[/bold cyan]")
            if mode.upper() == 'E':
                res = DataEncoder.encode(data, fmt)
            else:
                res = DataEncoder.decode(data, fmt)
            console.print(f"\n[bold green]Result:[/bold green] {res}")
        elif choice == "5":
            pwd = Prompt.ask("[bold cyan]Enter password to validate[/bold cyan]", password=True)
            res = PasswordValidator.validate(pwd)
            if res["is_valid"]:
                console.print("[bold green]Password meets all complexity requirements![/bold green]")
            else:
                console.print("[bold red]Password failed complexity policy:[/bold red]")
                for issue in res["issues"]:
                    console.print(f" - {issue}")
        elif choice == "6":
            algo = Prompt.ask("[bold cyan]Algorithm[/bold cyan]", choices=["rsa", "ed25519"], default="ed25519")
            out_dir = Prompt.ask("[bold cyan]Output directory[/bold cyan]", default="keys")
            if algo == "rsa":
                res = SSHKeyGenerator.generate_rsa(output_dir=out_dir)
            else:
                res = SSHKeyGenerator.generate_ed25519(output_dir=out_dir)
            if "error" in res:
                console.print(f"[bold red]Error:[/bold red] {res['error']}")
            else:
                console.print(f"[bold green]Keys generated successfully:[/bold green]\n - Private: {res['private_key']}\n - Public: {res['public_key']}")
        elif choice == "7":
            token = Prompt.ask("[bold cyan]Enter JWT token[/bold cyan]")
            res = JWTInspector.inspect(token)
            if res.get("error"):
                console.print(f"[bold red]Error parsing JWT:[/bold red] {res['error']}")
            else:
                console.print("\n[bold yellow]Header:[/bold yellow]")
                console.print(json.dumps(res["header"], indent=2))
                console.print("\n[bold yellow]Payload:[/bold yellow]")
                console.print(json.dumps(res["payload"], indent=2))
                
        Prompt.ask("\n[dim]Press Enter to continue...[/dim]")

def main():
    while True:
        clear_screen()
        show_banner()
        main_menu()
        
        choice = Prompt.ask("\n[bold yellow]Select a category[/bold yellow]", choices=["1", "2", "3", "4", "5", "0"])
        
        if choice == "1":
            menu_network()
        elif choice == "2":
            menu_crypto()
        elif choice in ["3", "4", "5"]:
            console.print("[bold red]This module category is currently under development (Phase 2-5).[/bold red]")
            Prompt.ask("\n[dim]Press Enter to continue...[/dim]")
        elif choice == "0":
            console.print("[bold green]Goodbye![/bold green]")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[bold red]Exiting...[/bold red]")
        sys.exit(0)
