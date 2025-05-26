# 🔐 Phantom Keystorm ⚡  
*A high-performance, rainbow-colored wordlist generator for ethical hacking.*  

![Demo](assets/demo.gif)  

---

## 🚀 Quick Start  
### Prerequisites  
- Python 3.8+  
- Git (optional)  

### Installation  
```bash
# Clone repository
git clone https://github.com/darkbert781/phantom_keystorm.git
cd phantom_keystorm

# Install dependencies
pip install -r requirements.txt
🛠️ Basic Usage

Run interactively:
bash

python3 phantom_keystorm.py

Follow the prompts:

    Enter minimum password length (e.g., 4)

    Enter maximum length (e.g., 6)

    Specify characters (e.g., abc123!@#)

    Set output filename (e.g., custom_wordlist.txt)
![word](https://github.com/user-attachments/assets/d8c09a30-a9be-4158-b100-155532994290)


⚡ Advanced Usage
One-Line Automation
bash

python3 phantom_keystorm.py <<< "4 6 abc123!@# passwords.txt"

Format: min_len max_len charset output_file
Real-Time Monitoring
bash

watch -n 1 'wc -l passwords.txt'  # View line count updates

🌟 Key Features
Feature	Description
RGB ASCII Art	Dynamic color cycling with colorama
Military-Grade Speed	50K+ combinations/second (i7 CPU)
Smart Interrupts	Ctrl+C auto-deletes incomplete files
Custom Charsets	Supports letters, numbers, symbols
🛑 Legal Notice

Authorized Use Only
diff

+ Allowed: Security research, authorized pentesting  
- Forbidden: Unauthorized system access, credential stuffing  

📜 License

MIT © 2023 Simfukwe Alinaswe


### Key Improvements:
1. **Structured Flow**: Installation → Basic Use → Advanced  
2. **Quick Copy-Paste** commands with examples  
3. **Feature Table** for quick scanning  
4. **Legal Warning** in diff syntax for visibility  
5. **Personalized Copyright** with your name  

Want me to add:  
- [ ] Screenshot of the interactive prompts  
- [ ] Performance comparison table  
- [ ] Badges (Python version, license, etc.)  

Let me know! 🚀
