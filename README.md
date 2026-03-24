Minecraft Auto-Miner (Python Script)
---

This is a very simple Python auto-miner script made for Minecraft.
It does one thing only: when you press `M`, your character will walk forward, sneak, and mine automatically.

Nothing fancy. No AI. No lava detection. Just a basic tool for strip mining.

---
<b>What this script does</b>

When you press `M` in-game:

Your character walks forward (W)
Sneaks (Shift) so you don’t fall into holes
Holds left click to keep mining

Press `M` again and everything stops.

That’s it. Very simple and very direct.

---

<b>Requirements</b>

You only need Python and one library.

Install the library using this command:
```pip install pynput```

How to use it?
1. Download the script
2. Save it as something like:
autominer.py
3. Run it:
```python autominer.py```
4. Open Minecraft
5. Press `M` to turn it ON
6. Press `M` again to turn it OFF

---

<b>What this script does NOT do</b>

Just so expectations are clear:

1. It does not avoid lava
2. It does not switch tools
3. It does not detect ores
4. It does not think for you

It simply holds keys for you while you strip mine.

---

<b>Tips</b>

1. Keep your sound on so you can hear lava
2. Make sure your pickaxe doesn’t break
3. If it doesn’t work, try running Python as Administrator

---
<b>Why this exists</b>

This was made as a very basic beginner project.
The goal was just to make something that works, not something advanced.

If you want to improve it later, you could add:

automatic tool switching
hotbar detection
timer-based mining
safer mining logic
