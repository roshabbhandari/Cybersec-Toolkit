import os
import sys
import json
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, IntPrompt
from rich.table import Table
from rich.align import Align
from rich.text import Text

from core.port_scanner import PortScanner
from core.password_analyzer import PasswordAnalyzer
from core.file_crypto import FileCrypto
from core.hash_toolkit import HashToolkit
from core.log_analyzer import LogAnalyzer
from core.ssl_checker import SSLChecker
from core.dns_recon import DNSRecon
from core.data_encoder import DataEncoder
from core.pwd_validator import PasswordValidator
from core.ssh_keygen import SSHKeyGenerator
from core.jwt_inspector import JWTInspector
from core.system_audit import SystemAudit
from core.integrity_checker import IntegrityChecker
from core.security_headers import SecurityHeaders

console = Console()

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def pause():
    Prompt.ask("\n[dim]Press Enter to continue...[/dim]", default="")

def show_banner():
    banner = r'''  ____      _                 ____               _____           _ _    _ _
 / ___|   _| |__   ___ _ __  / ___|  ___  ___   |_   _|__   ___ | | | _(_) |_
| |  | | | | '_ \ / _ \ '__| \___ \ / _ \/ __|    | |/ _ \ / _ \| | |/ / | __|
| |__| |_| | |_) |  __/ |     ___) |  __/ (__     | | (_) | (_) | |   <| | |_
 \____\__,_|_.__/ \___|_|    |____/ \___|\___|    |_|\___/ \___/|_|_|\_\_|\__|'''
    panel = Panel(
        Align.center(
            Text(banner, style="bold cyan")
            + Text("\n\nAdvanced Defensive Security Toolkit", style="bold white")
            + Text("\nDeveloped by: Roshab Bhandari", style="bold green")
        ),
        border_style="cyan",
        title="[bold yellow]v2.1[/bold yellow]",
        padding=(1, 2)
    )
    console.print(panel)

def show_menu(title, items):
    table = Table(show_header=False, box=None, padding=(0, 2))
    table.add_column(style="bold cyan")
    table.add_column(style="white")
    for key, label in items:
        table.add_row(f"[{key}]", label)
    console.print(Panel(table, title=f"[bold green]{title}[/bold green]", border_style="green", expand=False))

def menu_network():
    while True:
        clear_screen(); show_banner()
        show_menu("Network & Reconnaissance", [("1", "Port Scanner (Threaded + Banner Grabbing)"), ("2", "DNS / Subdomain Recon (Passive)"), ("3", "SSL/TLS Certificate Checker"), ("0", "Back")])
        choice = Prompt.ask("\n[bold yellow]Select a tool[/bold yellow]", choices=["1", "2", "3", "0"])
        if choice == "0": return
        if choice == "1":
            target = Prompt.ask("[cyan]Enter target IP or Domain[/cyan]")
            maximum = IntPrompt.ask("[cyan]Maximum port[/cyan]", default=1024)
            results = PortScanner(target, range(1, maximum + 1)).run()
            table = Table(title="Open Ports"); table.add_column("Port"); table.add_column("Banner")
            for port, banner in results or []: table.add_row(str(port), str(banner))
            console.print(table if results else "[yellow]No open ports found.[/yellow]")
        elif choice == "2":
            domain = Prompt.ask("[cyan]Enter domain[/cyan]")
            for record_type, records in DNSRecon(domain).run().items():
                console.print(f"\n[bold yellow]{record_type}[/bold yellow]")
                for record in records: console.print(f" - {record}")
        elif choice == "3":
            host = Prompt.ask("[cyan]Enter hostname[/cyan]")
            result = SSLChecker(host).check()
            if "error" in result: console.print(f"[red]{result['error']}[/red]")
            else:
                table = Table(title=f"SSL/TLS: {host}"); table.add_column("Property"); table.add_column("Value")
                for key, value in result.items(): table.add_row(key.replace("_", " ").title(), str(value))
                console.print(table)
        pause()

