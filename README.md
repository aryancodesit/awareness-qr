# ⚠ SYSTEM ALERT: Awareness QR

> **"Curiosity killed the cat... but satisfaction brought it back (secured)."**

<div align="center">
  <img src="./awareness_qr.png" alt="Scan to Try" width="300" />
  
  ### 📱 SCAN TO TEST YOUR VIGILANCE 📱
  *(Dare to scan? Don't say I didn't warn you.)*
  
  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
  ![Status](https://img.shields.io/badge/System-COMPROMISED..._Just_Kidding-red)
</div>

---

## 🕵️‍♂️ What is this?

**Awareness QR** is a Proof-of-Concept (PoC) tool designed to educate users about the dangers of **"Quishing"** (QR Code Phishing). 

It looks like a harmless QR code. You scan it, expecting a menu, a discount, or an app download. Instead, you're greeted with a heart-stopping (simulate) system breach! 😱 

But don't worry—it's benign. After the initial "shock," the app transitions into an educational hub, teaching users:
1.  **How to spot fake QR codes.**
2.  **Why you shouldn't blindly trust `scan -> go`.**
3.  **Tools to verify URLs before clicking.**

## 🚀 Features

*   **Realistic Glitch Effects**: Simulates a terminal-style "system compromise" to grab attention.
*   **Audio Feedback**: Uses urgency-inducing sound effects (safe for work... mostly).
*   **Vibration API**: Provides haptic feedback on supported mobile devices for extra immersion.
*   **Educational Payload**: The "attack" resolves into a friendly, resource-rich learning page.

## 🛠️ Installation & Usage

### Option 1: The Easy Way (Live Demo)
Just scan the QR code above with your phone! 

### Option 2: Run Locally
Want to host your own "prank" for awareness training?

1.  **Clone the repo**
    ```bash
    git clone https://github.com/aryancodesit/awareness-qr.git
    cd awareness-qr
    ```

2.  **Generate your own QR Code**
    Modify `generator.py` to point to your hosted URL (or localhost address).
    ```bash
    pip install qrcode[pil]
    python generator.py
    ```

3.  **Serve it up**
    Open `index.html` in your browser or serve it with Python:
    ```bash
    python -m http.server 8000
    ```

## 🤝 Contributing
Got a scarier glitch effect? A better educational resource? Open a PR! 
1.  Fork it 🍴
2.  Create your branch (`git checkout -b feature/scarier-glitch`)
3.  Commit your changes (`git commit -m 'Added Matrix rain effect'`)
4.  Push to the branch (`git push origin feature/scarier-glitch`)
5.  Open a Pull Request

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
<div align="center">
  <sub>Built with bad intentions... for a good cause. 🛡️</sub>
</div>
