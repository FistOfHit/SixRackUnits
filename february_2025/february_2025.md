# February 2025
![]()

*caption*

**This month's updates:**

* SanDisk develops “high-bandwidth flash” memory, aiming for TB capacity on GPUs
* Meta reportedly looks to acquire Korean chip startup FuriosaAI
* Leading AI labs OpenAI and DeepSeek both developing custom AI accelerators
* An update on Intel’s roadmap - early signs of success from 18A

**Vendor spotlight:**

* NextSilicon

**One-pagers:**

* Racetrack memory
* Baseboard management controllers

* * *

# This month's updates:

## SanDisk develops high-bandwidth flash (HBF) memory

_High bandwidth memory (HBM) is one of the most important components of AI accelerators, enabling the massive amounts of rapid memory transfer needed for AI training workloads, but this performance comes at cost: DRAM - which makes up HBM - is expensive and takes up a lot of area per unit of storage. SanDisk, however, might just have solved this with HBF._

Regular DRAM struggles to saturate the bandwidth demand from AI accelerator compute elements, necessitating the development of technologies like LPDDR/X (low-power DDR/enhanced), GDDR (Graphics DDR), and HBM (High bandwidth memory). While implementation details vary greatly, there is one major common foundation they all share: DRAM. By design, DRAM strikes a balance between power use, density, and cost, leading to it being the best solution for on-device memory that lives just outside the processor but still closer than any larger capacity storage. 

SanDisk, having just completed their spin-off from Western Digital, have announced a possible solution that could combine the large capacities of flash storage memories such as SSDs with the bandwidth that HBM provides to the processor - HBF. At their annual investors day presentations, SanDisk revealed how they’ve prototyped a vertical stacking technology (just as HBM does with DRAM) to combine multiple flash memory dies into a single, high-throughput design that can meet the TB/s bandwidth requirements from HBM devices whilst providing the hundreds of GB of capacity enabled by higher density flash memory. 

Whilst they admit that latency will still be worse than DRAM-based memory, SanDisk show how AI hardware designers could combine HBF and HBM to have smaller volumes of fast access memory acting as another level of cache, and the higher capacity HBF acting as a higher level of warm storage that can keep data on device - avoiding the 10-100x relative cost of fetching data from the host server. The first generation of HBF is expected in 2H25 providing up to 500GB of capacity per stack, with the second (2026) and third (2027) generations increasing capacity further up to 1TB per stack and attempting to keep up with the bandwidth we can expect from HBM4.

## Samsung and Micron still in the race for HBM

_Last quarter, SK-Hynix and Nvidia both confirmed plans for 6th gen. HBM4 with the memory manufacturer agreeing to meet the 1H2025 deadline for sampling their devices on Nvidia's "Rubin" architectures. Now, Samsung and Micron both formally announce that they too are still competing for the future of this market._

Industry analysts report that the acquisition could be completed as early as by the end of this month, but looking at clues in papers released on the technology Furiosa implement, its possible that Meta (then Facebook) were collaborating with the startup’s technical team as far back as 2019. The buyout would likely lead to Meta mixing their development teams with Furiosa’s and incorporating future products into its existing custom silicon lineup, as Meta presently deploys two generations of their “Meta Training and Inference Accelerators” - MTIAs - for their ranking and recommendation systems that run their services on apps such as Facebook and Instagram. From a 2024 leaked internal memo, it appears that Meta already had plans for the next generation of their AI accelerator in 2025. Whether this plan included the merging in of Furiosa’s roadmap is unclear. 

Furiosa released their second processor, the RNGD, in 2024 - a PCIe form factor server chip targeting LLM training and inference providing ~1.6-2x the efficiency of Nvidia H100s on inferencing models in the 6-8B parameter range. The success of their accelerators is down to two key innovations: a tensor contraction compiler (1 2), and a tensor contraction processor. Tensor contraction is a higher dimensional generalisation of matrix multiplication, and the compiler’s success comes down to optimising memory layout and caching for better read/write patterns. All of this is then enabled by the unique processor design which performs dot-product operations on variable data shapes. All this results in a CGRA-like architecture designed for variable tensor input sizes, more so than even Google’s systolic array based TPUs.

* As for its specs (1 2 3 4):
* Using TSMCs 5nm process node
* PCIe dual-slot FH 3/4L form factor 
* 256MB on chip SRAM (384TB/s)
* 256TFLOPS at BF16
* 150W TDP air cooled
* 2 x 24GB 12hi HBM3 (likely SK-Hynix)
* 48GB of 12hi HBM3 (1.5TB/s)
* 1GHz TCP frequency
* Supermicro server integration
* $10,000 (analyst estimate)

## OpenAI and DeepSeek developing custom accelerators

_Tech organisations tend towards developing custom hardware as their technical capabilities grow and the demand for their products increases beyond what is cost-effective to run on merchant silicon such as GPUs from Nvidia or on the cloud from hyperscalers. OpenAI and DeepSeek are not the first - and certainly not the last - AI foundation model labs taking this route._

## Intel’s roadmap and its dependence on 18A

_Intel’s roadmap on AI accelerators has changed so frequently in recent years that some large customers interested in the Gaudi series decided to stick with vendors able to provide more maintainable and upgradeable product, but recent successes with their 18A process node and PC/server CPUs might finally turn things around._

* * *

# Vendor spotlight:

## NextSilicon

_One of the few chip designers aiming at scientific compute, NextSilicon develops “intelligent compute accelerators” (ICAs) that optimise for natively running C++ and Fortran workloads at efficiencies and throughputs/latencies unmatched by CPUs and GPUs. Their “Maverick” ICA now looks to prove itself and break into the datacentre server space._

