# Network Host Discovery Using Python

A Python-based network discovery utility that scans a range of IP addresses to identify reachable hosts using ICMP ping. The project demonstrates network probing through system commands executed with Python's `subprocess` module.

## Overview

The repository provides two implementations for pinging multiple hosts within a specified network range:

- **Sequential Scanning (`ping_range.py`):** Executes ping operations sequentially, waiting for each operation to complete before moving to the next host.
- **Background Scanning (`ping_range_bg.py`):** Executes ping operations in the background, allowing multiple hosts to be probed concurrently for faster scanning.

Both implementations aim to identify hosts that respond to ICMP echo requests within the specified network range.

## Architecture

```text
              NETWORK HOST DISCOVERY
                       │
                       ▼
              Define IP Address Range
                       │
                       ▼
                Select Scanner
                  /        \
                 /          \
                ▼            ▼
          Sequential      Background
            Scanner         Scanner
                │              │
                ▼              ▼
          Ping Host 1     Ping Multiple
                │          Hosts
                ▼              │
          Ping Host 2          ▼
                │         Collect Results
                ▼              │
          Ping Host N          │
                │              │
                └──────┬───────┘
                       ▼
               Identify Reachable
                     Hosts
```

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core implementation |
| subprocess | Execute system-level ping commands |
| ICMP | Network host reachability testing |

## Project Structure

```text
ping-network-host/
│
├── ping_range.py       # Sequential host discovery using ping
├── ping_range_bg.py    # Background/concurrent host discovery
└── ReadMe.md           # Project documentation
```
