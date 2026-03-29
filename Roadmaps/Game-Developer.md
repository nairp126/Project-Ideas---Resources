# 🎮 Game Developer Roadmap (12 Months)

*Last Updated: 2026-03-29*

![Unity](https://img.shields.io/badge/Unity-000000?style=flat&logo=unity&logoColor=white)
![Unreal Engine](https://img.shields.io/badge/Unreal%20Engine-313131?style=flat&logo=unrealengine&logoColor=white)
![C#](https://img.shields.io/badge/C%23-239120?style=flat&logo=csharp&logoColor=white)
![C++](https://img.shields.io/badge/C++-00599C?style=flat&logo=cplusplus&logoColor=white)
![Godot](https://img.shields.io/badge/Godot-478CBF?style=flat&logo=godotengine&logoColor=white)
![OpenGL](https://img.shields.io/badge/OpenGL-5586A4?style=flat&logo=opengl&logoColor=white)

This roadmap guides you from programming fundamentals to a job-ready Game Developer in 12 months.

**Primary Engine Focus:** Unity (C#) — with Unreal Engine (C++) introduced in later months.

---

## Month 1-2: Programming Fundamentals & Game Math

**Focus:** Building the programming and math foundation every game developer needs.

### Technologies

* **Language:** C# (for Unity) or GDScript (for Godot)
* **Engine:** Unity 2022 LTS or Godot 4
* **Tooling:** VS Code or Rider, Git

### Concepts to Master

* **C# Basics:** Variables, loops, conditionals, functions, classes, interfaces.
* **OOP for Games:** Components, inheritance, polymorphism, composition over inheritance.
* **Game Math:** Vectors (2D/3D), dot product, cross product, basic trigonometry.
* **Coordinate Systems:** World space vs. local space, screen space.
* **Version Control:** Git basics for game projects (`.gitignore` for large assets).

### Projects

1. **Pong Clone:** Implement ball physics, paddle movement, collision detection, and score tracking from scratch.
2. **Math Visualizer:** A small Unity scene that visualizes vector operations (addition, dot product) interactively.

### Resources

* [Unity Learn](https://learn.unity.com/) - Official beginner pathways.
* [3Blue1Brown — Essence of Linear Algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) - Game math foundation.
* [Godot Docs](https://docs.godotengine.org/en/stable/) - If using Godot.

### Milestone

By the end of Month 2, you can build a simple 2D game with movement, collision, and a win/lose condition.

---

## Month 3-4: 2D Game Development

**Focus:** Mastering 2D game systems — physics, animation, tilemaps, and UI.

### Technologies

* **Engine:** Unity 2D or Godot 4
* **Art Tools:** Aseprite (pixel art), GIMP
* **Audio:** FMOD or Unity Audio Mixer

### Concepts to Master

* **Physics Engine:** Rigidbody2D, colliders, triggers, layers, raycasting.
* **Animation System:** Animator Controller, blend trees, animation events.
* **Tilemaps:** Tile palettes, rule tiles, autotiling.
* **Scene Management:** Scene loading, additive scenes, persistent objects (DontDestroyOnLoad).
* **UI System:** Canvas, anchors, UI events, health bars, menus.

### Projects

1. **Platformer Game:** A 2-level platformer with player movement, enemies, collectibles, and a HUD.
2. **Top-Down RPG Prototype:** Overworld movement, NPC dialogue system, and a simple inventory.

### Resources

* [Brackeys YouTube Channel](https://www.youtube.com/@Brackeys) - Classic Unity 2D tutorials.
* [Game Maker's Toolkit](https://www.youtube.com/@GMTK) - Game design theory.
* [Kenney Assets](https://kenney.nl/) - Free game assets for prototyping.

### Milestone

By the end of Month 4, you can ship a complete 2D game to itch.io with a working build.

---

## Month 5-6: 3D Game Development

**Focus:** Transitioning to 3D — rendering, lighting, cameras, and 3D physics.

### Technologies

* **Engine:** Unity 3D (URP pipeline)
* **3D Modeling:** Blender (basics)
* **Shaders:** ShaderGraph (Unity)

### Concepts to Master

* **3D Physics:** Rigidbody, CharacterController, NavMesh, raycasting in 3D.
* **Rendering Pipeline:** URP vs. HDRP, materials, PBR texturing.
* **Lighting:** Baked vs. real-time lighting, light probes, reflection probes.
* **Camera Systems:** Cinemachine, third-person and first-person controllers.
* **Shader Basics:** Vertex/fragment shaders, ShaderGraph nodes.

### Projects

1. **First-Person Shooter Prototype:** Player movement, shooting mechanics, enemy AI with NavMesh, ammo system.
2. **3D Puzzle Game:** Physics-based puzzles using joints, constraints, and interactive objects.

### Resources

* [Catlike Coding](https://catlikecoding.com/unity/tutorials/) - Deep Unity rendering tutorials.
* [Blender Guru](https://www.youtube.com/@blenderguru) - Blender fundamentals.
* [Unity URP Documentation](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@latest)

### Milestone

By the end of Month 6, you can build a playable 3D prototype with proper lighting, a camera system, and basic AI.

---

## Month 7-8: Game Systems & Architecture

**Focus:** Writing scalable, maintainable game code using proven patterns.

### Technologies

* **Patterns:** ScriptableObjects, Event System, State Machines
* **Tools:** Unity Profiler, Memory Profiler
* **Serialization:** JSON, PlayerPrefs, SaveSystem

### Concepts to Master

* **Design Patterns:** Singleton, Observer, State Machine, Object Pooling, Command pattern.
* **ScriptableObjects:** Data-driven design, decoupled event channels.
* **Save Systems:** Serializing game state to JSON, encryption basics.
* **Performance:** Object pooling, draw call batching, LOD (Level of Detail).
* **Input System:** Unity's new Input System package, input rebinding.

### Projects

1. **Inventory & Equipment System:** Drag-and-drop UI, item data via ScriptableObjects, equip/unequip logic.
2. **Save/Load System:** Persist player progress, inventory, and world state across sessions.

### Resources

* [Jason Weimann — Game Architecture](https://www.youtube.com/@Unity3dCollege) - Architecture patterns.
* [Game Programming Patterns](https://gameprogrammingpatterns.com/) - Free online book.

### Milestone

By the end of Month 8, you can architect a mid-sized game project with clean, extensible code.

---

## Month 9-10: Multiplayer & Networking

**Focus:** Adding real-time multiplayer to games.

### Technologies

* **Networking:** Unity Netcode for GameObjects or Mirror
* **Backend:** Photon PUN2 or PlayFab
* **Protocol:** UDP vs. TCP for games

### Concepts to Master

* **Client-Server Model:** Authority, prediction, reconciliation.
* **Lag Compensation:** Interpolation, extrapolation, rollback netcode.
* **Lobby Systems:** Matchmaking, room management.
* **Cheat Prevention:** Server-side validation, anti-cheat basics.
* **Serialization:** Efficient data packing for network messages.

### Projects

1. **Multiplayer Pong/Tanks:** Two-player real-time game with server authority and lag compensation.
2. **Lobby System:** A matchmaking lobby where players can create/join rooms and start a game.

### Resources

* [Unity Netcode Docs](https://docs-multiplayer.unity3d.com/) - Official multiplayer docs.
* [Fast-Paced Multiplayer](https://www.gabrielgambetta.com/client-server-game-architecture.html) - Classic article series.

### Milestone

By the end of Month 10, you can build a functional two-player online game with basic lag compensation.

---

## Month 11: Publishing, Monetization & Analytics

**Focus:** Getting your game in front of players and understanding the business side.

### Technologies

* **Platforms:** Steam (Steamworks SDK), itch.io, Google Play, App Store
* **Analytics:** Unity Analytics, GameAnalytics
* **Monetization:** Unity IAP, AdMob

### Concepts to Master

* **Build Pipelines:** Platform-specific builds (PC, Android, WebGL).
* **Store Listings:** Screenshots, trailers, descriptions, keywords (ASO).
* **Monetization Models:** Premium, freemium, ads, DLC.
* **Analytics:** Retention metrics, funnel analysis, A/B testing.
* **Localization:** Unity Localization package, string tables.

### Projects

1. **Steam Page Setup:** Prepare a complete Steam store page for one of your projects (capsule art, screenshots, trailer).
2. **Mobile Port:** Port a 2D game to Android with touch controls and AdMob integration.

### Resources

* [Steamworks Documentation](https://partner.steamgames.com/doc/home)
* [How to Market Your Game](https://howtomarketagame.com/) - Indie marketing blog.

### Milestone

By the end of Month 11, you have at least one game published on a public platform.

---

## Month 12: Portfolio & Job Prep

**Focus:** Landing a role at a game studio or shipping your indie game.

### Technologies

* **Portfolio:** itch.io, GitHub, personal website
* **Interview Prep:** LeetCode (C++/C#), game-specific algorithms

### Activities

1. **Flagship Project Polish:** Pick your best project, add a trailer, write a detailed postmortem, and ensure the GitHub repo has a clean README.
2. **Technical Interview Prep:** Practice common game dev interview topics — collision detection math, A* pathfinding, memory management in C++.
3. **Networking:** Join game jams (Ludum Dare, Global Game Jam), Discord communities, and local dev meetups.

### Resources

* [Game Dev Careers](https://www.gamedevcareer.com/) - Industry career advice.
* [Ludum Dare](https://ldjam.com/) - Participate in a game jam to build portfolio pieces fast.

### Milestone

**You are hired (or shipped your indie game)!** 🎮

---

## 💰 Salary & Job Market

* **Median Salary (US):** $75,000–$115,000/year (Junior to Mid-level)
* **Senior Game Developer:** $120,000–$160,000+
* **Top Hiring Companies:** EA, Activision Blizzard, Riot Games, Epic Games, Ubisoft, Valve, indie studios
* **In-Demand Skills:** Unity, Unreal Engine (C++), multiplayer networking, shader programming, mobile game development, VR/AR development
* **Job Market Note:** The indie game market is thriving on Steam and mobile. AAA studios are competitive but internship programs are a strong entry point.

---

## ⚠️ Common Mistakes

1. **Scope creep on first projects** — Beginners consistently try to build their dream RPG first. Start with Pong, Breakout, or Flappy Bird. Finishing a small game teaches more than abandoning a large one.
2. **Ignoring game feel early** — Juice (screen shake, sound effects, particle effects, animation polish) is what separates a prototype from a game. Add it earlier than you think you need to.
3. **Not using version control** — Game projects get complex fast. Not using Git from day one leads to lost work and unrecoverable bugs. Commit often.
4. **Skipping the math** — Developers who avoid vectors and linear algebra hit a hard wall when implementing physics, AI, or shaders. Invest time in game math early.
5. **Optimizing too early** — Premature optimization kills momentum. Build it working first, then profile and optimize only where the profiler shows bottlenecks.
