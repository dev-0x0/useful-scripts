# Useful scripts
A place for any useful scripts I write


_Disclaimer:
Please heed any warnings at the top of the scripts. 
I am not responsible for any damage or loss that may result from executing
any of the code in this repository. I provide no guarantees that any code in this repo works as stated. Never execute some code you find online
without knowing exactly what you're doing._

**burpsuite_update.py** - An easy way to update burpsuite on Kali Linux.

**self_delete_linux.py**   - A simple script that self deletes, using _shred_ 

**self_delete_windows.py** - A simple script that self deletes with _os.remove_ and _cipher_

**parse_log_for_js.sh**    - Sort and list the unique Javascript filenames in a web server log 

### Active Directory

**enum-ad-spn.ps1**	- Enumerate SPNs on a domain-joined Windows system

**enum-ad-nested-groups.ps1** - Enumerate Nested Groups on a domain-joined Windows System

### Buffer Overflows

**getbadchars.py**  - Generate bad character byte array for BOF. Allows for exclusion of specified bytes.
**addr_to_little_endian.py** - Convert memory address to little endian in bytes
**hexify-badchars.py** - Takes string of bad chars as output by mona.py and outputs in byte format
