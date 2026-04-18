# ![LOGO](images/logo.png)

 Welcome to the GitHub Repository of Team XLNC Apex from Kazakhstan, competing in the World Robot Olympiad Future Engineers 2026 category.

# Contents
- The team
- Challenge Overview
- Our Robot
- Mechanical systems
- Electronic systems
- Software

---

# The team

### Members

- Karabayev Darkhan

- Abenov Sayan

### Coach

Usoltsev Vladimir


---

# Challenge Overview

The **WRO Future Engineers** category requires building a **fully autonomous self-driving vehicle** that:

- Navigates a closed track without external control  
- Detects and avoids obstacles dynamically  
- Maintains stability and precision at speed  
- Adapts to uncertain and changing conditions  

Key engineering challenges:
- Real-time perception  
- Reducing sensor errors  
- Keeping right distance from walls  
- Reliability under competition constraints  

---

# System Architecture

Our robot is designed as a modular system consisting of three tightly integrated layers:

### 1. Perception Layer
- Vision-based detection using **Pixy2 camera**
- Object tracking and color signature recognition  
- Distance estimation using onboard sensors  

### 2. Control Layer
- Closed-loop control using **PID algorithms**  
- Steering and speed regulation  
- Real-time decision-making  

### 3. Execution Layer
- Motor actuation via LEGO EV3 platform  
- Precise movement and trajectory correction  

This layered approach allows us to isolate complexity and improve reliability.

---

# Our Robot

Our robot is a compact autonomous vehicle optimized for **speed, stability, and deterministic behavior**.

### Key Design Principles
- **Consistency over complexity**  
- **Low-latency decision making**  
- **Mechanical reliability first**  

### Capabilities
- Lane following using vision  
- Obstacle detection and avoidance  
- Smooth cornering with PID stabilization  
- Real-time trajectory correction  

---

# Mechanical Systems

The mechanical design is focused on achieving predictable and stable motion.

### Features
- Rigid and lightweight chassis  
- Optimized center of mass for high-speed turns  
- High-precision steering mechanism  
- Efficient drivetrain using LEGO components  

### Engineering Decisions
- Minimized mechanical play for better control accuracy  
- Balanced gear ratios for torque vs speed trade-off  
- Structural reinforcement for competition durability  

---

# Electronic Systems

Our robot is powered by the **LEGO EV3** platform with extended sensing capabilities.

### Core Components
- **LEGO EV3 Brick** — main controller  
- **Pixy2 Camera** — primary vision sensor  
- Motors with encoder feedback  
- Auxiliary sensors (distance, color, etc.)  

### Design Focus
- Reliable communication between modules  
- Low-latency sensor data processing  
- Stable power distribution  

---

# Software

The software stack is built using **Pybricks (MicroPython)** and follows a modular architecture.

### Core Modules
- **Perception Module**  
  - Pixy2 data processing  
  - Object detection and filtering  

- **Control Module**  
  - PID controllers for steering and speed  
  - Trajectory correction logic  

- **Decision Module**  
  - Obstacle avoidance strategy  
  - State-based behavior system  

- **Integration Layer**  
  - Sensor fusion  
  - Real-time execution loop  

### Key Features
- Deterministic control loop  
- Robust error handling  
- Scalable architecture for rapid iteration  

---

# Performance & Strategy

Our approach prioritizes **reliability and repeatability** over aggressive but unstable strategies.

### Strategy Highlights
- Stable lane tracking as baseline behavior  
- Early obstacle detection and smooth avoidance  
- Conservative speed tuning for maximum consistency  

### Continuous Improvements
- PID tuning through iterative testing  
- Mechanical refinements for reduced vibration  
- Optimization of vision processing latency  

---

🚀 **Goal:** Build a highly reliable autonomous system capable of consistent performance at the highest level of WRO competition.