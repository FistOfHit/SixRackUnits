[![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/assets/header.png)](https://sixrackunits.substack.com)

# March 2025

![What would the densest possible storage device look like? We will inevitably move away from transistors and capacitors. The intermediate steps are unclear, but the end goal might be to use something created by nature itself and find a way to tap into it.*](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/march_2025/images/1.png)

*What would the densest possible storage device look like? We will inevitably move away from transistors and capacitors. The intermediate steps are unclear, but the end goal might be to use something created by nature itself and find a way to tap into it.*

[**This month's updates:**](#this-months-updates)
  - [**Bolt Graphics reveals “Zeus” GPU – Claiming to 10x the Nvidia 5090’s performance**](#bolt-graphics-reveals-the-zeus-gpu)
  - [**Other notable headlines**](#other-notable-headlines)

[**Vendor spotlight:**](#vendor-spotlight)
  - [**Kove**](#kove)

[**One-pagers:**](#one-pagers)

---

# This month's updates:

## Bolt Graphics reveals the Zeus GPU

## Other notable headlines

---

# Vendor spotlight:

## Cerebras

*In a semiconductor fabrication unit, the manufacturer partitions a large silicon wafer into lots of small chips and each of those then goes on to be integrated into a device such as a CPU or GPU. Cerebras instead decide that they will use the entire wafer and keep it in one piece, for an enormous, monolithic chip called the wafer-scale engine (WSE).*

Conventionally, a chip designer would never consider using an entire silicon wafer as a single device, let alone exceeding the size limits of what can be fabricated without dropping yield rates. If a designer decides to pursue this regardless, then there are two significant issues to overcome: managing the impact of the inevitable manufacturing defects, and designing the I/O software and hardware for connecting the wafer efficiently. Cerebras tackles both with their various innovative approaches and then packages their wafer-scale engine (WSE) in their “CS” systems. 

Having defects during manufacturing that can cause a few cores to be written off are expected, and Cerebras works around these issues with its reconfigurable architecture that modifies the core-core interconnect paths dynamically around deactivated cores. In addition, connections between the die themselves are specially designed in collaboration with TSMC to enable cross scribe line communication, scribe lines being where the silicon is supposed to be physically cut. These technologies, along with many other advancements, enable the WSE to offer industry leading single-server specs.

Here is what we know about the latest generation, the WSE-3 as revealed in 1Q24 (1 2 3 4):
- A total of 125 PFLOPS of dense FP16 (most likely) at a TDP of ~23kW
- 44GB of “on-chip” SRAM, delivering an aggregate of 21PB/s of bandwidth from memory to the compute
- 214Pb/s aggregate bandwidth between all cores on the wafer using fabric routers and cross-scribe wires

Cerebras currently operate 3 datacentres with their 2nd and 3rd gen. CS-2 and CS-3 systems deployed and have confirmed an additional 6 across NA and EU by the end of 4Q25. Private sector customers include AstraZeneca, Total energies, Tokyo electron devices and more across NA and APAC. They also have significant presence in public sector research and academia, with Argonne, Livermore, and Sandia among the largest names in national labs currently confirmed to be trialling or purchasing CS-2 systems.


---

# One-pagers:

[![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/assets/logo.png)](https://sixrackunits.substack.com)