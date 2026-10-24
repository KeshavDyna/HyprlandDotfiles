<div align="center">

  <h1>✨ Hyprland Dotfiles (Lua Edition)</h1>
  <p>A sleek, dynamic, keyboard-driven Wayland environment configured entirely in Lua with smooth animations, custom blur, and Nvidia compatibility.</p>

  <p>
    <img src="https://img.shields.io/badge/WM-Hyprland-blue?style=flat-square&logo=archlinux" alt="Hyprland" />
    <img src="https://img.shields.io/badge/Language-Lua-000080?style=flat-square&logo=lua" alt="Lua" />
    <img src="https://img.shields.io/badge/Terminal-Kitty-black?style=flat-square&logo=gnometerminal" alt="Kitty" />
    <img src="https://img.shields.io/badge/Editor-Neovim%20%7C%20VSCode-green?style=flat-square&logo=neovim" alt="Editor" />
    <img src="https://img.shields.io/badge/GPU-NVIDIA-76B900?style=flat-square&logo=nvidia" alt="Nvidia" />
  </p>

  <!-- Replace with your actual screenshot path -->
  <img src="assets/preview.png" alt="Desktop Preview" width="100%" />

</div>

---

## ⚡ Highlights

- **Pure Lua Configuration**: Programmatic and declarative Hyprland config using clean Lua tables and dispatchers.
- **High Refresh & Dual Display**: Optimized out-of-the-box for a 240Hz main display alongside a secondary utility monitor.
- **Nvidia DRM Ready**: Pre-configured environment flags (`nvidia_drm`, `__GLX_VENDOR_LIBRARY_NAME`) for low-latency Wayland composition.
- **Aesthetic Depth**: Subtle border contrasts, 10px rounded corners, spring physics pop-in animations, and custom background blur.
- **Dual Launchers & Managers**: Integrated with both GUI (`Thunar`, `Rofi`, `Wofi`) and terminal-native tools (`Yazi`, `Neovim`).

---

## 🖥️ System & Tools

| Component | Software |
| :--- | :--- |
| **Compositor** | [Hyprland](https://hyprland.org/) (Lua API) |
| **Status Bar** | [Waybar](https://github.com/Alexays/Waybar) |
| **Terminal** | [Kitty](https://sw.kovidgoyal.net/kitty/) |
| **Launchers** | [Rofi](https://github.com/davatorium/rofi) / [Wofi](https://hg.sr.ht/~scoopta/wofi) |
| **File Managers**| [Yazi](https://github.com/sxyazi/yazi) (TUI) & [Thunar](https://docs.xfce.org/xfce/thunar/start) (GUI) |
| **Code Editors** | [Neovim](https://neovim.io/) & [Visual Studio Code](https://code.visualstudio.com/) |
| **Wallpaper & Widgets** | `awww-daemon` & `eww daemon` |
| **Color Temperature** | [Hyprsunset](https://github.com/hyprwm/hyprsunset) (4500K toggle) |
| **Screenshots** | `grim` + `slurp` -> `wl-copy` |

---

## ⌨️ Keybindings

The primary modifier key is **`SUPER`** (Windows key). Secondary modifier is **`SUPER + SHIFT`**.

### 🚀 Applications & Launchers

| Keybinding | Action |
| :--- | :--- |
| `SUPER + Space` | Open App Launcher (`rofi drun`) |
| `SUPER + SHIFT + Space` | Open Run Dialog (`rofi run`) |
| `SUPER + R` | Open Alternate Menu (`wofi`) |
| `SUPER + T` | Launch Terminal (`kitty`) |
| `SUPER + Return` | Launch Editor (`kitty -e nvim`) |
| `SUPER + SHIFT + Return` | Launch GUI IDE (`code`) |
| `SUPER + B` | Launch Web Browser (`brave`) |
| `SUPER + D` | Launch Chat (`discord`) |
| `SUPER + M` | Launch Music (`spotify`) |
| `SUPER + E` | Open TUI File Manager (`yazi`) |
| `SUPER + SHIFT + E` | Open GUI File Manager (`thunar`) |

### 🪟 Window Management & Navigation

| Keybinding | Action |
| :--- | :--- |
| `SUPER + Q` | Close focused window |
| `SUPER + V` | Toggle floating mode |
| `SUPER + F` | Maximize window |
| `SUPER + SHIFT + F` | Toggle true fullscreen |
| `SUPER + P` | Toggle pseudo-tiling |
| `SUPER + J` | Toggle layout split orientation |
| `SUPER + Arrow Keys` | Move focus across windows |
| `SUPER + SHIFT + Arrow Keys` | Move window position |
| `SUPER + [1-9]` | Switch to workspace [1-9] |
| `SUPER + SHIFT + [1-9]` | Move active window to workspace [1-9] |
| `SUPER + Mouse Scroll` | Cycle workspaces |
| `SUPER + LMB / RMB Drag` | Move / Resize windows |

### 🛠️ Utilities

| Keybinding | Action |
| :--- | :--- |
| `SUPER + SHIFT + S` | Select area screenshot to clipboard (`grim + slurp`) |
| `SUPER + SHIFT + N` | Toggle Night Light (`hyprsunset 4500K`) |
| `SUPER + SHIFT + F4` | Session exit / shutdown prompt |
| `Media Keys` | Volume, mute, brightness, and player controls |

---