def menu_crypto():
    while True:
        clear_screen(); show_banner()
        show_menu("Cryptography & Identity", [("1", "Password Strength Analyzer"), ("2", "File Encryptor / Decryptor (AES-256)"), ("3", "Hash Toolkit"), ("4", "Data Encoder / Decoder"), ("5", "Password Complexity Validator"), ("6", "SSH Key Pair Generator"), ("7", "JWT Token Inspector"), ("0", "Back")])
        choice = Prompt.ask("\n[bold yellow]Select a tool[/bold yellow]", choices=list("12345670"))
        if choice == "0": return
        if choice == "1":
            result = PasswordAnalyzer(Prompt.ask("[cyan]Password[/cyan]", password=True)).analyze()
            console.print(f"Entropy: [cyan]{result['entropy']} bits[/cyan]\nStrength: [green]{result['strength']}[/green]")
            for warning in result.get("warnings", []): console.print(f"[red]- {warning}[/red]")
        elif choice == "2":
            mode = Prompt.ask("[cyan]Encrypt or Decrypt?[/cyan]", choices=["E", "D"])
            path = Prompt.ask("[cyan]File path[/cyan]")
            password = Prompt.ask("[cyan]Password[/cyan]", password=True)
            try:
                result = FileCrypto(password).encrypt_file(path) if mode == "E" else FileCrypto(password).decrypt_file(path)
                console.print(f"[green]Completed:[/green] {result}")
            except Exception as exc: console.print(f"[red]{exc}[/red]")
        elif choice == "3":
            mode = Prompt.ask("[cyan]Generate or Identify?[/cyan]", choices=["G", "I"])
            if mode == "G":
                text = Prompt.ask("[cyan]Text[/cyan]"); algo = Prompt.ask("[cyan]Algorithm[/cyan]", default="sha256")
                console.print(HashToolkit.hash_string(text, algo))
            else: console.print(HashToolkit.identify_hash(Prompt.ask("[cyan]Hash[/cyan]")))
        elif choice == "4":
            mode = Prompt.ask("[cyan]Encode or Decode?[/cyan]", choices=["E", "D"])
            fmt = Prompt.ask("[cyan]Format[/cyan]", choices=["base64", "hex", "binary", "url", "rot13"])
            data = Prompt.ask("[cyan]Data[/cyan]")
            console.print(DataEncoder.encode(data, fmt) if mode == "E" else DataEncoder.decode(data, fmt))
        elif choice == "5":
            result = PasswordValidator.validate(Prompt.ask("[cyan]Password[/cyan]", password=True))
            console.print("[green]Password meets the policy.[/green]" if result["is_valid"] else "[red]Password failed:[/red]")
            for issue in result.get("issues", []): console.print(f" - {issue}")
        elif choice == "6":
            algo = Prompt.ask("[cyan]Algorithm[/cyan]", choices=["rsa", "ed25519"], default="ed25519")
            directory = Prompt.ask("[cyan]Output directory[/cyan]", default="keys")
            result = SSHKeyGenerator.generate_rsa(output_dir=directory) if algo == "rsa" else SSHKeyGenerator.generate_ed25519(output_dir=directory)
            console.print(result)
        elif choice == "7":
            result = JWTInspector.inspect(Prompt.ask("[cyan]JWT token[/cyan]"))
            if result.get("error"): console.print(f"[red]{result['error']}[/red]")
            else:
                console.print(Panel(json.dumps(result["header"], indent=2), title="Header"))
                console.print(Panel(json.dumps(result["payload"], indent=2), title="Payload"))
        pause()

