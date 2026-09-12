path = "/home/stark/zunix/README.md"
with open(path, "r", encoding="utf-8") as f:
    readme = f.read()

# Replace repo URL
readme = readme.replace("zunix-frontend", "zunix")

# Update Deployments section
old_deployments = """## 🌐 Live Production Deployments

- **Live Campus Hub**: [https://davidalbertstark-lab.github.io/zunix/](https://davidalbertstark-lab.github.io/zunix/)
- **Live 6-Step Onboarding & Review Card**: [https://davidalbertstark-lab.github.io/zunix/setup-student.html](https://davidalbertstark-lab.github.io/zunix/setup-student.html)
- **Live 3D Neon ID Card Customizer**: [https://davidalbertstark-lab.github.io/zunix/profile-card.html](https://davidalbertstark-lab.github.io/zunix/profile-card.html)
- **Live Gamified Rewards**: [https://davidalbertstark-lab.github.io/zunix/Rewards.html](https://davidalbertstark-lab.github.io/zunix/Rewards.html)"""

new_deployments = """## 🌐 Live Production Deployments

- **Live Campus Hub**: [https://davidalbertstark-lab.github.io/zunix/](https://davidalbertstark-lab.github.io/zunix/)
- **Interactive XP Rewards Simulator**: [https://davidalbertstark-lab.github.io/zunix/pages/rewards.html](https://davidalbertstark-lab.github.io/zunix/pages/rewards.html)
- **3D Student ID Card & Canvas PNG Export**: [https://davidalbertstark-lab.github.io/zunix/pages/profile-card.html](https://davidalbertstark-lab.github.io/zunix/pages/profile-card.html)
- **Programs Directory with Live Search**: [https://davidalbertstark-lab.github.io/zunix/pages/programs.html](https://davidalbertstark-lab.github.io/zunix/pages/programs.html)
- **6-Step Onboarding & Review Card**: [https://davidalbertstark-lab.github.io/zunix/pages/setup-student.html](https://davidalbertstark-lab.github.io/zunix/pages/setup-student.html)
- **Unified Student Authentication**: [https://davidalbertstark-lab.github.io/zunix/pages/login.html](https://davidalbertstark-lab.github.io/zunix/pages/login.html)"""

readme = readme.replace(old_deployments, new_deployments)

with open(path, "w", encoding="utf-8") as f:
    f.write(readme)

print("Updated README.md successfully")
