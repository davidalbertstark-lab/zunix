# Zunix — Digital Campus Platform & Student Identity Engine

[![Platform](https://img.shields.io/badge/Platform-Web-00ffcc?style=for-the-badge&logo=google-chrome&logoColor=black)](#)
[![Vanilla Frontend](https://img.shields.io/badge/Architecture-Modular%20Vanilla%20ES6+-00b050?style=for-the-badge&logo=javascript&logoColor=white)](#)
[![Firebase](https://img.shields.io/badge/Backend-Firebase%20Auth%20%26%20Firestore-ffca28?style=for-the-badge&logo=firebase&logoColor=black)](#)
[![Aesthetics](https://img.shields.io/badge/Design-Cyberpunk%20Glassmorphism-ff0066?style=for-the-badge)](#)

> **Zunix** is an all-in-one digital campus ecosystem engineered to empower African tertiary students across learning, earning, networking, and institutional recognition. It features an intelligent multi-step onboarding funnel, real-time cascading geographic & collegiate data binding, dynamic 3D neon-glass student ID generation, and gamified engagement loops.

---

## 🚀 Key Modules & Experience

| View | Access Path | Description |
| :--- | :--- | :--- |
| **Campus Portal** | [`index.html`](index.html) | High-impact campus landing hub with fluid typography, feature showcases, and program navigation. |
| **Student Onboarding** | [`setup-student.html`](setup-student.html) | 6-step guided enrollment funnel with age validation, cascading campus data, and live ID generation. |
| **Digital ID Generator** | [`profile-card.html`](profile-card.html) | Interactive 3D cyberpunk neon-glass student ID card customizer and live demo previewer. |
| **Student Access Portal** | [`LoginPage.html`](LoginPage.html) | Integrated authentication gateway supporting Email/Password and Google OAuth via Firebase. |
| **Rewards & Leaderboards** | [`Rewards.html`](Rewards.html) | Gamified Zunix Points (ZP) engine with tier levels, bonus tracking, and engagement metrics. |
| **Academic & Career Programs** | [`Programs.html`](Programs.html) | Directory of ambassador squads, freelance collectives, peer academic assistance, and promos. |
| **Campus Communities** | [`Communities.html`](Communities.html) | Student clubs, trending campus topics, and cross-institutional linkups. |

---

## 🛠️ Architecture & Data Flow

```mermaid
flowchart TD
    subgraph Client ["Client Interface (Zero-Dependency Modern Web)"]
        LP[LoginPage.html<br/>Firebase Auth / Google] -->|Session Auth| SS[setup-student.html<br/>6-Step Onboarding]
        SS --> S1[Step 1: Identity & Username]
        S1 --> S2[Step 2: Gender Selection]
        S2 --> S3[Step 3: Age & DOB Validation]
        S3 --> S4[Step 4: Cascading Geo-Location]
        S4 --> S5[Step 5: Collegiate & Faculty Data]
        S5 --> S6[Step 6: Live 3D Neon Review Card]
        S6 --> S7[Step 7: Enrollment Complete 🎉]
    end

    subgraph DataEngine ["Data & State Pipelines"]
        LOC[(data/location-data.json<br/>Region → State → City)] -->|Cascading Populate| S4
        INST[(json/institution.json<br/>Accredited Campuses)] -->|Autocomplete Match| S5
        S2 -->|Gender Branch| AVATAR{Dynamic Avatar<br/>boyss.png vs girls.png}
        AVATAR --> S6
    end

    subgraph Persistence ["Dual-Tier Persistence Engine"]
        S6 -->|Cloud Sync| FS[(Firebase Firestore<br/>students/{uid})]
        S6 -->|Offline Fallback| LS[(LocalStorage<br/>zunix_student_profile)]
    end
```

---

## 🎨 Unified Profile Card Engine

Originally prototyped as an experimental neon-glass card (`zunix-profile-card`), the component has been natively elevated into a production-grade digital student credential across Zunix:

1. **Reactive Two-Way Binding**: As students advance through enrollment, their name, handle, institutional affiliation, department, and projected graduation year dynamically populate the card.
2. **Dynamic Avatar Engine**: Contextually switches between character avatars (`src/img/boyss.png` for male, `src/img/girls.png` for female) with glowing status indicators.
3. **Verified Security Tag**: Real-time cryptographic ID generation (`ZUN-2025-XXXX`) indicating platform-verified credential status.
4. **Standalone Customizer ([`profile-card.html`](profile-card.html))**: An interactive playground allowing students to customize their digital campus pass, copy raw badge parameters, or print physical cards directly from the browser.

---

## 💻 Tech Stack & Engineering Highlights

- **Languages**: HTML5 Semantic Architecture, CSS3 (Custom Properties, Flexbox, CSS Grid, Glassmorphism `backdrop-filter`, Keyframe Animations), Modern JavaScript (ES6+ Modules).
- **Authentication & Cloud Database**: Firebase Auth (Email/Password, Google OAuth) + Cloud Firestore (`students/{uid}`).
- **Zero Heavy Frameworks**: Pure vanilla web implementation providing sub-millisecond execution times and 100% standards compliance.
- **Resilient Offline/Preview Mode**: Built-in fallback caches form data to `localStorage`, enabling full end-to-end recruitment or test runs even in offline or sandboxed environments.
- **Universal Cross-Platform Navigation**: Shared CSS-driven responsive navigation bar (`Header.css`) providing fluid hamburger drawers across desktop, tablet, and mobile displays without JavaScript overhead.

---

## 📂 Repository Structure

```
zunix/
├── index.html                  # Main campus ecosystem homepage
├── setup-student.html          # Guided 6-step student onboarding & ID confirmation
├── profile-card.html           # Standalone interactive 3D ID card generator & customizer
├── LoginPage.html              # Firebase authentication portal (Sign Up & Sign In)
├── Features.html               # Comprehensive platform capability showcase
├── Rewards.html                # Gamified rewards system & ZP engagement score
├── Programs.html               # Ambassador, Freelancer, and Creator programs
├── Events.html                 # Campus cultural & tech events directory
├── Communities.html            # Student clubs, guilds, and social hubs
├── AboutUs.html                # Platform mission, founding ethos & pillars
├── ContactUsPage.html          # Strategic inquiry & student support portal
├── Partners.html               # Institutional & brand collaboration roles
├── Faq.html                    # Frequently asked questions
├── CookiePolicy.html           # Cookie privacy documentation
├── PrivacyPolicy.html          # Legal privacy policy
├── Terms.html                  # Terms & conditions of service
├── CopyrightPolicy.html        # Intellectual property guidelines
├── data/
│   └── location-data.json      # Nigerian geopolitical zones, states, and city mapping
├── json/
│   └── institution.json        # Accredited university, polytechnic & college index
└── src/
    ├── img/                    # High-res character avatars, logos, and UI graphics
    ├── js/
    │   ├── main.js             # Onboarding bootstrapper & auth state listener
    │   ├── ui.js               # Step state machine, dynamic card populator & DOM manager
    │   ├── setup-student.js    # Cascading dropdowns & institution autocomplete
    │   ├── validation.js       # Student age, matriculation level & year validator
    │   ├── auth.js             # Firebase auth handlers & session storage
    │   ├── firebase.js         # Firebase SDK configuration
    │   └── form-handler.js     # Firestore sync & local session caching engine
    └── styles/
        ├── Header.css          # Universal responsive navigation bar & mobile drawer
        ├── step6.css           # Cyberpunk neon-glass card styles & animations
        ├── setup-student.css   # Onboarding funnel form styling & animations
        └── ...                 # Modular stylesheets for all platform subpages
```

---

## ⚡ Local Development

To run Zunix locally:

```bash
# Clone the repository
git clone https://github.com/davidalbertstark-lab/zunix.git

# Navigate into the project
cd zunix

# Start a local static server (Python 3)
python3 -m http.server 8000
```

Open `http://localhost:8000` in any modern web browser.

---

## 👨‍💻 Author

**David Albert Stark** ([@davidalbertstark-lab](https://github.com/davidalbertstark-lab))  
*Systems & Frontend Software Engineer*