def menu_endpoint():
    while True:
        clear_screen(); show_banner()
        show_menu("Endpoint Security & Forensics", [("1", "Local System Security Audit"), ("2", "File SHA-256 Integrity Check"), ("3", "File Permission Audit"), ("0", "Back")])
        choice = Prompt.ask("\n[bold yellow]Select a tool[/bold yellow]", choices=["1", "2", "3", "0"])
        if choice == "0": return
        if choice == "1":
            table = Table(title="Local System Audit"); table.add_column("Property"); table.add_column("Value")
            for key, value in SystemAudit.collect().items(): table.add_row(key, str(value))
            console.print(table)
        elif choice == "2":
            result = IntegrityChecker.sha256(Prompt.ask("[cyan]File path[/cyan]"))
            console.print(result if "error" in result else f"SHA-256: [green]{result['sha256']}[/green]\nSize: {result['size']} bytes")
        elif choice == "3":
            result = SystemAudit.file_permissions(Prompt.ask("[cyan]File path[/cyan]"))
            if result.get("error"): console.print(f"[red]{result['error']}[/red]")
            else:
                for key, value in result.items(): console.print(f"{key}: {value}")
        pause()

def menu_incident():
    while True:
        clear_screen(); show_banner()
        show_menu("Log Analysis & Incident Response", [("1", "SSH Failed-Login Analyzer"), ("2", "Export Findings as JSON"), ("0", "Back")])
        choice = Prompt.ask("\n[bold yellow]Select a tool[/bold yellow]", choices=["1", "2", "0"])
        if choice == "0": return
        path = Prompt.ask("[cyan]Log file path[/cyan]")
        results = LogAnalyzer(path).analyze()
        if results is None: console.print("[red]Log file not found.[/red]")
        elif isinstance(results, str): console.print(f"[red]{results}[/red]")
        elif choice == "1":
            table = Table(title="Failed SSH Logins"); table.add_column("Source IP"); table.add_column("Attempts")
            for ip, count in results: table.add_row(ip, str(count))
            console.print(table if results else "[green]No matching failed-login events found.[/green]")
        else:
            output = path + ".findings.json"
            with open(output, "w", encoding="utf-8") as file: json.dump({"source": path, "failed_logins": results}, file, indent=2)
            console.print(f"[green]Findings saved to {output}[/green]")
        pause()

def menu_compliance():
    while True:
        clear_screen(); show_banner()
        show_menu("Compliance, Cloud & Configuration", [("1", "HTTP Security Headers Audit"), ("2", "Local Security Checklist"), ("0", "Back")])
        choice = Prompt.ask("\n[bold yellow]Select a tool[/bold yellow]", choices=["1", "2", "0"])
        if choice == "0": return
        if choice == "1":
            url = Prompt.ask("[cyan]Website URL you are authorized to audit[/cyan]")
            result = SecurityHeaders.check(url)
            if "error" in result: console.print(f"[red]{result['error']}[/red]")
            else:
                table = Table(title=f"Security Headers: {result.get('final_url', url)}"); table.add_column("Header"); table.add_column("Status / Value")
                for key, value in result.items():
                    if key not in {"status", "final_url"}: table.add_row(key, str(value))
                console.print(table)
                console.print(f"HTTP status: {result.get('status')}")
        else:
            checks = [
                "Keep the operating system and security software updated",
                "Use MFA on important accounts",
                "Back up important data",
                "Restrict unnecessary services and permissions",
                "Review logs and authentication events regularly",
                "Use HTTPS and modern security headers on web services",
            ]
            console.print(Panel("\n".join(f"[green]✓[/green] {item}" for item in checks), title="Defensive Checklist"))
        pause()

def main():
    while True:
        clear_screen(); show_banner()
        show_menu("Main Categories", [
            ("1", "Network & Reconnaissance"),
            ("2", "Cryptography & Identity Management"),
            ("3", "Endpoint Security & Forensics"),
            ("4", "Log Analysis & Incident Response"),
            ("5", "Compliance, Cloud & Configuration"),
            ("0", "Exit")
        ])
        choice = Prompt.ask("\n[bold yellow]Select a category[/bold yellow]", choices=["1", "2", "3", "4", "5", "0"])
        if choice == "1": menu_network()
        elif choice == "2": menu_crypto()
        elif choice == "3": menu_endpoint()
        elif choice == "4": menu_incident()
        elif choice == "5": menu_compliance()
        else:
            console.print("[green]Goodbye![/green]"); break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[red]Exiting...[/red]")
        sys.exit(0)
