# APIFuzzer

**Simple API fuzzer for enumeration testing.**

## Usage
To start fuzzing an API, provide a wordlist via standard input:
```bash
cat wordlist.txt | python3 fuzz.py
```

![APIfuzzer](https://github.com/user-attachments/assets/61cb21c5-d199-4d5b-a687-e122dae951b9)

## Description
This script enumerates API endpoints using `{JSON} Placeholder`, a fake yet reliable API for testing and prototyping.

If you want to change the target API, modify the base URL in `fuzz.py`:
```python
response = requests.get(url=f"https://jsonplaceholder.typicode.com/{word.strip()}")
```
Replace `"https://jsonplaceholder.typicode.com"` with your own API URL.

## Disclaimer
**APIFuzzer is provided "as is", without any warranty, express or implied, including but not limited to warranties of merchantability, fitness for a particular purpose, and non-infringement.**  
The author(s) **are not responsible** for any damage, security vulnerabilities, or legal consequences resulting from the use of this tool. **Use it at your own risk.**

## License
This project is licensed under the **MIT License**. See the LICENSE file for details.

---
