## Choosing programming framework

One of the first things to decide on was how we will program our EV3 brick.

Following criteria are beneficial:

- fast execution
- fast startup/boot
- ergonomic coding
- stability
- support, active community
- All EV3motors, sensors should work

We tested many frameworks.

## Brief comparison table:

| Framework | Supported | Stable | Ease of use | Polling rate| Performace| Fast startup | Wireless | Coding pleasure | Docs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [Pybricks bare metal](#pybricks-bare-metal)  | 🟢 | 🟡 | 🟢 | 🟢 | 🟡 | 🟢 | 🔴 | 🟡 | 🟢 |
| [Pybricks 2.0](#pybricks-20-ev3dev) | 🔴 | 🟡 | 🟢 | 🟢 | 🔴 | 🔴 | 🟢 | 🟡 | 🟡|
| [c4ev3](#c4ev3) | 🔴 | 🟡 | 🔴 | 🔴 | 🔴 | 🟡 | ? | 🟡 | 🔴 |
| [Rust (EV3DEV)](#rust-ev3dev) | 🟢 | 🟢 | 🟢 | 🟡 | 🟢 | 🔴 | ? | 🟢 | 🟢 |
| [EV3RT](#ev3rt-hrp3) | 🔴 | 🔴 | 🔴 | 🟢 | 🟢 | 🟢 | ? | 🟡 | 🟡 |
| [CLEV3R](#clev3r) | 🔴 | ? | 🔴 | 🟢 | 🟢 | ? | 🟢 | 🔴 | 🟡 |

? - untested

### [c4ev3](https://c4ev3.github.io/)
${\color{lime}\textsf{Pros:}}$
- Similar experience to stock EV3 programs
- C

${\color{red}\textsf{Cons:}}$
- hard to build, install
- Abandoned
- slow sensor polling rate
- bad performance

### [ev3rt (hrp3)](https://github.com/ev3rt-git/ev3rt-hrp3.git)
${\color{lime}\textsf{Pros:}}$
- Lightweight, bare metal
- Fast
- Asynchronous programming

${\color{red}\textsf{Cons:}}$
- LCD does not work
- Hard to learn, C macros magic
- Abandoned
- MicroSD required

### [Clev3r](https://clev3r.ru/)
${\color{lime}\textsf{Pros:}}$
- Faster than blocks
- Popular

${\color{red}\textsf{Cons:}}$
- BASIC: personal ergonomics dislike
- Abandoned
- Need to use custom IDE

### [Rust (EV3DEV)](https://crates.io/crates/ev3dev-lang-rust)
${\color{lime}\textsf{Pros:}}$
- Fast execution
- Ergonomic code writing
- Helpful, smart compiler
- Access to vast crates ecosystem
- supported

${\color{red}\textsf{Cons:}}$
- Slow sensor polling rate(uses Python as backend and is ~4x times slower).
- Uses ev3dev, which is slow to start up
- MicroSD required


### [Pybricks 2.0 (EV3DEV)](https://pybricks.com/ev3-micropython)
${\color{lime}\textsf{Pros:}}$
- Ease of use
- Was popular

${\color{red}\textsf{Cons:}}$
- Uses ev3dev, which is slow to start up
- Bad performance compared to compiled languages
- Abandoned
- MicroSD required

### [Pybricks (Bare metal)](https://github.com/pybricks/pybricks-micropython/tree/master/bricks/ev3)
${\color{lime}\textsf{Pros:}}$
- Ease of use
- Bare metal: 
    - Blazing fast startup
    - Better performace than [Pybricks 2.0](#pybricks-20-ev3dev)
- Great support
- Nearly drop-in replacement for [Pybricks 2.0](#pybricks-20-ev3dev)
- Decent Documentation

${\color{red}\textsf{Cons:}}$
- Experimental: no wireless support yet
- Bad performance compared to compiled languages

## We chose [Pybricks bare metal](https://github.com/pybricks/pybricks-micropython/tree/master/bricks/ev3)

Due to the lightweight bare metal, fast startup times, ease of coding and sufficient polling rate and performance, decent documentation, although, accepting compromise of no wireless debugging, and no helpful smart compiler we chose Pybricks bare metal to program for EV3.

The next close candidate is Rust, however it's slow polling rate and slow startup of ev3dev were dealbreakers.