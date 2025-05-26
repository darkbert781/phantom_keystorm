#!/usr/bin/env python3
import itertools
import os
import sys
import time
from datetime import datetime
from colorama import init, Fore, Style
import math

# Initialize colorama
init(autoreset=True)

# Customize IP here
CUSTOM_IP = "192.168.1.77"

def rgb_char(char):
    """Return a single character with rotating RGB colors"""
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
    return colors[int(time.time() * 10) % len(colors)] + char  # Multiply by 10 for faster color cycling

def color_ascii(ascii_art):
    """Apply RGB coloring to ASCII art"""
    colored = ""
    for line in ascii_art.split('\n'):
        colored += ''.join([rgb_char(c) for c in line]) + '\n'
    return colored

def banner():
    tool_ascii = r"""
    ██████╗ ██╗  ██╗ █████╗ ███╗   ██╗████████╗ ██████╗ ███╗   ███╗
    ██╔══██╗██║  ██║██╔══██╗████╗  ██║╚══██╔══╝██╔═══██╗████╗ ████║
    ██████╔╝███████║███████║██╔██╗ ██║   ██║   ██║   ██║██╔████╔██║
    ██╔═══╝ ██╔══██║██╔══██║██║╚██╗██║   ██║   ██║   ██║██║╚██╔╝██║
    ██║     ██║  ██║██║  ██║██║ ╚████║   ██║   ╚██████╔╝██║ ╚═╝ ██║
    ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝
    ██╗  ██╗███████╗██╗   ██╗███████╗████████╗ ██████╗ ██████╗ ███╗   ███╗
    ██║ ██╔╝██╔════╝╚██╗ ██╔╝██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗████╗ ████║
    █████╔╝ █████╗   ╚████╔╝ ███████╗   ██║   ██║   ██║██████╔╝██╔████╔██║
    ██╔═██╗ ██╔══╝    ╚██╔╝  ╚════██║   ██║   ██║   ██║██╔══██╗██║╚██╔╝██║
    ██║  ██╗███████╗   ██║   ███████║   ██║   ╚██████╔╝██║  ██║██║ ╚═╝ ██║
    ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝
    """
    print(color_ascii(tool_ascii))
    print(Fore.CYAN + "By: Alinaswe Simfukwe")
    print(Fore.MAGENTA + f"There is no better place than {CUSTOM_IP}\n")

def generate_wordlist(min_len, max_len, chars, filename):
    if not chars:
        print(Fore.RED + "[-] Error: No characters specified!")
        return

    total_combinations = sum(len(chars)**i for i in range(min_len, max_len + 1))
    if total_combinations == 0:
        print(Fore.RED + "[-] Error: No possible combinations with these parameters!")
        return

    generated = 0
    start_time = time.time()
    
    try:
        with open(filename, 'w') as f:
            for length in range(min_len, max_len + 1):
                for combo in itertools.product(chars, repeat=length):
                    word = ''.join(combo)
                    f.write(word + '\n')
                    generated += 1
                    
                    # Update progress every 1000 combinations or when percentage changes
                    if generated % 1000 == 0 or generated == total_combinations:
                        progress = (generated / total_combinations) * 100
                        elapsed = time.time() - start_time
                        eta = (elapsed / max(1, generated)) * (total_combinations - generated)
                        
                        sys.stdout.write(f"\r[+] Generating: {progress:.2f}% complete | "
                                      f"ETA: {eta:.1f}s | "
                                      f"Speed: {generated/max(1, elapsed):,.0f} words/s")
                        sys.stdout.flush()
        
        # Clear the progress line
        sys.stdout.write("\r" + " " * 80 + "\r")
        sys.stdout.flush()
        
        print(Fore.GREEN + f"\n[+] Wordlist successfully generated: {os.path.abspath(filename)}")
        print(Fore.GREEN + f"[+] Total combinations: {total_combinations:,}")
        print(Fore.GREEN + f"[+] Generation time: {time.time() - start_time:.2f} seconds")
        
    except KeyboardInterrupt:
        print(Fore.RED + "\n[-] Generation interrupted by user!")
        try:
            os.remove(filename)
            print(Fore.YELLOW + f"[!] Deleted incomplete file: {filename}")
        except:
            pass
        return
    except Exception as e:
        print(Fore.RED + f"[-] Error: {str(e)}")
        return

def main():
    os.system('clear' if os.name == 'posix' else 'cls')
    banner()
    
    try:
        min_len = int(input(Fore.CYAN + "[?] Minimum length: " + Style.RESET_ALL))
        max_len = int(input(Fore.CYAN + "[?] Maximum length: " + Style.RESET_ALL))
        
        if min_len <= 0 or max_len <= 0:
            print(Fore.RED + "[-] Length must be positive integers!")
            return
            
        if min_len > max_len:
            print(Fore.RED + "[-] Minimum length cannot be greater than maximum length!")
            return

        chars = input(Fore.CYAN + "[?] Characters to include (e.g., abc123!@#): " + Style.RESET_ALL).strip()
        filename = input(Fore.CYAN + "[?] Output filename (without extension): " + Style.RESET_ALL) + ".txt"
        
        print(Fore.YELLOW + "\n[+] Generation Settings:")
        print(Fore.YELLOW + f"    - Length range: {min_len} to {max_len}")
        print(Fore.YELLOW + f"    - Character set: {chars}")
        print(Fore.YELLOW + f"    - Output file: {filename}\n")
        
        generate_wordlist(min_len, max_len, chars, filename)
        
    except ValueError:
        print(Fore.RED + "[-] Invalid input. Please enter valid numbers.")
    except KeyboardInterrupt:
        print(Fore.RED + "\n[-] Operation cancelled by user.")

if __name__ == "__main__":
    main()