Founded in 2017, Israeli startup NextSilicon differentiates itself from the competition in two key ways: the target market they pursue, and their requirement to support existing target workloads. Their products aren’t aimed at accelerating AI but instead at regular scientific compute workloads that have been - and still are - the biggest consumers of compute in the world. Applications that would benefit from NextSilicon’s designs include weather forecasting, finite element analysis, and graph algorithms, all of which rely on structured and repeatable computations on data but with less predictable memory access patterns and more varied control flows. Almost all such applications are written and maintained in two programming languages, C++ and Fortran, both in use for decades for building highly performant programs that run much of the world’s software today. NextSilicon aim to keep it that way by ensuring their “software-defined hardware” runs such applications natively, with no need for porting to another language or writing intermediate representations, which is what vendors like Nvidia, AMD, and Intel require when using their specialised accelerators. 

Their novel processor, the Maverick, now in its second generation, introduces software-defined hardware acceleration by taking scientific applications in their native forms (just as they would run on CPUs) and learning what the software requires from hardware to run optimally. It does this by running them on its own dynamically reconfigurable grid of general purpose “E-cores” and math-specialised “compute elements” and building graphs of the various paths data takes as it moves from memory, through the compute, and back to memory. It then reconfigures itself on the fly to best suit those computational graphs and accelerates application performance by up to 4x when compared to GPUs and 20x compared to high-end CPUs. As for specs, the Maverick 2 in its 300W-TDP PCIe form factor provides up to 32 E-cores and 224 compute elements, along with four stacks of HBM3E, totalling at 96GB. The OAM version supports two compute die and up to 192GB of HBM3E but has a TDP of 600W, requiring liquid cooling. Both forms are built on TSMCs 5nm process.

* * *

# One-pagers:

## Racetrack memory

_Device memory is usually stored as electric charge across a capacitor or as a state of a set of transistors, however magnetism provides a new way of complementing or replacing SSDs or DRAM with a low-latency/jitter, energy efficient, and non-wearing solution: RTM, which stores information between magnetic domains in nanowires shows promise._

Originally developed by researchers at IBM and now in the experimental stage with various other institutions, RTM aims to combine the high performance and reliability of solid-state memory with the cost-effectiveness and density of traditional magnetic storage. RTM, Unlike conventional memory which stores information in transistors and capacitors, uses “racetracks” or nano wires that hold multiple magnetic regions separated by thin domain walls or gaps. These domain walls represent the information to be stored, and information is moved from storage to read/write heads by shifting the magnetic domains up and down the wire using electrical currents. 

The shifting action, as well as how quick and efficient it is to read and write information to the wires, leads to the potential for RTM to become part of future memory devices. Additionally, unlike flash storage which requires distinguishing charge levels in a capacitor that wears out over time, racetrack nanowires do not degrade with use. The use case and capabilities of RTM-based memory depends on its structure and the design of the device, just as with flash and DRAM based technologies. Whether the wires are arranged in two- or three-dimensional arrays, how many read/write heads are used to get and store information in parallel, or how error correction is optimised for shift-based memory movement all influence where and how RTM can be used and what advantages/disadvantages it presents. 

AI workloads - now the fastest growing use case for high-performance hardware - could potentially see significant improvements in throughput/latency and flops/watt with processors using RTM. With compilers that can breakdown high-dimensional matrix operations (most of what AI models do internally) into instructions suited to reading and writing from arrays of racetracks, hardware that utilises RTM to compliment or replace DRAM-based memory could theoretically lead to large improvements in performance. Currently, IBM appears to be the industry leader in RTM research, and many universities experimenting independently on their own prototypes.

## Baseboard management controllers (BMCs)

_A baseboard (or motherboard) hosts all the components of a server and connects them via copper wires or sockets and cables. The microcontroller which manages much of the state and functionality of the board is known as the baseboard management controller (BMC) and is one of the most important yet often overlooked parts of a server._

BMCs are dedicated chips on the baseboard that perform a variety of functions crucial to managing a server. Primarily, they enable out-of-band (OOB) management through their own dedicated network interfaces, allowing administrators to remotely power-cycle servers, update BIOS/UEFI firmware, or diagnose failures even when the host operating systems are unresponsive. Modern BMCs are usually built on ARM or RISC-V architectures - even in x86 servers - but operate independently from the CPUs and draw power through their own separate rails. For temperature and power management they interface with thermal sensors, voltage regulators, and fans/other cooling systems, and so can modify power supply/frequency to components to enforce programmable temperature limits. To interact with a BMC directly, most manufacturers provide APIs to expose key functions. The industry standard that has emerged over the past decade is Redfish, which provides ways to interact with the BMC through POST/GET calls, Python, and Ansible to name a few.

As servers tend towards hundreds of cores per CPU, multiple GPUs, and additional NICs/switches all on the same board, the demand on the BMCs increases super-linearly. Individual components become denser and more performant with every iteration, but the number of sensors and the frequency of incoming data also increases, resulting in an even greater load on the management controller and connections. This trend towards increased networking and processing load has resulted in BMCs having a higher core count and using high-bandwidth connectivity such as 400G NICs and PCIe 5.0 to support the data collection and processing required for managing increasingly complex baseboards.

Some BMCs implement advanced predictive maintenance via small AI models, to help prevent damage and wear on components, and incorporate specialised units such as NPUs to offload these small AI workloads. It’s also likely that BMCs will eventually integrate more and higher bandwidth memory such as HBM stacks to cache sensor data, enabling better management functionality on chip rather than sending data to remote management servers. This shift mirrors industry’s push toward “lights-out” datacentres, where fewer and fewer hardware faults require human intervention.
