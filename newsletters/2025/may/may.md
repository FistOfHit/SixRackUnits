[![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/assets/header.png)](https://sixrackunits.substack.com)

# May 2025

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/may/images/title.jpeg)

*What if interconnects became zero-latency over any distance? What about zero-latency for multiplexing/de-multiplexing, buffering, decoding etc.? Or what if there was no latency between a chip accessing a memory region in any other chip it was working with, regardless of where that other chip is? How would that change compute and memory?*

This is the SixRackUnits AI hardware newsletter, keeping you up to date with the latest in AI hardware, datacentre technology, and the future of compute. In addition, we also cover vendors of anything interesting in the space, as well as short "one-pagers" on a random topic that we find interesting (and hope you do too).

For a space to share sources and news/updates, check out the <a href="https://sixrackunits.substack.com/notes">notes</a> section of this newsletter or my <a href="https://www.linkedin.com/in/hitesh-kumar58">LinkedIn</a> for posts on similar topics!

[**This month's updates:**](#this-months-updates)
  - [**Nvidia opens up NVLink for custom CPUs and AI accelerators - NVLink fusion**](#nvidia-opens-up-nvlink-for-custom-cpus-and-ai-accelerators---nvlink-fusion)
  - [**Intel showcases the 6700 series of Xeon CPUs - Also confirms B300 HGX architecture**](#intel-showcases-the-6700-series-of-xeon-cpus---also-confirms-b300-hgx-architecture)
  - [**Nvidia's new Blackwell GPUs for China - unwavering resolve despite U.S. policy**](#nvidias-new-blackwell-gpus-for-china---unwavering-resolve-despite-us-policy)
  - [**Intel releases the PCIe form-factor of their Gaudi 3 AI accelerator**](#intel-releases-the-pcie-form-factor-of-their-gaudi-3-ai-accelerator)
  - [**Other notable headlines**](#other-notable-headlines)

[**Vendor spotlight:**](#vendor-spotlight)
  - [**iPronics**](#ipronics)

[**One-pager:**](#one-pager)
  - [**Wave Division Multiplexing**](#wave-division-multiplexing)

**Note**: From this issue onwards, the number of one-pagers (segments aimed at explaining a concept in a single page) will be limited to one per month. Due to an increase in writing on LinkedIn, I will be sharing a lot of content there that will be similar in nature to the one-pagers, but this will come at the cost of having less time to work on this newsletter. I apologise in advance.

**Note**: In addition to the above, this month has been particularly busy for me, with multiple occurrences that have prevented me from committing as much time as I would have liked to this publication. As a result, this issue only has four updates instead of the usual five. However, I have made sure to include links to everything I found useful and the update that I intended to write a segment about in the "other notable headlines" section. Apologies once again.

---

# This month's updates:

## Nvidia opens up NVLink for custom CPUs and AI accelerators - NVLink fusion

*At Computex '25 in Taiwan, Nvidia revealed their plan for tying themselves to a large portion of their competition in the merchant AI silicon space: NVLink Fusion. In the US and EU markets its arguable but in the Chinese market it's well agreed upon; Nvidia's second most important key to dominance is their NVLink scale-up interconnect. Investing in competing with that has now become unjustifiable for many competitors.*

The speed at which SOTA LLMs can be trained - or even inferenced now - has largely been bound by the bandwidth between GPUs rather than the compute capacity available or memory bandwidth on the package. Nvidia's NVLink technology has led the industry in this aspect, providing not just incredibly high bandwidths between devices but also enabling the collective communications software that the world relies on: NCCL. The [UALink (Ultra Accelerator Link)](https://ualinkconsortium.org/) consortium has tried to upstage NVLink as the preferred interconnect technology, but have so far experienced significant delays in outputting a standard and show no plans for supporting hardware from any vendor.

At Computex '25 this month, Nvidia dealt another blow to UALink by making their NVLink technology stack open to custom, non-Nvidia CPU and AI accelerator hardware under the name of ["NVLink Fusion"](https://www.nvidia.com/en-gb/data-center/nvlink-fusion/). This means access to both the C2C (chip-to-chip) interconnect used for CPU-CPU and CPU-GPU, and the NVLink switched fabric for GPU-GPU communications. Both will likely be using the 5th gen. of the tech stack, providing up to 1.8TB/s bidirectional bandwidth between NVLink capable devices, using Nvidia's proprietary [200G SERDES](https://www.nextplatform.com/2025/05/19/nvidia-licenses-nvlink-memory-ports-to-cpu-and-accelerator-makers/) over 18 Tx/Rx lane pairs, and perhaps even leveraging the potential scale-up size of 576 accelerators in a single domain.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/may/images/nvlink_fusion_slide.jpg)

*Source: ServeTheHome*

Since GTC25 back in March, Nvidia did indeed make a point about open sourcing a lot of software, the [Dynamo](https://www.nvidia.com/en-gb/ai/dynamo/) inferencing engine or "OS" being the centrepiece of this message. What wasn't expected was them opening up their hardware and related IP to others in the semiconductor design and manufacturing space. It should be noted though that this move doesn't fully open up and freely release the NVLink technology stack to anyone - firms will still have to [register/license with Nvidia](https://www.nextplatform.com/2025/05/19/nvidia-licenses-nvlink-memory-ports-to-cpu-and-accelerator-makers/) to use the IP and ultimately, Nvidia does have control over who uses this technology. In addition, only one of the CPU or AI accelerator can be custom, leaving space for Nvidia to sell their own chips through every such integration.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/may/images/nvlink_block_diagram.jpg)

*Source: Next Platform*

Currently, Nvidia intends to work with [existing close partners](https://www.nasdaq.com/articles/nvidia-unveils-nvlink-fusion-integrate-third-party-cpus-its-ai-gpu-ecosystem) such as Astera labs, Cadence, Synopsis, MediaTek, and Marvell on the SERDES and chiplet IP. Key first customers appear to be [Fujitsu](https://www.fujitsu.com/global/products/computing/servers/supercomputer/a64fx/) and [Qualcomm](https://www.reuters.com/business/media-telecom/qualcomm-make-data-center-processors-that-connect-nvidia-chips-2025-05-19/), both known for having success with CPUs and NPUs. According to Dylan Patel of SemiAnalysis in a [conversation](https://www.youtube.com/watch?v=1BTREsSEUZg) with industry analyst Ian Cutress, "only the losers" will be interested in this technology, referring to players who have less experience and no existing proven hardware in this market. In addition, they implied that those with multiple generations of well-established products, a serious roadmap for the future, and a mature interconnect technology already in use - Google, AWS, Meta, etc. - will not have any interest in NVLink Fusion.

## Intel showcases the 6700 series of Xeon CPUs - Also confirms B300 HGX architecture

*Intel have been slowly revealing progressions of their 6th generation datacentre-class Xeon CPUs - dubbed "Sierra Forest" and "Granite Rapids" for the efficiency and performance focused versions respectively. At Computex '25, they debuted the 6700 series, packing up to 86 "P" - performance - cores per socket. With this reveal, they may have also (possibly prematurely) let loose details on the upcoming B300 HGX servers.*

Intel's long-awaited P-core 6700 series were [officially detailed](https://www.storagereview.com/news/intel-debuts-xeon-6-cpus-with-up-to-128-p-cores-powering-nvidia-dgx-b300) at Computex in Taiwan earlier this month, and they intended to deliver a loud and clear message: Xeon is the AI server CPU. Nvidia's NVLink fusion reveal may have pulled some of the attention towards CPUs from soon-to-be competitors [Qualcomm](https://www.reuters.com/business/media-telecom/qualcomm-make-data-center-processors-that-connect-nvidia-chips-2025-05-19/) and a few others, but Intel's presentation was still impressive.

The 6th generation are the first to come in different SKUs for the [E (Efficient) and P (Performance)](https://industrialpc.com/blog/intel-cpu-ecore-pcore/?srsltid=AfmBOopsxPd98BXWQRd1YFz9sklUMTE0ztQjuWyF-5zhm0N1k6C3wvQl) variants. The E-core versions target primarily cloud-native and easily scalable workloads where individual core performance is not as important as the overall density and energy efficiency of the server. The P-core variants, on the other hand, are aimed at high-performance workloads such as AI training and inference, HPC, and other compute-intensive tasks where higher overall performance is required.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/may/images/intel_xeon_chart.jpg)

*Source: Intel*

In particular, the [larger of the 6700P](https://www.intel.com/content/www/us/en/products/sku/243691/intel-xeon-6776p-processor-336m-cache-2-30-ghz/specifications.html) series will top out at 86-cores and will support a maximum shared L2/L3 ["smart"](https://en.wikipedia.org/wiki/CPU_cache#:~:text=time%20instruction%20cache.-,Smart%20cache,-%5Bedit%5D) cache size of 336 MB. They will present up to 8 memory channels per socket, so a theoretical maximum of 4TB per socket with dual 256GB DIMMs per channel, but realistically we think they will practically only carry up to 2TB. In addition, the number of PCIe lanes increases to 88 per socket but stays at gen. 5 (64GB/s per an x16 connection). A new feature that Intel stressed heavily in their showcase was the [priority core turbo](https://newsroom.intel.com/artificial-intelligence/new-intel-xeon-6-cpus-maximize-gpu-ai-performance) or PCT technology, which allows the CPU to dynamically increase the clock speeds of the "most important" cores in a workload, up to 3.8GHz.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/may/images/intel_block_diagram.jpg)

*Source: Intel*

There is an unrelated but still very important detail we must point out: the above slide gives a pseudo-block diagram of the B300 HGX and shows NICs being used in place of PCIe 6.0 switches. This aligns with NVidia's [MGX architecture post](https://developer.nvidia.com/blog/nvidia-connectx-8-supernics-advance-ai-platform-architecture-with-pcie-gen6-connectivity/) where they specified that ConnectX-8 NICs will come with integrated PCIe 6.0 switches with a 48-lane capacity. In this case it appears that each NIC will provide two x16 PCIe 6.0 connections (128GB/s each) to each of the two GPUs and one x16 PCIe 5.0 (64GB/s) to the CPU, with the CPUs using [Intel's UPI](https://en.wikipedia.org/wiki/Intel_Ultra_Path_Interconnect) for up to 384GB/s bidirectional. In the case of HGX servers, the switched NVLink scale-up fabric will remove the need for the PCIe links to be used for cross-socket GPU-GPU communication.

## Nvidia's new Blackwell GPUs for China - unwavering resolve despite U.S. policy

*Rising out of the confusion and panic caused by recent changes in semiconductor and hardware export regulations, Nvidia has announced its latest Blackwell-architecture GPUs for the Chinese market. The name mutated from H30 to B40 and now appears to have settled down to 6000D, but one detail had been clear from early-on: it will use GDDR instead of HBM.*

Amidst rumours of yet another and even stricter restriction from the U.S. on the export of hardware to China coming in April, the first three months of this year saw up to [$16B of orders](https://www.reuters.com/technology/chinese-firms-place-16-billion-order-new-nvidia-chips-information-reports-2025-04-02/) for Nvidia's H20 GPUs. Despite this volume of sales, Wall Street now [predicts a loss](https://www.reuters.com/business/nvidia-forecasts-second-quarter-revenue-below-estimates-2025-05-28/#:~:text=On%20Wednesday%2C%20Nvidia%20said%20the,billion%20in%20the%20second%20quarter.) of up to $12.5B from existing inventory write off for unsellable H20s and the loss of potential revenue in Q2 for Nvidia. In addition, Huawei's Ascend series of GPUs has [gained significant traction](https://www.techinasia.com/news/huaweis-hisilicon-doubles-revenue-market-share-at-12) in the Chinese market in its third generation, due to the rapid maturing of their software stack to match the reliability and functionality of CUDA, and their incredible efforts in competing with Nvidia at [networking multiple racks](https://semianalysis.com/2025/04/16/huawei-ai-cloudmatrix-384-chinas-answer-to-nvidia-gb200-nvl72/) effectively. 

At the start of this month, rumours of the new GPU began to surface though notably they were much quieter than in the past. First referred to as the ["H30"](https://www.tweaktown.com/news/105046/nvidias-next-gen-china-specific-h30-ai-gpu-rumored-with-gddr-memory-instead-of-hbm/index.html) or a direct successor to the H20, then called the ["B40"](https://mp.weixin.qq.com/s?__biz=MzU4ODY5ODU5Ng==&mid=2247492845&idx=1&sn=852404d268583f0442ce4d6a955b1cb1&chksm=fca744f4fc1631e58d9047ed4947f69d34557eba7dc184673dc94a568b5ce1823f09e09c9f6e) as analysts speculated that it would be an inferencing focused card improving upon the popular L40S but with a Blackwell architecture. Finally, the name seems to have stabilised at ["RTX Pro 6000D"](https://www.theregister.com/2025/05/28/nvidia_us_chipmakers_ai_requirements_china/), in line with the regular RTX Pro 6000 which is the Blackwell generations datacentre and desktop grade inferencing card. What was even more surprising than Nvidia conceding on AI training in the Chinese market was that these GPUs - aimed at the largest and most demanding AI labs in the east - would use GDDR instead of HBM.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/may/images/nvidia_rtx6000.png)

*Source: Nvidia - The RTX Pro 6000*

[GDDR](https://en.wikipedia.org/wiki/GDDR_SDRAM) is a type of memory designed for graphics cards, providing significantly more bandwidth to GPU compute elements than regular DDR. Even at this increased performance however, GDDR is not capable of competing with HBM which in its current generation can provide many times as much bandwidth. In this case though, the limits to performance are enforced by policy and not technology. An [intercepted email](https://www.silicon.co.uk/cloud/ai/intel-china-ai-609032) from Intel to its Chinese customers describes the limits on bandwidth prescribed by the new policy being 1.4TB/s for device memory, 1.1TB's of interconnect, and 1.7TB/s combined. We speculate that this approach leaves room for providing multiple SKUs and offering some variations in performance based on customer requirements. A more detailed analysis of this is available from [The Register](https://www.theregister.com/2025/05/28/nvidia_us_chipmakers_ai_requirements_china/).

Regardless, it will almost certainly still be purchased in volume by firms in the east. It may require another tightening of export controls to finally make NVidia accelerators too difficult to justify when purchasing. Even with Huawei's solutions offering a viable alternative on paper, many AI labs in these businesses have extensive experience and existing code using CUDA and related software/frameworks. Transitioning from this will require more than just higher performing systems or even lower costs, but the process is underway for sure.

## Intel releases the PCIe form-factor of their Gaudi 3 AI accelerator

*Intel has long since terminated their Gaudi roadmap, ending the lineage of the AI accelerators made by the acquired Habana Labs in favour of a joint Intel-Habana architecture called Falcon/Jaguar shores, due 2026. In the meanwhile, Intel has released (on schedule) the surprisingly competitive PCIe form factor of their final accelerator in this series, the Gaudi 3.*

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/may/images/intel_pciecard.png)

*Source: Intel*

The Gaudi 3 "add-on" card has just been released. Codenamed the [HL-338](https://www.intel.com/content/www/us/en/content-details/817488/intel-gaudi-3-ai-accelerator-hl-338-pcie-add-in-card-product-brief.html), this is a FHFL (full-height, full length) double-width PCIe card supporting 16 lanes of PCIe gen. 5 and is designed to be added into medium/large AI/HPC servers. Originally announced in 2Q24 as part of Intel's now discontinued roadmap for the Gaudi AI accelerator series, the HL-338 is intended for both training and inference workloads as a standalone card or as part of a reference architecture. The official documentation describes four interconnected cards using 3/4 of their network bandwidth to form a fully connected mesh scale-up network, and 1/4 for scale-out via host NICs.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/may/images/intel_diagram.png)

*Source: Intel*

Habana Labs originally developed the Gaudi series independently and in parallel to Intel's own "Max" series of GPUs, but as early as 2Q23, [Intel announced](https://www.tomshardware.com/news/intel-explains-falcon-shores-redefinition-shares-roadmap-and-first-details) the merging of the two technologies into one product line, codenamed the Falcon shores. Shortly afterwards, Intel also declared that they would [no longer](https://www.hpcwire.com/2024/09/17/intels-falcon-shores-future-looks-bleak-as-it-concedes-ai-training-to-gpu-rivals/) be designing the new merged GPU around AI training, but for Inference and HPC workloads only. Further, just 3 months later they [scrapped Falcon shores](https://www.tomshardware.com/tech-industry/artificial-intelligence/intel-cancels-falcon-shores-gpu-for-ai-workloads-jaguar-shores-to-be-successor) (a PCIe form factor card) from their sales plans and stated that they would focus on their [Jaguar shores](https://www.tomshardware.com/tech-industry/artificial-intelligence/intel-redefines-ai-strategy-jaguar-shores-to-be-rack-level-design-with-focus-on-silicon-photonics) (larger OAM card), with an emphasis on rack-scale systems just as Nvidia and now AMD are doing.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/may/images/intel_roadmap_old.png)

*Source: Intel*

Rack scale solutions also exist, but are in the form of [reference architectures](https://www.intel.com/content/www/us/en/content-details/817486/intel-gaudi-3-ai-accelerator-white-paper.html) only, not custom racks like Nvidia's NVL72 or AMD's upcoming [IF64/128](https://semianalysis.com/2025/04/23/amd-2-0-new-sense-of-urgency-mi450x-chance-to-beat-nvidia-nvidias-new-moat/) solutions. That being said, the reference architectures are comprehensive and provide guidance on the rack layouts, network topologies, and even server/fabric configurations for developers and engineers to follow. 

Finally, the specs ([1](https://www.intel.com/content/www/us/en/content-details/817488/intel-gaudi-3-ai-accelerator-hl-338-pcie-add-in-card-product-brief.html) [2](https://www.intel.com/content/www/us/en/content-details/817486/intel-gaudi-3-ai-accelerator-white-paper.html) [3](https://www.intel.com/content/www/us/en/content-details/817489/intel-gaudi-3-ai-accelerator-hlb-325-baseboard-product-brief.html) [4](https://www.synopsys.com/blogs/chip-design/soc-hbm2e-capacity-speed-benefits.html)):
- ~1.8 PFLOPs of BF16
- 96MB SRAM @ 12.8 TB/s bandwidth
- 128GB HBM2E @ 3.7TB/s (8 stacks of 12hi from SK-Hynix most likely)
- 64GB/s H2D bandwidth via PCIe gen. 5 x16
- Using TSMC's 5nm process
- 600W TDP
AND:
- Single card: Up to 4.8TB/s aggregate scale-out bandwidth via 24 x 200G RoCE ports (48 lanes @ 112G)
OR
- 4 x cards: Up to 4.8TB/s aggregate scale-out + 14.4TB/s aggregate scale-up (1:3 ratio scale-out:scale-up)

## Other notable headlines

* [Nvidia might postpone the adoption of SOCAMM LPDDR5X modules for its GB300 boards, sources cite thermal issues and stability problems](https://zdnet.co.kr/view/?no=20250514101636)
* [AMD's Venice CPUs (2026) confirmed to use TSMC's 2nm process - "TSMC is the leader in 2nm", AMD states](https://www.tweaktown.com/news/105305/amd-says-tsmcs-new-2nm-node-is-superior-to-all-alternatives-talks-using-samsung-foundry/index.html)
* [Nvidia's 1.6T optical transceiver's likely delayed from 4Q25 to 1Q26, sources cite supply chain issues](https://www.digitimes.com.tw/tech/dt/n/shwnws.asp?CnlID=1&Cat=40&id=0000721735_JVO6R7644LFNHC4YWMO00)
* [Nvidia's Connectx-8 NICs to come with PCIe 6.0 switches inside - acting as the interface between CPU and two GPUs each](https://developer.nvidia.com/blog/nvidia-connectx-8-supernics-advance-ai-platform-architecture-with-pcie-gen6-connectivity/)
* [IBM releases the LinuxONE Emperor 5 platform - Mainframe, but without the need to survive an earthquake](https://www.ibm.com/products/linuxone-5)
* [Samsung confident in their 1c DRAM node, betting on improving yields and outpacing competitors SK-Hynix and Micron in HBM4](https://www.trendforce.com/news/2025/05/22/news-samsung-reportedly-plans-1c-dram-expansion-for-hbm4-in-hwaseong-and-pyeongtaek-by-year-end/)
* [AMD acquires silicon photonics startup Enosemi - Aiming to compete with Nvidia and Intel in co-packaged optics](https://www.datacenterdynamics.com/en/news/amd-acquires-silicon-photonics-startup-enosemi/)
* [Apple reportedly developing M-series chips up to three generations ahead - M8 "Sotra" chip may have up to 256 CPU cores and 640 GPU cores in one package](https://www.tweaktown.com/news/105163/apples-future-gen-m6-m7-m8-chips-in-development-up-to-256-core-cpu-640-gpu-teased/index.html)
* [Nvidia backtracks to the "Bianca" model for their SXM motherboards, delaying plans for the "Cordelia" which would have allowed for socketed, replaceable GPUs](https://www.datacenterdynamics.com/en/news/nvidia-server-makers-solve-blackwell-technical-issues-ramp-up-shipments-of-gb200-racks-report/)
* [AMD rumoured to launch a GPU for the chinese market following the same path as Nvidia's RTX Pro 6000D: a version of the Radeon AI PRO R9700 with GDDR7](https://wccftech.com/amd-to-launch-a-china-specific-ai-chip-option-to-rival-nvidia/)
---

# Vendor spotlight:

## iPronics

*Datacentre switching is reaching a point where the relative power draw of the optical-electrical interfaces (transceivers) required to carry the extreme bandwidths of AI fabrics is becoming a concern. 800G fabrics now need special transceiver casings, as well as taller ports just to stay cool. One way to avoid scaling implementation and integration difficulty is to use optical circuit switching, or OCS.*

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/may/images/ipronics_logo.png)

Founded in 2019, Spanish startup [iPronics](https://ipronics.com/) focusing on "software-defined photonics", or photonics hardware designed to be programmable and reconfigurable. iPronics' OCS technology seeks to replace power hungry and fixed-bandwidth electrical switches in datacentres with photonic (light-based) switches that route optical signals without converting them to electrical signals.

Electrical conversion requires significant amounts of power, maintenance, and specialised hardware to support a limited number of bandwidths based on the signal processor design. For example, a 400G switch (referred to as a 25.6T switch by aggregating its 64 ports) requires datacentre staff to use a guide on plugging in the right cable into the right transceiver into the right port, in a particular pattern in order to cable up a particular topology. In addition, these transceivers can only support 400G, 2 x 200G, or 4 x 100G bandwidths usually, and upgrading to higher bandwidths requires new switch ASICs, ports, and transceivers.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/may/images/ipronics_puc.gif)

*Source: iPronics*

Their ["ONE" switch](https://ipronics.com/ipronics-optical-networking-engine/) is a 32-port 1U switch based on their [programmable unit cell](https://ipronics.com/technology/) technology, which is a versatile compute/switching unit that can be combined into structures of seemingly arbitrary size to create something analogous to a switch ASIC with compute attached. Using this, the OCS device can not only route and process signals on the same package but can also be reconfigured via software to modify the routing and processing within 100s of microseconds. This means that in theory, switches made from these programmable unit cells should be able to support in-network compute as well as rapid topology changes to the fabric without extensive maintenance and costly downtime.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/may/images/ipronics_one.png)

*Source: iPronics*

Finally, the specs for the ONE switch are as follows:
- 32 ports independent of bandwidth (up to some limits most likely)
- 1U form factor with 8 physical ports it seems
- <30ns switching latency (compared to 500-1000ns for high end electrical switches)
- <300 microseconds reconfiguration time compared to 100s of milliseconds for mirror-based optical switches

---

# One-pager:

## Wave Division Multiplexing

*Optical fibre itself does have a limit to how much bandwidth it can carry, but current technology is not yet at that wall. To increase bandwidths for cables that need to carry multiple signals at once, one method is wave-division multiplexing (WDM), using multiple wavelengths (or colours) of light to simultaneously carry multiple distinct signals through one fibre.*

WDM is used widely in industry for long range optical communication such as undersea cables, telecoms networks, and more recently, datacentre interconnects. It is a method of multiplexing multiple signals over a single optical fibre by using different wavelengths (or colours) of light. Each wavelength carries its own data stream, and the combined signals are transmitted over a single fibre. At the receiving end, a de-multiplexer separates the combined signals back into their original wavelengths.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/may/images/wdm_architecture.png)

*Source: MEETOPTICS*

Initially, WDM in the 1980s used four wavelengths of light at around ~850nm, but since then the technology has advanced to allow for an order of magnitude more of wavelengths at much higher wavelengths of between 1525-1610nm. WDM that uses a few, widely spaced set of wavelengths is now called coarse WDM (CWDM), while more modern dense WDM (DWDM) uses many closely spaced wavelengths. The latter is the most common in use today, with some practical implementations enabling up to 96 distinct wavelengths to be carried over a single fibre. Using a modern 400G signal, DWDM would allow for an effective bandwidth of 96x400Gbps or 38Tbps over a single fibre.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/may/images/wdm_spacing.png)

*Source: Neos networks*

Using narrower gaps between wavelengths requires more precise hardware to avoid signal loss due to interference and attenuation, but the limitations of existing fibre optics technology leave no other option. Due to various physical phenomena and interactions between light and the glass fibre, certain bands of wavelengths result is less signal loss than others. The C and L bands (1530-1565nm and 1565-1625nm respectively) are the most commonly ranges used for DWDM, and increasing the number of distinct usable wavelengths in these bands requires narrowing the gaps between them.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/may/images/wdm_bands.jpg)

*Source: Pan Dacom Direkt*

[![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/assets/logo.png)](https://sixrackunits.substack.com)
