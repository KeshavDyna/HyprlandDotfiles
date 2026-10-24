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

- **Pure Lua Configuration**: Programmatic and declarative Hyprland config using clean Lua tables and dispatchers[cite: 1].
- **High Refresh & Dual Display**: Optimized out-of-the-box for a 240Hz main display alongside a secondary utility monitor[cite: 1].
- **Nvidia DRM Ready**: Pre-configured environment flags (`nvidia_drm`, `__GLX_VENDOR_LIBRARY_NAME`) for low-latency Wayland composition[cite: 1].
- **Aesthetic Depth**: Subtle border contrasts, 10px rounded corners, spring physics pop-in animations, and custom background blur[cite: 1].
- **Dual Launchers & Managers**: Integrated with both GUI (`Thunar`, `Rofi`, `Wofi`) and terminal-native tools (`Yazi`, `Neovim`)[cite: 1].

---

## 🖥️ System & Tools

| Component | Software |
| :--- | :--- |
| **Compositor** | [Hyprland](https://hyprland.org/) (Lua API)[cite: 1] |
| **Status Bar** | [Waybar](https://github.com/Alexays/Waybar)[cite: 1] |
| **Terminal** | [Kitty](https://sw.kovidgoyal.net/kitty/)[cite: 1] |
| **Launchers** | [Rofi](https://github.com/davatorium/rofi) / [Wofi](https://hg.sr.ht/~scoopta/wofi)[cite: 1] |
| **File Managers**| [Yazi](https://github.com/sxyazi/yazi) (TUI) & [Thunar](https://docs.xfce.org/xfce/thunar/start) (GUI)[cite: 1] |
| **Code Editors** | [Neovim](https://neovim.io/) & [Visual Studio Code](https://code.visualstudio.com/)[cite: 1] |
| **Wallpaper & Widgets** | `awww-daemon` & `eww daemon`[cite: 1] |
| **Color Temperature** | [Hyprsunset](https://github.com/hyprwm/hyprsunset) (4500K toggle)[cite: 1] |
| **Screenshots** | `grim` + `slurp` -> `wl-copy`[cite: 1] |

---

## ⌨️ Keybindings

The primary modifier key is **`SUPER`** (Windows key)[cite: 1]. Secondary modifier is **`SUPER + SHIFT`**[cite: 1].

### 🚀 Applications & Launchers

| Keybinding | Action |
| :--- | :--- |
| `SUPER + Space` | Open App Launcher (`rofi drun`)[cite: 1] |
| `SUPER + SHIFT + Space` | Open Run Dialog (`rofi run`)[cite: 1] |
| `SUPER + R` | Open Alternate Menu (`wofi`)[cite: 1] |
| `SUPER + T` | Launch Terminal (`kitty`)[cite: 1] |
| `SUPER + Return` | Launch Editor (`kitty -e nvim`)[cite: 1] |
| `SUPER + SHIFT + Return` | Launch GUI IDE (`code`)[cite: 1] |
| `SUPER + B` | Launch Web Browser (`brave`)[cite: 1] |
| `SUPER + D` | Launch Chat (`discord`)[cite: 1] |
| `SUPER + M` | Launch Music (`spotify`)[cite: 1] |
| `SUPER + E` | Open TUI File Manager (`yazi`)[cite: 1] |
| `SUPER + SHIFT + E` | Open GUI File Manager (`thunar`)[cite: 1] |

### 🪟 Window Management & Navigation

| Keybinding | Action |
| :--- | :--- |
| `SUPER + Q` | Close focused window[cite: 1] |
| `SUPER + V` | Toggle floating mode[cite: 1] |
| `SUPER + F` | Maximize window[cite: 1] |
| `SUPER + SHIFT + F` | Toggle true fullscreen[cite: 1] |
| `SUPER + P` | Toggle pseudo-tiling[cite: 1] |
| `SUPER + J` | Toggle layout split orientation[cite: 1] |
| `SUPER + Arrow Keys` | Move focus across windows[cite: 1] |
| `SUPER + SHIFT + Arrow Keys` | Move window position[cite: 1] |
| `SUPER + [1-9]` | Switch to workspace [1-9][cite: 1] |
| `SUPER + SHIFT + [1-9]` | Move active window to workspace [1-9][cite: 1] |
| `SUPER + Mouse Scroll` | Cycle workspaces[cite: 1] |
| `SUPER + LMB / RMB Drag` | Move / Resize windows[cite: 1] |

### 🛠️ Utilities

| Keybinding | Action |
| :--- | :--- |
| `SUPER + SHIFT + S` | Select area screenshot to clipboard (`grim + slurp`)[cite: 1] |
| `SUPER + SHIFT + N` | Toggle Night Light (`hyprsunset 4500K`)[cite: 1] |
| `SUPER + SHIFT + F4` | Session exit / shutdown prompt[cite: 1] |
| `Media Keys` | Volume, mute, brightness, and player controls[cite: 1] |

---
